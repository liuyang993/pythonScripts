# python TryToFindSimilarKLineTestForLoop.py oi2209_20220805  09:00:00  11:30:00 oi day


import sys
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as md
import pymysql
import numpy as np
import datetime as dt
import pandas as pd
# import seaborn as sns
import time
from statistics import mean
import sys
#sys.argv += 'if1906_20190516 09:30:00 10:00:00'.split()      #debug 时用
# import RBKLineNew


def getKLineData(p_tablename,p_starttime,p_endtime):

    conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')

    a=conn.cursor()

    sql = 'select lastprice, happentime   from ' + p_tablename  + ' where time(happentime)>"'  + p_starttime  + '" and time(happentime)<"' + p_endtime + '";' 
 
    a.execute(sql)
    data=a.fetchall()
    t=[]
    s=[]
    for result in data:
        t.append(result[0])
        s.append(result[1])

    return(t,s)


def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 


def SplitArrayAndCalAver(arraySrc,arrayDst,n):
    x = list(divide_chunks(arraySrc, n)) 
    for j in range(len(x)):
        arrayDst.append(mean(x[j]))

def normalizeArray(pa):                 # 归一化
    amin,amax = min(pa),max(pa)
    if amin == amax:
        for j in range(len(pa)):   # TODO check if amax == amin to avoid devide by zero   
            pa[j]=amin
    else:
        for j in range(len(pa)):   # TODO check if amax == amin to avoid devide by zero   
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


def startCheckCurveSimilar(p_tablename,p_starttime,p_endtime,p_tablefirstchar,p_dayornight):
    # print(p_tablename)
    # print(p_starttime)
    # print(p_endtime)
    # print(p_tablefirstchar)
    # print(p_dayornight)
    conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
    a=conn.cursor()

    sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + p_tablename  + ' where time(happentime)>"'  + p_starttime  + '" and time(happentime)<"' + p_endtime  + '";' 
    # print(sql)
    a.execute(sql)
    data=a.fetchall()


    x=[]
    s0=[]
    for result in data:
        x.append(result[0])
        s0.append(result[1])


    xOneMinAver= []

    SplitArrayAndCalAver(x,xOneMinAver,60)

    #print(x)

    x= xOneMinAver
    # print("x is ")
    # print(x)
    normalizeArray(x)
    print('orignal array have ' , len(x) , ' elements ')

    print('************************************************')


    loopi = 1 
    loopTableName = p_tablename

    matchtables = 1

    while loopi < 1000:
        loopi = loopi + 1
        #sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else haentime end  from if1906_20190419'   + ' where time(happentime)<"'  + sys.argv[2]  + '";'

        # sql = 'SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = "shfuture" and table_name like "' + sys.argv[4] + '%" and table_name < "' + loopTableName + '" order by create_time desc limit 1;'

        # sql = 'SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = "shfuture" and table_name like "' + sys.argv[4] + '%" and SUBSTRING_INDEX(table_name,"_",-1) < SUBSTRING_INDEX("' + loopTableName + '","_",-1) order by create_time desc limit 1;'

        sql = 'SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = "shfuture" and table_name like "' + p_tablefirstchar + '%" and SUBSTRING_INDEX(table_name,"_",-1) < SUBSTRING_INDEX("' + loopTableName + '","_",-1) order by SUBSTRING_INDEX(table_name,"_",-1) desc limit 1;'


        # print(sql)
        a.execute(sql)
        data=a.fetchall()
        for result in data:
            loopTableName = result[0]
        # print(loopTableName)

        sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + loopTableName  + ' where time(happentime)>"'  + p_starttime  + '" and time(happentime)<"' + p_endtime  + '";' 
        #print(sql)
        a.execute(sql)
        data=a.fetchall()

        y=[]
        s0=[]
        for result in data:
            y.append(result[0])
            s0.append(result[1])


        if not y:
            # print('no data from ' , loopTableName)
            continue

        #print(y)

        #s = time.time()

        yOneMinAver = []
        SplitArrayAndCalAver(y,yOneMinAver,60)
        y=  yOneMinAver

        normalizeArray(y)
        #print("original array normalize  Took %f seconds" % (time.time() - s))

        distances = np.zeros((len(y), len(x)))    #建立一个 len(y) 行 , len(x) 列 的矩阵 ，并初始化为零
        #print(distances)

        s = time.time()
        for i in range(len(y)):
            for j in range(len(x)):
                distances[i,j] = (x[j]-y[i])**2    # 计算 y的每个点到 x的距离 

        #print("cal x y distance matrix use time %f seconds" % (time.time() - s))

        #print(distances)        

        #distance_cost_plot(distances)

        # 另一个矩阵
        accumulated_cost = np.zeros((len(y), len(x)))
        accumulated_cost[0,0] = distances[0,0]

        s = time.time()
        for i in range(1, len(x)):
            accumulated_cost[0,i] = distances[0,i] + accumulated_cost[0, i-1]    

        for i in range(1, len(y)):
            accumulated_cost[i,0] = distances[i, 0] + accumulated_cost[i-1, 0]    

        for i in range(1, len(y)):
            for j in range(1, len(x)):
                accumulated_cost[i, j] = min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]) + distances[i, j]    #这句是最慢的 
        
        #print("cal accumulate matrix use time %f seconds" % (time.time() - s))

        #distance_cost_plot(accumulated_cost)    不用画图

        #找出最短路径 
        s = time.time()
        path, cost = path_cost(x, y, accumulated_cost, distances)
        #print("find shortest path use time %f seconds" % (time.time() - s))
        #print(path)

        # print('DTM value from ' , sys.argv[1]  , ' to ' , loopTableName  , ' is '  , cost)





        if cost<0.4:
            print('DTM value from ' , p_tablename  , ' to ' , loopTableName  , ' is '  , cost)
            # if matchtables>5:
            #     plt.show()
            #     break
            # print('DTM value from ' , p_tablename  , ' to ' , loopTableName  , ' is '  , cost)
            # # 
            # # RBKLineNew.startDrawKLine(loopTableName,p_starttime,p_endtime)
            # tp =[]
            # sp =[]
            # if p_dayornight =="day":
            #     tp,sp = getKLineData(loopTableName,p_starttime,"14:59:59")
            # else:
            #     tp,sp = getKLineData(loopTableName,p_starttime,"22:59:59")       
            # # print(sp[-1])
           
            # # print(sp[-1].year)
            # # print(sp[-1].month)
            # # print(sp[-1].day)

            # d = dt.datetime.strptime(p_endtime, '%H:%M:%S')
            # # print(d.hour)
            # # print(d.minute)
            # # print(d.second)


            # time0 = dt.datetime(sp[-1].year,sp[-1].month,sp[-1].day,d.hour,d.minute,d.second)
            # # print(time0)


            # try:
            #     x0 = sp.index(time0)

            #     # plt.figure(figsize=(10,10))

            #     plt.subplot(5, 1, matchtables)
            #     # plt.tight_layout()


            #     plt.plot(sp[:x0+1], tp[:x0+1])
            #     plt.plot(sp[x0:], tp[x0:])


            #     plt.title(loopTableName + " " + str(cost))
            #     matchtables=matchtables+1
            # except:
            #     plt.subplot(5, 1, matchtables)
            #     plt.tight_layout()
            #     plt.plot(sp,tp)


            #     plt.title(loopTableName + " " + str(cost))
            #     matchtables=matchtables+1
   
            
    plt.show()




if __name__ == '__main__':
    startCheckCurveSimilar(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])

# if __name__ == '__main__':
