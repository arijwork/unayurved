# Pre-computed Target Coordinates by Size

Derived from 500ml reference design (283×435px) using per-axis scale factors.  
Scale W = target_width / 283. Scale H = target_height / 435.

These are the **expected** positions after resize + fix. Use them directly in `position_element` and `resize_element` operations — no calculation needed.

---

## 200ml — 230×396px (Scale W = 0.813, Scale H = 0.910)

### Font minimums
All text elements must have `fontSize ≥ 10px`. If the resized font is below 10, apply `format_text` to set it to 10.

### BACK LABEL — Page 2

| Element | Expected top | Expected left | Expected font | Fix if left deviation > |
|---|---|---|---|---|
| Top bar | 0 | 0 | — | 1px |
| "ROSE water" in bar | 5.3 | 43.7 | 10.8 → set 10 (min) | 1px |
| Ingredients label | 37.3 | 12.8 | 9.7 → set 10 (min) | 1px |
| Ingredients content text | 54.1 | 11.9 | 9.1 → set 10 (min) | 1px |
| Nutrition Information label | 73.2 | 12.3 | 9.7 → set 10 (min) | 1px |
| Table header "Nutrient" | 94.1 | 18.5 | 8.5 → set 10 (min) | 1px |
| Table header "Per 100 ml" | 92.1 | 153.8 | 8.5 → set 10 (min) | 1px |
| Energy (label) | 108.6 | 18.5 | 8.2 → set 10 (min) | 1px |
| Energy (value) | 106.9 | 153.8 | 8.2 → set 10 (min) | 1px |
| Total Fat (label) | 122.5 | 18.5 | 8.2 → set 10 (min) | 1px |
| Total Fat (value) | 122.0 | 153.8 | 8.2 → set 10 (min) | 1px |
| — Saturated Fat (label) | 135.8 | 20.6 | 8.2 → set 10 (min) | 1px |
| — Saturated Fat (value) | 135.6 | 153.8 | 8.2 → set 10 (min) | 1px |
| — MUFA (label) | 149.1 | 20.8 | 8.2 → set 10 (min) | 1px |
| — MUFA (value) | 149.1 | 153.8 | 8.2 → set 10 (min) | 1px |
| — PUFA (label) | 163.0 | 20.8 | 8.2 → set 10 (min) | 1px |
| — PUFA (value) | 163.3 | 153.8 | 8.2 → set 10 (min) | 1px |
| — Trans Fat (label) | 176.3 | 20.7 | 8.2 → set 10 (min) | 1px |
| — Trans Fat (value) | 176.3 | 153.8 | 8.2 → set 10 (min) | 1px |
| Cholesterol (label) | 189.2 | 18.5 | 8.2 → set 10 (min) | 1px |
| Cholesterol (value) | 189.8 | 153.8 | 8.2 → set 10 (min) | 1px |
| Total Carbs (label) | 203.0 | 18.5 | 8.2 → set 10 (min) | 1px |
| — Total Sugars (label) | 215.7 | 20.6 | 8.2 → set 10 (min) | 1px |
| — Total Sugars (value) | 217.5 | 153.8 | 8.2 → set 10 (min) | 1px |
| Protein (label) | 229.6 | 18.5 | 8.2 → set 10 (min) | 1px |
| Protein (value) | 229.6 | 153.8 | 8.2 → set 10 (min) | 1px |
| Sodium (label) | 243.0 | 18.5 | 8.2 → set 10 (min) | 1px |
| Sodium (value) | 244.0 | 153.8 | 8.2 → set 10 (min) | 1px |
| Storage block | 274.3 | 12.0 | 8.5 → set 10 (min) | 1px |
| Manufactured by | 296.7 | 12.0 | 8.5 → set 10 (min) | 1px |
| Address | 298.1 | 12.0 | 8.5 → set 10 (min) | 1px |
| MRP | 317.9 | 12.0 | 8.5 → set 10 (min) | 1px |
| Best Before | 328.4 | 12.0 | 8.5 → set 10 (min) | 1px |
| Mfg. Date | 340.9 | 12.0 | 8.5 → set 10 (min) | 1px |
| USP(per ml) | 360.0 | 12.0 | 8.5 → set 10 (min) | 1px |
| Country of origin | 375.6 | 12.0 | 8.5 → set 10 (min) | 1px |
| Rose illustration | 295.0 | 147.0 | — | 2px |

### FRONT LABEL — Page 1 (200ml)

| Element | Expected top | Expected left | Note |
|---|---|---|---|
| Logo group | ≥ 8, ≤ 15 | 64.5 | Must not clip at top |
| "Steam Distilled" group | 103.2 | 61.1 | Check bottom edge of logo group |
| "Rose" text | 112.2 | 54.3 | Font: 47.6px |
| "Water" text | 150.7 | 49.8 | Font: 38.3px |
| Descriptors text | 196.4 | 52.7 | Font: 5.9px (too small — set 8) |
| NET QTY text | 327.5 | 14.1 | Must say "200 ml" |
| Veg symbol | 313.9 | 197.4 | — |

---

## 100ml — 192×302px (Scale W = 0.678, Scale H = 0.694)

### Font minimums
All text elements must have `fontSize ≥ 12px`. If the resized font is below 12, apply `format_text` to set it to 12.

