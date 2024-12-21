import numpy as np
import pandas as pd
import yfinance as yf

def binomial_tree(S, K, T, r, sigma, N, option_type="call"):
    
    dt = T / N  # Time step
    u = np.exp(sigma * np.sqrt(dt))  # Up factor
    d = 1 / u  # Down factor
    p = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral probability

    # Initialize asset prices at maturity
    prices = np.zeros(N + 1)
    for i in range(N + 1):
        prices[i] = S * (u ** i) * (d ** (N - i))

    # Initialize option values at maturity
    option_values = np.zeros(N + 1)
    for i in range(N + 1):
        if option_type == "call":
            option_values[i] = max(0, prices[i] - K)
        elif option_type == "put":
            option_values[i] = max(0, K - prices[i])

    # Step back through the tree
    for j in range(N - 1, -1, -1):
        for i in range(j + 1):
            option_values[i] = np.exp(-r * dt) * (p * option_values[i + 1] + (1 - p) * option_values[i])

    return option_values[0]

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
steps = 100  # Number of steps in the binomial tree

# Adjust strikes around the reference strike (nearest multiple of 25)
reference_strike = round(spot_price / 25) * 25
strikes = [reference_strike + i * 25 for i in range(-5, 6)] 

results = []
for K in strikes:
    call_price = binomial_tree(spot_price, K, maturity, risk_free_rate, volatility, steps, option_type="call")
    put_price = binomial_tree(spot_price, K, maturity, risk_free_rate, volatility, steps, option_type="put")
    results.append({"Strike": K, "Call Price": call_price, "Put Price": put_price})

df = pd.DataFrame(results)

print(f"\nOption Pricing for {ticker} (Spot Price: {spot_price:.2f})")
print(df)
