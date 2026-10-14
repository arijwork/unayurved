# Unayurved Label Standardize Formatting

**Make all product labels pixel-perfect matches to the coconut oil reference design.**

---

## QUICK START

### The Problem
You create a rose water label in Canva AI. It looks right visually, but when you compare pixel coordinates to coconut oil, everything is slightly off:
- Logo is 2px too far left
- Table rows are misaligned
- Margins are inconsistent
- Spacing doesn't match

**Result:** Inconsistent look across products, potential print quality issues.

### The Solution
This skill extracts the **exact technical specifications** from coconut oil (the final, approved design) and applies them to rose water **without changing content, fonts, or images**.

---

## FILES IN THIS SKILL

| File | Purpose |
|---|---|
| **skill.md** | How the skill works, workflow steps, troubleshooting |
| **spec.md** | Complete technical specifications from coconut oil 500ml reference |
| **README.md** | This file — quick start guide |

---

## WHAT THIS SKILL EXTRACTS FROM COCONUT OIL

✅ **Preserved Exactly**
- Element positions (top, left in pixels)
- Element sizes (width, height)
- Font sizes (px values)
- Colors (hex codes)
- Spacing and margins
- Table structure and grid lines
- Illustration dimensions and positions
- Logo placement and scale

❌ **NOT Extracted/Changed**
- Font families (kept as-is)
- Text content (product-specific)
- Image files (only positions matter)
- Canvas dimensions (always 283×435)

---

## HOW TO USE (3 STEPS)

### Step 1: Open the target design
Open the rose water or new product design in Canva.  
Note its design ID (shown in URL): `https://canva.com/design/DAHX9sxCpt4/...`

### Step 2: Run the skill
Ask me:
> "Standardize formatting for rose water. Reference: DAHX4LYYL2Q (coconut oil), Target: DAHX9sxCpt4 (rose water), scope: all"

Or shorter:
> "/unayurved-label-standardize-formatting target:DAHX9sxCpt4"

### Step 3: Review & approve
I'll show you:
- Audit report: what's misaligned
- Proposed fixes: what will be corrected
- Visual diff: before/after

You approve, and fixes are applied.

---

## EXAMPLE WORKFLOW

**Scenario:** You just created rose water labels in Canva AI. The front label looks good, but you want to ensure back label formatting matches coconut oil exactly.

```
You: "Standardize rose water back label against coconut oil. 
       Target: DAHX9sxCpt4, Reference: DAHX4LYYL2Q, Scope: back"

Me:  [Reads both designs]
     [Compares specifications]
     [Generates audit report]

     AUDIT RESULTS:
     ✅ Top bar: position OK
     ✅ Ingredients section: position OK
     ⚠️ Table header row: 1.2px too high — FIX NEEDED
     ✅ Margins: OK
     
     Proposed fix: Move table header from top=115.70 to top=115.87
     
     Commit? (yes/no)

You: "Yes"

Me:  [Applies MCP operations]
     [Validates result]
     
     ✅ COMPLETE
     Back label now matches coconut oil spec exactly.
```

---

## KEY NUMBERS TO REMEMBER

### Canvas
- **Width × Height:** 283 × 435 pixels

### Margins
- **Left margin:** 15−16px (most text)
- **Right margin:** 15−17px

### Front Label Key Positions
- **Logo group:** top = −5.83px, left = 79.42px
- **Product name "Rose":** top = 103.09px
- **Product name "Water":** top = 152.10px
- **Illustration zone:** Starts ~top=210px

### Back Label Key Positions
- **Top bar:** height = 26.48px
- **Ingredients label:** top = 53.48px
- **Nutrition header:** top = 115.87px
- **Table data starts:** top = 131.79px
- **Storage section:** top = 301.79px
- **Manufacturer block:** top = 325.98px

---

## COMMON SCENARIOS

### "I just created rose water in Canva AI"
→ Run this skill to align formatting to coconut oil reference

### "I resized the label to 200ml and everything moved"
→ Run this skill to restore formatting to 500ml spec (you'll then resize to 200ml separately)

### "The logo looks right but print came out misaligned"
→ Run this skill to catch sub-pixel positioning issues that visual inspection missed

### "I'm creating a new product (e.g., kalonji oil)"
→ Run this skill to ensure it matches coconut oil formatting from day one

---

## REFERENCE DESIGN SPECS

The reference design is **Coconut Oil 500ml** (Design ID: `DAHX4LYYL2Q`).

All specifications are locked down in `spec.md`:
- Exact pixel coordinates for every element
- Font size for every text block
- Color hex codes
- Spacing and margins
- Table structure
- Illustration sizing

**This is your source of truth.** If it's not in the spec, it doesn't matter for standardization.

---

## WHAT HAPPENS BEHIND THE SCENES

1. **Read Reference:** Fetch coconut oil design, extract all element specs
2. **Read Target:** Fetch rose water design, get current element specs
3. **Compare:** Calculate deviation for each element
4. **Audit:** Report which elements are off by how much
5. **Generate Operations:** Build MCP commands to correct deviations
6. **Apply:** Execute all corrections in one transaction
7. **Validate:** Re-read target design to confirm all fixes applied

---

## PRECISION & TOLERANCE

Deviations are only flagged if they exceed tolerances:

| Metric | Tolerance | Action |
|---|---|---|
| **Position (px)** | ±0.5px | Flag if beyond |
| **Size (px)** | ±1px | Flag if beyond |
| **Font size** | 0px (exact) | Flag if any deviation |
| **Color** | Exact hex | Flag if different |

Small deviations (e.g., 0.3px) are OK and left alone. Larger ones trigger fixes.

---

## TROUBLESHOOTING

**Q: How do I find the design ID?**
A: Open the design in Canva. Look at the URL: `canva.com/design/[THIS_IS_THE_ID]/...`

**Q: Can I use this for different bottle sizes (200ml, 100ml)?**
A: Not yet. This spec is for 500ml only. Different sizes need scaled specs (coming in future versions).

**Q: What if I've already made edits to rose water?**
A: The skill compares against current state, so your edits are preserved. Only positioning/sizing is corrected.

**Q: Will this change my text content?**
A: No. The skill only touches positioning, sizing, and spacing. Content stays exactly as you wrote it.

**Q: Can I revert if something goes wrong?**
A: Yes. The skill runs in a transaction that can be rolled back before commit. You'll review and approve before any changes are permanent.

---

## NEXT STEPS

Ready to use the skill?

1. **Prepare:** Have your target design open in Canva
2. **Identify:** Get the design ID from the URL
3. **Request:** Ask me to standardize against coconut oil reference
4. **Review:** Check the audit report and proposed fixes
5. **Approve:** Say "yes" and fixes are applied

Or read `skill.md` for detailed workflow documentation.

---

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-10-14 | Initial skill created, coconut oil 500ml specs extracted |

---

## QUESTIONS?

This skill is designed to be self-contained and reusable. If you have feedback or requests for improvements, let me know and I can update the specifications or automation logic.
