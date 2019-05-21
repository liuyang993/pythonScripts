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
for result in data:
    x.append(result[0])
    s0.append(result[1])

#print(x)
normalizeArray(x)
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
    for result in data:
        y.append(result[0])
        s0.append(result[1])
    #print(y)

    #s = time.time()
    normalizeArray(y)
    #print("original array normalize  Took %f seconds" % (time.time() - s))

    distances=[]
    s = time.time()
    #print(len(y))
    #print(len(x))
    
    
    #for i in range(len(y)):
        #try:      
            #distances.append((x[i]-y[i])**2)    # 计算 x,y的每个相同 x坐标的点的距离 
        #except ValueError:
            #print('i is ',i)
    #print("cal x y distance  use time %f seconds" % (time.time() - s))
    #sumDis = np.sum(distances)
    #print('sum distance value from ' , sys.argv[1]  , ' to ' , loopTableName  , ' is '  , sumDis)

    EuclideanDistance=sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
    #print(distances)        
    print('Euclidean distance value from ' , sys.argv[1]  , ' to ' , loopTableName  , ' is '  , EuclideanDistance)


    #print(path)









