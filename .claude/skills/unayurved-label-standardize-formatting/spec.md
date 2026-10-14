# Unayurved Label Standardize Formatting Skill

**Version:** 1.0  
**Reference Design:** Coconut Oil 500ml (DAHX4LYYL2Q)  
**Last Updated:** 2026-10-14

---

## OVERVIEW

This skill standardizes technical formatting (pixel positions, sizes, font sizes, spacing) across all Unayurved product labels. It preserves content and fonts while ensuring pixel-perfect consistency with the approved reference design.

**Golden Rule:** If it looks right in coconut oil, it should look identical in rose water.

---

## REFERENCE DESIGN SPECIFICATIONS

### CANVAS DIMENSIONS
- **Width:** 283px
- **Height:** 435px

### PAGE 1: FRONT LABEL

#### Logo Group (UNAYURVED + Flower Mark)
- **Group Position:** top=−5.83px, left=79.42px
- **Flower Icon:** width=65.91px, height=76.50px, rotation=0°
- **"unayurved" Text:**
  - Font: Custom serif (font ref: YADZ-QAiu6o)
  - Size: 17.71px
  - Color: #1f803f (forest green)
  - Alignment: Center
  - Letter spacing: +0.25px
  - Line height: 1.0
  - Position: top=67.66px, left=79.42px
- **"Unani | Ayurvedic" Subtitle:**
  - Font: Sans-serif bold (font ref: YACgEdYQidM)
  - Size: 9.56px
  - Color: #2b2b2b (dark grey)
  - Weight: Bold
  - Alignment: Center
  - Position: top=91.84px, left=95.33px

#### Claim Line (STEAM DISTILLED)
- **Type:** Decorative rules + text
- **Text:**
  - Content: "Steam Distilled"
  - Font: Sans-serif light (font ref: YAFdJjbTu24, weight 1)
  - Size: 7.41px
  - Color: #d65b6a (dusty rose)
  - Alignment: Center
  - Letter spacing: +0.25px
  - Position: top=101.99px, left=95.62px

#### Product Name (ROSE / WATER)
- **"Rose" Line:**
  - Font: Large serif (font ref: YAD1aYG82rc)
  - Size: 58.62px
  - Color: #000000 (black)
  - Alignment: Center
  - Line height: 1.4
  - Position: top=103.09px, left=67.55px
- **"Water" Line:**
  - Font: Same serif (YAD1aYG82rc)
  - Size: 47.20px
  - Color: #000000 (black)
  - Alignment: Center
  - Line height: 1.4
  - Position: top=152.10px, left=61.88px

#### Descriptors (Sub-claim text)
- **Content:** "Distilled from Damask Rose Petals" + "100% Pure · Preservative Free"
- **Font:** Sans-serif light (YAFdJjbTu24)
- **Size:** 6.68px
- **Color:** #8f8f8f (medium grey)
- **Alignment:** Center
- **Line height:** 1.4
- **Position:** top=210.33px, left=85.13px

#### Botanical Illustration (Bottom 48%)
- **Left Palm/Stem (rotated):**
  - Position: top=221.84px, left=−5.64px
  - Size: 81.95px × 120.46px
  - Rotation: −10.99°
  - Opacity: 1.0
  - Bleed: Extends past left edge
- **Right Botanical Elements:**
  - Position: top=211.06px, left=217.90px
  - Size: 65.56px × 110.51px
- **Center Coconuts/Roses:**
  - Position: top=240.90px, left=130.58px
  - Size: 131.12px × 95.45px
- **Bottom Botanical Frame:**
  - Position: top=276.12px, left=10.75px
  - Size: 120.10px × 125.57px
- **Large Right Element:**
  - Position: top=296.02px, left=92.43px
  - Size: 147.51px × 135.78px

#### Net Quantity (Bottom-left)
- **Text:** "NET QTY: 500 ml"
- **Font:** Sans-serif semibold (YAFdJjbTu24)
- **Size:** 8.82px
- **Color:** #ffffff (white)
- **Alignment:** Left
- **Position:** top=403.69px, left=15.29px

