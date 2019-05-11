import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time
import logging
from enum import Enum
import queue

logging.basicConfig(filename='example.log',level=logging.DEBUG)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

# if FuPan calculate morning ,  use   x = datetime.datetime(2018,11,28,9,15)     ; hour(happentime)>=9
# if RealTime calculate morning ,  use   x = datetime.datetime(2018,11,28,11,33)  ; hour(happentime)>=9

#if RealTime cal night use x = datetime.datetime(2018,11,29,23,15)   ;  hour(happentime)>=21
#if FuPan cal night use x = datetime.datetime(2018,11,29,21,5)   ;  hour(happentime)>=21

def compareQueue(L):
    LofQ = list(L.queue)
    IGreater = 0 
    for k in range(0,len(LofQ),1):
        #print(LofQ[k])
        if k!=len(LofQ)-1:
            if LofQ[k]<LofQ[k+1]:
                IGreater=IGreater+1
        if k==len(LofQ)-1:
            if LofQ[k-1]<LofQ[k]:
                IGreater=IGreater+1
    return IGreater





x = datetime.datetime(2019,5,9,9,30)

currentOneMinuteSlope=0.0    
currentOneMinutePrice=0.0

LastTimeSlope=0.0
LastTimePrice=0.0

LastTwoTimeSlope=0.0
LastTwoTimePrice=0.0

class State(Enum):
    beginRaise = 1
    stopRaise = 2
    beginDrop = 3
    null      = 9


currentState = State.null

initRecords =120    #  1 minutes 

qSlope= queue.Queue(maxsize=10)   # 10 个元素的队列 
qSlope.empty()

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

    if qSlope.full():
        qSlope.get()
        qSlope.put(slope)
    else:
        qSlope.put(slope)

    #for elem in list(qSlope.queue):
        #print(elem)
    ii=0
    if qSlope.full():
        ii=compareQueue(qSlope)
    #print('ii is ',ii)

    if ii>=7:
        print("when ", datetime.datetime.fromtimestamp(t[0]) , ' at ' ,s[0] , " curve begin raise ")

    if ii<=3:
        print("when ", datetime.datetime.fromtimestamp(t[0]) , ' at ' ,s[0] , " curve stop raise ")


    #初始化前3次 slope
    #if currentOneMinuteSlope==0.0:
        #currentOneMinuteSlope = slope
        #continue
    
    #if LastTimeSlope==0.0:
        #LastTimeSlope = currentOneMinuteSlope
        #currentOneMinuteSlope = slope
        #continue

    #if LastTwoTimeSlope==0.0:
        #LastTwoTimeSlope = LastTimeSlope
        #LastTimeSlope = currentOneMinuteSlope
        #currentOneMinuteSlope = slope
        #continue       


    #now all slope is not 0 
    
    #LastTwoTimeSlope = LastTimeSlope
    #LastTimeSlope = currentOneMinuteSlope
    #currentOneMinuteSlope = slope 
     
    #if currentOneMinuteSlope>LastTimeSlope and LastTimeSlope > LastTwoTimeSlope and currentState!=State.beginRaise:
        #print("when ", datetime.datetime.fromtimestamp(t[0]) , "curve begin raise , slope is  " ,"%.6f" % slope, " and that time 's slope is ", "%.6f" % LastTimeSlope , 'and last two time slope is ',  "%.6f" % LastTwoTimeSlope)
        #currentState = State.beginRaise

    #if currentState==State.beginRaise:
        #initRecords = initRecords + 2 

    #if currentOneMinuteSlope<LastTimeSlope and LastTimeSlope < LastTwoTimeSlope and currentState==State.beginRaise:
        #print("when ", datetime.datetime.fromtimestamp(t[0]) , "curve stop raise , slope is  " ,"%.6f" % slope, " and that time 's slope is ", "%.6f" % LastTimeSlope , 'and last two time slope is ',  "%.6f" % LastTwoTimeSlope)
        #currentState = State.stopRaise
        #initRecords = 120


    #print("when ", datetime.datetime.fromtimestamp(t[0]) , " 1 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])
    
    #logging.debug("when ", datetime.datetime.fromtimestamp(t[0]) , " 1 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])

    #if slope<lastSlope and s[0]<lastPrice-3:
        #print('reach raise top point at ', s[0] , ' when ' , datetime.datetime.fromtimestamp(t[0]))
        #print('current slope is ', slope , ' lastSlope is ' , lastSlope)
        #print('current price is ', s[0] , ' lastPrice is ' , lastPrice)


    
    #lastSlope=slope
    #lastPrice=s[0]


    time.sleep(0.1)
    #time.sleep(5)    
    x= x + datetime.timedelta(seconds=1)
    #conn.close()    #very important , remember MUST close 
    #plt.plot(t, s)
    #plt.show()
conn.close() 
