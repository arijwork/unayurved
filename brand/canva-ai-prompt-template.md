# Canva AI Prompt Template — Unayurved Front Labels

Use this template to generate the front label for any new product. Fill every `[PLACEHOLDER]` before pasting into Canva AI. The prompt is split into two blocks — Illustration Zone and Text Zone — because Canva AI handles them differently. Generate front first, then write the back label using the back-label template at the bottom.

---

## Step 0 — Product brief (fill this before writing the prompt)

| Field | Value |
|---|---|
| Product name (2 words max) | e.g. ROSE WATER |
| Processing / origin claim | e.g. STEAM DISTILLED / COLD PRESSED / WOOD PRESSED |
| Key descriptor lines (2 lines) | e.g. "Distilled from Damask Rose Petals" / "100% Pure · Preservative Free" |
| Net qty | e.g. 500 ml / 200 ml / 100 ml |
| Botanical subject | e.g. Damask roses + foliage / coconuts + palm fronds / nigella seeds + flowers |
| Illustration accent colour | e.g. #C0485A (dusty rose) / keep forest green (#1A6B1A) for most oils |
| All nutritional data (per 100ml) | Energy, Total Fat, Sat Fat, MUFA, PUFA, Trans Fat, Cholesterol, Carbs, Sugars, Protein, Sodium |
| Ingredients | e.g. 100% Cold Pressed Virgin Coconut Oil |
| Label size | 500ml = 75×115mm / 200ml = 61×105mm / 100ml = 51×80mm |

---

## Front Label Prompt

```
Create a premium product label illustration for a bottle of [PRODUCT NAME], [NET QTY]. 
Portrait format, tall and narrow — [WIDTH]mm wide × [HEIGHT]mm tall. 
Pure white background, smooth and clean.

**ILLUSTRATION ZONE — bottom 48% of the label, bleeds edge to edge:**

A richly detailed, photographic-realistic botanical scene. [DESCRIBE MAIN BOTANICAL: e.g. "Several fully open Damask rose blooms (Rosa damascena), deep dusty rose-red (#C0485A range), petals full and layered, slightly dewy with soft shadows. A few loose petals scattered at the base."]. 

Around and behind [BOTANICAL SUBJECT], dark glossy green foliage sweeps in from both sides and the bottom — same compositional structure as the label (framing the centrepiece). Leaves are rich and layered with visible veins.

[OPTIONAL: add buds, water droplets, secondary botanical details here]

Bottom-left of the illustration in small bold white text: NET QTY: [NET QTY]
Bottom-right: small green square with green circle (Indian vegetarian symbol)

Style: photographic-realistic botanical illustration. Rich and tactile. Not watercolour, not flat.

---

**TEXT ZONE — top 52% of the label, pure white background:**

Leave the top 30% completely empty — this is reserved for the logo which will be placed manually.

Below the empty logo zone, add the following text elements in exact order, all horizontally centred:

**Element 1 — Processing claim line:**
A thin horizontal rule in [ACCENT COLOUR] — then the text — then another thin rule in [ACCENT COLOUR].
Text: [PROCESSING CLAIM IN CAPS]
Font: Josefin Sans, Light weight, all uppercase
Colour: [MUTED VERSION OF ACCENT COLOUR, e.g. #A07878 for rose / #4A7A4A for green]
Size: approximately 9pt
Letter spacing: very wide, approximately +250 tracking

**Element 2 — Product name, two lines:**
Line 1: [WORD 1 OF PRODUCT NAME]
Line 2: [WORD 2 OF PRODUCT NAME]
Font: Playfair Display, Black weight (heaviest available). High-contrast thick-thin strokes, classic serif.
Colour: #1A1A18 (near-black, slightly warm)
Size: very large — each word fills close to the full label width
Letter spacing: slightly negative, -10 to -20
Line spacing: 0.88 (tight)

**Element 3 — Descriptor lines:**
Line 1: [DESCRIPTOR LINE 1]
Line 2: [DESCRIPTOR LINE 2]
Font: DM Sans, Light weight
Colour: #999990 (light grey)
Size: approximately 8pt
Letter spacing: normal
Line spacing: 1.5
Position: clear gap below [WORD 2] before these lines, then another clear gap before illustration begins

---

**Overall feel:** Minimal in the text zone, all richness concentrated in the illustration. Premium Indian wellness brand — like Kama Ayurveda or Forest Essentials, not pharma.
```

---

## What Canva AI typically gets wrong (fix checklist after generation)

