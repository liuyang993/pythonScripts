import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymysql
from scipy import stats
import numpy as np
import datetime
import time

plt.ion()
class DynamicUpdate():
    #Suppose we know the x range


    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots()
        # self.lines, = self.ax.plot([],[], 'o')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
   
        #Other stuff
        #self.ax.grid()
        ...

    def on_running(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines, = self.ax.plot(xdata,ydata)
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
        conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
        a=conn.cursor()
        # sql = 'select happentime,lastprice from ' + sys.argv[1]  + ' where hour(happentime) < 23 and hour(happentime) >=21;'
        sql = 'select happentime,lastprice from ' + sys.argv[1]  + ' where hour(happentime) < 23 and hour(happentime) >=21;'
        a.execute(sql)
        data=a.fetchall()
        conn.commit()
        for result in data:
            xdata.append(result[0])
            ydata.append(result[1])
        self.on_running(xdata, ydata)
        time.sleep(1)

        x = datetime.datetime(2022,7,19,23,30,2)
        while True: 
            # conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
            a=conn.cursor()
            # sql = 'select happentime,lastprice from oi2209_20220627 where happentime<=%s and hour(happentime)>=9  order by happentime desc limit 2;'
            sql = 'select happentime,lastprice from ' + sys.argv[1]  + ' where happentime<=%s and hour(happentime)>=21  order by happentime desc limit 2;'
            print(x)
            a.execute(sql,x)
            #print(sql)
            data=a.fetchall()
            conn.commit()
            for result in data:
                xdata.append(result[0])
                ydata.append(result[1])
                print(result[0])
                print(result[1])
            x= x + datetime.timedelta(seconds=1) 
            self.on_running(xdata, ydata)
            time.sleep(1)
        return xdata, ydata

    
d = DynamicUpdate()
d()

