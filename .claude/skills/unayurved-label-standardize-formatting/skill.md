# Skill: Unayurved Label Standardize Formatting

**Description:** Extract technical formatting specifications from coconut oil 500ml reference design and apply them pixel-perfect to any Unayurved product label (rose water, kalonji, etc.). Ensures consistent positioning, sizing, and spacing across all products without changing fonts, images, or element content.

**Triggered by:** When user wants to match formatting between products, or after creating a new design via Canva AI.

---

## WHAT THIS SKILL DOES

1. **Reads** the reference design (coconut oil 500ml) to extract technical specs
2. **Compares** target design (e.g., rose water) against those specs
3. **Identifies** all positioning, sizing, and spacing differences
4. **Generates** MCP operations to correct deviations
5. **Applies** fixes in one coordinated batch
6. **Validates** that target now matches reference perfectly

**Result:** Rose water looks identical to coconut oil in layout, spacing, and positioning — only content differs.

---

## KEY PRINCIPLES

### ✅ WHAT STAYS THE SAME
- Font families (keep "Sans-serif", "Serif", "Custom" as-is)
- Font sizes (don't adjust numerically)
- Colors (all hex codes preserved)
- Image/illustration elements
- Canvas dimensions

### 🔄 WHAT CHANGES (BY PRODUCT)
- Text content (product name, ingredients, descriptors)
- Ingredient/nutrition values
- Manufacturer details (address, dates, MRP)
- Botanical illustration images (but dimensions/positions stay same)
- Top bar color (if different accent needed)

---

## STEP-BY-STEP WORKFLOW

### PHASE 1: AUDIT (Understand the gaps)

**Inputs:**
- Reference design ID: `DAHX4LYYL2Q` (coconut oil 500ml)
- Target design ID: `DAHX9sxCpt4` (rose water 500ml working copy)

**What happens:**
1. Read both designs completely (all pages, all elements)
2. Extract specs from reference into structured format (see `spec.md`)
3. Compare each element: position, size, font size
4. Flag all differences (deviations > ±0.5px on position, ±1px on size)
5. Generate audit report: "Logo group is 2.3px too far left", "Table header off by 1.15px", etc.

**Output:** Audit report identifying exact mismatches

---

### PHASE 2: FIX (Apply corrections via MCP)

**What happens:**
1. Generate Canva MCP operations for each mismatch
2. Batch all operations (position, resize, recolor if needed)
3. Apply in single coordinated transaction
4. Commit changes

**Operations used:**
- `position_element` — move elements to correct top/left
- `resize_element` — adjust width/height to spec
- `find_and_replace_text` — update ONLY content (not formatting)
- `format_text` — use ONLY when font size is wrong (below spec minimum). For 500ml designs this rarely fires; for resized designs (200ml, 100ml) this is critical — see `unayurved-label-new-size` skill for resized-label font requirements

**Example operations:**
```json
{
  "type": "position_element",
  "element_id": "...",
  "top": 53.48,
  "left": 16.35
}
```

---

### PHASE 3: VALIDATE (Confirm alignment)

**What happens:**
1. Re-read target design after fixes
2. Compare every element against spec again
3. Check for any remaining deviations
4. Generate before/after diff (show what changed)

**Output:** 
- ✅ "All elements now match reference spec"
- ⚠️ If issues remain: specific list of what still needs fixing

---

## RUNNING THE SKILL

### Command Format

```
/unayurved-label-standardize-formatting
```

### Required Inputs

When you invoke the skill, provide:
1. **Reference Design ID** — the source design to extract specs from (usually `DAHX4LYYL2Q` for coconut oil)
2. **Target Design ID** — the product to fix (e.g., `DAHX9sxCpt4` for rose water)
3. **Scope** (optional) — which pages to standardize:
   - `all` — both front and back labels (default)
   - `front` — front label only
   - `back` — back label only

### Example Invocation

> "Standardize rose water formatting against coconut oil reference. Target: DAHX9sxCpt4, reference: DAHX4LYYL2Q, scope: all"

---

## OUTPUT & RESULTS

### Audit Phase Output
```
FORMATTING AUDIT REPORT
=======================
Design: Rose Water 500ml (DAHX9sxCpt4)
Reference: Coconut Oil 500ml (DAHX4LYYL2Q)
Date: 2026-10-14

PAGE 1 (FRONT LABEL):
  Logo group:     Position OK ✅
  Product name:   Position OK ✅
  Illustration:   Position OK ✅

PAGE 2 (BACK LABEL):
  Ingredients label:     Position deviates −0.5px left ⚠️ (within tolerance)
  Table header row:      Position deviates +1.2px down ❌ FIX NEEDED
  Nutrition table:       Spacing OK ✅
  Storage section:       Margins OK ✅

FIXES NEEDED: 1
```

### Fix Phase Output
```
APPLYING CORRECTIONS
====================
✓ Updated 1 element position
✓ No resizing needed
✓ No font changes needed
✓ No content changes

Transaction ID: 8877113792280998068
Status: COMMITTED ✅

Target design now matches reference spec.
```

---

## PRECISION & TOLERANCES

| Metric | Tolerance | Action if Off |
|---|---|---|
| **Position (top/left)** | ±0.5px | Move element to exact spec coordinate |
| **Size (width/height)** | ±1px | Resize element to exact spec dimension |
| **Font size** | Exact match | No tolerance — must match precisely |
| **Color (hex)** | Exact match | No tolerance — must match precisely |

---

## TROUBLESHOOTING

### Issue: "Element IDs don't match between designs"
**Reason:** Canva sometimes reassigns element IDs during certain operations (resize, duplicate).  
**Solution:** The skill re-reads designs after each major operation to get fresh element IDs.

### Issue: "Position looks right visually but spec says it's off"
**Reason:** Canva's API (px) and visual rendering (display pt) can have sub-pixel differences.  
**Solution:** Trust the spec — pixel-precision positions ensure perfect printing alignment.

### Issue: "Font changed after fix"
**Reason:** Only use `find_and_replace_text` for content, never `format_text` unless explicitly changing.  
**Solution:** The skill never modifies font properties — only text content.

---

## WHEN TO USE THIS SKILL

✅ **After creating a new product via Canva AI**
- AI generation rarely matches reference specs exactly
- Run this to align all technical formatting

✅ **When resizing a label to a new bottle size**
- Resize operation breaks positioning
- Use this to restore spec alignment

✅ **Before sending to print**
- Final audit to confirm every element is in place
- Catches drift that visual inspection might miss

---

## REFERENCE SPECS

See `spec.md` in this skill directory for complete technical specifications extracted from coconut oil 500ml reference design.

Key specs include:
- Canvas dimensions (283 × 435 px)
- All element positions (top/left coordinates)
- All element sizes (width/height)
- Font sizes and references
- Color hex codes
- Table structure and spacing
- Margin and padding standards

---

## RELATED SKILLS

- **`unayurved-label-new-size`** — use this when resizing a 500ml design to 200ml or 100ml. It handles proportional scaling, font-size minimums (10px for 200ml, 12px for 100ml), column realignment, and post-resize verification. After running new-size, this skill (standardize-formatting) is not needed for that design — the new-size skill covers all the formatting work.

## FUTURE ENHANCEMENTS

Possible additions (for future versions):
- Auto-generate visual diff images (before/after side-by-side)
- Batch-process multiple products in one run
- Export specs to JSON for external tools

---

## WHO TO CONTACT

Issues or improvements to this skill? Let me know, and I can update the specifications or workflow.
