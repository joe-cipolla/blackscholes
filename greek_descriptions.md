# Option Greek Descriptions

## What are Option Greeks?
Option Greeks are financial measures of the sensitivity of an option's price to its underlying asset's price, volatility and other parameters.  The Greeks are used to analyze an option portfolio's risk and assist in position management, as well as pricing.

The main option greeks that are most often used are:
- Delta - Measure of sensitivity of the option price to changes in the underlying asset's price
- Gamma - Measure of the delta's change relative to changes in the price of the underlying asset
- Theta - Measure of the option price decay over time
- Vega - Measure of the sensitivity of the option price to changes in the volatility of the underlying asset's price

## Option Greek Formulas
### Delta
Delta is a measure of the sensitivity of an option's price changes relative to the changes in the underlying asset's price. If the underlying asset increases by $1, then the price of the option will change by Delta.
<img src="https://latex.codecogs.com/gif.latex?\fn_jvn&space;\LARGE&space;\Delta&space;=\frac{\partial&space;V}{\partial&space;S}" title="\LARGE \Delta =\frac{\partial V}{\partial S}" />
Where:
<img src="https://latex.codecogs.com/gif.latex?\fn_phv&space;\large&space;\partial&space;=&space;first\,&space;order\,&space;derivative" title="\large \partial = first\, order\, derivative" />
<img src="https://latex.codecogs.com/gif.latex?\fn_phv&space;\large&space;V&space;=&space;option\,&space;price" title="\large V = option\, price" />
<img src="https://latex.codecogs.com/gif.latex?\fn_phv&space;\large&space;S&space;=&space;underlying\,&space;asset's\,&space;price" title="\large S = underlying\, asset's\, price" />

Call options have a delta between 0 and 1, while Put options have a delta between -1 and 0. The closer the option's delta to -1 or 1, the deeper in the money the option is. Delta can be used to hedge an option position's exposure to the underlying's price changes by either buying or selling (depending on the option position, long call, long put, etc.) shares of the underlying asset multiplied by the delta.

### Gamma

### Theta

### Vega
