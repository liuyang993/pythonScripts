# 2023-06-09  不能运行 非常慢还出错


import pandas as pd
import datetime
import pymysql
import numpy as np
import matplotlib.pyplot as plt

from tsfresh.examples.robot_execution_failures import download_robot_execution_failures,load_robot_execution_failures
from tsfresh import extract_features,select_features


connection = pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')


try:

    query = "SELECT  happentime,lastprice FROM if1901_20190102 where time(happentime)>='09:30:00' AND time(happentime)<='14:59:58'"
    df = pd.read_sql(query, connection)

    df = df.groupby('happentime', as_index=False, sort=False)['lastprice'].mean()
    # print(df)

    X = extract_features(df, column_id='lastprice', column_sort='lastprice')

finally:
    connection.close()



