# Skill Index: Unayurved Label Standardize Formatting

**Status:** ✅ Complete and Ready to Use  
**Version:** 1.0  
**Created:** 2026-10-14  
**Reference:** Coconut Oil 500ml (DAHX4LYYL2Q)

---

## WHAT THIS SKILL DOES

Automatically standardizes technical formatting (pixel positioning, sizing, spacing) across all Unayurved product labels. Extracts the exact specifications from coconut oil (the final approved design) and applies them to any new product (rose water, kalonji oil, etc.) **without changing fonts, images, or text content**.

---

## FILES IN THIS SKILL

### 📋 **README.md** — START HERE
Quick-start guide for end users.
- What the skill does
- Why you need it
- How to use it in 3 steps
- Common scenarios
- Troubleshooting

### 📊 **spec.md** — THE REFERENCE
Complete technical specifications extracted from coconut oil 500ml.
- Canvas dimensions
- Element-by-element coordinates (top, left, width, height)
- Font sizes and references
- Colors (hex codes)
- Spacing standards
- Table structure
- Constants (what never changes)
- Variables (what changes by product)

### 🎯 **quick-reference.md** — CHEAT SHEET
Compact coordinate table and color reference.
- Front label coordinates
- Back label coordinates
- Font references
- Color hex codes
- Spacing standards
- Tolerances
- Pre-print checklist

### 🔧 **skill.md** — TECHNICAL DOCUMENTATION
How the skill works internally.
- 3-phase workflow (Audit → Fix → Validate)
- MCP operations used
- Troubleshooting guide
- Precision and tolerances
- When to use this skill

---

## HOW TO INVOKE

### Quick Form (Recommended)
```bash
/unayurved-label-standardize-formatting target:DAHX9sxCpt4
```

### Full Form (Explicit)
```bash
/unayurved-label-standardize-formatting 
  reference:DAHX4LYYL2Q 
  target:DAHX9sxCpt4 
  scope:all
```

### Parameters
- **reference** (optional) — Source design ID (defaults to DAHX4LYYL2Q for coconut oil)
- **target** (required) — Design ID to standardize (e.g., DAHX9sxCpt4 for rose water)
- **scope** (optional) — `all`, `front`, or `back` (defaults to `all`)

---

## WORKFLOW (3 PHASES)

### Phase 1: AUDIT
- Reads both reference (coconut oil) and target (rose water) designs
- Extracts all technical specifications
- Compares every element: position, size, font size
- Flags deviations beyond tolerance
- **Output:** Audit report showing what's misaligned

### Phase 2: FIX
- Generates Canva MCP operations for each deviation
- Batches all operations into single transaction
- Applies corrections via Canva API
- **Output:** "Applied X corrections"

### Phase 3: VALIDATE
- Re-reads target design after fixes
- Confirms all elements now match spec
- **Output:** "All elements aligned" or "Issues remain"

---

## KEY SPECIFICATIONS

### Canvas Dimensions
- **Width:** 283px
- **Height:** 435px

### Front Label Key Positions
| Element | Top | Left |
|---|---|---|
| Logo group | −5.83 | 79.42 |
| "Rose" product name | 103.09 | 67.55 |
| "Water" product name | 152.10 | 61.88 |
| Illustration start | 210.33 | — |
| NET QTY | 403.69 | 15.29 |

### Back Label Key Positions
| Element | Top | Left |
|---|---|---|
| Top bar | 0.00 | 0.00 |
| "Ingredients" label | 53.48 | 16.35 |
| "Nutrition Info" label | 92.95 | 15.72 |
| Table header row | 115.87 | — |
| First data row (Energy) | 131.79 | — |
| Storage section | 301.79 | 15.49 |
| Manufacturer block | 325.98 | 15.29 |

### Font Sizes
| Use | Size |
|---|---|
| Logo "unayurved" | 17.71px |
| Product name "Rose" | 58.62px |
| Product name "Water" | 47.20px |
| Body text | 9.97px |
| Small text (descriptors) | 6.68px |
| Table text | 8.96−9.36px |

### Colors (Hex)
- **Dark text:** #2b2b2b
- **Headers/accent:** #d65b6a (dusty rose)
- **Light text:** #8f8f8f
- **Logo:** #1f803f (forest green)

---

## WHAT STAYS THE SAME

