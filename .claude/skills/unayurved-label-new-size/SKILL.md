---
name: unayurved-label-new-size
description: Creates a new Unayurved label size from an existing 500ml master Canva design. Runs resize-design, then does a systematic delta-audit (actual position vs. expected scaled position) for both pages, generates fix operations for every deviation, applies font-size corrections, and verifies after committing. Use when adding 200ml, 100ml, or any new size to an existing approved product.
---

# Unayurved label — new size

Creates a correctly formatted Canva design at a new label size from an approved 500ml master.

**Read first:** `brand/label-design-system.md` (dimensions, scale factors, typography minimums) and `brand/canva-mcp-workflow.md` (transaction pattern, coordinate system, known pitfalls).

**Pre-computed targets:** `targets.md` in this skill directory contains the exact expected coordinates for every key back-label element at 200ml and 100ml — use those values directly in fix operations rather than computing on the fly.

---

## Inputs required

Ask the user for (or confirm from context):

1. **Source design ID** — the approved 500ml Canva design to resize from
2. **Target size** — e.g. "200ml" or "100ml"
3. **Target dimensions** — confirm against the design system:
   - 200ml: 61mm × 105mm = 230 × 396px
   - 100ml: 51mm × 80mm = 192 × 302px

---

## Scale factors

These govern all position and font-size conversions from 500ml reference:

| Size | Canvas | Scale W (230/283) | Scale H (396/435) | Font scale |
|---|---|---|---|---|
| 500ml | 283×435 | 1.000 | 1.000 | 1.000 |
| 200ml | 230×396 | 0.813 | 0.910 | 0.910 |
| 100ml | 192×302 | 0.678 | 0.694 | 0.694 |

> **Note:** Canva's `resize-design` does not apply these scales perfectly to every element — text elements reflow, and table elements shift irregularly. Always audit after resize; never assume the resized design is correct.

---

## Step 1 — Resize

Load `mcp__claude_ai_Canva__resize-design`. Call it with the source design ID and target dimensions in px.

Record the new design ID from the response. **All element IDs are new** — source element IDs are invalid.

---

## Step 2 — Audit (Delta Comparison)

This step computes the **expected** position of each element and compares it against the **actual** position in the resized design. It generates a fix list, not just a status report.

**How to compute expected position:**
```
expected_top  = ref_top  × scale_h
expected_left = ref_left × scale_w
expected_font = ref_font × font_scale (then apply minimum if lower)
```

Where ref values come from the 500ml source design or from `targets.md`.

Open a read transaction on **page 1 (front label)**, then **page 2 (back label)** of the new design. For each element, record `element_id`, `top`, `left`, `width`, `height`, `type`, `fontSize`, and visible text.

---

### Front label audit checklist

- [ ] **Illustration images:** `left` should be ≤ 0 (bleeds left); `left + width` should exceed canvas width by ≥ 3px (bleeds right). Flag any image with `left > 5` as a bleed failure.
- [ ] **NET QTY text:** must say the target size (e.g., "200 ml"), not "500 ml". Generate `find_and_replace_text` if wrong.
- [ ] **Logo group top:** should be ≥ 8px and ≤ 15px (corrected from any negative clipping). Check the thumbnail.

---

### Back label audit — generate a fix list

For **each** element below, compute `expected = ref × scale`. If `|actual - expected| > 1px` for position, or `actual_font < minimum`, add it to the fix list.

**Font minimums (hard floor — override scale if below):**
- 200ml: 10px minimum for all text (body, labels, table data)
- 100ml: 12px minimum for all text (body, labels, table data)

> **Why:** Print legibility at small sizes requires a floor regardless of proportional scaling. The scale formula produces values below the floor at these sizes.

**Back label elements to check and fix:**

| Element role | 200ml expected left | 100ml expected left | 200ml expected font | 100ml expected font |
|---|---|---|---|---|
| Ingredients label | 12.8px | 10.7px | 10px (min) | 12px (min) |
| Ingredients content | 11.9px | 9.9px | 10px (min) | 12px (min) |
| Nutrition Information label | 12.3px | 10.3px | 10px (min) | 12px (min) |
| Table "Nutrient" column header | 18.5px | 15.4px | 10px (min) | 12px (min) |
| Table "Per 100 ml" column header | 153.8px | 128.4px | 10px (min) | 12px (min) |
| All table data rows — labels | 18.5px (left col) | 15.4px (left col) | 10px (min) | 12px (min) |
| All table data rows — values | 153.8px (right col) | 128.4px (right col) | 10px (min) | 12px (min) |
| Storage, Mfg, Address, Best Before, MRP, Mfg Date, USP, Country | 12px | 10px | 10px (min) | 12px (min) |
| Rose illustration left edge | 147px | 126px | — | — |

**Detailed expected coordinates by size:** see `targets.md`.

---

## Step 3 — Apply all fixes in transactions

