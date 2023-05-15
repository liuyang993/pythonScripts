import pandas as pd
import datetime
import pymysql
import numpy as np

connection = pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')

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

    # column = df.columns
    # print(column)

    # df['prev_gt_curr'] = df.expanding().apply(func)
    df['boolean_column'] = np.where(df['lastprice'] > 4000, True, False)
    # print(df.head(10))



    print(df.to_string())

    # https://stackoverflow.com/questions/73039481/check-if-values-in-all-n-previous-rows-are-greater-than-the-value-of-current-row
    # da = df[df['lastprice'] < df['lastprice'].shift().rolling(1000, min_periods=1).min()]
    # print(da)


finally:
    connection.close()


