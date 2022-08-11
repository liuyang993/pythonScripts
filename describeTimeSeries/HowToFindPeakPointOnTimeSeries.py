#2022-08-05 用于盘后复盘， 检查找出买卖点算法的胜率 
# 参数  python HowToFindPeakPointOnTimeSeries.py oi2209_20220805 day oi 09:00:00  
# day是白天的意思，夜盘用night 最后的参数的起始时间的意思 


import sys
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time
import queue
# sys.path.append('../../pythonScripts')

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
# import calledFromAnotherScript
from TryToFindSimilarKLineTestForLoop import startCheckCurveSimilar
import logging

# 找出极值   https://stackoverflow.com/questions/22583391/peak-signal-detection-in-realtime-timeseries-data/22640362#22640362
         #  https://github.com/Rgveda/GolemQ/tree/45beff9b1499da52042466eb207cffc7a1c1e2a3/analysis    中国人写的量化库

# class real_time_peak_detection(): 这种方法要先定义一个threshold，临界值， 但是实际情况中，上哪找这个临界值去。谁知道应该定义多少合适 

logging.basicConfig(filename='findexetime.log',level=logging.DEBUG)

def trendline(index,data, order=1):
    coeffs = np.polyfit(index, list(data), order)
    slope = coeffs[-2]
    return float(slope)


class real_time_peak_detection():
    def __init__(self, array, lag, threshold, influence):
        self.y = list(array)
        self.length = len(self.y)
        self.lag = lag
        self.threshold = threshold
        self.influence = influence
        self.signals = [0] * len(self.y)
        self.filteredY = np.array(self.y).tolist()
        self.avgFilter = [0] * len(self.y)
        self.stdFilter = [0] * len(self.y)
        self.avgFilter[self.lag - 1] = np.mean(self.y[0:self.lag]).tolist()
        self.stdFilter[self.lag - 1] = np.std(self.y[0:self.lag]).tolist()

    def thresholding_algo(self, new_value):
        self.y.append(new_value)
        i = len(self.y) - 1
        self.length = len(self.y)
        if i < self.lag:
            print('still not reach lag')
            return 0
        elif i == self.lag:
            self.signals = [0] * len(self.y)
            self.filteredY = np.array(self.y).tolist()
            self.avgFilter = [0] * len(self.y)
            self.stdFilter = [0] * len(self.y)
            self.avgFilter[self.lag] = np.mean(self.y[0:self.lag]).tolist()
            self.stdFilter[self.lag] = np.std(self.y[0:self.lag]).tolist()
            return 0

        self.signals += [0]
        self.filteredY += [0]
        self.avgFilter += [0]
        self.stdFilter += [0]

        if abs(self.y[i] - self.avgFilter[i - 1]) > (self.threshold * self.stdFilter[i - 1]):

            if self.y[i] > self.avgFilter[i - 1]:
                self.signals[i] = 1
            else:
                self.signals[i] = -1

            self.filteredY[i] = self.influence * self.y[i] + \
                (1 - self.influence) * self.filteredY[i - 1]
            self.avgFilter[i] = np.mean(self.filteredY[(i - self.lag):i])
            self.stdFilter[i] = np.std(self.filteredY[(i - self.lag):i])
        else:
            # print('from here return')
            self.signals[i] = 0
            self.filteredY[i] = self.y[i]
            self.avgFilter[i] = np.mean(self.filteredY[(i - self.lag):i])
            self.stdFilter[i] = np.std(self.filteredY[(i - self.lag):i])

        return self.signals[i]


def thresholding_algo(y, lag, threshold, influence):
    signals = np.zeros(len(y))
    filteredY = np.array(y)
    avgFilter = [0]*len(y)
    stdFilter = [0]*len(y)
    avgFilter[lag - 1] = np.mean(y[0:lag])
    stdFilter[lag - 1] = np.std(y[0:lag])
    for i in range(lag, len(y)):
        if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
            if y[i] > avgFilter[i-1]:
                signals[i] = 1
            else:
                signals[i] = -1

            filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
        else:
            signals[i] = 0
            filteredY[i] = y[i]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])

    return dict(signals = np.asarray(signals),
                avgFilter = np.asarray(avgFilter),
                stdFilter = np.asarray(stdFilter))



