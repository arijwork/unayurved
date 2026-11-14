# Research

Two separate pieces of work, kept apart because they answer different questions.

| Folder | What it is | Sensitive? |
|---|---|---|
| `amazon-market/` | The Amazon.in market for our seven products, cleaned from Helium 10 exports: what the true market size is once duplicates and off-category products are removed. | Competitor sales estimates from a paid tool. |
| `pnl/` | Internal unit economics: our purchase costs, profit per bottle on Amazon and through distributors, launch prices and a three-month target plan. | Yes. Our costs, shop prices and distributor terms. |
| `dashboard/` | Page source for the "Amazon True Market Size" dashboard, which shows both. It only renders inside the dashboard, not as a standalone file. | Yes. Includes the launch plan. |

`pnl/` depends on `amazon-market/`: it reads `amazon-market/cleaned-products.csv` for competitor volumes. Run the market step first.

```bash
cd research/amazon-market && python3 classify.py raw data.json
```

```bash
cd research/pnl && python3 economics.py
```
