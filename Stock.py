from pandas_datareader import data
from matplotlib import pyplot as plt
import pandas as pd
import datetime
import numpy as np
companies_dict = {
    'Amazon': 'AMZN',
    'Apple': 'AAPL',
    'Walgreen': 'WBA',
    'Northrop Grumman': 'NOC',
    'Boeing': 'BA',
    'Lockheed Martin': 'LMT',
    'McDonalds':  'MCD',
    'Intel': 'INTC',
    'Navistar': 'NAV',
    'IBM': 'IBM',
    'Texas Instruments': 'TXN',
    'MasterCard': 'MA',
    'Microsoft': 'MSFT',
    'General Electrics': 'GE',
    'Symantec': 'SYMC',
    'American Express': 'AXP',
    'Pepsi': 'PEP',
    'Coca Cola': 'KO',
    'Johnson & Johnson': 'JNJ',
    'Toyota': 'TM',
    'Honda': 'HMC',
    'Mistubishi': 'MSBHY',
    'Sony': 'SNE',
    'Exxon': 'XOM',
    'Chevron': 'CVX',
    'Valero Energy': 'VLO',
    'Ford': 'F',
    'Bank of America': 'BAC'}
    
companies = sorted(companies_dict.items(), key=lambda x: x[1])
data_source = 'yahoo'

# Define the start and end dates
start_date = '2018-01-01'
end_date = '2018-12-31'

# Use pandas_reader.data.DataReader to load the desired stock data
panel_data = data.DataReader(companies_dict.values(), data_source, start_date, end_date)

# Print Axes Labels
#print(panel_data.axes)
stock_close = panel_data.loc['Close']
stock_open = panel_data.loc['Open']

print(stock_close.iloc[1])
