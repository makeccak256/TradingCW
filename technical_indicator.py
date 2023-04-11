# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:16:52 2022

@author: Anqi
"""

import pandas as pd
import numpy as np


''' Define some technical indicators '''
def SMA(p,window=10,signal_type='long'):
    # p - price used for SMA, the nxm DataFrame
    # window - look-back window size
    # signal_type - long (default), short, or both (not recommended)
    signal = pd.DataFrame(index=p.index,columns=p.columns)
    sma = pd.DataFrame(index=p.index,columns=p.columns)
    for i in window+np.arange(p.shape[1]-window):
        #loop each column for all dates
        sma.iloc[:,i] = np.mean(p.iloc[:,(i-window):(i-1)],axis=1)
    if signal_type=='long':
        signal = (sma<p)*1 #1 for holding a long position
    elif signal_type=='short':
        signal = (sma>p)*(-1) #-1 for holding a short position
    elif signal_type=='both':
        signal = (sma<p)*1+(sma>p)*(-1)
    signal.iloc[:,-1]=0 #always close position at the market close
    # return sma and the signal DataFrames, both nxm
    return sma, signal
    
########## define more technical indicators by yourself ##########
    


# Load your DataFrame and select the 5th column as the AMZN adjusted close price


