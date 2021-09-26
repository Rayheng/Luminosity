 -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 23:18:24 2021
@author: Ray O Light
"""

import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import datetime
import numpy as np
import matplotlib.pyplot as plt

# Constructing an time series index
idx = pd.date_range("2021-01-01" , periods = len(y) , freq = 'D')

# Random-ness
df1 = pd.DataFrame(np.random.rand(126,1) , index = idx , columns = ['Val'])
df1.plot(title = 'Random Time Series' , legend = False , ylabel = 'Value')

# Trending
df2 = pd.DataFrame(np.arange(1, 3, 2/126) , index = idx , columns = ['Val'])
df2.plot(title = 'Trending Time Series' , legend = False , ylabel = 'Value')

# Cyclical 
x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)

df3 = pd.DataFrame(y , index = idx, columns = ['Val'])
df3.plot(title = 'Cyclical' , legend = False , ylabel = 'Value')

# f(x) = tremd + cyclical + randomnesss 
df= df1 + df2 + df3
df.plot(title = 'Time Series' , legend = False , ylabel = 'Value')

