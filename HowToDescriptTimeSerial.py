# 要实现的功能  1--- 实时描述图形 当前是涨势还是跌势， 标出转折点， 预测反弹和下跌点位， 


# 资料 ： https://phdinds-aim.github.io/time_series_handbook/02_LinearForecastingTrendandMomentumForecasting/02_LinearTrendandMomentumForecasting.html 
#         https://blog.csdn.net/youcans/article/details/117702996   

#    怎么画蜡烛图 -----  https://levelup.gitconnected.com/five-useful-pandas-scripts-for-financial-time-series-plots-99693c4025b2 

#  怎么判断dataframe 的 trend ： 
    # https://stackoverflow.com/questions/71031226/calculating-trend-per-customer-level-in-python-dataframe 
    # https://dev.to/acnice/sales-trend-analysis-with-pandas-1bcm
    


import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time
import queue
# from datetime import datetime as dt
import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt

t=[]
s=[]

df = pd.DataFrame( columns=['date','value'])

x = datetime.datetime(2018,12,21,9,30,2)

#for i in range(1500):
conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
# while True:
while x < datetime.datetime(2018,12,21,9,32,2):
    print("-----------------")
    a=conn.cursor()
    sql = 'select happentime,lastprice from if1901_20181221 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit 2 ;'
    a.execute(sql,x)
    data=a.fetchall()
    conn.commit()
    # print(x)
    #print(x)s
    for result in data:
        # if t.full():
        #     t.get()
        #     s.get()
        #     t.put(result[0].timestamp())
        #     s.put(result[1])
        # else:
        #     t.put(result[0].timestamp())
        #     s.put(result[1])
        t.append(result[0].timestamp())
        s.append(result[1])
        # print(result[0])
        # print(result[1])
        df=df.append({'date':result[0],'value':result[1]}, ignore_index=True)

    # print(t)
    # print(s)
    #print(s[-1])
    print(df.head(1000))


    # #print('Maximum is: ', max(s) , " and it position is ", s.index(max(s)))

    # if s.index(max(s)) < len(s)-600 and firstTop ==0:
    #     #print('Find first top value is : ' , max(s) )
    #     print('Find first top value is : ' , max(s) , ' at ' , t[s.index(max(s))] )
    #     firstTop = max(s)

    # #if firstTop !=0 and s[-1] > firstTop:
    # #    print('Find double top value is : ' , s[-1])

    # if firstTop !=0 and max(s) > firstTop and max(s)!=firstTop:
    #     print('Find double top value is : ' , max(s))
    #     firstTop=0
    
    
    #slope, intercept, r_value, p_value, std_err = stats.linregress(t,s)
    #print("when ", datetime.datetime.fromtimestamp(t[0]) , " 5 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])
    time.sleep(0.1)
    x= x + datetime.timedelta(seconds=1)
conn.close()    #very important , remember MUST close 
print('now will print description')
print(df['value'].describe())


    