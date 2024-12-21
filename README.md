# Option Pricers: Black-Scholes and Binomial Tree

This repository contains two Python-based tools for pricing financial options using the Black-Scholes model and the Binomial Tree model. These tools allow you to calculate call and put option prices for various strike prices and visualize the results.

## Features

- **Black-Scholes Pricer**:
  - Continuous-time option pricing model.
  - Calculates call and put prices using the Black-Scholes formula.
  - Fetches real-time market data from Yahoo Finance.

- **Binomial Tree Pricer**:
  - Discrete-time option pricing model.
  - Simulates the option value by building a binomial tree.
  - Configurable number of steps for precision.

- **Key Parameters**:
  - Spot price fetched from Yahoo Finance.
  - Strike prices adjusted around a reference value.
  - User-defined volatility, risk-free rate, and time to maturity.

## Example Output

Both scripts will display a table of option prices for call and put options based on various strikes. Example:

```
Option Pricing for ^FCHI (Spot Price: 7425.00)
   Strike  Call Price  Put Price
   7400    125.30      95.20
   7425    110.45      80.10
   7450     98.50      68.00
