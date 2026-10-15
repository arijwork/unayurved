---
name: unayurved-label-enforce-grammar
description: Unified skill that enforces Unayurved design grammar (mathematical formatting rules) on any label design at any size and any product. Reads label-patterns.json to understand universal rules, product rules, and size-specific rules. Applies these rules to ensure consistent positioning, sizing, spacing, and fonts without changing content. Works for front and back labels, all products, all sizes.
---

# Unayurved Label — Enforce Grammar

Enforces consistent design grammar across all Unayurved labels by applying mathematical rules extracted from 6 finalized designs.

**Core Philosophy:** Design is governed by universal rules (margins, fonts, section ordering), not by copying a single reference. This skill reads the design grammar from `label-patterns.json` and applies it to any label at any size.

**Read first:** `../reference/label-patterns.json` (the source of truth for all rules and patterns)

---

## Inputs Required

Ask the user for:

1. **Design ID** — the Canva design to enforce grammar on
2. **Declared size** — what size is this label? (500ml, 200ml, 100ml)
3. **Product type** (optional) — coconut oil, rose water, olive oil, etc. Helps determine content structure
4. **Pages to fix** (optional) — front (page 1), back (page 2), or both (default: both)

---

## Design Grammar Rules (from label-patterns.json)

### Universal Rules (apply to ALL labels)

| Rule | Implementation |
|------|-----------------|
| **Left margin** | 5-6% of canvas width (scales per size) |
| **Font floors** | 500ml: 9.36px (no floor), 200ml: 10px min, 100ml: 12px min |
| **Section order** (back label) | Top bar → Ingredients → Nutrition → Regulatory → Illustration |
| **Top bar height** | ~6% of canvas height, full width, color #d65b6a |
| **Top bar positioning** | Always at Y=0, always full width |
| **Page count** | Always 2 (front + back) |

### Size-Specific Rules

```
Canvas dimensions:
  500ml: 283×435px (1.0 scale)
  200ml: 230×396px (0.813w × 0.910h)
  100ml: 192×302px (0.678w × 0.694h)

Font floors:
  500ml: 9.36px (scale naturally, no floor)
  200ml: 10px (enforce minimum)
  100ml: 12px (enforce minimum)

Left margin calculations:
  500ml: canvas_width × 0.055 = ~15.5px
  200ml: canvas_width × 0.055 = ~12.6px → round to 12px
  100ml: canvas_width × 0.055 = ~10.5px → round to 10px
```

### Product-Specific Rules

| Product Type | Nutrition Table | Ingredients | Notes |
|---|---|---|---|
| **Oils (Coconut, Olive, etc.)** | Full macro table (Energy, Fat, Carbs, Protein) | Standard format | High nutritional content |
| **Water (Rose Water, Floral)** | Minimal/zero table (all 0g values) | Simple format | Water has no nutrition |
| **Future: Kalonji** | TBD (should match coconut structure) | Specialized | High cost item |

---

## Workflow: 4-Phase Grammar Enforcement

### PHASE 1: VALIDATE INPUT

Check:
- [ ] Design ID is valid and accessible
- [ ] Declared size is 500ml, 200ml, or 100ml
- [ ] Design has 2 pages (front + back)
- [ ] Pages are editable

**If any check fails:** Report to user, do not proceed.

---

### PHASE 2: AUDIT (Compare against grammar)

For **each page** (front, back):

1. Open read transaction on the page
2. Extract all elements:
   - Text elements: record `id`, `top`, `left`, `fontSize`, `fontFamily`, `color`, text content
   - Image elements: record `id`, `top`, `left`, `width`, `height`
   - Shapes: record `id`, `top`, `left`, `color`, purpose
3. For each element, compute **expected values** based on grammar rules:
   ```
   expected_left = canvas_width × 0.055  (for left-aligned text)
   expected_font = MAX(
     calculated_font,
     font_floor[declared_size]
   )
   ```
4. Record deviations:
   - Position deviation > 1px? Flag it
   - Font < minimum? Flag it
   - Color not in palette? Flag it
   - Section out of order? Flag it

**Output:** Audit report showing all deviations

---

### PHASE 3: FIX (Generate and apply operations)

For each deviation flagged:

#### Position Deviations
```json
{
  "type": "position_element",
  "locator_id": "<element_id>",
  "top": <expected_top>,
  "left": <expected_left>
}
```

#### Font Size Deviations
```json
{
  "type": "format_text",
  "locator_id": "<element_id>",
  "formatting": {
    "font_size": <expected_font_size>
  }
}
```

#### Color Deviations (if needed)
```json
{
  "type": "recolor_element",
  "locator_id": "<element_id>",
  "color": "<expected_hex>"
}
```

**Batching:**
1. Open edit transaction on page
2. Batch ALL operations (position + font + color) with `keep_open: true`
3. Call finalize with `finalize: commit` in a separate call

**Transaction pattern (CRITICAL):**
```
read-design → open_transaction=true → get transaction_id
edit-design → keep_open=true, operations=[...] → apply changes
edit-design → finalize=commit, operations=[] → commit all changes
```

---

### PHASE 4: VERIFY (Re-audit and confirm)

