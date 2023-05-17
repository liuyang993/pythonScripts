import pandas as pd
import datetime
import pymysql
import numpy as np
import matplotlib.pyplot as plt


connection = pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')


try:

    query = "SELECT  happentime,lastprice FROM if1901_20190102 where time(happentime)>='09:30:00' AND time(happentime)<='14:59:58' limit 10"
    df = pd.read_sql(query, connection)

    # print(df)

    # print(df["happentime"].unique())
    print(df.groupby(['happentime']))
    # print(df.groupby(np.arange(len(df))//2).mean())

    # dfnew = df.groupby(np.arange(len(df))//2).mean()
    # dfnew['happentime'] = df["happentime"].unique().tolist()
    # print(dfnew)

finally:
    connection.close()