> **Note:** 12px minimum at 100ml is a print legibility requirement. Even though scaling produces 6–7px values, do not use those — set everything to 12px minimum.

### BACK LABEL — Page 2

| Element | Expected top | Expected left | Expected font | Fix if left deviation > |
|---|---|---|---|---|
| Top bar | 0 | 0 | — | 1px |
| "ROSE water" in bar | 4.0 | 36.5 | 9.2 → set 12 (min) | 1px |
| Ingredients label | 28.4 | 10.7 | 7.4 → set 12 (min) | 1px |
| Ingredients content text | 41.3 | 10.0 | 6.9 → set 12 (min) | 1px |
| Nutrition Information label | 55.8 | 10.3 | 7.4 → set 12 (min) | 1px |
| Table header "Nutrient" | 71.8 | 15.4 | 6.5 → set 12 (min) | 1px |
| Table header "Per 100 ml" | 70.2 | 128.4 | 6.5 → set 12 (min) | 1px |
| Energy (label) | 82.8 | 15.4 | 6.2 → set 12 (min) | 1px |
| Energy (value) | 81.6 | 128.4 | 6.2 → set 12 (min) | 1px |
| Total Fat (label) | 93.5 | 15.4 | 6.2 → set 12 (min) | 1px |
| Total Fat (value) | 93.1 | 128.4 | 6.2 → set 12 (min) | 1px |
| — Saturated Fat (label) | 103.6 | 17.2 | 6.2 → set 12 (min) | 1px |
| — Saturated Fat (value) | 103.5 | 128.4 | 6.2 → set 12 (min) | 1px |
| — MUFA (label) | 113.8 | 17.4 | 6.2 → set 12 (min) | 1px |
| — MUFA (value) | 113.8 | 128.4 | 6.2 → set 12 (min) | 1px |
| — PUFA (label) | 124.4 | 17.4 | 6.2 → set 12 (min) | 1px |
| — PUFA (value) | 124.6 | 128.4 | 6.2 → set 12 (min) | 1px |
| — Trans Fat (label) | 134.5 | 17.3 | 6.2 → set 12 (min) | 1px |
| — Trans Fat (value) | 134.5 | 128.4 | 6.2 → set 12 (min) | 1px |
| Cholesterol (label) | 144.3 | 15.4 | 6.2 → set 12 (min) | 1px |
| Cholesterol (value) | 144.6 | 128.4 | 6.2 → set 12 (min) | 1px |
| Total Carbs (label) | 154.9 | 15.4 | 6.2 → set 12 (min) | 1px |
| — Total Sugars (label) | 164.6 | 17.2 | 6.2 → set 12 (min) | 1px |
| — Total Sugars (value) | 165.9 | 128.4 | 6.2 → set 12 (min) | 1px |
| Protein (label) | 175.2 | 15.4 | 6.2 → set 12 (min) | 1px |
| Protein (value) | 175.2 | 128.4 | 6.2 → set 12 (min) | 1px |
| Sodium (label) | 185.5 | 15.4 | 6.2 → set 12 (min) | 1px |
| Sodium (value) | 185.6 | 128.4 | 6.2 → set 12 (min) | 1px |
| Storage block | 209.2 | 10.0 | 6.5 → set 12 (min) | 1px |
| Manufactured by | 226.3 | 10.0 | 6.5 → set 12 (min) | 1px |
| Address | 227.3 | 10.0 | 6.5 → set 12 (min) | 1px |
| MRP | 242.9 | 10.0 | 6.5 → set 12 (min) | 1px |
| Best Before | 250.3 | 10.0 | 6.5 → set 12 (min) | 1px |
| Mfg. Date | 259.9 | 10.0 | 6.5 → set 12 (min) | 1px |
| USP(per ml) | 274.7 | 10.0 | 6.5 → set 12 (min) | 1px |
| Country of origin | 286.4 | 10.0 | 6.5 → set 12 (min) | 1px |
| Rose illustration | 225.3 | 126.0 | — | 2px |

### FRONT LABEL — Page 1 (100ml)

| Element | Expected top | Expected left | Note |
|---|---|---|---|
| Logo group | ≥ 6, ≤ 12 | 53.8 | Must not clip at top |
| "Steam Distilled" group | 78.8 | 55.5 | Check bottom edge of logo group |
| "Rose" text | 85.8 | 45.3 | Font: 39.7px |
| "Water" text | 114.9 | 50.5 | Font: 28.8px |
| Descriptors text | 149.9 | 58.1 | Font: 4.6px → set 8 (min) |
| NET QTY text | 250.1 | 22.5 | Must say "100 ml" |
| Veg symbol | 240.0 | 164.9 | — |

---

## How to use this file

1. After resizing, read the design to get actual element coordinates.
2. For each element above, compare `actual_left` vs `expected_left` and `actual_font` vs `expected_font`.
3. Generate `position_element` for any position deviation > 1px.
4. Generate `format_text` for any font below the stated minimum.
5. Batch all operations into a single transaction per page.
6. After commit, re-read and verify against this table.

---

## Source reference

All expected values derived from rose water 500ml master (DAHX9sxCpt4) back label coordinates × scale factors:
- 200ml: Scale W = 230/283 = 0.8127, Scale H = 396/435 = 0.9103
- 100ml: Scale W = 192/283 = 0.6784, Scale H = 302/435 = 0.6943
