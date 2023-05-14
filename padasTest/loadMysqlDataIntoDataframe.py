import pandas as pd
import datetime
import pymysql

connection = pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture20230322')

try:

    query = "SELECT * FROM if1901_20190102 "
    df = pd.read_sql(query, connection)

    # column = df.columns
    # print(column)


    # https://stackoverflow.com/questions/73039481/check-if-values-in-all-n-previous-rows-are-greater-than-the-value-of-current-row
    da = df[df['lastprice'] < df['lastprice'].shift().rolling(1000, min_periods=1).min()]
    print(da)

finally:
    connection.close()