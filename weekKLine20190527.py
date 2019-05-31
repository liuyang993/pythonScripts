#  每周连续7天的 k线     
#  用法 ：  python f:/code/pythonscripts/weekKLine.py 
#  LIUYANG      2019/5/30



import sys
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as md
import pymysql
import numpy as np
import datetime as dt


conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()

sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190527;'  

a.execute(sql)
data=a.fetchall()

x=[]
s0=[]
for result in data:
    x.append(result[0])
    s0.append(result[1])


sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190528;'  

a.execute(sql)
data=a.fetchall()

y=[]
s=[]
for result in data:
    y.append(result[0])
    s.append(result[1])


sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190529;'  

a.execute(sql)
data=a.fetchall()

y1=[]
s1=[]
for result in data:
    y1.append(result[0])
    s1.append(result[1])

sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190530;'  

a.execute(sql)
data=a.fetchall()

y2=[]
s2=[]
for result in data:
    y2.append(result[0])
    s2.append(result[1])    




plt.subplot(1, 5, 1)
plt.plot(s0,x)
plt.ylim(3500,3800)
#plt.legend()

plt.subplot(1, 5, 2)
plt.plot(s,y)
plt.ylim(3500,3800)


plt.subplot(1, 5, 3)
plt.plot(s1,y1)
plt.ylim(3500,3800)

plt.subplot(1, 5, 4)
plt.plot(s2,y2)
plt.ylim(3500,3800)



plt.show()

