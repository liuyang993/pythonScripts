import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time
import pyZMQTest

# if FuPan calculate morning ,  use   x = datetime.datetime(2018,11,28,9,15)     ; hour(happentime)>=9
# if RealTime calculate morning ,  use   x = datetime.datetime(2018,11,28,11,33)  ; hour(happentime)>=9

#if RealTime cal night use x = datetime.datetime(2018,11,29,23,15)   ;  hour(happentime)>=21
#if FuPan cal night use x = datetime.datetime(2018,11,29,21,5)   ;  hour(happentime)>=21


Last2TimeSlope = 0
Last1TimeSlope = 0
CurrentSlope = 0
BuyingState = 0
BuyingPrice=0
SellingState = 0
SellingPrice=0
StopLoseBuyPrice=0
StopLoseSellPrice=0


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

x = datetime.datetime(2018,11,30,11,33)
upBeginPrice =1 
while True:
    conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
    a=conn.cursor()
    sql = 'select happentime,lastprice from rb20181130 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit 600;'
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
    if CurrentSlope>Last1TimeSlope and Last1TimeSlope>Last2TimeSlope and Last1TimeSlope!=0 and Last2TimeSlope!=0 and BuyingState==0 and SellingState==0:    #and StopLoseBuyPrice + 5 < s[0]
        print("Start raise when ", datetime.datetime.fromtimestamp(t[0]) , " 1 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])
        print("buy 10 units at  ", s[0])
        sParam = "rb buy " + str(s[0]+3)
        pyZMQTest.SendCmdToCTP(sParam)
        BuyingPrice = s[0]
        BuyingState = 1
    #if already buy and profit great than 5 points , close it 
    if BuyingState==1 and s[0]>BuyingPrice+5:
        print("close buy 10 units at  ", s[0])
        sParam = "rb closebuy " + str(s[0]-2)
        pyZMQTest.SendCmdToCTP(sParam)
        BuyingState=0
        ResetSlope()
    # if buy wrong ,stop lose 
    if BuyingState==1 and s[0]<BuyingPrice-5:
        print("stop lose , close buy 10 units at  ", s[0])
        sParam = "rb closebuy  " + str(s[0]-3)
        pyZMQTest.SendCmdToCTP(sParam)
        BuyingState=0
        ResetSlope()
        StopLoseBuyPrice=BuyingPrice
    #if have not sell and tendence is down , sell it     
    if CurrentSlope<Last1TimeSlope and Last1TimeSlope<Last2TimeSlope and Last1TimeSlope!=0 and Last2TimeSlope!=0 and SellingState==0 and BuyingState==0:   #and StopLoseSellPrice>s[0] + 5 
        print("Start down when ", datetime.datetime.fromtimestamp(t[0]) , " 1 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])
        print("sell 10 units at  ", s[0]-3)
        sParam = "rb sell " + str(s[0])
        pyZMQTest.SendCmdToCTP(sParam)
        SellingPrice = s[0]
        SellingState = 1      
    #if already sell and profit great than 5 points , close it 
    if SellingState==1 and s[0]<SellingPrice-5:
        print("close sell 10 units at  ", s[0])
        sParam = "rb closesell " + str(s[0]+3)
        pyZMQTest.SendCmdToCTP(sParam)
        SellingState=0
        ResetSlope()
    # if sell wrong ,stop lose 
    if SellingState==1 and s[0]>SellingPrice+5:
        print("stop lose , close sell 10 units at  ", s[0])
        sParam = "rb closesell " + str(s[0]+3)
        pyZMQTest.SendCmdToCTP(sParam)
        SellingState=0
        ResetSlope()
        StopLoseSellPrice=SellingPrice

    #print("last2slope is ",Last2TimeSlope, " last1slpe is " , Last1TimeSlope , " current slope is " , CurrentSlope)
    #if slope>0.001:    # tendence begin up  
    #    upBeginPrice = s[0]
    #    print("Start raise when ", datetime.datetime.fromtimestamp(t[0]) , " 1 minutes slope is " ,"%.6f" % slope, " and that time 's price is ", s[0])
    time.sleep(3)
    x= x + datetime.timedelta(seconds=3)
    conn.close()    #very important , remember MUST close 




