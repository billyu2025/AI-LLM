import argparse
import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


@dataclass
class PortfolioConfig:
	baseline_weights: Dict[str, float]
	rebalance: str  # 'monthly' or 'quarterly'
	drift_band: float  # relative, e.g., 0.2 for ±20%
	tilt: str = 'none'  # 'none' or 'momentum'
	tilt_strength: float = 0.10  # fraction of equity sleeve to tilt
	tilt_lookback: int = 12  # months


def fetch_monthly_adj_close(tickers: List[str], start: str, end: str) -> pd.DataFrame:
	data = yf.download(tickers=tickers, start=start, end=end, auto_adjust=True, progress=False, group_by='ticker')
	# yfinance returns different shapes depending on tickers count; normalize to DataFrame of Adj Close
	if isinstance(data.columns, pd.MultiIndex):
		adj_close = pd.concat({t: data[t]['Close'] for t in tickers}, axis=1)
	else:
		adj_close = data['Close'].to_frame(name=tickers[0])
	adj_close = adj_close.resample('M').last().dropna(how='all')
	return adj_close


def compute_returns(prices: pd.DataFrame) -> pd.DataFrame:
	returns = prices.pct_change().dropna(how='all')
	return returns


def periodic_targets(config: PortfolioConfig) -> Dict[str, float]:
	return config.baseline_weights.copy()


def trailing_return(prices: pd.Series, as_of_date: pd.Timestamp, lookback: int) -> float:
	# Use price up to as_of_date (inclusive), compute return over lookback months
	hist = prices.loc[:as_of_date].dropna()
	if len(hist) < lookback + 1:
		return np.nan
	start_price = hist.iloc[-(lookback + 1)]
	end_price = hist.iloc[-1]
	if start_price <= 0:
		return np.nan
	return (end_price / start_price) - 1.0


def targets_with_momentum_tilt(baseline: Dict[str, float], prices: pd.DataFrame, as_of_date: pd.Timestamp,
							   equity_names: Tuple[str, str], strength: float, lookback: int) -> Dict[str, float]:
	# Only tilt within equity sleeve between equity_names[0] and equity_names[1]
	t0, t1 = equity_names
	weights = baseline.copy()
	equity_sum = (weights.get(t0, 0.0) + weights.get(t1, 0.0))
	if equity_sum <= 0:
		return weights

	r0 = trailing_return(prices[t0], as_of_date, lookback)
	r1 = trailing_return(prices[t1], as_of_date, lookback)
	if np.isnan(r0) or np.isnan(r1) or abs(r0 - r1) < 1e-12:
		return weights

	shift = equity_sum * strength
	if r0 > r1:
		# move weight from t1 to t0
		move = min(shift, weights.get(t1, 0.0))
		weights[t0] += move
		weights[t1] -= move
	else:
		move = min(shift, weights.get(t0, 0.0))
		weights[t1] += move
		weights[t0] -= move

	# Ensure non-negative and renormalize to 1
	for k in list(weights.keys()):
		if weights[k] < 0:
			weights[k] = 0.0
	total = sum(weights.values())
	if total > 0:
		weights = {k: v / total for k, v in weights.items()}
	return weights


def needs_rebalance(current_weights: Dict[str, float], targets: Dict[str, float], band: float) -> bool:
	for t, tw in targets.items():
		if t in current_weights and tw > 0:
			lower = tw * (1 - band)
			upper = tw * (1 + band)
			cw = current_weights[t]
			if cw < lower or cw > upper:
				return True
	return False


def rebalance_to_targets(values: Dict[str, float], targets: Dict[str, float]) -> Dict[str, float]:
	total = sum(values.values())
	if total <= 0:
		return {k: 0.0 for k in values.keys()}
	return {k: targets.get(k, 0.0) * total for k in values.keys()}


