import numpy as np
import pandas as pd
from scipy.stats import norm
import yfinance as yf


def black_scholes(S, K, T, r, sigma, option_type="call"):
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

# Fetch stock data from Yahoo Finance
def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    return data["Close"].iloc[-1]

# Parameters
ticker = ("^FCHI")
spot_price = get_stock_price(ticker)

maturity = 1  # Time to maturity in years
risk_free_rate = 0.03  # Risk-free interest rate
volatility = 0.2  # Annualized volatility

# Adjust strikes around the reference strike (nearest multiple of 25)
reference_strike = round(spot_price / 25) * 25
strikes = [reference_strike + i * 25 for i in range(-5, 6)] 

results = []
for K in strikes:
    call_price = black_scholes(spot_price, K, maturity, risk_free_rate, volatility, option_type="call")
    put_price = black_scholes(spot_price, K, maturity, risk_free_rate, volatility, option_type="put")
    results.append({"Strike": K, "Call Price": call_price, "Put Price": put_price})

df = pd.DataFrame(results)

print(f"\nOption Pricing for {ticker} (Spot Price: {spot_price:.2f})")
print(df)
