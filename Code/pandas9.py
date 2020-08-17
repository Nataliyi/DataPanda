import pandas as pd
import numpy as np
from time import time


stock = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/amzn_stock.csv', index_col='Date', parse_dates=True)
# make column 'Date' as index of dataframe
# it is comfortable for works and analysis by date

print(stock['2010'])
print(stock['2010-02': '2011-03'])
print(stock.resample('2h').asfreq())
# divide every day by a period of 2 hours
print(stock.resample('1w').mean())
# get average values by week
print(stock.rolling(3, min_periods=1).mean())
# get average values by three days, starts from 'min_periods'
print(stock.expanding().mean())
# get average values on the growing 1; 1 and 2; 1, 2 and 3...
print(stock.ewm(alpha=0.7).mean())
# counting values by weight
stock['Open'].plot()
ns = stock['Open'].rolling(10, min_periods=1).mean()
ns.plot()
print(stock.index.weekday)
print(stock.index.day_name().value_counts())
print(stock.index.dayofyear)
