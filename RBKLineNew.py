import sys
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
from matplotlib.pyplot import draw
import matplotlib.animation as animation
import matplotlib.dates as md
import pymysql
import numpy as np
import datetime as dt
import matplotlib.ticker as ticker

import pylab
import autoAnnotation




from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']




def startDrawKLine(p_tablename,p_starttime,p_endtime):

    #print(sys.argv[1])
    #print(sys.argv[2])

    #sys.argv += 'rb1910_20190701 23:30:00'.split() 

    conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')

    #conn=pymysql.connect(host='176.122.178.74',user='remoteuser',password='MYSQLTB',db='shfuture')

    a=conn.cursor()
    #sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from if1904_20190327;'
    #sql = 'select lastprice ,case when hour(happentime)<=11 then DATE_ADD(happentime,interval 90 minute) else happentime end  from ' + sys.argv[1]  + ';'


    # sql = 'select lastprice ,happentime from ' + sys.argv[1]  + ' where time(happentime)<"'  + sys.argv[2]  + '";'
    #sql = 'select lastprice ,happentime from ' + sys.argv[1]  + ';'
    sql = 'select lastprice, happentime   from ' + p_tablename  + ' where time(happentime)>"'  + p_starttime  + '" and time(happentime)<"' + p_endtime + '";' 
    #sql = 'select lastprice, happentime   from ' + sys.argv[1]  + ' where happentime>='''  + sys.argv[2]  + ''' and happentime<=''' + sys.argv[3]  + ''";' 


    #sql = 'select lastprice ,happentime from ' + sys.argv[1]  + ';'
    print(sql)
    a.execute(sql)
    data=a.fetchall()
    t=[]
    s=[]
    for result in data:
        t.append(result[0])
        s.append(result[1])
        #s.append(result[1].timestamp())   插值用这个

    # print(s)
    # print(t)


    #z1 = np.polyfit(s, t, 3)#用3次多项式拟合
    #p1 = np.poly1d(z1)
    #print(p1) #在屏幕上打印拟合多项式

    #20190701 add 
    #N = len(s)
    #ind = np.arange(N) # the evenly spaced plot indices

    #def format_date(x, pos=None):
        #保证下标不越界,很重要,越界会导致最终plot坐标轴label无显示
    #    thisind = np.clip(int(x+0.5), 0, N-1)
    #    return s[thisind].strftime('%Y-%m-%d %H:%M:%S')

    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.plot(s, t, 'o-')
    #ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    #fig.autofmt_xdate()
    #plt.show()


    # end of 20190701 add 
    # transformed=np.fft.fft(t) #傅里叶变换
    # itransformed = np.fft.ifft(transformed)
    # plt.plot(s, itransformed)   #20190701 comment 

    plt.plot(s, t)   #20190701 comment 



    #这段的作用是用不同的颜色画线    
    # startDropTime =  datetime.datetime(2021,7,2,11,20,0)

    # x0 = s.index(startDropTime)

    # plt.plot(s[:x0+1], t[:x0+1])
    # plt.plot(s[x0:], t[x0:])
 

    plt.plot(s, t)


    autoAnnotation.print_annotations(plt,p_tablename)



    # pylab.plot_date(s, t, xdate=False, linestyle='-', marker='')
    # pylab.show()



    #设置时间轴间隔 比如15分钟
    #xlocator = md.MinuteLocator(byminute=[0,15,30,45], interval = 1)
    #plt.xaxis.set_major_locator(xlocator)

    #from  https://stackoverflow.com/questions/42398264/matplotlib-xticks-every-15-minutes-starting-on-the-hour

    # draw()
    # plt.ion()
    plt.show()

    # plt.draw()  
    # plt.show(block=False)
    return
if __name__ == '__main__':
    startDrawKLine(sys.argv[1],sys.argv[2],sys.argv[3])
