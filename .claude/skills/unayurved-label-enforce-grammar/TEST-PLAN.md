# Test Plan: Unayurved Label Enforce Grammar

**Skill Version:** 1.0  
**Created:** 2026-10-15  
**Test Status:** Ready to execute  
**Success Criteria:** All 4 test scenarios must pass before retiring old skills

---

## Test Execution Summary

| Test # | Scenario | Design | Expected Result | Status |
|--------|----------|--------|-----------------|--------|
| 1 | Enforce on 200ml existing | Rose Water 200ml (DAHYFafRMYg) | Audit finds deviations, fix applies, verify passes | ⏳ Pending |
| 2 | Enforce on 500ml new product | Create new Olive Oil 500ml | Audit baseline, verify passes | ⏳ Pending |
| 3 | Enforce on 100ml scaled | Coconut Oil 500ml → 100ml | Resize + grammar enforce, all deviations fixed | ⏳ Pending |
| 4 | Error handling | Invalid design ID | Graceful error, clear message | ⏳ Pending |

---

## TEST 1: Enforce Grammar on Existing 200ml Design

**Purpose:** Validate that skill can audit an existing design, find deviations from grammar, and fix them.

**Setup:**
- Design ID: `DAHYFafRMYg` (Rose Water 200ml - already finalized)
- Declared size: 200ml
- Expected canvas: 230×396px
- Expected grammar:
  - Left margins: 12px (5.2% of 230px)
  - Font floor: 10px minimum for all text
  - Section order: Top bar → Ingredients → Nutrition → Regulatory

**Execution Steps:**

1. **Validate phase**
   - [ ] Read design metadata
   - [ ] Confirm 2 pages exist
   - [ ] Confirm size 200ml matches canvas 230×396px
   - [ ] Expected: ✅ All validations pass

2. **Audit phase (Page 1: Front)**
   - [ ] Extract all elements from front label
   - [ ] Check NET QTY text says "200 ml" (not "500 ml")
   - [ ] Check logo top position is 8-15px
   - [ ] Check illustration bleeds: left ≤ 0, right overflow ≥ 3px
   - [ ] Expected: ✅ Front label should audit clean (already finalized)

3. **Audit phase (Page 2: Back)**
   - [ ] Extract all elements from back label
   - [ ] For each text element, check:
     - `actual_left` vs `expected_left` (12px for regulatory, 15.4px for labels)
     - `actual_font` vs `expected_font` (all ≥ 10px)
   - [ ] Record deviations in audit report
   - [ ] Expected: ⚠️ Likely some minor deviations (0.1-0.5px) due to rounding, but all within tolerance

4. **Fix phase**
   - [ ] Generate position_element operations for deviations > 1px
   - [ ] Generate format_text operations for fonts < 10px
   - [ ] Expected: ✅ Few or no operations needed (already finalized)

5. **Verify phase**
   - [ ] Re-read design post-commit
   - [ ] Re-audit all elements
   - [ ] Check all deviations now within tolerance
   - [ ] Expected: ✅ All checks pass, design conforms to grammar

**Success Criteria:**
- ✅ Audit runs without error
- ✅ Fix applies without error (or reports no fixes needed)
- ✅ Verify confirms design meets grammar rules
- ✅ No elements left in invalid state

---

## TEST 2: Enforce Grammar on New 500ml Product

**Purpose:** Validate that skill can handle a brand-new design at 500ml size.

**Setup:**
- Design ID: `DAHX9sxCpt4` (Rose Water 500ml - already finalized, use as "new product")
- Declared size: 500ml
- Expected canvas: 283×435px
- Expected grammar:
  - Left margins: ~15-16px (5.5% of 283px)
  - Font floor: 9.36px (no enforced minimum at 500ml)
  - Section order: Top bar → Ingredients → Nutrition → Regulatory

**Execution Steps:**

1. **Validate phase**
   - [ ] Confirm canvas is 283×435px
   - [ ] Confirm 2 pages exist
   - [ ] Expected: ✅ Pass

