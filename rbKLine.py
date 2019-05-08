import sys
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
import numpy as np

#plt.figure()
#plt.subplot(1,2,1)

conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
sql = 'select lastprice ,case when hour(happentime)>=21 then DATE_ADD(happentime,interval 10 hour) else happentime end  from rb1905_20181217;'
a.execute(sql)
data=a.fetchall()
t=[]
s=[]
for result in data:
    t.append(result[0])
    s.append(result[1].timestamp())
    #s.append(result[1].timestamp())   插值用这个

#z1 = np.polyfit(s, t, 3)#用3次多项式拟合
#p1 = np.poly1d(z1)
#print(p1) #在屏幕上打印拟合多项式


plt.plot(s, t)

plt.show()



