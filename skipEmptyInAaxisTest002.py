from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker

# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
with cbook.get_sample_data('goog.npz') as datafile:
    r = np.load(datafile)['price_data'].view(np.recarray)
r = r[-30:]  # get the last 30 days
# Matplotlib works better with datetime.datetime than np.datetime64, but the
# latter is more portable.
date = r.date.astype('O')
#print(date)
#print(r.adj_close)

# first we'll do it the default way, with gaps on weekends
fig, axes = plt.subplots(ncols=2, figsize=(8, 4))
ax = axes[0]
ax.plot(date, r.adj_close, 'o-')
#ax.plot(date, r.adj_close)
#ax.xaxis.set_major_locator(ticker.MultipleLocator(5))   # 设置 横轴 密度
ax.set_title("Default")
fig.autofmt_xdate()

# next we'll write a custom formatter
N = len(r)
#print(N)

ind = np.arange(N)  # the evenly spaced plot indices
#print(ind)


def format_date(x, pos=None):
    print("x is ", x)
    thisind = np.clip(int(x + 0.5), 0, N - 1)
    print("thisind is ", thisind)
    return date[thisind].strftime('%Y-%m-%d')

ax = axes[1]
ax.plot(ind, r.adj_close, 'o-')
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
ax.set_title("Custom tick formatter")
fig.autofmt_xdate()

plt.show()


# from  https://matplotlib.org/2.1.2/gallery/api/date_index_formatter.html   这个是最正确的 ， 周末没有数据， 所以在第二个sub plot 没显示周末的日期 