1. Re-read the design (with new transaction)
2. Extract elements again
3. Compare against grammar rules
4. If all pass: ✅ **COMPLETE**
5. If any still deviate:
   - ⚠️ Report remaining issues
   - Ask user if they want to refine further OR accept current state

---

## Back Label Section Positioning (Reference)

After enforcing margins, sections should appear in this order:

| Section | Expected Top Offset | Height | Content |
|---------|-------------------|--------|---------|
| Top bar | 0% | ~6% | "PRODUCT water" or "Product name" |
| Ingredients | ~12-15% | Variable | "100% Pure X, Steam Distilled" |
| Nutrition Info | ~21-25% | Variable | "Nutrient / Per 100ml" table |
| Regulatory | ~60-70% | Variable | "Address, MRP, Mfg Date, Country" |
| Illustration | Overlaps regulatory | Variable | Product image (can overflow right edge) |

---

## Front Label Considerations

**Keep as-is (do not modify):**
- Product name positioning (already scaled correctly)
- Logo/branding elements
- Illustration sizing and content

**Check only:**
- NET QTY text says correct size ("200 ml", not "500 ml") → use `find_and_replace_text` if wrong
- Illustration bleeds are correct (left ≤ 0, right overflow ≥ 3px)
- Logo group top position (should be 8-15px to avoid clipping)

---

## Tolerance Levels

| Metric | Tolerance | Action if off |
|--------|-----------|---------------|
| Position (top/left) | ±1px | Fix with position_element |
| Font size | Below minimum | Fix with format_text |
| Color (hex) | Exact match | Fix with recolor_element if off-palette |
| Section ordering | Must match | Report as error; ask user to reorganize manually |

---

## Error Handling

**If audit fails to complete:**
- Cancel transaction
- Report which elements couldn't be read
- Ask user to check design integrity

**If fix operations fail during commit:**
- Transaction auto-cancels
- No changes applied
- Report error and suggest retry

**If verification shows issues:**
- Don't force completion
- Show remaining deviations to user
- Offer to refine further or accept current state

---

## Expected Outcomes

### Success ✅
```
GRAMMAR ENFORCED
─────────────────
Design: Rose Water 200ml (DAHYFafRMYg)
Size: 200ml (230×396px)

Page 1 (Front):
  ✓ All text positioned correctly
  ✓ NET QTY shows "200 ml"
  ✓ Illustration bleeds correct

Page 2 (Back):
  ✓ Left margins: 12px (expected 12px)
  ✓ Font sizes: all ≥10px (expected minimum)
  ✓ Sections in order: bar → ingredients → nutrition → regulatory
  ✓ Colors: all match brand palette

Status: All checks passed. Design conforms to grammar.
```

### Partial Success ⚠️
```
GRAMMAR ENFORCED (with notes)
──────────────────────────────
... [passes listed above]

Remaining issues:
  ⚠️ "Storage" section text left=11.5px (expected 12px) — off by 0.5px (within tolerance)
  ⚠️ Illustration right edge at 224px (canvas=230px) — 6px overflow (expected ≥3px) ✓

Action: Issues are minor/within tolerance. Design acceptable.
```

### Failure ❌
```
GRAMMAR ENFORCEMENT FAILED
──────────────────────────

Page 2 (Back):
  ❌ Section ordering broken: Nutrition table appears BEFORE Ingredients label
  ❌ Font: "MRP" text is 8.2px (expected minimum 10px for 200ml)
  ❌ Position: Regulatory text left=5px (expected 12px) — 7px deviation

Action: Cannot auto-fix section ordering. Requires manual reorganization.
        Font/position issues can be retried. Suggest user fix ordering first.
```

---

## Troubleshooting

**"Design has unknown size"**
→ Declared size must be 500ml, 200ml, or 100ml. Check design metadata.

**"Element IDs keep changing"**
→ Normal. Each read transaction gets fresh IDs. Use them immediately in the same transaction batch.

**"Font changes don't persist"**
→ Ensure `formatting: { "font_size": XX }` syntax (snake_case, not camelCase). Verify commit succeeded.

**"Some sections are in wrong order"**
→ This skill enforces *positioning*, not reordering. If a section is in the wrong place, ask user to reorder manually in Canva, then re-run.

**"Tolerances seem too strict"**
→ Tolerance is ±1px for position, exact match for fonts. This ensures print-ready precision. If acceptable, report as "within tolerance, acceptable."

---

## Related Skills

- **`unayurved-label-new-product`** — creates a brand-new product design from scratch (not yet built)
- **`unayurved-label-new-size`** — DEPRECATED after this skill is validated. Used to resize 500ml → 200ml/100ml; now handled by enforce-grammar
- **`unayurved-label-standardize-formatting`** — DEPRECATED after this skill is validated. Used to match against coconut oil reference; now handled by enforce-grammar with pattern-based rules

---

## Who Should Use This Skill

✅ Creating a new olive oil 200ml design and need it formatted correctly
✅ Have a basic rose water 500ml and need it grammar-checked
✅ Resizing a coconut oil 500ml to 100ml
✅ Standardizing any product design against brand rules
❌ Changing product content (ingredients, MRP, dates) — this is a grammar tool, not content editor
❌ Selecting font families or colors outside the brand palette — those are design decisions, not grammar enforcement