# y = np.array([1,1,1.1,1,0.9,1,1,1.1,1,0.9,1,1.1,1,1,0.9,1,1,1.1,1,1,1,1,1.1,0.9,1,1.1,1,1,0.9,
#        1,1.1,1,1,1.1,1,0.8,0.9,1,1.2,0.9,1,1,1.1,1.2,1,1.5,1,3,2,5,3,2,1,1,1,0.9,1,1,3,
#        2.6,4,3,3.2,2,1,1,0.8,4,4,2,2.5,1,1,1])

# # Settings: lag = 30, threshold = 5, influence = 0
# lag = 30
# threshold = 5
# influence = 0

# # Run algo with settings from above
# result = thresholding_algo(y, lag=lag, threshold=threshold, influence=influence)

# # Plot result
# plt.subplot(211)
# plt.plot(np.arange(1, len(y)+1), y)

# plt.plot(np.arange(1, len(y)+1),
#            result["avgFilter"], color="cyan", lw=2)

# plt.plot(np.arange(1, len(y)+1),
#            result["avgFilter"] + threshold * result["stdFilter"], color="green", lw=2)

# plt.plot(np.arange(1, len(y)+1),
#            result["avgFilter"] - threshold * result["stdFilter"], color="green", lw=2)

# plt.subplot(212)
# plt.step(np.arange(1, len(y)+1), result["signals"], color="red", lw=2)
# plt.ylim(-1.5, 1.5)
# plt.show()




# lag = 30
# threshold = 5
# influence = 0


# arrini = [
#         10.1,10,1,10.1,10,00.8,00.9,10,10.2,00.9,
#         1,10,10.1,10.2,10,10.5,10,3,20,5,
#         3,20,1,10,1,00.9,10,1,30, 20.6,
#         4,30,30.2,20,1,10,00.8,40,4,20,
#     ]

# arrini = [1,1,1.1,1,0.9,1,1,1.1,1,0.9,1,1.1,1,1,0.9,1,1,1.1,1,1,1,1,1.1,0.9,1,1.1,1,1,0.9,
#        1,1.1,1,1,1.1,1,0.8,0.9,1,1.2,0.9,1,1,1.1,1.2,1,1.5,1,3,2,5,3,2,1,1,1,0.9,1,1,3,
#        2.6,4,3,3.2,2,1,1,0.8,4,4,2,2.5,1,1,1]
# y = [
#         1,10,60.1,10,00.9,10,1,10.1,10,00.9,
#         1,10.1,10,1,00.9,10,1,10.1,10,1,
#         1,10,10.1,00.9,10,10.1,10,1,00.9,10,
#         10.1,10,1,10.1,10,00.8,00.9,10,10.2,00.9,
#         1,10,10.1,10.2,10,10.5,10,3,20,5,
#         3,20,1,10,1,00.9,10,1,30, 20.6,
#         4,30,30.2,20,1,10,00.8,40,4,20,
#         20.5,10,1,1
#     ]

# rtpd = real_time_peak_detection(arrini, lag, threshold, influence)

# num = 0
# while num < len(y):
#     res = rtpd.thresholding_algo(y[num])
#     print(y[num],res)
#     print('len is ')
#     print(len(rtpd.y))
    
#     num += 1
#     time.sleep(5)



firstTop =0
starttime =''
endtime = ''
t=[]
s=[]

xx=[]    # 存时间 10秒一跳 [10,20,30,......]
yy=[]    # 存每十秒的斜率


qSlope= queue.Queue(maxsize=60)   # 10 个元素的队列 
qSlope.empty()


def compareQueue(L):    # 计算10个元素的队列里，是不是最大值出现在中间， 如果是， 说明找到了值的顶部
    LofQ = list(L.queue)
    max_item = max(LofQ)
    maxIndex = LofQ.index(max_item)

    min_item = min(LofQ)
    minIndex = LofQ.index(min_item)

    str=''

    # if maxIndex==9 or maxIndex==10 :
    if maxIndex==30 :
        str='top'
        return  str,maxIndex
    if minIndex==20 :
        str='bottom'
        return  str,minIndex
    else:
        str='not'
        return  str,0
        
conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()
starttime = sys.argv[4]

if sys.argv[2] == 'day':
    # starttime ='13:33:00'
    endtime = '15:00:00'    
    # sql = 'select happentime,lastprice from ' + sys.argv[1]  + ' where hour(happentime)>=9 and hour(happentime)<=15 ;'
    sql = 'select happentime,lastprice from ' + sys.argv[1]  + ' where TIME(happentime)>= "' + starttime + '"  and hour(happentime)<=15 ;'
