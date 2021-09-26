# -*- coding: utf-8 -*-
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

idx = pd.date_range("2021-01-01" , periods = 20 , freq = 'D')


df = pd.to_datetime(['1/1/2021' , np.datetime64("2021-01-01")])
