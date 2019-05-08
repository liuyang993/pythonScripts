import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np

conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
sql = 'select happentime,lastprice from rb3 where hour(happentime)<=15 order by happentime desc limit 600;'
a.execute(sql)
data=a.fetchall()
t=[]
s=[]
for result in data:
    t.append(result[0].timestamp())
    s.append(result[1])

#print(t)
#print(s)
slope, intercept, r_value, p_value, std_err = stats.linregress(t,s)

print("last N minutes slope is ",slope)
#plt.plot(t, s)
#plt.show()