#### Vegetarian Symbol (Bottom-right)
- **Image Element:**
  - Position: top=395.68px, left=243.97px
  - Size: 22.30px × 25.27px
  - No rotation

---

### PAGE 2: BACK LABEL

#### Top Bar (Product Name Background)
- **Shape:** Rectangle with rounded gradient
- **Color:** #d65b6a (dusty rose)
- **Dimensions:** width=283.46px, height=26.48px
- **Position:** top=0px, left=0px

#### Product Name in Bar
- **Text:** "ROSE water"
- **Font:** Custom (YAFdtQi73Xs)
- **Size:** 13.30px
- **Color:** #ffffff (white)
- **Alignment:** Center
- **Letter spacing:** +0.40px
- **Position:** top=5.81px, left=53.82px

#### Ingredients Section
- **Label:**
  - Text: "Ingredients"
  - Font: Sans-serif (YAFdJnPX3ZE)
  - Size: 10.70px
  - Color: #d65b6a (dusty rose)
  - Letter spacing: +0.02px
  - Position: top=53.48px, left=16.35px

- **Content Text:**
  - Font: Sans-serif bold (YAFdJnPX3ZE)
  - Size: 9.97px
  - Color: #2b2b2b (dark grey)
  - Position: top=71.95px, left=15.29px
  - **[TEXT CONTENT VARIES BY PRODUCT]**

#### Nutrition Information Section
- **Label:**
  - Text: "Nutrition Information"
  - Font: Sans-serif (YAFdJnPX3ZE)
  - Size: 10.70px
  - Color: #d65b6a (dusty rose)
  - Letter spacing: +0.02px
  - Position: top=92.95px, left=15.72px

- **Table Header Row:**
  - "Nutrient" Column:
    - Font: Sans-serif (YAFdJnPX3ZE)
    - Size: 9.36px
    - Color: #000000 (black)
    - Position: top=115.87px, left=23.31px
  - "Per 100 ml" Column:
    - Font: Sans-serif (YAFdJnPX3ZE)
    - Size: 9.36px
    - Color: #000000 (black)
    - Alignment: Center
    - Position: top=115.87px, left=187.36px

- **Table Data Rows (4 rows for water-based products):**
  - **Row 1 - Energy:**
    - Label: top=131.79px, left=23.39px
    - Value: top=131.79px, left=194.57px
    - Font size: 8.96px
  - **Row 2 - Total Carbs:**
    - Label: top=235.57px, left=23.20px
    - Value: top=235.57px, left=204.66px
    - Font size: 8.96px
  - **Row 3 - Protein:**
    - Label: top=264.85px, left=23.38px
    - Value: top=264.85px, left=204.66px
    - Font size: 8.96px
  - **Row 4 - Sodium:**
    - Label: top=279.50px, left=23.36px
    - Value: top=279.50px, left=200.39px
    - Font size: 8.96px

- **Table Grid Lines:**
  - Horizontal lines: every 15−16px vertically
  - Vertical dividers: at left=14px, left=176px, left=265px
  - Color: #2b2b2b, opacity: 0.75, weight: 1px

#### Storage Instructions
- **Label & Content:**
  - Font: Sans-serif (YAFdJnPX3ZE)
  - Size: 9.33px
  - Weight: Bold for "Storage:" label
  - Color: #2b2b2b (dark grey)
  - Position: top=301.79px, left=15.49px
  - **[TEXT CONTENT VARIES BY PRODUCT]**

#### Manufacturer Block
- **"Manufactured by:" Line:**
  - Position: top=325.98px, left=15.29px
  - Font size: 9.33px
- **"Address:" Line:**
  - Position: top=340.11px, left=15.29px
  - Font size: 9.33px
- **"Best Before:" Line:**
  - Position: top=373.93px, left=16.00px
  - Font size: 9.33px
- **"MRP:" Line:**
  - Position: top=361.83px, left=16.78px
  - Font size: 9.33px
