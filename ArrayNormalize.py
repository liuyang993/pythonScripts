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

sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + sys.argv[1]  + ' where time(happentime)<"'  + sys.argv[2]  + '";'
#print(sql)
a.execute(sql)
data=a.fetchall()


x=[]
s0=[]
for result in data:
    x.append(result[0])
    s0.append(result[1])

print(x)
normalizeArray(x)
print(x)
#print(normalizeArray(x))



#Python36>python C:\Users\liuyang\Documents\ArrayNormalize.py if1906_20190430 09:31:00
