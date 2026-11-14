"""Dedup + classify Helium 10 exports into market buckets.
Usage: classify.py raw data.json [--review]   (writes data.json, products.json and cleaned-products.csv)"""
import csv, json, re, sys, collections

SRC, OUT = sys.argv[1].rstrip('/') + '/', sys.argv[2]
REVIEW = '--review' in sys.argv

MARKETS = {  # file -> (label, own-ingredient regex)
    'extravirgincocunutoil': ('Virgin Coconut Oil', r'coconut|nariyal|\bvco\b|coocnut'),
    'castoroil': ('Castor Oil', r'castor|arandi|erand'),
    'kalongioil': ('Kalonji Oil', r'kalonji|black ?seed|nigella|black cumin|kaloji|kalaunji'),
    'neemoil': ('Neem Oil', r'neem'),
    'rosewater': ('Rose Water', r'rose ?water|gulab ?jal|rose hydrosol|gulab ark|arq gulab|gulabari|rose mist|rosetone|rose glass skin mist|rose pore tightening toner'),
    'tiloil': ('Til (Sesame) Oil', r'sesame|gingelly|\btil\b|tilnad|nallennai'),
    'oliveoilpomace': ('Olive Oil', r'olive oil|olive pomace|pomace|olive aura|\bevoo\b'),
}
# other ingredients that signal a blend when they appear next to the own ingredient
OTHER = (r'rosemary|almond|onion|indigo|bhringraj|\bamla\b|argan|jojoba|tea ?tree|hibiscus|brahmi|lavender|pumpkin|'
         r'jatamansi|giloy|tulsi|basil|pongamia|sunflower|rice bran|groundnut|peanut|mustard|kewra|carrot seed|'
         r'castor|coconut|neem|kalonji|black ?seed|sesame|olive|glycerin|aloe|niacinamide|hyaluronic|vitamin c|'
         r'glycolic|witch hazel|ceramide|rice water|chamomile|vetiver|beetroot|turmeric|karanja|neem khal|himalayan water')
OWNWORD = r'coconut|castor|kalonji|black ?seed|neem|sesame|olives?|rose'
FORMAT = (r'capsule|face ?wash|shampoo|\bsoap\b|juice|face cleanser|water gel|\bcombo\b|roller|neemolice|lice killing|cooking spray|'
          r'eyelash growth oil|hair plus|nabhi|belly button|medicated|pack wrap|massage oil \(|softgel|tablet')
GARDEN = r'plant|garden|pest|insect|farming|\bppm\b|water[- ]solub|mealy|aphid|fungus|neemguard|neem guard|neem active'
PUJA = r'puja|pooja|\bdiya\b|deepak|\blamp\b|jyot|havan|poojan'
PET = r'\bdogs?\b|\bcats?\b|for pets|tick and flea'
PERSONAL = r'skin|hair|scalp|face|body|dandruff'

OVERRIDES = {}  # ASIN -> (bucket, reason); filled in after manual review


def num(x):
    try:
        return float(str(x).replace(',', ''))
    except ValueError:
        return 0.0


def size_ml(t):
    # volume first: titles also carry weights ("made with 40kg of roses") that are not the pack size
    m = re.search(r'(\d+(?:\.\d+)?)\s*-?\s*(ml|millilit\w*|ltr|litres?|liters?|lt\b|l\b|fl oz|oz\b|ounce)', t) \
        or re.search(r'(\d+(?:\.\d+)?)\s*(kg|gm?\b)', t)
    if not m:
        return None
    v, u = float(m.group(1)), m.group(2)
    if u.startswith(('ml', 'milli')) or u in ('g', 'gm'):
        return v
    if 'oz' in u or u == 'ounce':
        return round(v * 29.57)
    return v * 1000


def band(ml):
    if ml is None: return 'Unknown'
    if ml <= 120: return 'Up to 100 ml'
    if ml <= 250: return '121–250 ml'
    if ml <= 500: return '251–500 ml'
    if ml <= 1100: return '501 ml–1 L'
    return 'Over 1 L'


