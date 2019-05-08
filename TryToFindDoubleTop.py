import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time

x = datetime.datetime(2019,4,15,9,30)
firstTop =0
t=[]
s=[]
#for i in range(1500):
while True:
    conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
    a=conn.cursor()
    sql = 'select happentime,lastprice from if1904_20190415 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit 2 ;'
    a.execute(sql,x)
    data=a.fetchall()
    #print(data)
    #print(x)s
    for result in data:
        t.append(result[0].timestamp())
        s.append(result[1])
    #print(t)

    #print(s)
    #print(s[-1])

    #print('Maximum is: ', max(s) , " and it position is ", s.index(max(s)))

    if s.index(max(s)) < len(s)-600 and firstTop ==0:
        #print('Find first top value is : ' , max(s) )
        print('Find first top value is : ' , max(s) , ' at ' , t[s.index(max(s))] )
        firstTop = max(s)

    #if firstTop !=0 and s[-1] > firstTop:
    #    print('Find double top value is : ' , s[-1])

    if firstTop !=0 and max(s) > firstTop and max(s)!=firstTop:
        print('Find double top value is : ' , max(s))
        firstTop=0
    
    
    #slope, intercept, r_value, p_value, std_err = stats.linregress(t,s)
    #print("when ", datetime.datetime.fromtimestamp(t[0]) , " 5 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])
    time.sleep(1)
    x= x + datetime.timedelta(seconds=1)
    conn.close()    #very important , remember MUST close 
    