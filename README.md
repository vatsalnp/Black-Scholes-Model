# Black-Scholes Model Implementation

This repository contains a Python implementation of the Black-Scholes Model for option pricing. The implementation includes functions for calculating European call and put option prices, as well as option Greeks (Delta, Gamma, Theta, Vega).

## Features

- European call and put option pricing
- Option Greeks calculations (Delta, Gamma, Theta, Vega)
- Comprehensive test suite
- Example usage with sample parameters

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Black-Scholes-Model.git
cd Black-Scholes-Model
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from black_scholes import call_option_price, put_option_price, calculate_greeks

# Example parameters
S = 100  # Current stock price
K = 100  # Strike price
T = 1    # Time to maturity (1 year)
r = 0.05 # Risk-free interest rate
sigma = 0.2  # Volatility

# Calculate option prices
call_price = call_option_price(S, K, T, r, sigma)
put_price = put_option_price(S, K, T, r, sigma)

# Calculate Greeks
greeks = calculate_greeks(S, K, T, r, sigma)

print(f"Call Option Price: {call_price:.4f}")
print(f"Put Option Price: {put_price:.4f}")
print("\nGreeks:")
for greek, value in greeks.items():
    print(f"{greek}: {value:.4f}")
```

### Available Functions

1. `calculate_d1(S, K, T, r, sigma)`: Calculates the d1 parameter
2. `calculate_d2(d1, sigma, T)`: Calculates the d2 parameter
3. `call_option_price(S, K, T, r, sigma)`: Calculates European call option price
4. `put_option_price(S, K, T, r, sigma)`: Calculates European put option price
5. `calculate_greeks(S, K, T, r, sigma)`: Calculates option Greeks

### Parameters

- `S`: Current stock price
- `K`: Strike price
- `T`: Time to maturity (in years)
- `r`: Risk-free interest rate
- `sigma`: Volatility

### Running Tests

To run the test suite:
```bash
python -m pytest test_black_scholes.py
```

## Mathematical Background

The Black-Scholes Model is based on the following assumptions:
1. The stock price follows a geometric Brownian motion
2. The risk-free interest rate is constant
3. The stock pays no dividends
4. The option is European (can only be exercised at expiration)
5. The market is efficient and frictionless

### Option Pricing Formulas

Call Option Price:
```
C = S * N(d1) - K * e^(-rT) * N(d2)
```

Put Option Price:
```
P = K * e^(-rT) * N(-d2) - S * N(-d1)
```

Where:
- d1 = (ln(S/K) + (r + σ²/2)T) / (σ√T)
- d2 = d1 - σ√T
- N(x) is the cumulative distribution function of the standard normal distribution

## Dependencies

- numpy >= 1.21.0
- scipy >= 1.7.0
- matplotlib >= 3.4.0
- pandas >= 1.3.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
