import sys
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as md
import pymysql
import numpy as np
import datetime as dt
import pandas as pd
import seaborn as sns

def normalizeArray(pa):
    amin,amax = min(pa),max(pa)
    for j in range(len(pa)):
        pa[j]=(pa[j]-amin)/(amax-amin)


def distance_cost_plot(distances):
    im = plt.imshow(distances, interpolation='nearest', cmap='Reds') 
    plt.gca().invert_yaxis()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.colorbar()
    #plt.show()


def path_cost(x, y, accumulated_cost, distances):
    path = [[len(x)-1, len(y)-1]]
    cost = 0
    i = len(y)-1
    j = len(x)-1
    while i>0 and j>0:
        if i==0:
            j = j - 1
        elif j==0:
            i = i - 1
        else:
            if accumulated_cost[i-1, j] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
                i = i - 1
            elif accumulated_cost[i, j-1] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
                j = j-1
            else:
                i = i - 1
                j= j- 1
        path.append([j, i])
    path.append([0,0])
    for [y, x] in path:
        cost = cost +distances[x, y]
    return path, cost   



conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()

sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + sys.argv[1]  + ' where time(happentime)<"'  + sys.argv[2]  + '";'
#print(sql)
a.execute(sql)
data=a.fetchall()


x=[]
s0=[]
for result in data:
    x.append(result[0])
    s0.append(result[1])

#print(t)
normalizeArray(x)


sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190419'   + ' where time(happentime)<"'  + sys.argv[2]  + '";'
#print(sql)
a.execute(sql)
data=a.fetchall()


y=[]
s=[]
for result in data:
    y.append(result[0])
    s.append(result[1])

#print(t)
normalizeArray(y)

# python C:\Users\liuyang\Documents\TryToFindSimilarKLine.py if1906_20190430 09:31:00
#plt.plot(t0,'r', label='x')
#plt.plot(t, 'g', label='y')
#plt.legend()
#plt.show()


plt.plot(x,'r', label='x')
plt.plot(y, 'g', label='y')
plt.legend()

#plt.show()

distances = np.zeros((len(y), len(x)))    #建立一个 len(y) 行 , len(x) 列 的矩阵 ，并初始化为零
#print(distances)

for i in range(len(y)):
    for j in range(len(x)):
        distances[i,j] = (x[j]-y[i])**2    # 计算 y的每个点到 x的距离 

#print(distances)        

distance_cost_plot(distances)

# 另一个矩阵
accumulated_cost = np.zeros((len(y), len(x)))
accumulated_cost[0,0] = distances[0,0]

for i in range(1, len(x)):
    accumulated_cost[0,i] = distances[0,i] + accumulated_cost[0, i-1]    

for i in range(1, len(y)):
    accumulated_cost[i,0] = distances[i, 0] + accumulated_cost[i-1, 0]    

for i in range(1, len(y)):
    for j in range(1, len(x)):
        accumulated_cost[i, j] = min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]) + distances[i, j]


distance_cost_plot(accumulated_cost)

#找出最短路径 
path, cost = path_cost(x, y, accumulated_cost, distances)

#print(path)
print(cost)







