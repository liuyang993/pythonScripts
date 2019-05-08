import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time

# if FuPan calculate morning ,  use   x = datetime.datetime(2018,11,28,9,15)     ; hour(happentime)>=9
# if RealTime calculate morning ,  use   x = datetime.datetime(2018,11,28,11,33)  ; hour(happentime)>=9

#if RealTime cal night use x = datetime.datetime(2018,11,29,23,15)   ;  hour(happentime)>=21
#if FuPan cal night use x = datetime.datetime(2018,11,29,21,5)   ;  hour(happentime)>=21


x = datetime.datetime(2018,12,19,11,31)
#for i in range(1500):
while True:
    conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
    a=conn.cursor()
    sql = 'select happentime,lastprice from if1901_20181219 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit 120;'
    a.execute(sql,x)
    data=a.fetchall()
    #print(data)
    #print(x)s
    t=[]
    s=[]
    for result in data:
        t.append(result[0].timestamp())
        s.append(result[1])

    #print(t)
    #print(s)
    slope, intercept, r_value, p_value, std_err = stats.linregress(t,s)
    #if abs(slope)>0.1:
    print("when ", datetime.datetime.fromtimestamp(t[0]) , " 5 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])
    time.sleep(2)
    x= x + datetime.timedelta(seconds=3)
    conn.close()    #very important , remember MUST close 
    #plt.plot(t, s)
    #plt.show()