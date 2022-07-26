# my owner test 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as md
import pymysql
import numpy as np
import datetime as dt
import matplotlib.ticker as ticker
import pylab as pl

t=[4100,4105,4100,4105,4100,4105,4100,4105,4100,4105,4100,4105]
s=[dt.datetime.now(),dt.datetime.now()+dt.timedelta(seconds=1),dt.datetime.now()+dt.timedelta(seconds=2),dt.datetime.now()+dt.timedelta(seconds=3),
dt.datetime.now()+dt.timedelta(seconds=4),
dt.datetime.now()+dt.timedelta(seconds=5),
dt.datetime.now()+dt.timedelta(seconds=6),
dt.datetime.now()+dt.timedelta(seconds=7),
dt.datetime.now()+dt.timedelta(seconds=8),
dt.datetime.now()+dt.timedelta(seconds=9),
dt.datetime.now()+dt.timedelta(seconds=10),
dt.datetime.now()+dt.timedelta(minutes=1)]


N = len(s)
ind = np.arange(N) # the evenly spaced plot indices

def format_date(x, pos=None):
    thisind = np.clip(int(x+0.5), 0, N-1)
    return  pl.num2date(x).strftime('%Y-%m-%d %H:%M:%S')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(s, t)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
fig.autofmt_xdate()
plt.show()
