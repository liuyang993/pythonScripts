import pandas as pd
import datetime
import pymysql
import numpy as np

connection = pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture20230322')

def func(window):
    # # print(window)
    mask = (window > window.iloc[-1] -300  )
    rows = window[mask]  # all previous values grater then current value 
    # # value = rows.min()   # minimal value 
    # value = True

    # return value


    # if window['lastprice'] > window.iloc[-1]['lastprice'] + 20:
    #     return True
    # else:
    #     return False 

    print(window)
    print("----")
    print(rows)
    print("*******************************")
    return 1

try:

    query = "SELECT  happentime,lastprice FROM if1901_20190102 limit 5 "
    df = pd.read_sql(query, connection)

    # print(df.iloc[0])    # 第一行
    # print(df.iloc[-1])    #最后一行
    

    # print(df.iloc[:,0])   # 所以行的第一列
    # print(df.iloc[:,-1])   # 所以行的最后一列 

    # print(df.iloc[0:5])   # 1到5行， 所有列
    
    # print(df.iloc[:, 0:2]) #所有行的第一和第二列 

    # print(df.iloc[0:5, 5:8])  # 前5行， 第5，6，7列


    # column = df.columns
    # print(column)

    # df['prev_gt_curr'] = df.expanding().apply(func)
    # df['boolean_column'] = df.iloc[np.argmax(df['lastprice'] > 3000)] 
    # df['boolean_column'] = np.where(df['lastprice'] > 4000, True, False)
    # print(df.head(10))

    for index, row in df.iterrows():
        # print(row['lastprice'])
        print(df.iloc[index+1:5, 1].to_numpy())
        print("******")


    # print(df.to_string())

    # https://stackoverflow.com/questions/73039481/check-if-values-in-all-n-previous-rows-are-greater-than-the-value-of-current-row
    # da = df[df['lastprice'] < df['lastprice'].shift().rolling(1000, min_periods=1).min()]
    # print(da)


finally:
    connection.close()


