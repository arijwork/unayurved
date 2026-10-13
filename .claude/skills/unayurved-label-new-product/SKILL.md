---
name: unayurved-label-new-product
description: Runs the full workflow for a brand new Unayurved product label — from product brief to Canva AI prompts ready to paste, then post-generation analysis and MCP fixes. Covers front label (Canva AI generates illustration + text) and back label (text layout). After 500ml is approved, calls unayurved-label-new-size for 200ml and 100ml. Use when starting kalonji oil, neem oil, rose water, or any new SKU.
---

# Unayurved label — new product

Full workflow from brief to print-ready Canva design for a new product SKU.

**Read first:** `brand/label-design-system.md`, `brand/canva-ai-prompt-template.md`, `brand/canva-mcp-workflow.md`.

---

## Step 1 — Fill the product brief

Ask the user to confirm (or fill from context) all fields in the intake table. Do not proceed until every field is confirmed:

| Field | |
|---|---|
| Product name (2 words max for label hero) | |
| Processing / origin claim | e.g. COLD PRESSED / STEAM DISTILLED / WOOD PRESSED |
| Descriptor line 1 | e.g. "Distilled from Damask Rose Petals" |
| Descriptor line 2 | e.g. "100% Pure · Preservative Free" |
| Net qty | 500 ml (generate 200ml/100ml after approval) |
| Botanical subject | species name + visual description + hex colour range |
| Accent colour | hex — use the product line guide in canva-ai-prompt-template.md |
| Ingredients text | full legal ingredients string |
| Nutrition data (per 100ml) | all 11 values: Energy, Total Fat, Sat Fat, MUFA, PUFA, Trans Fat, Cholesterol, Carbs, Sugars, Protein, Sodium |
| Storage instruction | max 2 lines |

---

## Step 2 — Write the front label prompt

Build the front label prompt using the two-zone structure from `brand/canva-ai-prompt-template.md`. Every text element must include:
- Font name and weight (Josefin Sans Light / Playfair Display Black / DM Sans Light)
- Exact hex colour
- Approximate pt size
- Letter spacing value

Output the prompt as a single code block the user can copy and paste directly into Canva AI. Do not summarise it — output the full prompt verbatim.

Tell the user: "Paste this into Canva AI. Send me the generated PDF or screenshot and I'll give you a fix list."

**Wait for the user to send the generated result before continuing.**

---

## Step 3 — Analyse the generated front label

When the user sends the screenshot or PDF:

Review against the spec. Report:
1. What Canva AI got right — confirm each element against the brief
2. Specific fixes needed — list every issue with the exact action to take (e.g. "Delete the duplicate tagline below the illustration — it shouldn't be there", "Logo zone is empty as expected — place the Unayurved logo SVG now")
3. Dimension check reminder — ask the user to confirm dimensions are set to 75mm × 115mm in Canva before proceeding

Standard fix checklist (check every time):
- [ ] Duplicate tagline — Canva AI often repeats descriptor lines. Delete the extra.
- [ ] Illustration bleed — confirm the botanical image reaches all four canvas edges with no white gap
- [ ] NET QTY text present in illustration zone bottom-left
- [ ] Veg dot present bottom-right
- [ ] Logo zone is empty (correct — user places manually)
- [ ] Font substitution — check Playfair Display Black is actually applied to the product name

---

## Step 4 — Write the back label prompt

Once the front label is approved (user says "front looks good" or similar), write the back label prompt using the filled brief data.

The back label prompt includes all actual text content — do not leave nutrition values or ingredients as placeholders. Use exact data from the brief.

Reference: back label prompt template in `brand/canva-ai-prompt-template.md`.

Output as a single copy-paste code block. Wait for the user to send the generated result.

---

## Step 5 — Analyse the generated back label

Review against:
- All FSSAI mandatory fields present (ingredients, nutrition table, net qty, manufacturer name, FSSAI lic no placeholder, country of origin, MRP placeholder, best before placeholder, batch no placeholder)
- No botanical watermark behind text (kills legibility — if present, flag it for removal)
- Font sizes visually readable
- Two-column bottom block (manufacturer left, barcode right)
- Veg dot present in top strip

---

## Step 6 — Copy to Canva and apply fixes via MCP

Once both pages are approved, the user will have a Canva design with the generated layout. Get the design ID from the user (or resolve from the Canva URL).

Apply any layout fixes (bleed, margins, text corrections) using the MCP transaction pattern from `brand/canva-mcp-workflow.md`.

Update `brand/canva-mcp-workflow.md` → Active design file IDs table with the new design ID.

---

## Step 7 — Scale to 200ml and 100ml

After 500ml is approved, invoke `unayurved-label-new-size` twice:
1. Target 200ml (230×396px)
2. Target 100ml (192×302px)

---

## Fixed brand elements (never change per product)

| Element | Value |
|---|---|
| Font: processing claim | Josefin Sans Light, all caps, ~9pt, +250 tracking |
| Font: product name | Playfair Display Black, fills label width, line spacing 0.88 |
| Font: descriptors | DM Sans Light, ~8pt, #999990, line spacing 1.5 |
| Product name colour | #1A1A18 |
| Descriptor colour | #999990 |
| Background | Pure white |
| Zone split | 48% illustration / 52% text |
| Logo zone | Top 30% of text zone — empty, placed manually |
| Illustration style | Photographic-realistic botanical, bleeds all edges |

## Variable per product

Accent colour · Processing claim text · Botanical species and hex · Descriptor lines · NET QTY · All back label content
