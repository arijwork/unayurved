# Handoff — pending tasks for next session

Last updated: 2026-10-13

---

## 1. Apply formatting fixes to 200ml and 100ml Canva designs

The 200ml (`DAHXzqqAOcU`) and 100ml (`DAHXzmkQA9E`) designs were created via Canva's `resize-design` tool. Canva auto-reflows all elements on resize, which breaks bleed, margins, and text content. The audit was completed — fixes are specified below. Use skill `/unayurved-label-new-size` or apply manually using the transaction pattern in `brand/canva-mcp-workflow.md`.

---

### 200ml Front Label (page 1, canvas 230×396px)

| Element ID | Issue | Fix |
|---|---|---|
| `LBW1xmbkdttL4mJN` (right palm) | Right edge at 226.9px, should reach ~231px | Increase width by ~4px |
| `LBfT6Tfwck2LJcfW` (bottom image) | Right edge at 226.5px, should reach ~231px | Increase width by ~4px |
| `LBlSczDWKR2Vf2XW` (NET QTY) | Says "500 ml" | `find_and_replace_text`: "500 ml" → "200 ml" |

### 200ml Back Label (page 2, canvas 230×396px)

Left margin collapsed to 2–4px on all text elements (should be 12–15px).

| Element ID | Current left | Target left |
|---|---|---|
| `LBFylB3kGztqv1RX` (Ingredients label) | 3.6px | 12px |
| `LBHC9pC2Ml3TCGrR` (ingredient value) | 2.8px | 12px |
| `LBjDM8V0WgNtXRtm` (Nutrition Information) | 3.1px | 12px |
| `LBxcnnxZCKSZCtR5` (Nutrient col header) | 9.3px | 18px |
| `LBHPM8DTzFFjRpBh` (Per 100 ml col header) | 142.3px | 162px |
| All table left-column body rows | ~9–11px | ~18px |
| All table right-column value rows | ~148–157px | ~162px |
| `LBpTBVcs9Fbngcm3` (table background) | left 1.7px, width 203.4px | left 11px, width ~215px |
| `LBqCThC5ZtxTZ6JP` (large right image) | right edge 228px | extend to ~238px |

---

### 100ml Front Label (page 1, canvas 192×302px)

All illustration images are missing bleed — they have positive left margins and don't reach the right canvas edge.

| Element ID | Issue | Fix |
|---|---|---|
| `LBrN9TlY6JBbb6yg` (left palm) | left=+5.5px | Move to left≈−4px, increase width to compensate |
| `LBW1xmbkdttL4mJN` (right palm) | Right edge 178.2px, needs ~193px | Increase width |
| `LBfT6Tfwck2LJcfW` (bottom image) | left=+7.6px, right edge short | left≈−1.6px, extend right to ~193px |
| `LBXXZcwHGrsP3M4m` (dark overlay) | left=+8.9px, right edge 177.9px | left≈−0.1px, right to ~192px |
| `LBlSczDWKR2Vf2XW` (NET QTY) | Says "500 ml" | `find_and_replace_text`: "500 ml" → "100 ml" |

### 100ml Back Label (page 2, canvas 192×302px)

Same element IDs as 200ml but different target positions (scale 0.679×).

| Element ID | Current left | Target left |
|---|---|---|
| `LBFylB3kGztqv1RX` | 3.0px | 10px |
| `LBHC9pC2Ml3TCGrR` | 2.3px | 10px |
| `LBjDM8V0WgNtXRtm` | 2.6px | 10px |
| `LBxcnnxZCKSZCtR5` | 7.8px | 15px |
| `LBHPM8DTzFFjRpBh` | 118.8px | 135px |
| All table left-column body rows | ~7–10px | ~15px |
| All table right-column value rows | ~127–130px | ~135px |
| `LBpTBVcs9Fbngcm3` (table background) | left 1.4px, width 169.8px | left 9.5px, width ~180px |
| `LBqCThC5ZtxTZ6JP` (large right image) | right edge 190.6px | extend to ~199px |

---

## 2. Fix font sizes on back labels (after margin fixes)

After repositioning, check and raise any font sizes below the print minimum:

- **200ml minimum:** 10px api_px (= 7.5pt display) — body text on 200ml back is currently ~7.3px
- **100ml minimum:** 12px api_px (= 9pt display) — body text on 100ml back is currently ~6.1px

Use `format_text` operations in the same transaction.

---

## 3. 100ml back label — remove MUFA/PUFA/Trans Fat rows

The 100ml label is too small to carry the full 11-row nutrition table. Per the design system rule for 100ml, remove these three rows to stay within the content budget:
- Monounsaturated Fat
- Polyunsaturated Fat
- Trans Fat

These rows are zero-value for coconut oil and are not FSSAI mandatory at this label size.

---

## Notes for the session picking this up

- Read `brand/canva-mcp-workflow.md` before touching any Canva MCP tool — specifically the transaction pattern and the known pitfalls from resize-design
- The element IDs above were captured during the audit. If they can't be found, re-read the design to get fresh IDs (Canva sometimes reassigns IDs on certain operations)
- Apply all fixes for one design + one page in a single transaction where possible — batching saves round trips
- Commit a note to this file once fixes are applied, or delete this file when all items are done
