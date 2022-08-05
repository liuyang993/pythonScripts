import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time
import queue
import threading

# 找出极值   https://stackoverflow.com/questions/22583391/peak-signal-detection-in-realtime-timeseries-data/22640362#22640362
         #  https://github.com/Rgveda/GolemQ/tree/45beff9b1499da52042466eb207cffc7a1c1e2a3/analysis    中国人写的量化库

# class real_time_peak_detection(): 这种方法要先定义一个threshold，临界值， 但是实际情况中，上哪找这个临界值去。谁知道应该定义多少合适 


firstTop =0
t=[]
s=[]

xx=[]
yy=[]

def trendline(index,data, order=1):
    coeffs = np.polyfit(index, list(data), order)
    slope = coeffs[-2]
    return float(slope)

def realtimequeryDB(tablename):
    # x = datetime.datetime(2022,8,5,9,1,2)
    x = datetime.datetime.now()

    conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
    a=conn.cursor()


    jjj=0
    # while x < datetime.datetime(2022,8,5,15,0,2):
    while True:
            
        if (x.time() >  datetime.time(10,15)) and (x.time() <  datetime.time(10,30)):
            x= x + datetime.timedelta(seconds=1)
            time.sleep(1)
            continue

        if (x.time() >  datetime.time(11,30)) and (x.time() <  datetime.time(13,30)):
            x= x + datetime.timedelta(seconds=1)
            time.sleep(1)
            continue

        strtime = x.time().strftime("%H:%M:%S")
        
        sql = 'select happentime,lastprice from ' + tablename  + ' where time(happentime)<=%s and hour(happentime)>=9  order by happentime desc limit 2 ;'
        a.execute(sql,strtime)

        data=a.fetchall()
        conn.commit()        

        t.append(data[0][0].timestamp())
        # t.append(data[ii][0])
        s.append((data[0][1] + data[1][1])/2)

        # print(datetime.datetime.fromtimestamp(t[-1]))
        # print(s[-1])        

        if jjj==10:
            # slope, intercept, r_value, p_value, std_err = stats.linregress(t[-iii:],s[-iii:])
            # print(slope)
            # print(s)
            # print('------------------')
            
            # print(s[-jjj:])
            resultent=trendline(t[-jjj:],s[-jjj:])
            # print(resultent)  
            
            jjj=0
            if not xx:
                xx.append(10)
            else:
                xx.append(xx[-1] + 10 )  
            yy.append(resultent)      
            # print(xx)
            # print(yy)

            
            if len(yy)>3 and (yy[-1]<yy[-2]) and (yy[-2]<yy[-3]) and ((yy[-1]+yy[-2]+yy[-3]) < -2.0) : 
                print (tablename ,' find quick down trend at ' ,datetime.datetime.fromtimestamp(t[-1]) , ' value is ' , s[-1]  )

            if len(yy)>3 and (yy[-1]>yy[-2]) and (yy[-2]>yy[-3]) and ((yy[-1]+yy[-2]+yy[-3]) > 2.0) : 
                print (tablename ,' find quick up trend at ' ,datetime.datetime.fromtimestamp(t[-1]) , ' value is ' , s[-1]  )

              

        # print(datetime.datetime.fromtimestamp(t[-1]))
        # print(s[-1])

        jjj=jjj+1
        time.sleep(1)
        x= x + datetime.timedelta(seconds=1)      

realtimequeryDB(sys.argv[1])


# 发现多线程有问题 2022-08-05

# # creating thread
# t1 = threading.Thread(target=realtimequeryDB, args=('oi2209_20220805',))
# t2 = threading.Thread(target=realtimequeryDB, args=('pta2209_20220805',))

# # starting thread 1
# t1.start()
# # starting thread 2
# t2.start()

# # wait until thread 1 is completely executed
# t1.join()
# # wait until thread 2 is completely executed
# t2.join()