2. **Audit phase**
   - [ ] Extract all elements (both pages)
   - [ ] Compare margins: record actual vs expected (15-16px)
   - [ ] Compare fonts: record actual vs expected (9.36px baseline, no floor)
   - [ ] Check section ordering (should be correct since it's finalized)
   - [ ] Expected: ✅ Minimal deviations (this is a finalized reference design)

3. **Fix phase**
   - [ ] Generate operations for any deviations
   - [ ] Expected: ✅ Few/no operations needed

4. **Verify phase**
   - [ ] Re-audit and confirm all grammar rules met
   - [ ] Expected: ✅ All checks pass

**Success Criteria:**
- ✅ Skill handles 500ml canvas correctly (no scaling artifacts)
- ✅ Font floor logic works (9.36px baseline, no enforced minimum)
- ✅ Margins calculated at 5.5% of canvas width
- ✅ Verify passes

---

## TEST 3: Enforce Grammar After Resize (500ml → 100ml)

**Purpose:** Validate that skill can enforce grammar on a resized design, handling scale factors and font floors correctly.

**Setup:**
- Source design: `DAHYFcxvUKA` (Coconut Oil 500ml)
- Target size: 100ml
- Expected canvas post-resize: 192×302px
- Scale factors: width ×0.678, height ×0.694
- Font floor for 100ml: 12px minimum

**Execution Steps:**

1. **Pre-test: Resize via Canva API**
   - [ ] Call resize-design with source=DAHYFcxvUKA, target_size=192×302
   - [ ] Record new design ID
   - [ ] Expected: ✅ New design created with correct canvas

2. **Validate phase**
   - [ ] Confirm canvas is 192×302px
   - [ ] Confirm 2 pages exist
   - [ ] Declared size: 100ml
   - [ ] Expected: ✅ Pass

3. **Audit phase (Back label)**
   - [ ] Extract all text elements
   - [ ] For each element, compute:
     - `expected_left = 500ml_left × 0.678`
     - `expected_font = MAX(500ml_font × 0.694, 12px)`
   - [ ] Example calculations:
     - Ingredients label: 16.35px (500ml) × 0.678 = 11.08px → round to 10px expected
     - Energy row: 8.96px (500ml) × 0.694 = 6.22px → enforce 12px minimum
   - [ ] Record deviations
   - [ ] Expected: ⚠️ Many position deviations (scales are imperfect), many font violations (below 12px floor)

4. **Fix phase**
   - [ ] Generate position_element operations for each deviation > 1px
   - [ ] Generate format_text operations for each font < 12px
   - [ ] Expected: ✅ Batch operations and apply
   - [ ] Expected operation count: ~30-40 (positions) + ~35-40 (fonts)

5. **Verify phase**
   - [ ] Re-audit all elements post-fix
   - [ ] Confirm:
     - All left margins within 1px of expected
     - All fonts ≥ 12px
     - Section ordering correct
   - [ ] Expected: ✅ All checks pass

**Success Criteria:**
- ✅ Scale factors applied correctly (0.678w, 0.694h)
- ✅ Font floors enforced (all text ≥ 12px)
- ✅ Position deviations fixed to within ±1px
- ✅ Verify passes post-fix
- ✅ Design is now properly formatted at 100ml size

---

## TEST 4: Error Handling

**Purpose:** Validate that skill handles errors gracefully and provides useful feedback.

### Test 4a: Invalid Design ID

**Setup:**
- Design ID: `INVALID_DESIGN_ID_XXXXX`
- Declared size: 200ml

**Execution:**
- [ ] Call enforce-grammar with invalid design ID
- [ ] Expected: ❌ Skill reports "Design not found" or similar
- [ ] Expected: ✅ Error message is clear and actionable
- [ ] Expected: ✅ No hang or crash

**Success Criteria:**
- ✅ Clear error message (not a generic API error)
- ✅ Graceful failure (no stack trace visible to user)

### Test 4b: Unknown Size

**Setup:**
- Design ID: `DAHYFafRMYg` (valid design)
- Declared size: "50ml" (not in label-patterns.json)

**Execution:**
- [ ] Call enforce-grammar with unknown size
- [ ] Expected: ❌ Skill reports "Size 50ml not supported. Known sizes: 500ml, 200ml, 100ml"
- [ ] Expected: ✅ Error is clear

**Success Criteria:**
- ✅ Helpful error message naming supported sizes
- ✅ Graceful failure

### Test 4c: Design with <2 pages

**Setup:**
- Create or find a design with only 1 page
- Declared size: 200ml

**Execution:**
- [ ] Call enforce-grammar
- [ ] Expected: ❌ Skill reports "Design must have 2 pages (front + back). This design has 1 page."

**Success Criteria:**
- ✅ Clear error message
- ✅ Suggests fix (add missing page)

---

## Test Execution Notes

### For Test 1 & 2 (Already-Finalized Designs)
These should audit clean or with minimal deviations because they're already finalized designs. This validates that:
- Skill doesn't over-correct or make unnecessary changes
- Skill can distinguish between "off by 0.1px" and "off by 2px"
- Tolerances are reasonable

### For Test 3 (Resized Design)
This is the real validation because:
- Resize introduces systematic deviations
- Font minimums must be enforced
- Scale factors must be applied correctly
- This tests the core strength of the new skill (handling scaled designs better than old skills)

### For Test 4 (Errors)
Validates robustness and user experience.

---

## Validation Checklist

After all 4 tests complete, answer:

### Functionality
- [ ] Audit correctly identifies deviations from grammar
- [ ] Fix generates appropriate MCP operations
- [ ] Commit succeeds without errors
- [ ] Verify confirms all deviations fixed
- [ ] Error handling is graceful and informative

### Correctness
- [ ] Font floors are enforced (10px for 200ml, 12px for 100ml)
- [ ] Scale factors are applied (0.813/0.910 for 200ml, 0.678/0.694 for 100ml)
- [ ] Margin percentages are consistent (5-6% across all sizes)
- [ ] Section ordering is validated
- [ ] Tolerances are reasonable (±1px for position)

### Completeness
- [ ] Both front and back labels are processed correctly
- [ ] All grammar rules from label-patterns.json are enforced
- [ ] Pattern-based approach works (no hardcoded values)

### Readiness to Retire Old Skills
- [ ] Test 1: ✅ Pass → standardize-formatting can be retired
- [ ] Test 2: ✅ Pass → standardize-formatting can be retired
- [ ] Test 3: ✅ Pass → new-size can be retired
- [ ] Test 4: ✅ Pass → no critical error cases

---

## Post-Test Actions

### If All Tests Pass ✅
1. Archive `unayurved-label-new-size` (keep for 30 days)
2. Archive `unayurved-label-standardize-formatting` (keep for 30 days)
3. Update documentation to recommend enforce-grammar
4. Start using enforce-grammar for all new products (olive oil, kalonji, etc.)

### If Any Test Fails ❌
1. Document which test failed and why
2. Review the failure scenario
3. Fix the skill or adjust test expectations
4. Re-run failed test
5. Keep both old skills active until all tests pass

---

## Test Data References

### Design IDs Used
- Rose Water 200ml: `DAHYFafRMYg` ← Test 1
- Rose Water 500ml: `DAHX9sxCpt4` ← Test 2
- Coconut Oil 500ml: `DAHYFcxvUKA` ← Test 3 (source for resize)
- Coconut Oil 100ml: `DAHYFcck-p0` ← Compare against for Test 3 expected values

### Pattern Rules Reference
See `.claude/reference/label-patterns.json` for all rules used in validation.

---

## Sign-Off

- [ ] Test 1 Complete: __________ (date) by __________
- [ ] Test 2 Complete: __________ (date) by __________
- [ ] Test 3 Complete: __________ (date) by __________
- [ ] Test 4 Complete: __________ (date) by __________
- [ ] All validations passed: __________ (date)
- [ ] Old skills archived/retired: __________ (date)
