from cgi import print_arguments
import sys
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as md
import pymysql
import datetime as dt
import time
import sys

#先要清洗


print("this")

p_tablefirstchar = "20220926"
conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture20220926')
a=conn.cursor()

connlocal=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
ab=connlocal.cursor()


sql = 'SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = "shfuture20220926" and table_name like "%' + p_tablefirstchar + '%" ;'
# print(sql)
a.execute(sql)
data=a.fetchall()
for result in data:
    loopTableName = result[0]
    print("------------------")    
    print(loopTableName)
    sql = 'SELECT count(*) FROM ' + loopTableName + ';'
    a.execute(sql)
    datacount= a.fetchall()
    for result in datacount:
        print(result[0])
        if result[0] > 1000:
            print("this table have enough data")
            #        
            sqllocal = 'SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = "shfuture" and table_name = "' + loopTableName + '" ;'
            print(sqllocal)
            ab.execute(sqllocal)
            if ab.rowcount == 0:
                print("没有夜盘 直接copy")

            else:
                datalocal=ab.fetchall()
                for result in datalocal:
                    localloopTableName = result[0]
                    print(localloopTableName)
                    #如果能找到同样的表名，说明此品种有夜盘


