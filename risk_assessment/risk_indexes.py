import numpy as np

trading_days = 252


def annualized_return(returns):
    return returns.mean() * trading_days


def annualized_volatility(returns):
    return returns.std() * np.sqrt(trading_days)


def sharpe_ratio(returns, risk_free_rate=0.06):
    excess_returns = returns - (risk_free_rate / trading_days)
    return (excess_returns.mean() / excess_returns.std()) * np.sqrt(trading_days)


def sortino_ratio(returns, risk_free_rate=0.06):
    excess_returns = returns - (risk_free_rate / trading_days)
    downside = excess_returns[excess_returns < 0]

    if len(downside) == 0:
        return np.nan

    return (excess_returns.mean() / downside.std()) * np.sqrt(trading_days)


def max_drawdown(price_series):
    rolling_max = price_series.cummax()

    drawdown = (price_series - rolling_max) / rolling_max
    return drawdown.min()


def value_at_risk(returns, confidence=0.95):
    returns = returns.dropna()
    if len(returns) == 0:
        return np.nan
    return np.percentile(returns, (1 - confidence) * 100)


def conditional_var(returns, confidence=0.95):
    var = value_at_risk(returns, confidence)
    return returns[returns <= var].mean()
