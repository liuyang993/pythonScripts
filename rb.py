import sys
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql

#plt.figure()
#plt.subplot(1,2,1)

conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
#sql = 'select * from rb20181212 where hour(happentime)=21 and  hour(happentime)<=23;'
sql = 'select lastprice ,case when hour(happentime)>=21 then DATE_ADD(happentime,interval 10 hour) else happentime end  from rb20181212;'
a.execute(sql)
data=a.fetchall()
t=[]
s=[]
for result in data:
    t.append(result[0])
    s.append(result[1])
plt.plot(s, t)

plt.show()



