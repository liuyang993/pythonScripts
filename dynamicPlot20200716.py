#From 

# https://stackoverflow.com/questions/10944621/dynamically-updating-plot-in-matplotlib


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
    min_x = 0
    max_x = 100
    x = datetime.datetime(2019,6,28,13,10)

    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[], 'o')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_autoscalex_on(True)

        # self.ax.set_xlim(self.min_x, self.max_x)
        #Other stuff
        self.ax.grid()
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
        import pymysql


        conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
        a=conn.cursor()

        t=[]
        s=[]

        sql = 'select happentime,lastprice from fu2009_20200717 where hour(happentime) < 11;'
        a.execute(sql)
        data=a.fetchall()
        for result in data:
            t.append(result[0])
            s.append(result[1])


        self.on_launch()
        xdata = []
        ydata = []


        xindex =0
        yindex=0

        print("here")

        while True: 
            xdata.append(t[xindex])
            xdata.append(t[xindex+1])

            ydata.append(s[yindex])
            ydata.append(s[yindex+1])            
            self.on_running(xdata, ydata)
            xindex=xindex+2
            yindex=yindex+2
            time.sleep(0.01)

            # print(xdata)

        return xdata, ydata


        # self.on_launch()
        # xdata = []
        # ydata = []
        # for x in np.arange(0,10,0.5):
        #     xdata.append(x)
        #     ydata.append(np.exp(-x**2)+10*np.exp(-(x-7)**2))
        #     self.on_running(xdata, ydata)
        #     time.sleep(1)
        # return xdata, ydata


d = DynamicUpdate()
d()
