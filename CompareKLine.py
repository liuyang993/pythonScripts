import sys
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as md
import pymysql
import numpy as np
import datetime as dt

def normalizeArray(pa):
    amin,amax = min(pa),max(pa)
    for j in range(len(pa)):
        pa[j]=(pa[j]-amin)/(amax-amin)

conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()

#sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + sys.argv[1]  + ' where time(happentime)<"'  + sys.argv[2]  + '";'
sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + sys.argv[1]  + ' where time(happentime)>"'  + sys.argv[2]  + '" and time(happentime)<"' + sys.argv[3]  + '";' 



#print(sql)
a.execute(sql)
data=a.fetchall()


x=[]
s0=[]
for result in data:
    x.append(result[0])
    s0.append(result[1])

#print(t)
#normalizeArray(x)


sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190426'   + ' where time(happentime)>"'  + sys.argv[2]  + '" and time(happentime)<"' + sys.argv[3]  + '";'
#print(sql)
a.execute(sql)
data=a.fetchall()


y=[]
s=[]
for result in data:
    y.append(result[0])
    s.append(result[1])

#print(t)
#normalizeArray(y)

# python C:\Users\liuyang\Documents\TryToFindSimilarKLine.py if1906_20190430 09:31:00

#plt.plot(x,'r', label='x')
#plt.plot(y, 'g', label='y')
#plt.legend()
#plt.show()


plt.subplot(2, 1, 1)
plt.plot(x,'r', label='x')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(y, 'g', label='y')
plt.legend()

plt.show()

