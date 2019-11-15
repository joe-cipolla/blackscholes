import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import seaborn as sns

# This script loads stock data and compare manual option price and greek calculation against market values

pd.options.display.expand_frame_repr=False
sns.set()

# Define data load parameters
tickers = ['AAPL', 'MSFT', '^GSPC']
start_date = '2010-01-01'
end_date = '2019-11-01'

# load stock data
aapl = pdr.get_data_yahoo('AAPL', start_date, end_date)
msft = pdr.get_data_yahoo('MSFT', start_date, end_date)
spy = pdr.get_data_yahoo('^GSPC', start_date, end_date)

aapl.describe()
aapl.head()
aapl.tail()

# plot Close prices
aapl['Close'].plot(label='AAPL')
msft['Close'].plot(label='MSFT')
(spy['Close']/30).plot(label='^GSPC / 30')
plt.title('Daily Close Prices')
plt.ylabel('Share Price ($)')
plt.legend()
plt.show()

# Delta calcuation
