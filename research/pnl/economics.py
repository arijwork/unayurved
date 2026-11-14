"""Profit per bottle for Unayurved's three bottles, self-shipped on Amazon (Easy Ship).
Usage: economics.py  -> writes economics.json and ramp.json next to this file and prints the table.
Reads costs.json here and ../amazon-market/cleaned-products.csv.

Every assumption that did not come from the founder is in ASSUMED and should be checked in Seller Central / with a CA.
"""
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
costs = json.load(open(os.path.join(HERE, 'costs.json')))
OIL = costs['oil_cost_per_litre_inr']

# bottle -> (fill ml, bottle+cap, label), all GST-inclusive, from the founder
PACK = {'100 ml': (100, 8, 6.25), '200 ml': (200, 10, 8), '400 ml': (400, 15, 15)}

ASSUMED = {
    'outer_box_and_packing': 10,        # per order, GST-inclusive; not yet given
    'gst_on_sale': {'default': 0.05, 'Rose Water': 0.18},   # oils 5%; rose water as a skin toner 18%
    'gst_on_liquid': {'default': 0.05, 'Rose Water': 0.18},
    'gst_on_packaging': 0.18,
    'referral_fee': 0.0,                # Amazon.in: 0% up to Rs 1,000 for oils and haircare (from 16 Mar 2026)
    'closing_fee': [(300, 3), (500, 24), (1000, 35)],       # Easy Ship, after the 7 Sep 2026 rise; top band is a guess
    'shipping_fee': {'100 ml': 55, '200 ml': 55, '400 ml': 55},  # Easy Ship: Rs 55 up to 500 g packed (plastic bottles); Rs 75 if a packed 400 ml goes over
    'brand_share_of_mrp_via_distributor': 0.40,   # distributor asks for 60% of MRP
    'carton_share_per_bottle': 2,                 # bulk carton for distributor orders, guess
}

# (market, bottle) -> (launch price, verdict, why).  Prices sit at or just under what the size sells for today.
PLAN = {
    ('Rose Water', '200 ml'): (279, 'Launch', 'Largest rose water size (47% of core revenue). Best sellers: WishCare Rs 345, Vitro Rs 283, UrbanBotanics Rs 279.'),
    ('Rose Water', '100 ml'): (199, 'Launch', 'Second size (20% of revenue). Matches the best seller, Nat Habit at Rs 201.'),
    ('Rose Water', '400 ml'): (299, 'Hold', 'Large rose water sells very cheaply: Dabur 400 ml is under Rs 100 a bottle in multipacks. Little demand at a paying price.'),
    ('Kalonji Oil', '100 ml'): (369, 'Launch', 'The main kalonji size (56% of revenue). Just under Caraway Rs 375 and Hesthetic Rs 399; cheap listings earn little here.'),
    ('Kalonji Oil', '200 ml'): (429, 'Launch', '12% of revenue. UrbanBotanics leads at Rs 390; the 250 ml leaders charge Rs 645 to 799, so there is room above Rs 390.'),
    ('Kalonji Oil', '400 ml'): (849, 'Hold', 'Almost nobody buys kalonji at this size online (0.2% of revenue at 500 ml), and it ties up the most cash per bottle.'),
    ('Neem Oil', '200 ml'): (249, 'Launch', 'Half of a small market. Sits between Nat Habit Rs 349 and Rey Naturals Rs 219.'),
    ('Neem Oil', '100 ml'): (159, 'Later', 'Only 10% of neem revenue. Goodcare leads at Rs 189. Priced at your current MRP of Rs 159. Add once the 200 ml sells.'),
    ('Neem Oil', '400 ml'): (299, 'Hold', 'One seller at 500 ml (Veda Oils Rs 242) and 4% of revenue. No real demand.'),
    ('Castor Oil', '200 ml'): (199, 'Launch', 'The castor market (56% of revenue). Dabur Rs 164, WishCare Rs 199, Rey Naturals Rs 229, Nat Habit Rs 319.'),
    ('Castor Oil', '100 ml'): (149, 'Launch', 'Trial size with 17% of units. Khadi Rs 130, Soulflower Rs 199.'),
    ('Castor Oil', '400 ml'): (299, 'Later', '500 ml is 13% of revenue; Phalada sells it at Rs 233, so a 400 ml fill has to stay at or under Rs 299.'),
    ('Virgin Coconut Oil', '400 ml'): (349, 'Launch', 'The 500 ml size is 47% of revenue at Rs 418 to 467. A 400 ml fill must be priced about 20% lower to compare fairly per ml.'),
    ('Virgin Coconut Oil', '200 ml'): (219, 'Launch', '200 to 250 ml is 28% of revenue. Kapiva 250 ml sells at Rs 249, so 200 ml belongs near Rs 219.'),
    ('Virgin Coconut Oil', '100 ml'): (129, 'Hold', 'Under 1% of coconut revenue. Not worth a listing.'),
    ('Til (Sesame) Oil', '200 ml'): (249, 'Later', 'Sells only as a massage and body oil (3.5% of revenue). Nat Habit Rs 269, Goodcare Rs 214. Decide the positioning first.'),
    ('Til (Sesame) Oil', '400 ml'): (229, 'Hold', 'Cooking size. Idhayam 500 ml sells at Rs 285 and Patanjali at Rs 140, so 400 ml cannot go above about Rs 229.'),
    ('Til (Sesame) Oil', '100 ml'): (129, 'Hold', 'No market at this size (0.5% of revenue).'),
    ('Olive Oil', '400 ml'): (299, 'Hold', 'Pomace olive oil is bought in 1 L to 5 L packs; 500 ml and below is 0.5% of revenue. Better through distributors.'),
    ('Olive Oil', '200 ml'): (179, 'Hold', 'No online market for pomace at this size.'),
    ('Olive Oil', '100 ml'): (119, 'Hold', 'No online market for pomace at this size.'),
}
SHOP = costs['current_shop_prices_inr']          # prices already printed and on sale in the partner's shop
# MRP to print where there is no label yet, or where the current one is too low to list at the Amazon price (about 25% above it)
NEW_MRP = {('Rose Water', '100 ml'): 249, ('Rose Water', '200 ml'): 349, ('Kalonji Oil', '200 ml'): 549, ('Kalonji Oil', '400 ml'): 999,
           ('Neem Oil', '200 ml'): 319, ('Neem Oil', '400 ml'): 379, ('Castor Oil', '200 ml'): 249, ('Castor Oil', '400 ml'): 379,
           ('Til (Sesame) Oil', '200 ml'): 319, ('Til (Sesame) Oil', '400 ml'): 299, ('Olive Oil', '200 ml'): 229, ('Olive Oil', '400 ml'): 379}
