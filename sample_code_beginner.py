# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:29:50 2022

@author: Anqi
"""

import numpy as np
import pandas as pd

#This is a short comment
''' This is a long comment '''

''' Test how the list works '''
a = [2,4,6]
b = [6,5,4]
print(a+b)

''' Test how the numpy array works '''
print(np.arange(10)) #an integer series from 0 to 9
x = np.array(a)
y = np.array(b)
print(x+y)
print(x[2]) #get the 3rd element in x

''' Test how the numpy matrix works '''
mat = np.zeros((3,5)) #a 3x5 matrix filled with 0s
mat[0,3] = 6 #change value in row 1 column 4 to 6
mat[1,1] = 3
mat[1] = np.arange(5)
print(mat[1]) #get the 2nd row
print(mat[-1]) #get the last row
print(mat[1:3,:3]) #get the rows 2-3 and columns 0-3
print(mat[:,1])#get the 2nd column -> transferred into an array

''' An example of pandas dataframe '''
dat = pd.DataFrame(index=3+np.arange(len(x)),columns=['x','y'])
dat['x'] = x #assign values
dat['y'] = y
dat.iloc[1] #get the 2nd row of records
dat.loc[5] #get the row of records with index=5
dat.iloc[:3]
dat.loc[3:5,'x']
dat.iloc[1:3]['y']