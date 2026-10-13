# Example: Virgin Coconut Oil — Back Label Prompt

**Product:** Extra Virgin Coconut Oil, 500ml  
**Status:** Generated and applied to `DAHXzNXZGDY` page 2. This is the reference prompt for back label structure.  
**Note:** After generation, the back label was rebuilt via Canva MCP tools (not Canva AI) to fix font sizes, margins, and layout. The prompt below captures the intended structure; the MCP edits made it print-ready.

---

Create the back label for Unayurved Extra Virgin Coconut Oil 500ml. Same dimensions as the front label — tall portrait format, 75mm × 115mm. Pure white background, clean. No botanical watermark or illustration behind the text — that kills legibility at this size.

**Top strip:** A narrow dark forest green bar (#1A3A1A) across the full width at the very top. Inside it, centred, in small white uppercase spaced letters: EXTRA VIRGIN COCONUT OIL. To the right end of the strip, the small green vegetarian dot symbol (green square with green circle inside).

**Just below the green strip:** A single thin horizontal green rule line.

**Ingredients section:**
Label in small bold dark grey uppercase: INGREDIENTS
Body text below in small regular dark grey: 100% Cold Pressed Virgin Coconut Oil

**Nutritional Information table:**
Header in small bold dark grey uppercase: NUTRITION INFORMATION

A clean bordered two-column table — Nutrient / Per 100 ml — with the following rows:

| Nutrient | Per 100 ml |
|---|---|
| Energy | 892 kcal |
| Total Fat | 99.1 g |
| — Saturated Fat | 86.5 g |
| — Monounsaturated Fat | 5.8 g |
| — Polyunsaturated Fat | 1.8 g |
| — Trans Fat | 0 g |
| Cholesterol | 0 mg |
| Total Carbohydrates | 0 g |
| — Total Sugars | 0 g |
| Protein | 0 g |
| Sodium | 0 mg |

Table styling: thin grey borders, alternating very faint rows for readability, column headers bold. All text very small but legible — minimum 6pt.

**Below the table:**
*"% Daily Values are based on a 2000 kcal diet."* — very small italic grey

**Storage:** Store in a cool, dry place away from direct sunlight. Keep cap tightly closed. May solidify below 24°C — this is natural. Warm gently to liquefy.

**Manufacturer block — two columns side by side:**
Left column (small text, left-aligned):
Manufactured by: Unayurved
Address: [To be filled]
Customer Care: [To be filled]
FSSAI Lic. No.: [Pending]
Country of Origin: India

Right column:
[Barcode placeholder — rectangular white box, ~20mm × 12mm, thin grey border, labelled "Barcode" in very small grey text]

**Bottom row across full width, very small text:**
MRP: ₹ ___ (Incl. of all taxes) | Best Before: ___/___ | Batch No.: _______ | Mfg. Date: ___/___

---

## What this prompt produced — notes for future reference

**Root problem identified:** 500ml back label tried to fit ~40 lines of content. At minimum readable font size (6pt), the label holds ~29 lines maximum. This caused everything to collapse below readable size.

**Content cut to reach the 29-line budget:**
- "How to use" section removed — not FSSAI mandatory for oils
- Logo removed from back — already on front
- "Per Serving" column removed — kept only Per 100ml (FSSAI allows single-column under 100cm²)
- % Daily Values footnote removed

**Typography floors enforced via MCP edits:**
- Body text: 7pt (8px api_px scaled from 500ml reference)
- Table text: 6.5pt
- Section headers: 8pt bold
- Footer row: 6pt

**MCP edit session:** Copied V1 approved design (`DAHXtJzEroQ`) → working copy (`DAHXzNXZGDY`) → edited page 2 with all fixes applied via transaction workflow.