✅ Font families (never changed)  
✅ Canvas dimensions (always 283×435)  
✅ Image/illustration elements (only positions adjusted)  
✅ Color hex codes (exact matches required)  
✅ Font sizes (must match spec precisely)  
✅ Spacing standards (margins, gaps, row heights)  

---

## WHAT CHANGES (BY PRODUCT)

🔄 Text content (product name, ingredients, descriptors)  
🔄 Ingredient/nutrition values  
🔄 Manufacturer details (address, MRP, dates)  
🔄 Botanical illustration images (size/position stay same)  
🔄 Top bar color (if different accent by product)  

---

## PRECISION TOLERANCES

| Metric | Tolerance | Example |
|---|---|---|
| **Position (top/left)** | ±0.5px | Spec: 115.87px, OK if 115.37 to 116.37 |
| **Size (width/height)** | ±1px | Spec: 283px, OK if 282 to 284 |
| **Font size** | Exact (0px) | Spec: 17.71px, must be exactly 17.71 |
| **Color (hex)** | Exact | Spec: #2b2b2b, must be exactly #2b2b2b |

Deviations beyond tolerance trigger automated corrections.

---

## EXAMPLE: APPLYING TO ROSE WATER

**Input:**
- Reference design: Coconut Oil 500ml (DAHX4LYYL2Q)
- Target design: Rose Water 500ml (DAHX9sxCpt4)
- Scope: All pages

**Skill does:**
1. Reads coconut oil design → extracts ~60 element specs
2. Reads rose water design → compares each element
3. Finds: Logo is 1.2px too far left, table header is off by 0.8px
4. Generates MCP operations to fix misalignments
5. Applies fixes in single transaction
6. Validates: "All elements now match coconut oil spec"

**Output:**
Rose water design now has pixel-perfect formatting matching coconut oil. Only text content differs (product name, ingredients, etc.).

---

## RELATED SKILLS

- **`unayurved-label-new-size`** — creates and fully formats a 200ml or 100ml label from an approved 500ml master. Handles proportional column alignment, font-size floors, and post-commit verification. Use this instead of running the current skill on a resized design.

## FUTURE ENHANCEMENTS

Possible additions in next versions:
- Visual diff images (side-by-side before/after)
- Batch-process multiple products simultaneously
- Auto-export specs to JSON
- Integration with print preparation workflow

---

## TROUBLESHOOTING

**"Design looks right visually but spec says it's wrong"**  
→ Trust the spec. Print precision requires pixel-perfect alignment.

**"Element IDs changed after my edits"**  
→ The skill fetches fresh IDs each run, so this is handled automatically.

**"Text content changed, but I only wanted positioning fixed"**  
→ This shouldn't happen. Report it, and I'll fix the skill.

**"I want to use this for 200ml size, not 500ml"**  
→ Use the `unayurved-label-new-size` skill instead — it handles proportional scaling, column realignment, and font-size minimums (10px/200ml, 12px/100ml) for resized designs.

---

## WHO CREATED THIS

**Created:** 2026-10-14  
**Based on:** Coconut Oil 500ml final approved design  
**Reference Design ID:** DAHX4LYYL2Q  
**Extraction Method:** Full Canva API read of both pages, all element specifications documented  

---

## HOW TO GET STARTED

### For First-Time Users:
1. Read **README.md** (5 min)
2. Look at **quick-reference.md** (3 min)
3. Invoke skill on your design

### For Advanced Users:
1. Review **spec.md** for complete specifications
2. Use **quick-reference.md** while designing
3. Invoke skill with explicit parameters

### For Skill Maintenance:
1. Reference **spec.md** as source of truth
2. Update **spec.md** if coconut oil design changes
3. All other files auto-derive from spec.md

---

## SUPPORT

Questions? Here's what to check:
- **How do I use it?** → README.md
- **What are the exact specs?** → spec.md
- **Quick numbers?** → quick-reference.md
- **How does it work internally?** → skill.md
- **Is my issue listed?** → skill.md troubleshooting section

---

## VERSION LOG

| Version | Date | Changes |
|---|---|---|
| **1.0** | 2026-10-14 | Initial release. Coconut oil 500ml specs extracted and documented. 3-phase audit/fix/validate workflow. 4-file documentation suite. |

---

## READY TO USE

This skill is complete and production-ready. You can start using it immediately on any Unayurved label design.

**Start with:** `/unayurved-label-standardize-formatting target:[YOUR_DESIGN_ID]`

Good luck! 🚀
