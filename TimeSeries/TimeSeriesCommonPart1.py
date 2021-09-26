 -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 23:18:24 2021
@author: Ray O Light
"""

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

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

# f(x) = trend + cyclical + randomnesss 
df= df1 + df2 + df3
df.plot(title = 'Time Series' , legend = False , ylabel = 'Value')

df['MA_10'] = df.rolling(10)['Val'].mean()
df['MA_20'] = df.rolling(20)['Val'].mean()
df['MA_50'] = df.rolling(50)['Val'].mean()


# Art and Craft Time
fig , ax = plt.subplots(figsize = (12, 8))

# Add x-axis and y-axis
ax.plot(df.index.values, df['Val'], color='black' , label = 'Time Series')
ax.plot(df.index.values, df['MA_10'], color='red' , label = 'MA (10)')
ax.plot(df.index.values, df['MA_20'], color='green' , label = 'MA (20)')
ax.plot(df.index.values, df['MA_50'], color='blue' , label = 'MA (50)')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Value",
       title="Time Series with Moving Average")

# Define the date format
date_form = DateFormatter("%d-%b")
ax.xaxis.set_major_formatter(date_form)

# Ensure a major tick for each week using (interval=1) 
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
ax.legend()

plt.show()

