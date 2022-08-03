import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time
import queue

# 找出极值   https://stackoverflow.com/questions/22583391/peak-signal-detection-in-realtime-timeseries-data/22640362#22640362
         #  https://github.com/Rgveda/GolemQ/tree/45beff9b1499da52042466eb207cffc7a1c1e2a3/analysis    中国人写的量化库
            

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



lag = 3
threshold = 25
influence = 0


# arrini = [
#         10.1,10,1,10.1,10,00.8,00.9,10,10.2,00.9,
#         1,10,10.1,10.2,10,10.5,10,3,20,5,
#         3,20,1,10,1,00.9,10,1,30, 20.6,
#         4,30,30.2,20,1,10,00.8,40,4,20,
#     ]

arrini = [
        10.1,10,1,10.1
    ]    

y = [
        1,10,60.1,10,00.9,10,1,10.1,10,00.9,
        1,10.1,10,1,00.9,10,1,10.1,10,1,
        1,10,10.1,00.9,10,10.1,10,1,00.9,10,
        10.1,10,1,10.1,10,00.8,00.9,10,10.2,00.9,
        1,10,10.1,10.2,10,10.5,10,3,20,5,
        3,20,1,10,1,00.9,10,1,30, 20.6,
        4,30,30.2,20,1,10,00.8,40,4,20,
        20.5,10,1,1
    ]

rtpd = real_time_peak_detection(arrini, lag, threshold, influence)

num = 0
while num < len(y):
    res = rtpd.thresholding_algo(y[num])
    print(y[num],res)
    time.sleep(5)
    num += 1



# firstTop =0
# t=[]
# s=[]

# qSlope= queue.Queue(maxsize=60)   # 10 个元素的队列 
# qSlope.empty()


# def compareQueue(L):    # 计算10个元素的队列里，是不是最大值出现在中间， 如果是， 说明找到了值的顶部
#     LofQ = list(L.queue)
#     max_item = max(LofQ)
#     maxIndex = LofQ.index(max_item)

#     min_item = min(LofQ)
#     minIndex = LofQ.index(min_item)

#     str=''

#     # if maxIndex==9 or maxIndex==10 :
#     if maxIndex==30 :
#         str='top'
#         return  str,maxIndex
#     if minIndex==20 :
#         str='bottom'
#         return  str,minIndex
#     else:
#         str='not'
#         return  str,0
        



# conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
# a=conn.cursor()

# sql = 'select happentime,lastprice from pta2209_20220725 where hour(happentime)>=9 and hour(happentime)<=15 ;'
# a.execute(sql)
# data=a.fetchall()
# conn.commit()

# # print(data[0][0])
# # print(data[0][1])
# # print(data[1][0])
# # print(data[1][1])


# lag = 30
# threshold = 5000
# influence = 0

# iii=0
# while True:

#     t.append(data[iii][0].timestamp())
#     # t.append(data[ii][0])
#     s.append((data[iii][1] + data[iii+1][1])/2)






#     # print(t)
#     # print(s)
#     iii=iii+2 
#     # time.sleep(5)

#     if len(t)>60:
#         rtpd = real_time_peak_detection(s, lag, threshold, influence)
#         print(rtpd.thresholding_algo((data[iii][1] + data[iii+1][1])/2))


#         slope, intercept, r_value, p_value, std_err = stats.linregress(t[-60:],s[-60:])
#         # print("time  is ", result[0], " price is " , result[1] , " current slope is " , "%.6f" % slope )

#         if qSlope.full():  # 如果满了 ，最早的出队
#             qSlope.get()
#             qSlope.put("{:.4f}".format(slope))
#         else:
#             qSlope.put("{:.4f}".format(slope))
#         # print(list(qSlope.queue))

#         if qSlope.full():            # 队列满了就比较
#             strRtn,ii=compareQueue(qSlope)
#             if ii>0:
#                 if strRtn=='top':
#                     # print("time  is ", result[0], " price is " , result[1] , " current slope is " , "%.6f" % slope )
#                     # print(ii)
#                     # print("time  is ", datetime.datetime.fromtimestamp(t[-ii:]), " price is " , s[-ii:] , " find top value "  )
#                     print("time  is ", datetime.datetime.fromtimestamp(t[-ii]), " price is " , s[-ii] , " find top value , and current time is " , datetime.datetime.fromtimestamp(t[-1]) , 'current price is ' , s[-1] )

#                     # print(list(qSlope.queue))
#                 if strRtn=='bottom':
#                     # print("time  is ", result[0], " price is " , result[1] , " current slope is " , "%.6f" % slope )
#                     # print(ii)
#                     # print("time  is ", datetime.datetime.fromtimestamp(t[-ii:]), " price is " , s[-ii:] , " find top value "  )
#                     print("time  is ", datetime.datetime.fromtimestamp(t[-ii]), " price is " , s[-ii] , " find bottom value , and current time is " ,datetime.datetime.fromtimestamp(t[-1]) , 'current price is ' , s[-1] )

#                     # print(list(qSlope.queue))
