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
import time
from math import*
import similaritymeasures

import sys
sys.argv += 'if1906_20190517 09:30:00 10:00:00'.split()      #debug 时用

def normalizeArray(pa):                 # 归一化
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



conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()

sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + sys.argv[1]  + ' where time(happentime)>"'  + sys.argv[2]  + '" and time(happentime)<"' + sys.argv[3]  + '";' 
#print(sql)
a.execute(sql)
data=a.fetchall()


x=[]
s0=[]

i=1
for result in data:
    x.append(result[0])
    #s0.append(result[1].timestamp())
    s0.append(i)
    i=i+1

tdArray = np.zeros((len(x), 2))
tdArray[:, 0] = x
tdArray[:, 1] = s0

#print(x)
print('orignal array have ' , len(x) , ' elements ')

print('************************************************')


loopi = 1 
loopTableName = sys.argv[1]
while loopi < 20:
    loopi = loopi + 1
    #sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1906_20190419'   + ' where time(happentime)<"'  + sys.argv[2]  + '";'
    sql = 'SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = "shfuture" and table_name like "if%" and table_name < "' + loopTableName + '" order by create_time desc limit 1;'

    #print(sql)
    a.execute(sql)
    data=a.fetchall()
    for result in data:
        loopTableName = result[0]
    print(loopTableName)






    sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + loopTableName  + ' where time(happentime)>"'  + sys.argv[2]  + '" and time(happentime)<"' + sys.argv[3]  + '";' 
    #print(sql)
    a.execute(sql)
    data=a.fetchall()

    y=[]
    s0=[]
    i=1
    for result in data:
        y.append(result[0])
        #s0.append(result[1].timestamp())
        s0.append(i)
        i=i+1
    #print(y)

    TwoDarrayLoop = np.zeros((len(y), 2))
    TwoDarrayLoop[:, 0] = y
    TwoDarrayLoop[:, 1] = s0


    # quantify the difference between the two curves using PCM
    #pcm = similaritymeasures.pcm(TwoDarrayLoop, tdArray)

    # quantify the difference between the two curves using
    # Discrete Frechet distance
    #df = similaritymeasures.frechet_dist(TwoDarrayLoop, tdArray)

    # quantify the difference between the two curves using
    # area between two curves
    #area = similaritymeasures.area_between_two_curves(TwoDarrayLoop, tdArray)

    # quantify the difference between the two curves using
    # Curve Length based similarity measure
    #cl = similaritymeasures.curve_length_measure(TwoDarrayLoop, tdArray)

    # quantify the difference between the two curves using
    # Dynamic Time Warping distance
    dtw, d = similaritymeasures.dtw(TwoDarrayLoop, tdArray)

    #print(pcm, '---', area, '---', cl, '---',dtw)
    print('---',dtw)

    #minX = np.min(TwoDarrayLoop[:, 0])
    #plt.figure()
    #plt.plot(TwoDarrayLoop[:, 0], TwoDarrayLoop[:, 1])
    #plt.plot(tdArray[:, 0], tdArray[:, 1])
    #plt.show()


    #maxX = np.max(x)
    #minY = np.min(y)
    #maxY = np.max(y)

    #xi = (x - minX) / (maxX - minX)
    #eta = (y - minY) / (maxY - minY)
    #xiP = (w - minX) / (maxX - minX)
    #etaP = (z - minY) / (maxY - minY)


    #print('pcm is ', pcm)








