#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
from pandas_datareader import data, wb # 需要安装 pip install pandas_datareader
import datetime
import matplotlib.pyplot as plt
import matplotlib

# 定义获取数据的时间段
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016,5,20)
sh = data.DataReader("000001.SS", 'yahoo', start, end)
sh.head(3) # 数据获取成功

sh.describe() # 数据整体概览

sh['Close'].plot() #看一下收盘趋势

sh.to_csv('sh.csv',header=None)
names = ['Date','Open','High','Low','Close','Volume','Adj Close']
sh1 = pd.read_csv('sh.csv',names=names,index_col='Date')
sh1.tail(2)

# Detect missing values,用isnull函数
pd.isnull(sh).head() # or sh.isnull()