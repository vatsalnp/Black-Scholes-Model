import numpy as np
import pytest
from black_scholes import (
    calculate_d1, calculate_d2,
    call_option_price, put_option_price,
    calculate_greeks
)

def test_d1_d2_calculation():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    
    # Test d1 calculation
    expected_d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    assert np.isclose(d1, expected_d1)
    
    # Test d2 calculation
    expected_d2 = d1 - sigma*np.sqrt(T)
    assert np.isclose(d2, expected_d2)

def test_call_put_parity():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    call_price = call_option_price(S, K, T, r, sigma)
    put_price = put_option_price(S, K, T, r, sigma)
    
    # Call-Put Parity: C - P = S - K*e^(-rT)
    parity = call_price - put_price
    expected_parity = S - K * np.exp(-r*T)
    
    assert np.isclose(parity, expected_parity)

def test_greeks():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    greeks = calculate_greeks(S, K, T, r, sigma)
    
    # Test if all Greeks are present
    expected_greeks = ['delta_call', 'delta_put', 'gamma', 
                      'theta_call', 'theta_put', 'vega']
    assert all(greek in greeks for greek in expected_greeks)
    
    # Test put-call delta relationship
    assert np.isclose(greeks['delta_call'] - greeks['delta_put'], 1)

def test_at_the_money_options():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    call_price = call_option_price(S, K, T, r, sigma)
    put_price = put_option_price(S, K, T, r, sigma)
    
    # For ATM options, call and put prices should be approximately equal
    assert np.isclose(call_price, put_price, rtol=0.01)

if __name__ == "__main__":
    pytest.main([__file__]) 