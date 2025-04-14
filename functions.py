import numpy as np
from scipy.stats import norm
from datetime import datetime
import yfinance as yf


def bs_formula(
    S: float, K: float, T: float, sigma: float, _type: str = "call", r: float = None
) -> float:
    if not r:
        r = get_r()

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if _type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif _type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise Exception("Wrong option type!")
    return float(price)


def get_r():
    irx = yf.Ticker("^IRX")
    data = irx.history(period="1d")  # or "1y", "max", etc.\
    r = data.tail().Close.values[0] / 100
    return float(r)


def get_last_price(ticker: str):
    ticker = yf.Ticker(ticker)
    data = ticker.history(period="1d")
    price = data.tail().Close.values[0]
    return float(price)


def get_sigma(ticker):
    ticker = yf.Ticker(ticker)
    data = ticker.history(period="3mo")
    sigma = data.Close.apply(lambda x: np.log(x)).diff(1).std() * np.sqrt(252)
    return float(sigma)
