# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:59:07 2023
@author: Anqi
"""

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt

def merge_data(file1,file2):
    #read file1 and file2 as dataframe; merge to df
    #to extend historical data records
    date_parser = lambda file1: pd.to_datetime('-'.join(file1.split('-')[:-1]))
    df1 = pd.read_csv(file1, parse_dates=['Datetime'], date_parser=date_parser, index_col='Datetime')
    date_parser2 = lambda file2: pd.to_datetime('-'.join(file2.split('-')[:-1]))
    df2 = pd.read_csv(file2, parse_dates=['Datetime'], date_parser=date_parser2, index_col='Datetime')
    df = pd.merge(df1,df2,how='outer',left_index=True, right_index=True)
    ind = np.sum(np.isnan(df.iloc[:,:6]),axis=1).values==6
    df.iloc[ind,:6] = df.iloc[ind,6:]
    df = df.iloc[:,:6]
    df.columns=df1.columns
    return df

''' sample code: download and save data '''
#set dates 
sd = datetime(2023,3,18)
ed = datetime(2023,3,24)
#Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
#get historical 1-min data (7 days limit, 30 days max)
df = yf.download(tickers='AMZN', start=sd, end=ed, interval="1m")
#get historical 5-min data (60 days max)
df = yf.download(tickers='MSFT', start=sd, end=ed, interval="5m")
df.to_csv('MSFT_5m.csv') #save the file for further analysis

#take a look at the data types
type(df.index)
df.dtypes
print(df[0:5])

''' download and merge your data'''
df = yf.download(tickers='AMZN', start=datetime(2023,4,3), end=datetime(2023,4,10), interval="1m")
df.to_csv('AMZN_1m_1.csv') 
df2 = yf.download(tickers='AMZN', start=datetime(2023,3,26), end=datetime(2023,4,2), interval="1m")
df2.to_csv('AMZN_1m_2.csv')
df3 = yf.download(tickers='AMZN', start=datetime(2023,3,18), end=datetime(2023,3,25), interval="1m")
df3.to_csv('AMZN_1m_3.csv')
df4 = yf.download(tickers='AMZN', start=datetime(2023,3,13), end=datetime(2023,3,17), interval="1m")
df4.to_csv('AMZN_1m_4.csv')



#merge the two dataset
df_12 = merge_data('AMZN_1m_1.csv','AMZN_1m_2.csv')
df_12.to_csv('first_merge.csv')
df_22 = merge_data('AMZN_1m_3.csv','AMZN_1m_4.csv')
df_22.to_csv('second_merge.csv')
month_df = merge_data('first_merge.csv','second_merge.csv')
month_df.to_csv('Amzn_13-11_March-April')




# Plot the close price of the AAPL
df['Adj Close'].plot()
plt.show()





    