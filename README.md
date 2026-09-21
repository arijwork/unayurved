# Unayurved

Product label system for Unayurved — a modern Unani + Ayurvedic wellness brand.

## Status

- [x] Brand language document
- [x] Brand tokens (CSS)
- [x] 500ml front label
- [x] 500ml back label
- [ ] 250ml labels
- [ ] 100ml labels

## How to print a label

1. Open the `.html` file in Chrome (internet connection required for Google Fonts)
2. Press `Cmd+P` (Print)
3. Set **Destination** → Save as PDF
4. Set **Paper size** → Custom → enter exact label dimensions
5. Set **Margins** → None
6. Set **Scale** → 100%
7. Enable **Background graphics**
8. Save PDF → send to label printer

## Label dimensions

| Size | Width × Height |
|------|---------------|
| 500ml | 75mm × 115mm |
| 250ml | 50mm × 80mm |
| 100ml | 45mm × 70mm |

## Structure

```
brand/
  brand-language.md   ← positioning, visual direction, color palette, typography, claims rules
  tokens.css          ← CSS variables — single source of truth for all labels
  assets/
    logo-primary.png  ← Logo 1 (print labels)
    logo-digital.png  ← Logo 2 (website, social — not used on labels)
labels/
  500ml/
    front.html
    back.html
decisions/
  decision-log.md     ← every significant design decision with rationale
exports/              ← PDF and PNG exports go here
```

## Before final export

- Fill in: manufacturer address, FSSAI licence number, customer care contact
- Generate actual barcode (EAN-13 recommended for retail India)
- Verify FSSAI fields checklist against back label
- Print on paper, cut to size, test readability of smallest text at 500ml dimensions
