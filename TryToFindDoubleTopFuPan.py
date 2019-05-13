import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time

x = datetime.datetime(2019,9,9,9,31)
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
#sql = 'select happentime,lastprice from if1904_20190325 where happentime<=%s and hour(happentime)>=9  order by happentime asc ;'
sql = 'select happentime,lastprice from ' + sys.argv[1]  + ' where happentime<=%s and hour(happentime)>=9  order by happentime asc ;'
a.execute(sql,x)
data=a.fetchall()
#print(data)
#print(x)s
t=[]
s=[]
for result in data:
    t.append(result[0])
    #t.append(result[0].timestamp())
    s.append(result[1])
conn.close()    #very important , remember MUST close 

Todaymin=min(s)
Todaymax =max(s)
    
FuPanArray=[]
i =0

while i<len(s): 
    #if oporTime>=4:
        #break

    FuPanArray.append(s[i])
    i=i+1
    #print(FuPanArray)
    #time.sleep(1)
    if CurrentState==0:
        if FuPanArray.index(max(FuPanArray)) < len(FuPanArray)-600 and firstTop ==0:
            print('Find first top value is : ' , max(FuPanArray) , ' at ' , t[FuPanIndexBegin + FuPanArray.index(max(FuPanArray))] )
            firstTop = max(FuPanArray)
            continue
        if firstTop !=0 and FuPanArray[-1] > firstTop - 5  and doubletop==0:
            print('Find double top value is : ' , FuPanArray[-1], ' wait until double top reach high')
            doubletop = FuPanArray[-1]
            continue
        if firstTop !=0 and doubletop!=0 and  FuPanArray[-1] > doubletop:
            doubletop = FuPanArray[-1]
            continue

        if firstTop !=0 and doubletop!=0 and  FuPanArray[-1] < doubletop-2:    
            print('double top max value is : ' , doubletop, 'but now have begin to drop down , will sell it at price ' , FuPanArray[-1] , ' when  ' , t[i])
            firstTop=0
            doubletop = 0
            sellingPrice = FuPanArray[-1]
            lowPrice = sellingPrice
            FuPanArray.clear()
            FuPanIndexBegin =  i
            CurrentState =1 
            #print(FuPanIndexBegin)
            oporTime=oporTime+1
            continue
    if CurrentState == 1:
        if FuPanArray[-1] < sellingPrice - 10:
            print('selling profit is enough , will stop win at price  : ' , FuPanArray[-1] , ' when ' , t[i] )
            sellingPrice=0
            CurrentState = 0
            FuPanArray.clear()
            FuPanIndexBegin =  i
            #break
            oporTime=oporTime+1
            continue
        if FuPanArray[-1] > sellingPrice + 5:
            print('selling profit must stop lose at price  : ' , FuPanArray[-1] , ' when ' , t[i] )
            sellingPrice=0
            CurrentState = 0
            FuPanArray.clear()
            FuPanIndexBegin =  i
            oporTime=oporTime+1
            continue     

       #print(t)

print('Today min is : ', Todaymin , ' Today high is : ' , Todaymax)

    #print(s)
    #print(s[-1])

    #print('Maximum is: ', max(s) , " and it position is ", s.index(max(s)))

    #if s.index(max(s)) < len(s)-600 and firstTop ==0:
    #    print('Find first top value is : ' , max(s) )
    #    firstTop = max(s)

    #if firstTop !=0 and s[-1] > firstTop:
    #    print('Find double top value is : ' , s[-1])

    #if firstTop !=0 and max(s) > firstTop and max(s)!=firstTop:
    #    print('Find double top value is : ' , max(s))
    #    firstTop=0


     