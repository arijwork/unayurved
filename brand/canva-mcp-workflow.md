# Canva MCP Workflow — Patterns and Pitfalls

Reference for any Claude Code session working on Unayurved labels via Canva MCP tools.

---

## Core transaction pattern

Every edit requires a transaction. Never call `edit-design` without a transaction ID.

```
1. read-design(design_id, page_index, open_transaction: true)
   → returns transaction_id + all element data

2. edit-design(design_id, transaction_id, operations: [...], keep_open: true)
   → apply operations without committing (batch as many as possible)

3. edit-design(design_id, transaction_id, operations: [], keep_open: false)
   → commit (no operations needed on the final call, just close the transaction)
```

Batch all operations for a page into as few `edit-design` calls as possible — each call is a round trip.

---

## Coordinate system

- Unit: pixels (px)
- 1mm = 3.77px
- Top-left is origin (0,0)
- `top` = distance from top edge
- `left` = distance from left edge
- Negative `left` = element extends past the left canvas edge (bleed)
- Element `width + left > canvas_width` = right bleed

**Canvas sizes in px:**
- 500ml: 283 × 435px
- 200ml: 230 × 396px
- 100ml: 192 × 302px

---

## Font size conversion

Canva API uses px internally; print/display uses pt.

```
display_pt = api_px × 0.75
api_px     = display_pt ÷ 0.75
```

Minimum readable font size for commercial digital press: **6pt = 8px api_px**

For 200ml (0.81× scale): minimum is 9.9px api_px. Round up to 10px.
For 100ml (0.68× scale): minimum is 11.8px api_px. Round up to 12px (8pt display).

---

## Bleed mechanics

Illustration images on front labels MUST bleed past all canvas edges. Canva's resize-design will pull elements inward and break bleed. After any resize, audit every full-bleed image element.

**Target for front label illustrations:**
- Left edge: `left` should be negative (≤ −3px typically)
- Right edge: `left + width` should exceed canvas width by ≥ 3px
- Top and bottom: same principle

---

## resize-design behaviour

`resize-design` creates a brand new design with all-new element IDs. It does NOT preserve the working layout from the source.

After every resize:
1. Read the new design to get the new element IDs (they won't match the source)
2. Audit positions: margins, bleeds, column alignments
3. Fix manually using position_element and resize_element operations
4. Fix NET QTY text (will still say the source size)
5. Fix font sizes that dropped below the 6pt minimum

---

## Common element operations

**Position an element:**
```json
{
  "type": "position_element",
  "element_id": "LB...",
  "top": 42,
  "left": 18.7
}
```

**Resize an element:**
```json
{
  "type": "resize_element",
  "element_id": "LB...",
  "width": 244,
  "height": 14
}
```

**Replace text:**
```json
{
  "type": "find_and_replace_text",
  "find": "500 ml",
  "replace": "200 ml"
}
```

**Format text (font size):**
```json
{
  "type": "format_text",
  "element_id": "LB...",
  "font_size": 10
}
```

---

## Back label — standard left margin

After resize-design, all back label text elements collapse to ~2–4px left margin. Target left margins:

| Element | 500ml | 200ml | 100ml |
|---|---|---|---|
| Body text (left column) | 18.7px | 12px | 10px |
| Nutrition col headers | 18.7px | 18px | 15px |
| Right value column | varies | 162px | 135px |
| Table background left | 11px | 11px | 9.5px |

---

## Known element IDs — 500ml working copy (DAHXzNXZGDY)

Back label page 2 elements:
- `LBmqTjcvd2ngWy50`: Header bar (green rect)
- `LBrYb8pbNSs7hhKp`: Header text
- `LBFylB3kGztqv1RX`: "Ingredients" label
- `LBHC9pC2Ml3TCGrR`: Ingredient value text
- `LBjDM8V0WgNtXRtm`: "Nutrition Information" header
- `LBxcnnxZCKSZCtR5`: "Nutrient" column header
- `LBHPM8DTzFFjRpBh`: "Per 100 ml" column header
- `LBpTBVcs9Fbngcm3`: Table background image
- `LBqCThC5ZtxTZ6JP`: Large right-side decorative image

Note: 200ml and 100ml have the same element ID slugs (resize-design preserves ID names) but positions differ from the 500ml reference.

---

## Active design file IDs

| Product | Size | Design ID | Edit URL |
|---|---|---|---|
| Virgin Coconut Oil | 500ml (master) | DAHXzNXZGDY | https://www.canva.com/d/iUwPuyVhv7gZ38e |
| Virgin Coconut Oil | 200ml | DAHXzqqAOcU | https://www.canva.com/d/ovWrkMx8EYs4wJX |
| Virgin Coconut Oil | 100ml | DAHXzmkQA9E | https://www.canva.com/d/an6QDnKFL2xYTUn |
| Virgin Coconut Oil | V1 approved (DO NOT EDIT) | DAHXtJzEroQ | — |

---

## Print export checklist (before sending to printer)

- [ ] Dimensions confirmed in Canva (File → Resize → check mm values)
- [ ] All illustration images bleed past canvas edges on all sides
- [ ] Smallest text ≥ 6pt (≥ 8px api_px; higher for smaller label sizes)
- [ ] NET QTY correct for each size
- [ ] Logo placed manually (Canva AI leaves this empty)
- [ ] No duplicate taglines or placeholder text remaining
- [ ] FSSAI mandatory fields present: ingredients, nutrition table, net qty, manufacturer name, FSSAI lic no, country of origin, MRP, best before, batch no
- [ ] Export as PDF → Print (not PDF Standard) at 300 DPI
- [ ] Ask printer if they need CMYK or accept RGB PDF — Canva exports RGB by default; printer may need a CMYK conversion
