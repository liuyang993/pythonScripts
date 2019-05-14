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

def compareQueue(L):    # 计算10个元素的队列里， 后一个比前一个数值大情况有多少 
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


#x = datetime.datetime(2019,5,13,9,33,13)
x = datetime.datetime(2019,5,14,9,30)

startRaiseTime = datetime.datetime(2000,1,1,9,30)
startDropTime =  datetime.datetime(2000,1,1,9,30)



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

initRecords =4    #  1 minutes 

qSlope= queue.Queue(maxsize=10)   # 10 个元素的队列 
qSlope.empty()

conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
while True:
    #sql = 'select happentime,lastprice from if1906_20190514 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit %s;'     # %s
    sql = 'select happentime,b1 from if1906_20190514 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit %s;'     # %s

    #a.execute(sql,x)

    input = (x,initRecords)
    a.execute(sql,input)
    #a.execute(sql,x)  
    data=a.fetchall()
    #print(data)
    #print(x)s
    t=[]
    s=[]


    i=0
    isum=0
    for result in data:
        if i!=2:
            #print('add first two element')
            isum= isum + result[1]
            i = i +1 
            if i==2:
                t.append(result[0].timestamp())
                s.append(isum/2)
                i=0
                isum=0 

    #print(t)
    #print(s)
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(t,s)
    
    #slope = (s[-1]-s[0])/(t[-1]-t[0])
    #slope = 0-slope
    
    if qSlope.full():  # 如果满了 ，最早的出队
        qSlope.get()
        qSlope.put(slope)
    else:
        qSlope.put(slope)

    #for elem in list(qSlope.queue):
        #print(elem)
    ii=0
    if qSlope.full():            # 队列满了就比较
        ii=compareQueue(qSlope)
    #print('ii is ',ii)

    if ii>=8 and currentState != State.beginRaise :
        print("when ", datetime.datetime.fromtimestamp(t[0]) , ' at ' ,s[0] , " curve begin raise ")
        currentState=State.beginRaise
        #for elem in list(qSlope.queue):
            #print(elem)
        print('i is ',ii)
        startRaiseTime = datetime.datetime.fromtimestamp(t[0])
        if startRaiseTime < startDropTime + datetime.timedelta(minutes=1):
            print(" find real buy point ")        
        #initRecords=initRecords+2
    #if currentState == State.beginRaise:
        #print("when ", datetime.datetime.fromtimestamp(t[0]) , ' at ' , s[0], ", slope is  " ,"%.6f" % slope)
    if ii<=3 and ii!=0 and currentState != State.beginDrop :                        # s[0]<s[1]
        print("when ", datetime.datetime.fromtimestamp(t[0]) , ' at s[0] is  ' ,s[0] , ' and s[1] is ' , s[1] ,  " curve begin drop ")
        currentState=State.beginDrop
        #for elem in list(qSlope.queue):
            #print(elem)
        print('i is ',ii)
        startDropTime = datetime.datetime.fromtimestamp(t[0])
        if startDropTime < startRaiseTime + datetime.timedelta(minutes=1):
            print(" find real sell point ")

    #print('...........')

    initRecords=initRecords+2 
    #print(s[-1],s[0],t[-1],t[0],slope,ii)
    #print(slope)    


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
    
    conn.autocommit(True)      # 如果不加这句 ， 会一直查出同样的结果 
    time.sleep(0.01)
    #time.sleep(5)    
    x= x + datetime.timedelta(seconds=1)
    #print(x)
    #conn.close()    #very important , remember MUST close 
    #plt.plot(t, s)
    #plt.show()
conn.close() 

