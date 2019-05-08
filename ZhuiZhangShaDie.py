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


Last2TimeSlope = 0
Last1TimeSlope = 0
CurrentSlope = 0
BuyingState = 0
BuyingPrice=0

def UpdateSlope(s):
    global Last2TimeSlope
    global Last1TimeSlope
    global CurrentSlope
    Last2TimeSlope = Last1TimeSlope
    Last1TimeSlope=CurrentSlope
    CurrentSlope=s

def ResetSlope():
    global Last2TimeSlope
    global Last1TimeSlope
    global CurrentSlope
    Last2TimeSlope = 0
    Last1TimeSlope=0
    CurrentSlope=0    

x = datetime.datetime(2018,11,29,9,20)
upBeginPrice =1 
while True:
    conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
    a=conn.cursor()
    sql = 'select happentime,lastprice from rb20181129 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit 120;'
    a.execute(sql,x)
    data=a.fetchall()
    #print(data)
    #print(x)
    t=[]
    s=[]
    for result in data:
        t.append(result[0].timestamp())
        s.append(result[1])

    slope, intercept, r_value, p_value, std_err = stats.linregress(t,s)
    UpdateSlope(slope)
    print("last2slope is ", "%.6f" % Last2TimeSlope, " last1slpe is " , "%.6f" % Last1TimeSlope , " current slope is " , "%.6f" % CurrentSlope , " current price is ", s[0])

    #if have not buy and tendence is up , buy it 
    if CurrentSlope>Last1TimeSlope and Last1TimeSlope>Last2TimeSlope and Last1TimeSlope!=0 and Last2TimeSlope!=0 and BuyingState!=1:
        print("Start raise when ", datetime.datetime.fromtimestamp(t[0]) , " 1 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])
        print("buy 10 units at  ", s[0])
        BuyingPrice = s[0]
        BuyingState = 1
    #if already buy and profit great than 5 points , close it 
    if BuyingState==1 and s[0]>BuyingPrice+5:
        print("close buy 10 units at  ", s[0])
        BuyingState=0
        ResetSlope()
    if BuyingState==1 and s[0]<BuyingPrice-5:
        print("stop lose , close buy 10 units at  ", s[0])
        BuyingState=0
        ResetSlope()        



    #print("last2slope is ",Last2TimeSlope, " last1slpe is " , Last1TimeSlope , " current slope is " , CurrentSlope)
    #if slope>0.001:    # tendence begin up  
    #    upBeginPrice = s[0]
    #    print("Start raise when ", datetime.datetime.fromtimestamp(t[0]) , " 1 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])
    x= x + datetime.timedelta(seconds=3)
    conn.close()    #very important , remember MUST close 




