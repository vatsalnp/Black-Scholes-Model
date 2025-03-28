# BlackScholes Option Pricing Model

This project implements the Black-Scholes model to price European call and put options using Python. It provides both a theoretical overview and a practical implementation, including visualizations to demonstrate how option prices vary with different parameters.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Enhancements](#enhancements)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Black-Scholes model is a widely used mathematical model for pricing European-style options. Its main formula for a call option is given by:

\[
C = S_0 \, N(d_1) - K e^{-rT} \, N(d_2)
\]

where:
- \( S_0 \) is the current stock price.
- \( K \) is the strike price.
- \( T \) is the time to maturity (in years).
- \( r \) is the risk-free interest rate.
- \( \sigma \) is the volatility of the underlying asset.
- \( N(\cdot) \) is the cumulative distribution function for a standard normal distribution.
- \( d_1 \) and \( d_2 \) are defined as:

\[
d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}.
\]

## Project Structure

