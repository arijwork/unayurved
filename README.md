# Unayurved

Product label system for Unayurved — a modern Unani + Ayurvedic wellness brand.

**Current tool:** Canva (MCP + Canva AI). The original HTML approach was abandoned — see decisions log.  
**First product:** Virgin Coconut Oil in three sizes.

---

## Current status

| Item | Status |
|---|---|
| Brand language | ✅ Done |
| Label design system | ✅ Done — `brand/label-design-system.md` |
| Canva AI prompt template | ✅ Done — `brand/canva-ai-prompt-template.md` |
| Canva MCP workflow guide | ✅ Done — `brand/canva-mcp-workflow.md` |
| Example prompts | ✅ Done — `brand/examples/` |
| 500ml front + back (Canva) | ✅ Approved and print-tested |
| 200ml front + back (Canva) | ⚠️ Created — formatting fixes pending (see HANDOFF.md) |
| 100ml front + back (Canva) | ⚠️ Created — formatting fixes pending (see HANDOFF.md) |
| Rose water — any size | 🔲 Not started — prompt ready in `brand/examples/` |

---

## Label dimensions (confirmed from physical bottles)

| Size | Width × Height | Canva design ID |
|---|---|---|
| 500ml | 75mm × 115mm | `DAHXzNXZGDY` (working copy) |
| 200ml | 61mm × 105mm | `DAHXzqqAOcU` |
| 100ml | 51mm × 80mm | `DAHXzmkQA9E` |
| 500ml V1 approved | 75mm × 115mm | `DAHXtJzEroQ` ← DO NOT EDIT |

Sizing rule: each label covers 40% of bottle circumference. Front + back = 80%, 10% gap each side.

---

## How to work on this

**Starting a new product (e.g. rose water, kalonji oil):**
Use skill `/unayurved-label-new-product` — it walks through brief intake, writes both Canva AI prompts, analyses the output, and applies MCP fixes.

**Adding a new size to an existing product:**
Use skill `/unayurved-label-new-size` — audits and fixes all bleed/margin/NET QTY issues after Canva resize.

**Editing an existing design directly:**
Read `brand/canva-mcp-workflow.md` for the transaction pattern before touching any Canva MCP tool.

---

## Repo structure

```
brand/
  label-design-system.md      ← dimensions, scale factors, typography minimums, FSSAI fields
  canva-ai-prompt-template.md ← two-zone prompt structure for any new product
  canva-mcp-workflow.md       ← transaction pattern, font conversion, bleed rules, design IDs
  brand-language.md           ← positioning, visual direction, claims rules
  tokens.css                  ← CSS color/font tokens (kept for reference)
  assets/
    logo-primary.png          ← Logo 1 (print — flower mark + UNAYURVED wordmark)
    logo-digital.png          ← Logo 2 (website/social only)
  examples/
    coconut-oil-front-prompt.md   ← approved, printed prompt — primary reference
    coconut-oil-back-prompt.md    ← back label + content budget notes + MCP fix record
    rose-water-front-prompt.md    ← second product — shows what changes per product
.claude/
  skills/
    unayurved-label-new-product/  ← skill: full new product workflow
    unayurved-label-new-size/     ← skill: resize + audit + fix
decisions/
  decision-log.md             ← every significant design decision with rationale
HANDOFF.md                    ← pending tasks for next session
```

---

## Before sending any label to print

- [ ] Dimensions confirmed in Canva (File → Resize → check mm values)
- [ ] Illustration bleeds to all four canvas edges
- [ ] Smallest text ≥ 6pt (higher minimum for 200ml and 100ml — see design system)
- [ ] NET QTY correct for each size
- [ ] Logo placed manually (Canva AI always leaves the logo zone empty)
- [ ] FSSAI fields present: ingredients, nutrition table, net qty, manufacturer name, FSSAI lic no, country of origin, MRP, best before, batch no
- [ ] Manufacturer address, FSSAI licence number, customer care contact filled in
- [ ] Actual barcode generated (EAN-13 for Indian retail) and placed
- [ ] Export as PDF → Print at 300 DPI — confirm CMYK with your printer