- [ ] **Tagline duplicated** — "Unani | Ayurvedic" or descriptor may appear twice. Delete the extra.
- [ ] **Logo placeholder inserted** — Canva AI sometimes puts a generic logo. Delete it; you'll place the real logo manually.
- [ ] **Dimensions not set to spec** — Go to Resize & Magic Switch and confirm mm dimensions before any editing.
- [ ] **Illustration doesn't bleed** — Check that botanical image extends to all four edges with no white gap. If it stops short, resize the element until edges disappear off canvas.
- [ ] **NET QTY says wrong size** — If you generated from a 500ml prompt and resized, find and replace "500 ml" with the correct size.
- [ ] **Font substituted** — If Playfair Display Black is unavailable, Canva may substitute. Check and manually set the font after generation.

---

## What to do after Canva AI generates the front label

1. Set exact dimensions (File → Resize)
2. Delete duplicate tagline if present
3. Place actual Unayurved logo SVG (flower mark + wordmark) into the reserved top zone
4. Verify illustration bleeds on all edges
5. Check NET QTY text
6. Screenshot and review at 100% — check legibility of descriptor lines at print size
7. Approved? → Proceed to back label

---

## Back Label Prompt

The back label is mostly text — do not ask Canva AI to generate illustration here. Use Canva AI's text-layout generation with this prompt, or build manually using the design system.

```
Create the back label for Unayurved [PRODUCT NAME] [NET QTY]. 
Same dimensions: [WIDTH]mm × [HEIGHT]mm. Warm cream background (unbleached linen, subtle paper texture). Clean, organised, premium — like a high-end Indian natural product brand.

**Top strip:** Narrow dark forest green bar (#1A3A1A) across the full width at the very top. Inside it, centred, in small white uppercase spaced letters: [PRODUCT NAME]. Veg dot (green square, green circle) at the right end of the strip.

**Just below green strip:** Single thin horizontal green rule line.

**Ingredients section:**
Label: INGREDIENTS (small bold dark grey uppercase)
Body: [FULL INGREDIENTS TEXT]

**Nutrition Information table:**
Header: NUTRITION INFORMATION (small bold dark grey uppercase)

Two-column table (Nutrient / Per 100ml) with these rows:
| Nutrient | Per 100 ml |
|---|---|
| Energy | [VALUE] kcal |
| Total Fat | [VALUE] g |
| — Saturated Fat | [VALUE] g |
| — Monounsaturated Fat | [VALUE] g |
| — Polyunsaturated Fat | [VALUE] g |
| — Trans Fat | [VALUE] g |
| Cholesterol | [VALUE] mg |
| Total Carbohydrates | [VALUE] g |
| — Total Sugars | [VALUE] g |
| Protein | [VALUE] g |
| Sodium | [VALUE] mg |

Table styling: thin grey borders, alternating faint cream/white rows, column headers bold. All text small but legible.

Below table: *"% Daily Values are based on a 2000 kcal diet."* — very small italic grey.

**Storage:** [STORAGE TEXT — max 2 lines]

**Manufacturer block (small, left-aligned):**
Manufactured by: Unayurved
Address: [To be filled]
Customer Care: [To be filled]

**FSSAI block:**
FSSAI Lic. No.: [Pending]
[Rectangular outline labelled "FSSAI" as placeholder]

**Bottom row (full width, very small):**
MRP: ₹ ___ (Incl. of all taxes) | Best Before: ___/___ | Batch No.: _______ | Mfg. Date: ___/___

**Bottom-right:** Rectangular blank box ~20mm × 12mm, thin grey border, labelled "Barcode" in very small grey.

**Bottom-left:** Country of Origin: India

Background: pure white or very faint cream. NO botanical watermark behind the text — that killed legibility in testing.
```

---

## Product line — accent colour guide

| Product | Main botanical | Accent colour | Processing claim |
|---|---|---|---|
| Virgin Coconut Oil | Coconuts + palm fronds | Forest green #1A6B1A | COLD PRESSED |
| Rose Water | Damask roses | Dusty rose #C0485A | STEAM DISTILLED |
| Kalonji Oil | Nigella seeds + flowers | Deep amber #8B4513 | COLD PRESSED |
| Neem Oil | Neem leaves + white flowers | Olive green #5A7A1A | COLD PRESSED |
| Sesame Oil | Sesame stems + seeds | Warm gold #B8860B | COLD PRESSED |

---

## Sizing rules (from label-design-system.md)

| Size | Width | Height | Scale factor |
|---|---|---|---|
| 500ml | 75mm | 115mm | 1.0× (reference) |
| 200ml | 61mm | 105mm | 0.81× |
| 100ml | 51mm | 80mm | 0.68× |

Recommended workflow: generate and approve 500ml first → use Canva resize-design for 200ml and 100ml → audit all elements for bleed and margin after resize (Canva auto-reflow breaks positioning) → apply fixes using MCP tools.
