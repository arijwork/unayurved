# Skill Index: Unayurved Label Enforce Grammar

**Status:** ✅ Ready for Testing (first unified skill, replacing new-size and standardize-formatting)  
**Version:** 1.0  
**Created:** 2026-10-15  
**Reference Data:** `.claude/reference/label-patterns.json`

---

## WHAT THIS SKILL DOES

Enforces consistent **design grammar** (mathematical rules) on any Unayurved label design—any product, any size, front or back. Based on patterns extracted from 6 finalized reference designs (coconut oil + rose water, 500/200/100ml).

Instead of "match this one reference design," the skill understands *why* labels look the way they do: margins are 5-6% of canvas width, fonts have size floors based on container, sections always appear in the same order.

**Key insight:** One unified system replaces two separate skills (new-size + standardize-formatting).

---

## HOW TO USE

### Quick Form
```
/unayurved-label-enforce-grammar target:DAHX_e3ijSk size:200ml product:coconut-oil pages:both
```

### Full Invocation
User provides:
1. Design ID (Canva design to enforce grammar on)
2. Declared size (500ml, 200ml, 100ml)
3. Product type (optional: coconut oil, rose water, etc.)
4. Pages to check (optional: front, back, or both)

---

## FILES IN THIS SKILL

### 📋 **SKILL.md** — How the skill works
Complete technical documentation:
- 4-phase workflow (Validate → Audit → Fix → Verify)
- Grammar rules extracted from label-patterns.json
- MCP operation syntax
- Error handling and troubleshooting

### 📊 **INDEX.md** — This file
Overview, quick reference, what to expect

### 🔍 **REFERENCE: `..reference/label-patterns.json`** — The Source of Truth
Mathematical patterns from 6 finalized designs:
- Canvas dimensions and scale factors
- Font floor rules by size
- Margin percentages
- Section ordering
- Product variations
- Discovered patterns and confidence levels

---

## WORKFLOW AT A GLANCE

```
INPUT: Design ID + Declared Size
         ↓
    [PHASE 1: VALIDATE]
    ├─ Check design exists
    ├─ Confirm 2 pages
    └─ Verify size is known (500/200/100ml)
         ↓
    [PHASE 2: AUDIT]
    ├─ Read design pages
    ├─ Extract all elements
    ├─ Compare against grammar rules
    └─ Flag deviations > 1px or font < minimum
         ↓
    [PHASE 3: FIX]
    ├─ Generate position_element ops
    ├─ Generate format_text ops (fonts)
    ├─ Batch all operations
    └─ Commit to Canva
         ↓
    [PHASE 4: VERIFY]
    ├─ Re-read design
    ├─ Confirm all deviations fixed
    └─ Report status (✅ Pass, ⚠️ Minor issues, ❌ Fail)
         ↓
OUTPUT: ✅ Design now conforms to grammar
```

---

## GRAMMAR RULES (Quick Reference)

### Universal (all products, all sizes)
| Rule | Value |
|------|-------|
| **Left margin** | 5-6% of canvas width |
| **Section order** | Bar → Ingredients → Nutrition → Regulatory → Illustration |
| **Top bar color** | #d65b6a (dusty rose) |
| **Body text color** | #2b2b2b (dark gray) |
| **Page count** | 2 (always) |

### By Size
| Size | Canvas | Font Floor | Left Margin |
|------|--------|-----------|-------------|
| **500ml** | 283×435px | 9.36px | 15-16px |
| **200ml** | 230×396px | **10px** | 12px |
| **100ml** | 192×302px | **12px** | 10px |

### By Product Type
| Product | Nutrition Table | Notes |
|---------|-----------------|-------|
| **Oils** (Coconut, Olive) | Full table (Energy, Macros) | High nutritional content |
| **Water** (Rose Water) | Minimal (all 0g) | Water has no nutrition |

---

## WHAT CHANGES IN OPERATION

### Previous Workflow
```
1. If creating 200ml from 500ml → use unayurved-label-new-size
   (hardcoded targets.md, only rose water + coconut oil)

2. If formatting any product → use unayurved-label-standardize-formatting
   (compare against coconut oil 500ml reference)

= Two different skills, two different approaches
```

### New Workflow
```
1. Creating 200ml from 500ml olive oil?
   → /unayurved-label-enforce-grammar target:olive_oil_500ml size:200ml

2. Formatting any product at any size?
   → /unayurved-label-enforce-grammar target:any_design size:declared_size product:type

= One unified skill, mathematical rules, pattern-based
```

---

## SUCCESS CRITERIA FOR TESTING

This skill is considered **production-ready** when:

✅ **Test 1: Standardize 200ml design**
- Input: Rose Water 200ml design, declare as 200ml
- Expected: Left margins become 12px, fonts enforced to ≥10px, positions corrected
- Pass if: Audit shows deviations fixed, verify passes

✅ **Test 2: Enforce on new product at 500ml**
- Input: Olive Oil 500ml (brand new design), declare as 500ml
- Expected: Margins ~15-16px, section ordering verified
- Pass if: Audit passes (no massive deviations)

✅ **Test 3: Handle size transitions**
- Input: Coconut Oil 500ml, declare as 100ml
- Expected: Scale factors applied, fonts enforced to ≥12px
- Pass if: Verify shows correct canvas (192×302px), fonts all ≥12px

✅ **Test 4: Error handling**
- Input: Invalid design ID or unknown size
- Expected: Graceful error, clear message, no hang
- Pass if: User gets actionable feedback

---

## WHEN TO RETIRE OLD SKILLS

Once all tests pass:
1. Archive (don't delete) `unayurved-label-new-size` → users stay on enforce-grammar
2. Archive (don't delete) `unayurved-label-standardize-formatting` → users stay on enforce-grammar
3. Keep for 30 days in case we need to revert
4. Then remove from skill list

---

## ADVANTAGES OVER PREVIOUS SKILLS

| Aspect | Old (2 skills) | New (1 skill) |
|--------|---|---|
| **Resizing 500ml → 200ml** | unayurved-label-new-size (hardcoded) | enforce-grammar (pattern-based) |
| **Standardizing any product** | unayurved-label-standardize-formatting (coconut ref) | enforce-grammar (grammar rules) |
| **New product (olive oil)** | Broken (targets only for rose/coconut) | Works (uses patterns for any product) |
| **Scaling to new size (e.g., 50ml)** | Must hardcode new targets | Just read pattern table, apply rules |
| **Learning system** | No data structure for learning | Built on label-patterns.json (grows with new products) |
| **Maintenance burden** | Update multiple files | Update one source file |

---

## RELATED DOCUMENTATION

- **Technical details**: `SKILL.md` (this directory)
- **Pattern data**: `.claude/reference/label-patterns.json`
- **Design system**: `.claude/brand/label-design-system.md`
- **MCP workflow**: `.claude/brand/canva-mcp-workflow.md`

---

## SUPPORT & TROUBLESHOOTING

See `SKILL.md` troubleshooting section for common issues.

For unexpected errors, provide:
- Design ID that failed
- Declared size
- Error message from verify phase
- Screenshot of design (optional)
