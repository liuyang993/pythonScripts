import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time


class DynamicUpdate():
    #Suppose we know the x range
    min_x = 0
    max_x = 10
    x = datetime.datetime(2019,6,28,13,10)

    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[], 'o')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(self.min_x, self.max_x)
        #Other stuff
        #self.ax.grid()
        ...

    def on_running(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    #Example
    def __call__(self):
        import numpy as np
        import time
        self.on_launch()
        xdata = []
        ydata = []

        sql = 'select happentime,lastprice from rb1910_20190628 where hour(happentime) < 11;'
        a.execute(sql)
        data=a.fetchall()
        for result in data:
            xdata.append(result[0])
            ydata.append(result[1])
        self.on_running(xdata, ydata)
        time.sleep(1)


        while True: 
            xdata.append(x)
            ydata.append(np.exp(-x**2)+10*np.exp(-(x-7)**2))
            self.on_running(xdata, ydata)
            time.sleep(1)
        return xdata, ydata

x = datetime.datetime(2019,6,28,23,10)
firstTop =0
doubletop=0
FuPanIndexBegin = 0

sellingPrice = 0

lowPrice = 0
lastStopWinPrice = 0 

oporTime = 0
CurrentState = 0      #  0 mean observer ,  1 selling , 2 buying  

Todaymin=0
Todaymax =0

conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()

t=[]
s=[]


annotateIndexX=[]
annotateIndexY=[]

#sql = 'select happentime,lastprice from ' + sys.argv[1]  + ';'

# sql = 'select happentime,lastprice from rb1910_20190628 where hour(happentime) < 11;'
# a.execute(sql)
# data=a.fetchall()
# for result in data:
#     t.append(result[0])
#     s.append(result[1])

# plt.plot(t, s)
# plt.show()

#print(len(t))

while True: 
    sql = 'select happentime,lastprice from rb1910_20190628 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit 2;'
    a.execute(sql,x)
    #print(sql)
    data=a.fetchall()
    for result in data:
        t.append(result[0])
        s.append(result[1])

    x= x + datetime.timedelta(seconds=1)

    #print(len(t))
    
    #print(s)

    plt.clf()
    plt.plot(t, s)
    plt.show()

    #print(t[-1])
    #print(s[-1])
    #if s.index(max(s)) < len(s)-600 :       # 发现高点，保存备注的坐标    
        #print(t.index(t[-1]))
        #print(s.index(s[-1]))
        #plt.annotate('Something', xy=(t[-1], s[-1]))
        #annotateIndexX.append(t[-1])
        #annotateIndexY.append(s[-1])
        #print('already down 5 mins form last high point' , max(s))        


    #print(annotateIndex)

    #for i in range(len(annotateIndexX)):      #  试图加上备注  
    #    print('find high point at ', s[-1])
    #    plt.annotate('HighPoint', xy=(annotateIndexX[i],annotateIndexY[i]))

    #plt.annotate('Something', xy=(t[-1],s[-1]))


    ######################################

    ##plt.draw()
    #plt.pause(0.0001)
    # plt.pause(1)    


    


