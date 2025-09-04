# Growth Portfolio (VTI/VXUS/BND/TIP/IAU/VNQ)

This app backtests a simple growth-oriented core-satellite ETF allocation and produces a monthly rebalance plan.

- Core weights (baseline):
  - VTI 50%
  - VXUS 15%
  - BND 20%
  - TIP 5%
  - IAU 5%
  - VNQ 5%

- Frequency: monthly data; Rebalance: quarterly by default, with 20% relative drift bands.
- Optional: 12-month time-series momentum tilt (±10% within equity sleeve between VTI and VXUS).

## Quickstart

```bash
pip3 install -r apps/growth_portfolio/requirements.txt
python3 apps/growth_portfolio/src/main.py --start 2012-01-01 --end 2025-01-01 \
  --rebalance quarterly --tilt momentum --tilt_strength 0.10 --tilt_lookback 12
```

Outputs:
- CSV of monthly portfolio values and weights in `apps/growth_portfolio/out/`
- Basic performance metrics printed to console
- Plots saved: `nav.png` (indexed NAV), `weights.png` (stacked weights)

(Non-investment advice. For research only.)