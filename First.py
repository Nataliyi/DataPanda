import pandas as pd
import numpy as np
from time import time


stock = pd.read_csv('C:/Users/ediga/Projects/Python_Ln/Data/Files/amzn_stock.csv', index_col='Date', parse_dates=True)
# make column 'Date' as index of dataframe
# it is comfortable for works and analysis by date

print(stock['2010'])
print(stock['2010-02': '2011-03'])
print(stock.resample('2h').asfreg())
# divide every day by a period of 2 hours
print(stock.resample('1w').mean())
# get average values by week
print(stock.rolling)
