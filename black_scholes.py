import numpy as np
from scipy.stats import norm

def calculate_d1(S, K, T, r, sigma):
    """
    Calculate d1 parameter for Black-Scholes formula
    
    Parameters:
    S: Current stock price
    K: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility
    
    Returns:
    float: d1 parameter
    """
    return (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))

def calculate_d2(d1, sigma, T):
    """
    Calculate d2 parameter for Black-Scholes formula
    
    Parameters:
    d1: d1 parameter
    sigma: Volatility
    T: Time to maturity (in years)
    
    Returns:
    float: d2 parameter
    """
    return d1 - sigma*np.sqrt(T)

def call_option_price(S, K, T, r, sigma):
    """
    Calculate European call option price using Black-Scholes formula
    
    Parameters:
    S: Current stock price
    K: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility
    
    Returns:
    float: Call option price
    """
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    return call_price

def put_option_price(S, K, T, r, sigma):
    """
    Calculate European put option price using Black-Scholes formula
    
    Parameters:
    S: Current stock price
    K: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility
    
    Returns:
    float: Put option price
    """
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    
    put_price = K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

def calculate_greeks(S, K, T, r, sigma):
    """
    Calculate option Greeks (Delta, Gamma, Theta, Vega)
    
    Parameters:
    S: Current stock price
    K: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility
    
    Returns:
    dict: Dictionary containing option Greeks
    """
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    
    # Delta
    delta_call = norm.cdf(d1)
    delta_put = delta_call - 1
    
    # Gamma (same for both call and put)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    
    # Theta
    theta_call = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - 
                 r * K * np.exp(-r*T) * norm.cdf(d2))
    theta_put = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) + 
                 r * K * np.exp(-r*T) * norm.cdf(-d2))
    
    # Vega (same for both call and put)
    vega = S * np.sqrt(T) * norm.pdf(d1)
    
    return {
        'delta_call': delta_call,
        'delta_put': delta_put,
        'gamma': gamma,
        'theta_call': theta_call,
        'theta_put': theta_put,
        'vega': vega
    }

if __name__ == "__main__":
    # Example usage
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