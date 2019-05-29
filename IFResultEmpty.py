import pymysql

conn=pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')
a=conn.cursor()

#一次全取出
sql = 'select happentime,b1 from ic1906_20190513;' 
a.execute(sql)
data=a.fetchall()
if a.rowcount==0:
    print('empty')
else:
    print('not empty')