# 要实现的功能  1--- 实时描述图形 


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
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'], index_col='date')


firstTop =0
t=[]
s=[]

qSlope= queue.Queue(maxsize=240)   # 10 个元素的队列 
qSlope.empty()



# t= queue.Queue(maxsize=10)   # 10 个元素的队列 
# t.empty()


# s= queue.Queue(maxsize=10)   # 10 个元素的队列 
# s.empty()



# def compareQueue(L):    # 计算10个元素的队列里， 后一个比前一个数值大情况有多少 
#     LofQ = list(L.queue)
#     IGreater = 0 
#     for k in range(0,len(LofQ),1):
#         #print(LofQ[k])
#         if k!=len(LofQ)-1:
#             if LofQ[k]<LofQ[k+1]:
#                 IGreater=IGreater+1
#         if k==len(LofQ)-1:
#             if LofQ[k-1]<LofQ[k]:
#                 IGreater=IGreater+1
#     return IGreater


def compareQueue(L):    # 计算10个元素的队列里，是不是最大值出现在中间， 如果是， 说明找到了值的顶部
    LofQ = list(L.queue)
    max_item = max(LofQ)
    maxIndex = LofQ.index(max_item)

    min_item = min(LofQ)
    minIndex = LofQ.index(min_item)

    str=''

    # if maxIndex==9 or maxIndex==10 :
    if maxIndex==120 :
        str='top'
        return  str,maxIndex
    if minIndex==120 :
        str='bottom'
        return  str,minIndex
    else:
        str='not'
        return  str,0
        



x = datetime.datetime(2018,12,21,9,30,2)

#for i in range(1500):
conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
while True:
    # print("-----------------")
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
        print(result[0])
        print(result[1])


    # print(t)
    # print(s)
    #print(s[-1])



    if len(t)>10:
        slope, intercept, r_value, p_value, std_err = stats.linregress(t[-10:],s[-10:])
        print("time  is ", result[0], " price is " , result[1] , " current slope is " , "%.6f" % slope )

        if qSlope.full():  # 如果满了 ，最早的出队
            qSlope.get()
            qSlope.put("{:.4f}".format(slope))
        else:
            qSlope.put("{:.4f}".format(slope))
        # print(list(qSlope.queue))

        if qSlope.full():            # 队列满了就比较
            strRtn,ii=compareQueue(qSlope)
            if ii>0:
                if strRtn=='top':
                    # print("time  is ", result[0], " price is " , result[1] , " current slope is " , "%.6f" % slope )
                    # print(ii)
                    # print("time  is ", datetime.datetime.fromtimestamp(t[-ii:]), " price is " , s[-ii:] , " find top value "  )
                    print("time  is ", datetime.datetime.fromtimestamp(t[-ii]), " price is " , s[-ii] , " find top value , and current time is " , x , 'current price is ' , s[-1] )

                    # print(list(qSlope.queue))
                if strRtn=='bottom':
                    # print("time  is ", result[0], " price is " , result[1] , " current slope is " , "%.6f" % slope )
                    # print(ii)
                    # print("time  is ", datetime.datetime.fromtimestamp(t[-ii:]), " price is " , s[-ii:] , " find top value "  )
                    print("time  is ", datetime.datetime.fromtimestamp(t[-ii]), " price is " , s[-ii] , " find bottom value , and current time is " , x , 'current price is ' , s[-1] )

                    # print(list(qSlope.queue))


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
    time.sleep(5)
    x= x + datetime.timedelta(seconds=1)
conn.close()    #very important , remember MUST close 
    