ORDER = ['Rose Water', 'Kalonji Oil', 'Neem Oil', 'Castor Oil', 'Virgin Coconut Oil', 'Til (Sesame) Oil', 'Olive Oil']


def rate(table, market):
    return table.get(market, table['default'])


def unit(market, bottle, price, oil_per_litre=None):
    fill, bottle_cost, label = PACK[bottle]
    g_out, g_liq, g_pack = rate(ASSUMED['gst_on_sale'], market), rate(ASSUMED['gst_on_liquid'], market), ASSUMED['gst_on_packaging']
    net_price = price / (1 + g_out)                         # what is left after GST on the sale
    liquid = (oil_per_litre or OIL[market]) * fill / 1000 / (1 + g_liq)   # input GST is claimed back
    packaging = (bottle_cost + label + ASSUMED['outer_box_and_packing']) / (1 + g_pack)
    closing = next(fee for cap, fee in ASSUMED['closing_fee'] if price <= cap)
    fees = price * ASSUMED['referral_fee'] + closing + ASSUMED['shipping_fee'][bottle]
    profit = net_price - liquid - packaging - fees
    return dict(gst=round(price - net_price), liquid=round(liquid), packaging=round(packaging), fees=round(fees),
                profit=round(profit), marginPct=round(profit / price * 100))


def distributor_profit(market, bottle, mrp, oil_per_litre=None, share=None):
    fill, bottle_cost, label = PACK[bottle]
    g_out, g_liq, g_pack = rate(ASSUMED['gst_on_sale'], market), rate(ASSUMED['gst_on_liquid'], market), ASSUMED['gst_on_packaging']
    received = mrp * (share or ASSUMED['brand_share_of_mrp_via_distributor']) / (1 + g_out)
    liquid = (oil_per_litre or OIL[market]) * fill / 1000 / (1 + g_liq)
    return round(received - liquid - (bottle_cost + label + ASSUMED['carton_share_per_bottle']) / (1 + g_pack))


def mrp_fields(market, bottle, price, oil_per_litre=None):
    shop = SHOP.get(market, {}).get(bottle)
    mrp = NEW_MRP.get((market, bottle), shop)
    status = 'Keep' if shop and mrp == shop else ('Raise' if shop else 'New')
    return dict(shopPrice=shop if shop else '', mrp=mrp, mrpStatus=status, distributorProfit=distributor_profit(market, bottle, mrp, oil_per_litre),
                distributorProfit60=distributor_profit(market, bottle, mrp, oil_per_litre, 0.60),
                priceAtShopMrp=unit(market, bottle, shop, oil_per_litre)['profit'] if shop and shop < price else '')


