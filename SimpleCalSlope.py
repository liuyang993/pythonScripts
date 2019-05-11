import sys
import pymysql
from scipy import stats
import numpy as np
import datetime
import time


# if FuPan calculate morning ,  use   x = datetime.datetime(2018,11,28,9,15)     ; hour(happentime)>=9
# if RealTime calculate morning ,  use   x = datetime.datetime(2018,11,28,11,33)  ; hour(happentime)>=9

#if RealTime cal night use x = datetime.datetime(2018,11,29,23,15)   ;  hour(happentime)>=21
#if FuPan cal night use x = datetime.datetime(2018,11,29,21,5)   ;  hour(happentime)>=21


x = datetime.datetime(2019,5,9,9,30)





initRecords =120    #  1 minutes 

conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
while True:
    sql = 'select happentime,lastprice from if1906_20190509 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit %s;'
    #a.execute(sql,x)

    input = (x,initRecords)
    a.execute(sql,input) 
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



    print("when ", datetime.datetime.fromtimestamp(t[0]) , " 1 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])



    time.sleep(0.1)
    #time.sleep(5)    
    x= x + datetime.timedelta(seconds=1)
    #conn.close()    #very important , remember MUST close 
    #plt.plot(t, s)
    #plt.show()
conn.close() 
