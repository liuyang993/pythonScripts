# 要实现的功能  1--- 实时描述图形 当前是涨势还是跌势， 标出转折点， 预测反弹和下跌点位， 在哪里做
                    # 假顶和假底了， 什么点位买入卖出的人上当了？ 
                    


# 资料 ： https://phdinds-aim.github.io/time_series_handbook/02_LinearForecastingTrendandMomentumForecasting/02_LinearTrendandMomentumForecasting.html 
#         https://blog.csdn.net/youcans/article/details/117702996   

#    怎么画蜡烛图 -----  https://levelup.gitconnected.com/five-useful-pandas-scripts-for-financial-time-series-plots-99693c4025b2 

#  怎么判断dataframe 的 trend ： 
    # https://stackoverflow.com/questions/71031226/calculating-trend-per-customer-level-in-python-dataframe 
    # https://dev.to/acnice/sales-trend-analysis-with-pandas-1bcm
    
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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
from statsmodels.tsa.stattools import adfuller

def trendline(index,data, order=1):
    coeffs = np.polyfit(index, list(data), order)
    slope = coeffs[-2]
    return float(slope)



t=[]
s=[]

df = pd.DataFrame( columns=['startValue','endValue','upOrDown','slope'])

x = datetime.datetime(2022,8,4,13,30,2)

#for i in range(1500):
conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
# while True:

jjj=0

while x < datetime.datetime(2022,8,4,14,0,0):
    # print("-----------------")
    a=conn.cursor()
    sql = 'select happentime,lastprice from oi2209_20220804 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit 2 ;'
    a.execute(sql,x)
    data=a.fetchall()
    conn.commit()

    # for result in data:
    #     t.append(result[0].timestamp())
    #     s.append(result[1])
    #     print(result[0])
    #     print(result[1])
    #     # df=df.append({'date':result[0],'value':result[1]}, ignore_index=True)
    #     df = pd.concat([df, pd.DataFrame.from_records([{'date':result[0],'value':result[1]}])])

    

    t.append(data[0][0].timestamp())
    s.append((data[0][1] + data[1][1])/2)    
    jjj=jjj+1

    if jjj==60:
        # print('reach 1 minute')
        # print(t[-jjj:])
        # print(s[-jjj:])
        # print([s])
        resultent=trendline(t[-jjj:],s[-jjj:])
        # print(resultent)
        # print('***********************************')

        if resultent > 0 :
            print ('until time' ,datetime.datetime.fromtimestamp(t[-1]), 'the last one minute trend is up ,slop is  ' , resultent )
            df = pd.concat([df, pd.DataFrame.from_records([{'startValue':s[-60],'endValue':s[-1],'upOrDown':'Up','slope': resultent}])])

        if resultent < 0 :
            print ('until time' ,datetime.datetime.fromtimestamp(t[-1]), 'the last one minute trend is down ,slop is  ' , resultent )
            df = pd.concat([df, pd.DataFrame.from_records([{'startValue':s[-60],'endValue':s[-1],'upOrDown':'Down','slope': resultent}])])
        jjj=0
        # print(df.head(1000))
        # print(df[['startValue', 'endValue','slope']].to_numpy())
        # print(df[['upOrDown']].to_numpy())
        # print("****************************************")

    # time.sleep(3)
    x= x + datetime.timedelta(seconds=1)
conn.close()    #very important , remember MUST close 

X_train, X_test, y_train, y_test = train_test_split(df[['startValue', 'endValue','slope']].to_numpy(), df[['upOrDown']].to_numpy(), test_size=0.4, random_state = 42,shuffle=False)

print('----------')
print(X_train)
print(len(X_train))

print('----------')
print(X_test)
print(len(X_test))

print('----------')
print(y_train)
print(len(y_train))

print('----------')
print(y_test)
print(len(y_test))


knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test) 

print('actual Y value is :')
print(y_test)

print('knn predict  Y value is :')
print(y_pred_knn)

print('knn Train accuracy %s' % knn.score(X_train, y_train))

print('knn Regression Test accuracy %s' % accuracy_score(y_pred_knn, y_test)) #Test accuracy

print(classification_report(y_test, y_pred_knn)) #Classification Report


# df.to_csv('out.csv', sep='\t', encoding='utf-8')


# print('now will print description')
# print(df['value'].describe())

# X= df['value']
# result = adfuller(X)
# print('ADF Statistic: %f' % result[0])
# print('p-value: %f' % result[1])
# print('Critical Values:')
# for key, value in result[4].items():
# 	print('\t%s: %.3f' % (key, value))