def pack(ml):
    """Nearest standard pack size, finer than band(): what a buyer would call the bottle."""
    if ml is None: return 'Unknown'
    for hi, name in [(60, '50 ml or less'), (130, '100 ml'), (185, '150 ml'), (230, '200 ml'), (275, '250 ml'), (450, '300–400 ml'), (560, '500 ml'),
                     (1100, '1 L'), (2600, '2 L')]:
        if ml <= hi: return name
    return '5 L and up'


def subsegment(mkt, t):
    if mkt == 'oliveoilpomace':
        if 'pomace' in t: return 'Pomace'
        if re.search(r'extra virgin|\bevoo\b', t): return 'Extra virgin'
        if re.search(r'light', t): return 'Extra light'
        return 'Pure / classic'
    edible = re.search(r'edible|cooking|food grade|eating|kheer|biry', t)
    personal = re.search(PERSONAL + r'|massage|toner|mist', t)
    if mkt in ('tiloil', 'extravirgincocunutoil'):
        if edible and personal: return 'Multipurpose'
        if personal: return 'Hair & skin'
        return 'Cooking'
    if edible and personal: return 'Multipurpose'
    if edible: return 'Edible'
    return 'Hair & skin'


def classify(mkt, r):
    t = r['title'].lower()
    own = MARKETS[mkt][1]
    if r['asin'] in OVERRIDES:
        return OVERRIDES[r['asin']]
    if re.search(PUJA, t) and not re.search(r'cooking|edible|massage|skin|hair|food|face', t):
        return 'Wrong audience', 'Puja / lamp oil'
    if r['category'] == 'Pet Supplies' or re.search(PET, t):
        return 'Wrong audience', 'Pet product'
    if not re.search(own, t):
        for k, (lab, rx) in MARKETS.items():
            if k != mkt and re.search(rx, t):
                return 'Wrong product', f'Different product ({lab.lower()})'
        return 'Wrong product', 'Does not contain the searched ingredient'
    if mkt == 'oliveoilpomace' and re.search(r'sliced olives|olives,', t):
        return 'Wrong product', 'Table olives, not oil'
    if mkt == 'neemoil':
        if r['category'] == 'Garden & Outdoors' or (re.search(GARDEN, t) and not re.search(PERSONAL, t)):
            return 'Wrong audience', 'Gardening / plant care'
    if re.search(FORMAT, t):
        return 'Adjacent', 'Different format (' + re.search(FORMAT, t).group(0).strip() + ')'
    stripped = re.sub(own + '|' + OWNWORD if mkt != 'castoroil' or True else own, ' ', t)
    m = re.search(OTHER, stripped)
    if m:
        return 'Adjacent', f'Blend or added ingredient ({m.group(0)})'
    if mkt == 'extravirgincocunutoil' and not re.search(r'virgin|cold[- ]?press|wood[- ]?press|vco|raw|unrefined', t):
        return 'Adjacent', 'Regular (not virgin / cold pressed) coconut oil'
    return 'Core', 'Pure single-ingredient product'