else:
    # starttime ='21:00:00'
    endtime = '23:00:00'
    sql = 'select happentime,lastprice from ' + sys.argv[1]  + ' where TIME(happentime)>= "' + starttime + '"  and hour(happentime)<=23 ;'
print(sql)
a.execute(sql)
data=a.fetchall()
conn.commit()

# print(data[0][0])
# print(data[0][1])
# print(data[1][0])
# print(data[1][1])


# lag = 30
# threshold = 5000
# influence = 0

iii=0
jjj=0
while True:

    t.append(data[iii][0].timestamp())
    # t.append(data[ii][0])
    s.append((data[iii][1] + data[iii+1][1])/2)

    # print(data[iii][0])

    if jjj==10:
        # slope, intercept, r_value, p_value, std_err = stats.linregress(t[-iii:],s[-iii:])
        # print('------------------')
        # print(slope)
        # print(s)
        
        
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
            print ('find quick down trend at ' ,datetime.datetime.fromtimestamp(t[-1]), ' value is ' , s[-1] )
            logging.info ('find quick down trend at %s ,value is %s' , str(datetime.datetime.fromtimestamp(t[-1])), str(s[-1]) )
            #找过往图形比较 找出图形特征最像的
            startCheckCurveSimilar(sys.argv[1],starttime,str(datetime.datetime.fromtimestamp(t[-1]).time()),sys.argv[3],sys.argv[2])
        if len(yy)>3 and (yy[-1]>yy[-2]) and (yy[-2]>yy[-3]) and ((yy[-1]+yy[-2]+yy[-3]) > 2.0) : 
            print ('find quick up trend at ' ,datetime.datetime.fromtimestamp(t[-1]) , ' value is ' , s[-1])
            startCheckCurveSimilar(sys.argv[1],starttime,str(datetime.datetime.fromtimestamp(t[-1]).time()),sys.argv[3],sys.argv[2])
            logging.info('find quick up trend at %s ,   value is %s' ,str(datetime.datetime.fromtimestamp(t[-1]))  , str(s[-1]))
              

    # print(datetime.datetime.fromtimestamp(t[-1]))
    # print(s[-1])
    iii=iii+2 
    jjj=jjj+1
    # time.sleep(5)

    # if len(t)>60:
    #     # rtpd = real_time_peak_detection(s, lag, threshold, influence)
    #     # print(rtpd.thresholding_algo((data[iii][1] + data[iii+1][1])/2))


    #     slope, intercept, r_value, p_value, std_err = stats.linregress(t[-60:],s[-60:])
    #     # print("time  is ", result[0], " price is " , result[1] , " current slope is " , "%.6f" % slope )

    #     if qSlope.full():  # 如果满了 ，最早的出队
    #         qSlope.get()
    #         qSlope.put("{:.4f}".format(slope))
    #     else:
    #         qSlope.put("{:.4f}".format(slope))
    #     # print(list(qSlope.queue))

    #     if qSlope.full():            # 队列满了就比较
    #         strRtn,ii=compareQueue(qSlope)
    #         if ii>0:
    #             if strRtn=='top':
    #                 # print("time  is ", result[0], " price is " , result[1] , " current slope is " , "%.6f" % slope )
    #                 # print(ii)
    #                 # print("time  is ", datetime.datetime.fromtimestamp(t[-ii:]), " price is " , s[-ii:] , " find top value "  )
    #                 print("time  is ", datetime.datetime.fromtimestamp(t[-ii]), " price is " , s[-ii] , " find top value , and current time is " , datetime.datetime.fromtimestamp(t[-1]) , 'current price is ' , s[-1] )

    #                 # print(list(qSlope.queue))
    #             if strRtn=='bottom':
    #                 # print("time  is ", result[0], " price is " , result[1] , " current slope is " , "%.6f" % slope )
    #                 # print(ii)
    #                 # print("time  is ", datetime.datetime.fromtimestamp(t[-ii:]), " price is " , s[-ii:] , " find top value "  )
    #                 print("time  is ", datetime.datetime.fromtimestamp(t[-ii]), " price is " , s[-ii] , " find bottom value , and current time is " ,datetime.datetime.fromtimestamp(t[-1]) , 'current price is ' , s[-1] )

    #                 # print(list(qSlope.queue))
