# Unayurved — Decision Log

Newest first. Entries are immutable — supersede, don't edit.

---

**2026-10-13 — 100ml back label: drop MUFA/PUFA/Trans Fat rows**
The 100ml label cannot fit the full 11-row nutrition table at readable font sizes. MUFA, PUFA, and Trans Fat are all zero-value for coconut oil and are not FSSAI mandatory declarations. Removing them brings the 100ml back label within the content budget without losing any required information.

**2026-10-13 — Label sizes: 250ml replaced by 200ml; dimensions confirmed from physical bottles**
Original plan used estimated sizes (250ml: 50×80mm, 100ml: 45×70mm). Actual bottle measurements confirmed:
- 200ml bottle: 152.4mm circumference, 115mm flat height → label 61×105mm
- 100ml bottle: 127mm circumference, 90mm flat height → label 51×80mm
The 250ml SKU does not exist — the mid-size bottle is 200ml. All three sizes use the 40% circumference rule (see label-design-system.md).

**2026-10-13 — Typography: Playfair Display Black + Josefin Sans Light + DM Sans Light (supersedes 2026-09-21)**
Cormorant Garamond was the original choice but was not available in the weights needed for Canva AI generation. Playfair Display Black delivers the required high-contrast editorial serif at headline sizes. Josefin Sans Light handles the wide-tracked processing claim line. DM Sans Light remains for body/regulatory text. This trio is now the locked font system — see canva-ai-prompt-template.md for exact usage per element.

**2026-10-13 — Background: pure white #FFFFFF (supersedes 2026-09-21 warm white)**
Warm white (#FEFCF3) was the original decision. After seeing the printed label, pure white was confirmed as the correct choice — the warm parchment background was reading as stale rather than premium. The illustration's warm tones (coconut browns, palm greens) provide the warmth; the background does not need to add to it.

**2026-10-13 — Botanical illustrations: added to front label (supersedes 2026-09-21 no-illustrations decision)**
The original decision avoided botanical illustrations to prevent clutter and Heritage-Ceremonial territory. In practice, the label needed a visual anchor below the product name. Canva AI's photographic-realistic botanical illustrations (not flat or watercolour) deliver a premium, editorial quality that does not clash with the logo's botanical register. The illustration is contained to the bottom 48% of the front label only — the back label remains clean text.

**2026-10-13 — Tool: Canva (AI + MCP) replaces HTML+CSS+SVG (supersedes 2026-09-21)**
HTML labels were the original tool choice. Switched to Canva after Canva AI proved capable of generating photographic-quality botanical illustrations that could not be replicated with SVG or CSS. The MCP tools (read-design, edit-design, resize-design) provide programmatic control for precise positioning, scaling, and text corrections. HTML files are kept in the repo for reference but are no longer the production path. Canva design IDs are the authoritative source — see canva-mcp-workflow.md.

---

**2026-09-21 — Tool: HTML+CSS+SVG (no Canva)**
Labels built as print-exact HTML files, exported via Chrome → PDF.
Reason: zero MCP token overhead, full version control, CSS variables serve as brand token system, scaling across sizes is CSS adjustments only.

**2026-09-21 — Typography: Cormorant Garamond (display) + DM Sans (body/regulatory)**
Cormorant Garamond at headline sizes is editorial and slightly heritage without being ornate. DM Sans is the most legible free font at 5–7pt — critical for back-label regulatory content. Both are Google Fonts (free, commercially licensed for print). No third typeface introduced.

**2026-09-21 — Color: warm white background (#FEFCF3) over clinical white**
Deep forest green on clinical white reads pharmaceutical. Warm white (#FEFCF3) reads natural and premium. The logo already carries the green signal — the background does not need to repeat it.

**2026-09-21 — Color: no gold accent**
Green + gold is the most overused combination in Indian Ayurvedic packaging. Restraint is the differentiator. The divider/border color (#C8BFA0, warm sand) provides warmth without the gold cliché.

**2026-09-21 — Logo: Logo 1 (flower mark + wordmark) for print; Logo 2 for digital**
Logo 1 has gravitas and visual complexity suitable for physical products. Logo 2 (minimal lowercase) is optimized for screen/social.

**2026-09-21 — Visual territory: Lifestyle-Contemporary (not Heritage-Ceremonial)**
Heritage-Ceremonial (earthy green, gold, botanical illustrations, Sanskrit) is overcrowded. Clinical-Modern is cold. Lifestyle-Contemporary — modern editorial principles with intentional traditional cues — is the least saturated and most aligned with the brand's dual-heritage positioning.

**2026-09-21 — No botanical illustrations on label**
The 5-petal flower mark in Logo 1 already occupies the botanical register. Adding leaf/coconut illustrations would create visual clutter and push the label toward the Heritage-Ceremonial territory we are avoiding.

**2026-09-21 — Research methodology: independent before user samples**
Market research conducted independently (web search) before reviewing competitor images provided by the user. This prevents anchoring. User samples introduced afterward as validation only.
