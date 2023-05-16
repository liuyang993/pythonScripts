import pandas as pd
import datetime
import pymysql
import numpy as np
import matplotlib.pyplot as plt


connection = pymysql.connect(host='localhost',user='root',password='MYSQLTB',db='shfuture')


try:

    query = "SELECT  happentime,lastprice FROM if1901_20190102   "
    df = pd.read_sql(query, connection)


    IsSellPoint = []
    IsBuyPoint = []


    for index, row in df.iterrows():
        # print("current row price is : " , row['lastprice'])
        currentprice = row['lastprice']
        # print(df.iloc[index+1:len(df.index), 1].to_numpy())
        my_list1 = df.iloc[index+1:len(df.index), 1].to_numpy()
        # print(any(i < currentprice - 20 for i in my_list1))
        # print("******")
        # row['IfMaiDian ']=any(i < currentprice - 20 for i in my_list1)
        IsSellPoint.append(any(i < currentprice - 20 for i in my_list1))
        IsBuyPoint.append(any(i > currentprice + 20 for i in my_list1))
    # print(df.to_string())

    df["IsSellPoint"] = IsSellPoint
    df["IsBuyPoint"] = IsBuyPoint    
    print(df.head(10))
    df.to_csv('20230516.csv', sep='\t', encoding='utf-8')

    # plt.figure()

    # x = df['happentime']
    # y1 = df['lastprice']

    # plt.plot(x,y1)


    # plt.show()


finally:
    connection.close()