rows = []
for market in ORDER:
    for bottle in ('100 ml', '200 ml', '400 ml'):
        price, verdict, why = PLAN[(market, bottle)]
        rows.append(dict(sku=f'{market} {bottle}', market=market, fill=bottle, benchmark='500 ml' if bottle == '400 ml' else bottle, price=price, **unit(market, bottle, price), **mrp_fields(market, bottle, price), verdict=verdict, why=why))
        if market.startswith('Til') and bottle == '200 ml':
            u = unit(market, bottle, price, OIL['Til (Sesame) Oil, non-edible'])
            rows.append(dict(sku=f'{market} {bottle} (non-edible grade)', market=market, fill=bottle, benchmark=bottle, price=price, **u, **mrp_fields(market, bottle, price, OIL['Til (Sesame) Oil, non-edible']), verdict='Later',
                             why='Same massage oil made with the Rs 220 a litre non-edible grade. Cannot be sold or labelled as food.'))
rank = {'Launch': 0, 'Later': 1, 'Hold': 2}
rows.sort(key=lambda r: (rank[r['verdict']], -r['profit']))
json.dump(rows, open(os.path.join(HERE, 'economics.json'), 'w'), ensure_ascii=False, indent=1)

# ---- three-month hypothesis towards the 10,000-bottle goal
# Amazon volume is tied to what existing sellers move in each launch size; the rest of each month's target goes through distributors.
MARKET = os.path.join(HERE, '..', 'amazon-market', 'cleaned-products.csv')   # written by amazon-market/classify.py
products = [dict(p, units=float(p['units'] or 0)) for p in csv.DictReader(open(MARKET, encoding='utf-8-sig'))]
launch = [r for r in rows if r['verdict'] == 'Launch']


def at_rank(r, pick):
    units = sorted((p['units'] for p in products if p['bucket'] == 'Core' and p['market'] == r['market']
                    and p['packSize'] == r['benchmark'] and p['units'] > 0), reverse=True)
    return pick(units) if units else 0


median = lambda u: u[(len(u) - 1) // 2]
tenth = lambda u: u[min(9, len(u) - 1)]
STEPS = [('Month 1', 'No ads, no reviews: half of a typical listing', lambda u: median(u) / 2, 1500),
         ('Month 2', 'First reviews: a typical listing', median, 4500),
         ('Month 3', 'Ads running: the tenth-best seller', tenth, 10000)]
mean = lambda key: sum(r[key] for r in launch) / len(launch)
stock = sum(r['liquid'] + r['packaging'] for r in launch) / len(launch)      # cost of one average bottle, ex GST
ramp = []
for month, basis, pick, target in STEPS:
    amazon = round(sum(at_rank(r, pick) for r in launch))
    amazon_profit = round(sum(at_rank(r, pick) * r['profit'] for r in launch))
    other = target - amazon
    ramp.append(dict(month=month, target=target, amazonBasis=basis, amazonBottles=amazon, amazonProfit=amazon_profit,
                     distributorBottles=other, distributorProfit40=round(other * mean('distributorProfit')),
                     distributorProfit60=round(other * mean('distributorProfit60')),
                     totalProfit40=amazon_profit + round(other * mean('distributorProfit')),
                     totalProfit60=amazon_profit + round(other * mean('distributorProfit60')),
                     stockCost=round(target * stock)))
json.dump(ramp, open(os.path.join(HERE, 'ramp.json'), 'w'), ensure_ascii=False, indent=1)

if __name__ == '__main__':
    print(f"{'sku':46} price  gst liquid pack fees profit margin verdict | shop mrp status distProfit profitAtShopMrp")
    for r in rows:
        print(f"{r['sku']:46} {r['price']:5} {r['gst']:4} {r['liquid']:6} {r['packaging']:4} {r['fees']:4} {r['profit']:6} {r['marginPct']:5}% {r['verdict']:7}| {str(r['shopPrice']):4} {r['mrp']:4} {r['mrpStatus']:5} {r['distributorProfit']:5} {r['priceAtShopMrp']}")
    launch = [r for r in rows if r['verdict'] == 'Launch']
    for m in ramp: print(m)
    print('launch SKUs', len(launch), 'mean profit', round(sum(r['profit'] for r in launch) / len(launch)), 'mean distributor profit', round(sum(r['distributorProfit'] for r in launch) / len(launch)))