- **"Mfg. Date:" Line:**
  - Position: top=386.66px, left=16.89px
  - Font size: 9.33px
- **"USP(per ml):" Line:**
  - Position: top=399.79px, left=16.00px
  - Font size: 9.33px
- **"Country of origin:" Line:**
  - Position: top=412.92px, left=16.35px
  - Font size: 9.33px

#### Decorative Rose Illustration (Bottom-right)
- **Image Element:**
  - Position: top=324.18px, left=187.36px
  - Size: 226.77px × 173.48px
  - No rotation, full opacity

---

## KEY TECHNICAL CONSTANTS

| Specification | Value |
|---|---|
| **Canvas Width** | 283px |
| **Canvas Height** | 435px |
| **Left Margin (default)** | 15−16px |
| **Right Margin (default)** | 15−17px |
| **Primary Font (body/regulatory)** | Sans-serif (YAFdJnPX3ZE) |
| **Primary Font (headers)** | Sans-serif (YAFdJnPX3ZE) |
| **Display Font (product name)** | Serif large (YAD1aYG82rc) |
| **Logo Font** | Custom serif (YADZ-QAiu6o) |
| **Primary Color (dark text)** | #2b2b2b |
| **Secondary Color (headers/claim)** | #d65b6a (dusty rose) |
| **Accent Color (descriptors)** | #8f8f8f (medium grey) |
| **Table Row Spacing** | 15−16px |
| **Header Row Position** | top=115.87px |
| **First Data Row Position** | top=131.79px |
| **Line Height (body text)** | 1.4 or 1.3 (varies by use) |
| **Letter Spacing (headers)** | +0.02px |
| **Letter Spacing (logo)** | +0.25px |

---

## WHAT STAYS CONSTANT (NEVER CHANGE)

- ✅ Canvas dimensions (283×435px)
- ✅ All font references (YAFdJjbTu24, YAFdJnPX3ZE, etc.)
- ✅ Logo group structure and position
- ✅ Illustration element positions and bleeds
- ✅ Table grid structure (row heights, column positions)
- ✅ Color hex codes (#2b2b2b, #d65b6a, etc.)
- ✅ Font sizes for non-content text
- ✅ Line heights and letter spacing

---

## WHAT CHANGES (BY PRODUCT)

- 🔄 Text content (product name, ingredients, etc.)
- 🔄 Manufacturer details (address, MRP, dates)
- 🔄 Nutrition table values
- 🔄 Botanical illustrations (but same positions/sizes)
- 🔄 Top bar color (if product has different accent)

---

## HOW TO USE THIS SPEC

### For Front Label (Page 1):
1. Keep logo group exactly as specified
2. Preserve all positioning for product name, descriptors
3. Ensure illustrations maintain exact dimensions and positions
4. Only text content changes

### For Back Label (Page 2):
1. Keep top bar dimensions and position
2. Preserve all table grid lines and header positions
3. Ensure section labels stay at specified coordinates
4. Update only: content text, nutrition values, manufacturer info
5. Maintain all spacing and margins

### Using Canva MCP:
- Extract element IDs from target design
- Compare each element's top, left, width, height against this spec
- Use `position_element` and `resize_element` operations to match spec
- Use `find_and_replace_text` only for content (fonts/sizes stay same)

---

## PRECISION NOTES

All measurements are in **pixels (px)**. Tolerances:
- **Position:** ±0.5px (top/left coordinates)
- **Size:** ±1px (width/height)
- **Font size:** Exact (no rounding)
- **Colors:** Exact hex match required

---

## VALIDATION CHECKLIST

After applying specs to a new product, verify:
- [ ] Canvas dimensions match (283×283×435)
- [ ] Logo group positioned at top=−5.83, left=79.42
- [ ] Product name positioned correctly (top=103.09 for first line)
- [ ] All illustrations positioned and sized exactly
- [ ] Back label top bar color correct
- [ ] Table header row at top=115.87
- [ ] All section labels at specified top/left coordinates
- [ ] Margins consistent (15−16px left/right)
- [ ] No text extends past canvas edges
