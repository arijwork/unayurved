# Unayurved — Label Design System
*Reference document. Every future label starts here, not from scratch.*

---

## 1. Confirmed Label Dimensions

These are the physical dimensions of the printed label for each bottle SKU.
Width is 40% of bottle circumference (standard for separate front/back labels).
Height is the bottle's flat surface height minus 10mm (5mm margin top + 5mm bottom).

| SKU | Circumference | Flat surface height | **Label Width** | **Label Height** | Scale vs 500ml |
|---|---|---|---|---|---|
| 500ml | ~187mm | ~125mm | **75mm** | **115mm** | 1.00 (reference) |
| 200ml | 152mm | 115mm | **61mm** | **105mm** | 0.81× |
| 100ml | 127mm | 90mm | **51mm** | **80mm** | 0.68× |

**Rule:** When a new bottle SKU is added, measure flat surface height and circumference.
Label width = circumference × 0.40. Label height = flat surface height − 10mm.

---

## 2. Print Specifications

- **Printer type:** Commercial digital press
- **Minimum body text:** 6pt (below this is not reliably legible at print)
- **Minimum regulatory text:** 7pt (FSSAI mandatory declarations)
- **Bleed:** 3mm on all four edges
- **Safe inner margin:** 4mm from cut edge (no text or critical elements inside this margin)
- **Label type:** Separate front and back labels (not a single wrap-around)
- **Background:** Pure white (#FFFFFF) — confirmed working at print

---

## 3. Zone Proportions (Front Label)

These ratios apply to all sizes. Multiply the total label height by each ratio to get the zone height.

| Zone | Ratio | 500ml height | 200ml height | 100ml height |
|---|---|---|---|---|
| Logo zone (mark + wordmark + tagline) | 30% | 34.5mm | 31.5mm | 24mm |
| Text zone (claim + product name + descriptor) | 25% | 28.8mm | 26.3mm | 20mm |
| Illustration zone (full-bleed botanical) | 45% | 51.7mm | 47.3mm | 36mm |
| **Total** | **100%** | **115mm** | **105mm** | **80mm** |

---

## 4. Zone Proportions (Back Label)

| Zone | Ratio | 500ml height | 200ml height | 100ml height |
|---|---|---|---|---|
| Header strip (product name in green bar) | 8% | 9.2mm | 8.4mm | 6.4mm |
| Content zone (all text and table) | 85% | 97.8mm | 89.3mm | 68mm |
| Footer strip (MRP / batch / barcode row) | 7% | 8mm | 7.4mm | 5.6mm |
| **Total** | **100%** | **115mm** | **105mm** | **80mm** |

---

## 5. Typography Scale

### Base sizes (500ml — the reference)

| Text element | Font | Weight | Size | Colour |
|---|---|---|---|---|
| Logo mark | Unayurved SVG asset | — | 18mm tall | #1E7A34 |
| Wordmark "UNAYURVED" | Josefin Slab | Bold | 13pt | #1E7A34 |
| Tagline "Unani \| Ayurvedic" | Lora | Italic | 9pt | #5C5C4A |
| Processing claim (COLD PRESSED) | Josefin Sans | Light | 7pt | #999990 |
| Claim rules (flanking lines) | — | — | 0.5pt | #CCCCCC |
| Product name line 1 | Playfair Display | Black | 38pt | #1A1A18 |
| Product name line 2 | Playfair Display | Black | 38pt | #1A1A18 |
| Descriptor text | DM Sans | Light | 7pt | #999990 |
| Back: header strip text | Josefin Sans | Light | 8pt | #FFFFFF |
| Back: section headers | DM Sans | SemiBold | 7pt | #1A1A18 |
| Back: body text | DM Sans | Regular | 6pt | #1A1A18 |
| Back: table text | DM Sans | Regular | 6pt | #1A1A18 |
| Back: footer row | DM Sans | Regular | 5.5pt | #555555 |
| NET QTY overlay | DM Sans | Bold | 7pt | #FFFFFF |

### Scaled sizes (200ml — scale factor 0.81)

| Text element | Calculated | Applied (floor = 6pt) |
|---|---|---|
| Wordmark | 10.5pt | **11pt** |
| Tagline | 7.3pt | **7pt** |
| Processing claim | 5.7pt | **6pt** ← floor |
| Product name | 30.8pt | **31pt** |
| Descriptor text | 5.7pt | **6pt** ← floor |
| Back body text | 4.9pt | **6pt** ← floor |
| Back table text | 4.9pt | **6pt** ← floor |
| Back footer | 4.5pt | **6pt** ← floor |

### Scaled sizes (100ml — scale factor 0.68)

| Text element | Calculated | Applied (floor = 6pt) |
|---|---|---|
| Wordmark | 8.8pt | **9pt** |
| Tagline | 6.1pt | **6pt** |
| Processing claim | 4.8pt | **6pt** ← floor |
| Product name | 25.8pt | **26pt** |
| Descriptor text | 4.8pt | **6pt** ← floor |
| Back body text | 4.1pt | **6pt** ← floor |
| Back table text | 4.1pt | **6pt** ← floor |
| Back footer | 3.7pt | **6pt** ← floor |

**Floor rule:** No text on any label may go below 6pt. If scaling pushes a size below 6pt,
keep it at 6pt and instead reduce content volume (remove lines, not size).

---

## 6. Content Budget (Back Label)

At 6pt on commercial digital press, one line of text occupies approximately 3mm of height
(6pt × 1.4 line height = 8.4pt = 2.97mm).

| SKU | Content zone height | Usable after internal padding | **Maximum lines** |
|---|---|---|---|
| 500ml | 97.8mm | 88mm | **~29 lines** |
| 200ml | 89.3mm | 80mm | **~26 lines** |
| 100ml | 68mm | 60mm | **~20 lines** |

**The current 500ml back label has ~40 lines. It must be reduced to ~29.**

### Content priority — what to cut when the budget is tight

**Must keep (FSSAI mandatory, cannot remove):**
- Product name
- Net quantity
- Ingredients
- Nutritional information (can abbreviate — see below)
- Manufacturer name and address
- FSSAI Lic. No.
- Best before date
- Batch number
- MRP (incl. taxes)
- Country of origin
- Vegetarian symbol

**Can abbreviate:**
- Nutrition table: at 200ml and 100ml, drop the "Per Serving" column — use only "Per 100ml"
- Nutrition table at 100ml: reduce to 7 rows (Energy, Total Fat, Sat Fat, Carbs, Protein, Sodium — drop sub-rows for MUFA/PUFA/Trans Fat)
- Storage: reduce to 1 line ("Store cool and dry. Cap tightly after use.")
- % Daily Values note: drop on 100ml if budget is exceeded

**Can remove entirely:**
- "How to use" section (not FSSAI mandatory for oils)
- Logo on back (appears on front — no need to repeat)
- Watermark botanical background (optional decorative element, contributes to readability problems)

---

## 7. Scaling Rules Summary

When adapting from 500ml to a smaller size:

| What changes | What stays fixed |
|---|---|
| Label physical dimensions | Brand colours (always same hex) |
| Font pt sizes (scaled, subject to floor) | Font families (always same typefaces) |
| Logo mark height (scales proportionally) | Zone ratios (always same %) |
| Illustration detail level (simpler at smaller sizes) | Minimum margins (3mm bleed + 4mm safe) |
| Content volume (fewer lines at smaller sizes) | Typography hierarchy (same tier structure) |

---

## 8. Colour Tokens (fixed across all sizes and products)

| Token | Hex | Use |
|---|---|---|
| Brand green | #1E7A34 | Logo mark, wordmark, header strip |
| Header strip dark | #1A5C20 | Back label top bar background |
| Near-black | #1A1A18 | Product name, section headers |
| Mid-grey | #999990 | Descriptor text, claim text |
| Olive-grey | #5C5C4A | Tagline |
| White | #FFFFFF | Label background, text on green |
| Rule line | #CCCCCC | Thin decorative rules |

*Product accent colours (e.g. rose pink for rose water) are added per-product
but do not replace the above tokens — they supplement them in the illustration zone only.*

---

## 9. Application Checklist (before sending any label to print)

- [ ] Label dimensions match the confirmed table in Section 1
- [ ] 3mm bleed added on all sides in the design file
- [ ] No text or critical element inside the 4mm safe inner margin
- [ ] Minimum font size check: no text below 6pt (7pt for FSSAI mandatory)
- [ ] Back label line count within the budget for this SKU (Section 6)
- [ ] Product name matches on front AND back (e.g. both say "Extra Virgin" or both say "Virgin")
- [ ] FSSAI mandatory fields all present (Section 6 priority list)
- [ ] Veg dot present on both front and back
- [ ] Exported at 300 DPI minimum, CMYK colour mode, PDF/X-1a format for commercial print
