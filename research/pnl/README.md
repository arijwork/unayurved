# Internal P&L: profit per bottle and launch plan

Internal. Contains our purchase costs, shop prices and distributor terms.

## Files

| File | What it is |
|---|---|
| `costs.json` | Inputs from the founders: liquid cost per litre, bottle and label costs, current shop prices, GST status, fulfilment and distributor terms. |
| `economics.py` | The model. Its assumptions are in `ASSUMED`, launch prices and decisions in `PLAN`, and MRPs to print in `NEW_MRP`. |
| `economics.json` | Output: profit per bottle on Amazon and through a distributor, for every product in the 100, 200 and 400 ml fills. |
| `ramp.json` | Output: a three-month staging of the 10,000-bottle goal. |

```bash
python3 economics.py
```

It reads `../amazon-market/cleaned-products.csv` for competitor volumes, so run the market step first if the exports change.

## The logic

1. **Ceiling:** what that size sells for on Amazon today.
2. **Floor:** price minus GST, liquid, bottle, label, box and platform fees must leave a profit.
3. **Launch** only where the size has real demand and the gap is workable; otherwise Later or Hold.
4. The 500 ml bottle is filled with 400 ml, so it is priced about 20% below the 500 ml market price.
5. A product cannot be listed above its printed MRP, so shop prices are treated as MRP.

## Assumptions still to confirm

- **Amazon fees (self-shipped):** no referral fee up to ₹1,000; closing fee ₹3 up to ₹300, ₹24 up to ₹500, ₹35 above; pickup and delivery ₹55 a parcel under 500 g. Taken from Amazon's public fee page; confirm in Seller Central.
- **GST:** 5% on the oils, 18% on rose water, with input GST claimed back. Confirm with the accountant.
- **Outer box and tape:** ₹10 an order. Real cost not yet known.
- **Distributor:** modelled both ways, receiving 40% or 60% of MRP. Which is right is not yet confirmed.
- **Not included:** advertising, returns, breakage, transport and the founders' own time.
- **Til:** edible or non-edible positioning is undecided.