rows, stats = [], {}
for mkt, (label, _) in MARKETS.items():
    raw = list(csv.DictReader(open(SRC + mkt + '.csv', encoding='utf-8-sig')))
    seen = {}
    for x in raw:
        a = x['ASIN']
        if a in seen:
            seen[a]['placements'] += 1
            seen[a]['sponsored'] = seen[a]['sponsored'] or bool(x['Sponsored'])
            continue
        title = x['Product Details'].replace('($) ', '').strip()
        ml = size_ml(title.lower())
        seen[a] = dict(
            asin=a, market=label, mkt=mkt, title=title, brand=x['Brand'].strip() or 'Unbranded',
            price=num(x['Price  ₹']), units=round(num(x['ASIN Sales'])), revenue=round(num(x['ASIN Revenue'])),
            parentRevenue=round(num(x['Parent Level Revenue'])), bsr=num(x['BSR']) or None,
            rating=num(x['Ratings']) or None, reviews=int(num(x['Review Count'])), category=x['Category'] or 'Uncategorised',
            fulfillment=x['Fulfillment'], created=x['Creation Date'] if x['Creation Date'] != 'N/A' else '',
            sponsored=bool(x['Sponsored']), placements=1, url=x['URL'], sizeMl=ml, sizeBand=band(ml), packSize=pack(ml))
    for r in seen.values():
        r['bucket'], r['reason'] = classify(mkt, r)
        r['segment'] = subsegment(mkt, r['title'].lower()) if r['bucket'] in ('Core', 'Adjacent') else ''
        r['dead'] = r['revenue'] == 0
    stats[label] = dict(rawRows=len(raw), unique=len(seen), dupRows=len(raw) - len(seen),
                        rawRevenue=round(sum(num(x['ASIN Revenue']) for x in raw)), dedupRevenue=sum(r['revenue'] for r in seen.values()),
                        parentRevenue=round(sum(num(x['Parent Level Revenue']) for x in raw)))
    rows += seen.values()

# cross-file duplicates: count each ASIN once, in the market where it ranks best
rank = {'Core': 0, 'Adjacent': 1, 'Wrong audience': 2, 'Wrong product': 3}
by = collections.defaultdict(list)
for r in rows: by[r['asin']].append(r)
cross = 0
for a, rs in by.items():
    if len(rs) > 1:
        cross += 1
        rs.sort(key=lambda r: rank[r['bucket']])
        for r in rs[1:]:
            if r['bucket'] in ('Core', 'Adjacent'):
                r['bucket'], r['reason'], r['segment'] = 'Wrong product', f"Counted once under {rs[0]['market']}", ''
            elif rs[0]['bucket'] in ('Core', 'Adjacent'):
                r['reason'] = f"Belongs to {rs[0]['market']} (counted there)"

for r in rows: del r['mkt']

# flat export for the dashboard and for spreadsheets
KEEP = ['asin', 'market', 'bucket', 'reason', 'segment', 'packSize', 'sizeMl', 'brand', 'title', 'price', 'units', 'revenue',
        'rating', 'reviews', 'sponsored', 'placements', 'category', 'url']
flat = sorted(({k: ('Yes' if r[k] else 'No') if k == 'sponsored' else (r[k] or '') if k == 'rating' else r[k] for k in KEEP}
               for r in rows), key=lambda r: -r['revenue'])
base = OUT.rsplit('/', 1)[0] + '/' if '/' in OUT else ''
json.dump(flat, open(base + 'products.json', 'w'), ensure_ascii=False)
w = csv.DictWriter(open(base + 'cleaned-products.csv', 'w', newline='', encoding='utf-8-sig'), fieldnames=KEEP)
w.writeheader(); w.writerows(flat)
json.dump(dict(stats=stats, crossFile=cross, rows=rows), open(OUT, 'w'), ensure_ascii=False)

for label in stats:
    c = collections.Counter(); v = collections.Counter()
    for r in rows:
        if r['market'] == label: c[r['bucket']] += 1; v[r['bucket']] += r['revenue']
    print(label, '| raw %.2fcr dedup %.2fcr |' % (stats[label]['rawRevenue'] / 1e7, stats[label]['dedupRevenue'] / 1e7), ' '.join('%s %d/%.2fcr' % (b, c[b], v[b] / 1e7) for b in rank))
if REVIEW:
    for label in stats:
        for b in rank:
            print(f'\n## {label} :: {b}')
            for r in sorted((r for r in rows if r['market'] == label and r['bucket'] == b), key=lambda r: -r['revenue']):
                if r['revenue'] >= (25000 if b == 'Core' else 3000):
                    print('%s|%dk|%s|%s|%s' % (r['asin'], r['revenue'] / 1000, r['sizeBand'][:6], r['reason'][:30], r['title'][:72]))
