---
name: unayurved-label-new-size
description: Creates a new Unayurved label size from an existing 500ml master Canva design. Runs resize-design, audits both pages (front + back) against the 500ml reference for bleed, margins, column positions, and NET QTY text, then applies all fixes via MCP tools in one pass. Use when adding 200ml, 100ml, or any new size to an existing approved product.
---

# Unayurved label — new size

Creates a correctly formatted Canva design at a new label size from an approved 500ml master.

**Read first:** `brand/label-design-system.md` (dimensions, scale factors, typography minimums) and `brand/canva-mcp-workflow.md` (transaction pattern, coordinate system, known pitfalls).

**Reference examples:** `brand/examples/coconut-oil-back-prompt.md` contains notes on what breaks after resize and the MCP fixes that were applied — read it to understand what to audit.

---

## Inputs required

Ask the user for (or confirm from context):

1. **Source design ID** — the approved 500ml Canva design to resize from
2. **Target size** — e.g. "200ml" or "100ml"
3. **Target dimensions** — confirm against the design system:
   - 200ml: 61mm × 105mm = 230 × 396px
   - 100ml: 51mm × 80mm = 192 × 302px

---

## Step 1 — Resize

Load `mcp__claude_ai_Canva__resize-design`. Call it with the source design ID and target dimensions in px.

Record the new design ID from the response. This design has all-new element IDs — the source element IDs are no longer valid.

---

## Step 2 — Audit both pages

Open a read transaction on **page 1 (front label)**, then **page 2 (back label)** of the new design. For each, record every element's `element_id`, `top`, `left`, `width`, `height`, `type`, and visible text.

**Front label audit checklist:**
- [ ] Illustration images: `left` should be ≤ 0 (negative = bleeds left). `left + width` should exceed canvas width by ≥ 3px (bleeds right)
- [ ] NET QTY text: should say the target size (e.g. "200 ml"), not "500 ml"
- [ ] Any element with `left` > 5 and `type = image` is a bleed failure — flag it

**Back label audit checklist:**
- [ ] Body text left column: `left` should be ≥ 12px (200ml) or ≥ 10px (100ml). Values of 2–4px indicate auto-reflow collapse
- [ ] Nutrition column headers: left-column header `left` ≥ 18px (200ml) or ≥ 15px (100ml)
- [ ] Right value column: `left` ≈ 162px (200ml) or ≈ 135px (100ml)
- [ ] Table background element: `left` ≥ 11px (200ml) or ≥ 9.5px (100ml)
- [ ] Large right decorative image: right edge (`left + width`) should reach or exceed canvas width
- [ ] Font sizes: minimum api_px = 10 for 200ml, 12 for 100ml (= 6pt print minimum scaled)

---

## Step 3 — Apply all fixes in one transaction per page

Use the transaction pattern from `brand/canva-mcp-workflow.md`:
1. `read-design` with `open_transaction: true` to get transaction_id
2. Batch all operations for that page into one or two `edit-design` calls with `keep_open: true`
3. Final `edit-design` with `keep_open: false` to commit

**Front label fixes (apply as found in audit):**

For each illustration image that fails bleed:
```json
{ "type": "position_element", "element_id": "...", "left": <negative value> }
{ "type": "resize_element", "element_id": "...", "width": <canvas_width + |left| + 3> }
```

For NET QTY text:
```json
{ "type": "find_and_replace_text", "find": "500 ml", "replace": "<target size, e.g. 200 ml>" }
```

**Back label fixes (apply as found in audit):**

Position all body text elements to correct left margin. Position right-column value elements. Resize and reposition table background. Extend right decorative image to canvas edge.

Scale factor reference:
- 200ml (0.813×): body left → 12px, col headers left → 18px, right col → 162px
- 100ml (0.679×): body left → 10px, col headers left → 15px, right col → 135px

If any font sizes are below the minimum (10px for 200ml, 12px for 100ml), apply `format_text` operations to bring them up.

---

## Step 4 — Report

After both pages are committed, tell the user:
- New design ID and Canva edit URL
- Summary of fixes applied (count of elements repositioned, NET QTY corrected, font sizes adjusted)
- Any elements that could not be found or fixed (with element_id and reason)

Do not mark complete until both pages are committed.

---

## Scale reference

| Size | Canvas px | Scale | Body left margin | Col header left | Right col left | Table bg left |
|---|---|---|---|---|---|---|
| 500ml | 283×435 | 1.0× | 18.7px | 18.7px | varies | 11px |
| 200ml | 230×396 | 0.813× | 12px | 18px | 162px | 11px |
| 100ml | 192×302 | 0.679× | 10px | 15px | 135px | 9.5px |
