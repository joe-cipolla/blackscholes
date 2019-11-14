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

<img src="https://latex.codecogs.com/gif.latex?\fn_jvn&space;\large&space;\Delta&space;=\frac{\partial&space;V}{\partial&space;S}" title="\large \Delta =\frac{\partial V}{\partial S}" />
Where:
<img src="https://latex.codecogs.com/gif.latex?\fn_phv&space;\large&space;\partial&space;=&space;first\,&space;order\,&space;derivative" title="\large \partial = first\, order\, derivative" />
<img src="https://latex.codecogs.com/gif.latex?\fn_phv&space;\large&space;V&space;=&space;option\,&space;price" title="\large V = option\, price" />
<img src="https://latex.codecogs.com/gif.latex?\fn_phv&space;\large&space;S&space;=&space;underlying\,&space;asset's\,&space;price" title="\large S = underlying\, asset's\, price" />

Call options have a delta between 0 and 1, while Put options have a delta between -1 and 0. The closer the option's delta to -1 or 1, the deeper in the money the option is.
Delta can be used to hedge an option position's exposure to the underlying's price changes by either buying or selling (depending on the option position, long call, long put, etc.) shares of the underlying asset multiplied by the delta.
<br />  

### Gamma
Gamma is a measure of the delta's change relative to the changes in the price of the underlying asset. If the price of the underlying asset increases by $1, the option's delta will change by the gamma ammount.

<img src="https://latex.codecogs.com/gif.latex?\fn_jvn&space;\large&space;\Gamma&space;=\frac{\partial&space;\Delta&space;}{\partial&space;S}=\frac{\partial^{2}V}{\partial^{2}S}" title="\large \Gamma =\frac{\partial \Delta }{\partial S}=\frac{\partial^{2}V}{\partial^{2}S}" />

Long options have a positive gamma. An option has a maximum gamma when it is at-the-money (option price equals the price of the underlying asset). However, Gamma decreases when an option is deep in-the-money or out-the-money.  Similar to Delta, Gamma on a long call increases towards +1 when the underlying asset increases, and falls towards 0 when the underlying decreases. Long put's Gamma increases towards 0 when the underlying asset increases, and falls towards 0 when the underlying decreases.
<br />  

### Theta
Theta is a measure of how much the option's price will decrease with the passing of one day.

<img src="https://latex.codecogs.com/gif.latex?\fn_jvn&space;\large&space;\theta=-\frac{\partial&space;V}{\partial&space;\tau&space;}" title="\large \theta=-\frac{\partial V}{\partial \tau }" />
Where:
<img src="https://latex.codecogs.com/gif.latex?\fn_jvn&space;\large&space;\tau&space;=&space;option's\&space;time\&space;to\&space;maturity" title="\large \tau = option's\ time\ to\ maturity" />

All options have negative theta values.
<br />  

### Vega
Vegas is a measure of how much the option's price will change with a 1% change in implied volatility. If the volatility of the underlying assset's price increases 1%, the option price will change by the Vega amount.

<img src="https://latex.codecogs.com/gif.latex?\fn_jvn&space;\large&space;\textit{v}&space;=&space;\frac{\partial&space;V}{\partial&space;\sigma&space;}" title="\large \textit{v} = \frac{\partial V}{\partial \sigma }" />
Where:
<img src="https://latex.codecogs.com/gif.latex?\fn_jvn&space;\large&space;\sigma&space;=&space;\sum_{1}^{n}\frac{(V_{\mu&space;}-V_{n})^2}{n}" title="\large \sigma = \sum_{1}^{n}\frac{(V_{\mu }-V_{n})^2}{n}" />

All options have positive Vega. When option prices become more expensive (they have more extrinsic value), implied volatility increases. When option prices decrease (less extrinsic value), implied volatility falls. Vega is expressed as a money amount, rather than a decimal number. An increase in Vega usually means an increase in the option value (either call or put.


(latex generator)https://www.codecogs.com/latex/eqneditor.php
