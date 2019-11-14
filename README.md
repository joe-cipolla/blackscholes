# blackscholes

## basic implementation of black scholes option pricing model in python\
The purpose of this model is to determine the price of a vanilla European
call and put options (option that can only be exercised at the end of its
maturity) based on price variation over time and assuming the asset has a
lognormal distribution.

## Assumptions
To determine the price of a vanilla European option, the following
assumptions are made:
- European options can only be exercised at expiration
- No dividends are paid during the option's life
- Market movements cannot be predicted
- The risk-free rate and volatility are constant (big assumption)
- Follows a lognormal distribution

## Parameters
- S, the spot price of the asset at time t
- T, the maturity of the option. Time to maturity is T - t
- K, the strike price of the option
- r, the risk-free interest rate, assumed to be constant between t and T
- sigma, volatility of underlying asset, the standard deviation of the asset returns

N(d) is the cumulative distribution of the standard normal variable Z

C(S, t) is the value at time t of a call option
P(S, t) is the value at time t of a put option

The Black-Scholes call formula is:
C(S, t) = S * N(d1) - (K * e^(-r(T-t))) * N(d2)
The put formula is:
P(S, t) = (K * e^(-r(T-t))) * N(-d2) - S * N(-d1)
where:
d1 = [ln(S/K) + (r + sigma^2/2) * (T - t)] / sigma * sqrt(T -t)
d2 = d1 - sigma * sqrt(T - t) =
		[ln(S/K) + (r - sigma^2/2) * (T - t)] / sigma * sqrt(T -t)