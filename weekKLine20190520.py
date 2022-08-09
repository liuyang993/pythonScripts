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

sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190520;'  

a.execute(sql)
data=a.fetchall()

x=[]
s0=[]
for result in data:
    x.append(result[0])
    s0.append(result[1])


sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190521;'  

a.execute(sql)
data=a.fetchall()

y=[]
s=[]
for result in data:
    y.append(result[0])
    s.append(result[1])


sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190522;'  

a.execute(sql)
data=a.fetchall()

y1=[]
s1=[]
for result in data:
    y1.append(result[0])
    s1.append(result[1])

sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190523;'  

a.execute(sql)
data=a.fetchall()

y2=[]
s2=[]
for result in data:
    y2.append(result[0])
    s2.append(result[1])    

sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190524;'  

a.execute(sql)
data=a.fetchall()

y3=[]
s3=[]
for result in data:
    y3.append(result[0])
    s3.append(result[1])  




plt.subplot(2, 1, 1)
plt.plot(s0,x)
# plt.ylim(3500,3800)
#plt.legend()

plt.subplot(2, 1, 2)
plt.plot(s,y)
# plt.ylim(3500,3800)


# plt.subplot(5, 1, 3)
# plt.plot(s1,y1)
# # plt.ylim(3500,3800)

# plt.subplot(5, 1, 4)
# plt.plot(s2,y2)
# # plt.ylim(3500,3800)

# plt.subplot(5, 1, 5)
# plt.plot(s3,y3)
# # plt.ylim(3500,3800)


plt.show()

