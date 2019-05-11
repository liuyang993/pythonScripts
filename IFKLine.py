import sys
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as md
import pymysql
import numpy as np
import datetime as dt

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

import everydayAnnotations

#print(sys.argv[1])
#print(sys.argv[2])

conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
#sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1904_20190327;'
#sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + sys.argv[1]  + ';'


sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + sys.argv[1]  + ' where time(happentime)<"'  + sys.argv[2]  + '";'
#sql = 'select lastprice, happentime   from ' + sys.argv[1]  + ' where time(happentime)<"'  + sys.argv[2]  + '";'


#sql = 'select lastprice ,happentime from ' + sys.argv[1]  + ';'
#print(sql)
a.execute(sql)
data=a.fetchall()
t=[]
s=[]
for result in data:
    t.append(result[0])
    s.append(result[1])
    #s.append(result[1].timestamp())   插值用这个

#print(s)
#print(t)


#z1 = np.polyfit(s, t, 3)#用3次多项式拟合
#p1 = np.poly1d(z1)
#print(p1) #在屏幕上打印拟合多项式

plt.plot(s, t)

everydayAnnotations.print_annotations(plt,sys.argv[1])






#设置时间轴间隔 比如15分钟
#xlocator = md.MinuteLocator(byminute=[0,15,30,45], interval = 1)
#plt.xaxis.set_major_locator(xlocator)

#from  https://stackoverflow.com/questions/42398264/matplotlib-xticks-every-15-minutes-starting-on-the-hour




plt.show()