Use the transaction pattern from `brand/canva-mcp-workflow.md`:
1. `read-design` with `open_transaction: true` → get transaction_id
2. Batch all operations for that page into `edit-design` calls with `keep_open: true`
3. Final `edit-design` with `finalize: commit`

Process **front label first**, then **back label**. Each page is a separate transaction.

---

### Front label fix operations

```json
// Fix NET QTY text (if wrong)
{ "type": "find_and_replace_text", "locator_id": "<id>", "find_text": "500 ml", "replace_text": "200 ml" }

// Fix bleed images (if left > 5)
{ "type": "position_element", "locator_id": "<id>", "left": -5 }
{ "type": "resize_element", "locator_id": "<id>", "width": <canvas_width + 8> }
```

---

### Back label fix operations

Apply position, font-size, and content fixes in one transaction per page.

**For every text element where font < minimum:**
```json
{ "type": "format_text", "locator_id": "<id>", "formatting": { "font_size": 10 } }
```
*(Use 10 for 200ml, 12 for 100ml. The property inside `formatting` is `font_size` with underscore — camelCase `fontSize` is silently ignored.)*

**For column header positioning (Nutrient + Per 100 ml):**
```json
{ "type": "position_element", "locator_id": "<nutrient_col_id>", "left": 18.5 }
{ "type": "position_element", "locator_id": "<per100ml_col_id>", "left": 153.8 }
```
*(Use values from targets.md for exact per-size coordinates)*

**For all table data rows — reposition left column and right column:**
```json
// Each label in left column (Energy, Total Fat, — Saturated Fat, — MUFA, etc.)
{ "type": "position_element", "locator_id": "<row_label_id>", "left": 18.5 }

// Each value in right column
{ "type": "position_element", "locator_id": "<row_value_id>", "left": 153.8 }
```

**For regulatory text block (Storage, Mfg, MRP, etc.):**
```json
{ "type": "position_element", "locator_id": "<id>", "left": 12 }
```

**For rose illustration (right edge should reach or exceed canvas edge):**
```json
{ "type": "position_element", "locator_id": "<id>", "left": 147 }
{ "type": "resize_element", "locator_id": "<id>", "width": <canvas_width - 147 + 10> }
```

> **Batching note:** Apply format_text and position_element operations in the same `edit-design` call (with keep_open: true) to minimize round-trips. Commit only after all operations are included.

---

## Step 4 — Verify (mandatory)

After committing, re-read both pages and check:

- [ ] NET QTY text shows correct size
- [ ] All text elements: `fontSize` ≥ 10 (200ml) or ≥ 12 (100ml)
- [ ] Nutrition "Nutrient" header: `left` ≈ 18-19px (200ml) or 15-16px (100ml)
- [ ] Nutrition "Per 100 ml" header: `left` ≈ 153-155px (200ml) or 128-130px (100ml)
- [ ] Table data row labels: `left` ≈ 18-20px (200ml) or 15-17px (100ml)
- [ ] Table data row values: `left` ≈ 153-155px (200ml) or 128-130px (100ml)
- [ ] Regulatory text left: ≥ 10px on all elements
- [ ] Rose illustration right edge: `left + width` ≥ canvas_width

If any check fails, open a new transaction and apply corrective operations. Do not report completion until all checks pass.

---

## Step 5 — Rename design

After formatting is confirmed correct, rename the design to follow the naming convention:
```
[Product] Label [Size]ml ([Width]mm × [Height]mm)_Final
```
Example: `Rose Water Label 200ml (61mm × 105mm)_Final`

---

## Step 6 — Report

After both pages are committed and verified, tell the user:
- New design ID and Canva edit URL
- Summary of fixes applied: count of elements repositioned, font sizes corrected, text content changed
- Any elements that could not be fixed (with locator_id and reason)
- Verification pass/fail status for each check

Do not mark complete until both pages are committed and the verify step passes all checks.

---

## Troubleshooting

**"format_text has no effect on font size"**  
`format_text` requires a `fontSize` parameter inside a `text_formatting` object. Check the Canva MCP tool schema for the correct parameter structure before calling.

**"Position fix reverted after commit"**  
Transaction was not committed. Confirm `finalize: commit` was passed in the last edit-design call.

**"Element IDs changed after resize"**  
Expected — resize always generates new element IDs. Always use IDs from the post-resize `read-design` call.

**"Rose illustration doesn't extend to canvas edge after resize"**  
The illustration's width was proportionally reduced during resize. Use `resize_element` to extend width beyond canvas edge (overflow is normal and creates the bleed).

---

## Scale reference

| Size | Canvas px | Scale W | Scale H | Body left margin | Table left col | Table right col | Table bg left |
|---|---|---|---|---|---|---|---|
| 500ml | 283×435 | 1.0× | 1.0× | 15–16px | 23px | 189px | 13.4px |
| 200ml | 230×396 | 0.813× | 0.910× | 12px | 18.5px | 153.8px | 10.9px |
| 100ml | 192×302 | 0.678× | 0.694× | 10px | 15.4px | 128.4px | 9.1px |
