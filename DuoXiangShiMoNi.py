import sys
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
import numpy as np


conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1901_20181220;'   # limit 10
a.execute(sql)

firstRow = a.fetchone()
startTimestamp = firstRow[1].timestamp()


data=a.fetchall()
t=[]
s=[]

for result in data:
    t.append(result[0])
    s.append(result[1].timestamp()-startTimestamp)
    #s.append(result[1].timestamp())   插值用这个

#print(s)
#print(t)

z1 = np.polyfit(s, t, 2)#用3次多项式拟合
p1 = np.poly1d(z1)
print(p1) #在屏幕上打印拟合多项式


#plt.plot(s, t)

#plt.show()