def simulate(prices: pd.DataFrame, config: PortfolioConfig, start_cash: float = 10000.0) -> Tuple[pd.DataFrame, pd.DataFrame]:
	tickers = list(config.baseline_weights.keys())
	rets = compute_returns(prices)

	portfolio_values: List[float] = []
	weights_hist: List[Dict[str, float]] = []

	# initialize holdings by targets
	# initial date for targets uses the first return date
	first_date = compute_returns(prices).index[0]
	targets = periodic_targets(config)
	if config.tilt == 'momentum':
		targets = targets_with_momentum_tilt(
			targets, prices, first_date, ('VTI', 'VXUS'), config.tilt_strength, config.tilt_lookback
		)
	values = {t: start_cash * w for t, w in targets.items()}

	for i, (date, period_ret) in enumerate(rets.iterrows()):
		# apply returns to each asset
		for t in tickers:
			asset_ret = period_ret.get(t, 0.0)
			values[t] = values.get(t, 0.0) * (1.0 + (0.0 if pd.isna(asset_ret) else asset_ret))

		# rebalance logic
		do_rebalance = False
		if config.rebalance == 'monthly':
			do_rebalance = True
		elif config.rebalance == 'quarterly':
			# months are 1..12; rebalance on Mar/Jun/Sep/Dec ends
			if date.month in (3, 6, 9, 12):
				do_rebalance = True

		current_total = sum(values.values())
		current_weights = {t: (values[t] / current_total if current_total > 0 else 0.0) for t in tickers}

		# Update targets for tilt on each period end, so band check references current targets
		if config.tilt == 'momentum':
			targets = targets_with_momentum_tilt(
				periodic_targets(config), prices, date, ('VTI', 'VXUS'), config.tilt_strength, config.tilt_lookback
			)

		if needs_rebalance(current_weights, targets, config.drift_band):
			do_rebalance = True

		if do_rebalance:
			values = rebalance_to_targets(values, targets)

		portfolio_values.append(sum(values.values()))
		weights_hist.append(current_weights)

	portfolio_series = pd.Series(portfolio_values, index=rets.index, name='portfolio_value')
	weights_df = pd.DataFrame(weights_hist, index=rets.index)
	return portfolio_series.to_frame(), weights_df


def performance_stats(nav: pd.Series) -> Dict[str, float]:
	returns = nav.pct_change().dropna()
	if returns.empty:
		return {"cagr": 0.0, "vol": 0.0, "sharpe": 0.0, "max_dd": 0.0}

	months = len(returns)
	cagr = (nav.iloc[-1] / nav.iloc[0]) ** (12 / months) - 1
	vol = returns.std() * np.sqrt(12)
	sharpe = (returns.mean() * 12) / (vol + 1e-9)
	# max drawdown
	roll_max = nav.cummax()
	drawdown = nav / roll_max - 1.0
	max_dd = drawdown.min()
	return {"cagr": float(cagr), "vol": float(vol), "sharpe": float(sharpe), "max_dd": float(max_dd)}


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--start', type=str, required=True)
	parser.add_argument('--end', type=str, required=True)
	parser.add_argument('--rebalance', type=str, default='quarterly', choices=['monthly', 'quarterly'])
	parser.add_argument('--tilt', type=str, default='none', choices=['none', 'momentum'])
	parser.add_argument('--tilt_strength', type=float, default=0.10)
	parser.add_argument('--tilt_lookback', type=int, default=12)
	parser.add_argument('--outdir', type=str, default='/workspace/apps/growth_portfolio/out')
	args = parser.parse_args()

	os.makedirs(args.outdir, exist_ok=True)

	baseline = {
		'VTI': 0.50,
		'VXUS': 0.15,
		'BND': 0.20,
		'TIP': 0.05,
		'IAU': 0.05,
		'VNQ': 0.05,
	}
	config = PortfolioConfig(
		baseline_weights=baseline,
		rebalance=args.rebalance,
		drift_band=0.20,
		tilt=args.tilt,
		tilt_strength=max(0.0, min(0.3, args.tilt_strength)),
		tilt_lookback=max(3, min(24, args.tilt_lookback)),
	)

	prices = fetch_monthly_adj_close(list(baseline.keys()), args.start, args.end)
	nav_df, weights_df = simulate(prices, config, start_cash=10000.0)

	stats = performance_stats(nav_df['portfolio_value'])
	print(f"CAGR: {stats['cagr']:.2%}  Vol: {stats['vol']:.2%}  Sharpe: {stats['sharpe']:.2f}  MaxDD: {stats['max_dd']:.2%}")

	nav_df.to_csv(os.path.join(args.outdir, 'portfolio_nav.csv'))
	weights_df.to_csv(os.path.join(args.outdir, 'weights.csv'))
	print(f"Saved outputs to {args.outdir}")

	# plots
	try:
		fig, ax = plt.subplots(figsize=(9, 5))
		(nav_df['portfolio_value'] / nav_df['portfolio_value'].iloc[0]).plot(ax=ax)
		ax.set_title('Portfolio NAV (Indexed = 1.0)')
		ax.grid(True, alpha=0.3)
		fig.tight_layout()
		fig.savefig(os.path.join(args.outdir, 'nav.png'), dpi=144)
		plt.close(fig)

		fig2, ax2 = plt.subplots(figsize=(9, 5))
		weights_df[list(config.baseline_weights.keys())].plot.area(ax=ax2, stacked=True)
		ax2.set_ylim(0, 1)
		ax2.set_title('Portfolio Weights')
		ax2.grid(True, alpha=0.3)
		fig2.tight_layout()
		fig2.savefig(os.path.join(args.outdir, 'weights.png'), dpi=144)
		plt.close(fig2)
		print("Saved plots nav.png and weights.png")
	except Exception as e:
		print(f"Plotting failed: {e}")


if __name__ == '__main__':
	main()