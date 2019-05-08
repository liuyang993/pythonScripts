import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time

x = datetime.datetime(2019,5,8,9,30)
firstTop =0
doubletop=0
FuPanIndexBegin = 0

sellingPrice = 0

lowPrice = 0
lastStopWinPrice = 0 

oporTime = 0
CurrentState = 0      #  0 mean observer ,  1 selling , 2 buying  

Todaymin=0
Todaymax =0

conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()

t=[]
s=[]


annotateIndexX=[]
annotateIndexY=[]

while True: 
    sql = 'select happentime,lastprice from ' + sys.argv[1]  + ' where happentime<=%s and hour(happentime)>=9  order by happentime desc limit 2;'
    a.execute(sql,x)
    data=a.fetchall()
    for result in data:
        t.append(result[0])
        s.append(result[1])

    x= x + datetime.timedelta(seconds=1)
    
    #print(s)

    plt.plot(t, s)
    #print(t[-1])
    #print(s[-1])
    if s.index(max(s)) < len(s)-600 :       # 发现高点，保存备注的坐标    
        #print(t.index(t[-1]))
        #print(s.index(s[-1]))
        #plt.annotate('Something', xy=(t[-1], s[-1]))
        annotateIndexX.append(t[-1])
        annotateIndexY.append(s[-1])        

    #print(annotateIndex)

    for i in range(len(annotateIndexX)):      #  试图加上备注  
        print('find high point at ', s[-1])
        plt.annotate('HighPoint', xy=(annotateIndexX[i],annotateIndexY[i]))

    #plt.annotate('Something', xy=(t[-1],s[-1]))

    #plt.draw()
    plt.pause(0.0001)
    #plt.pause(3)    
    plt.clf()


