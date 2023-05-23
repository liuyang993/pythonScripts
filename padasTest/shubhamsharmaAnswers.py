# 收录  https://stackoverflow.com/users/12833166/shubham-sharma 此用户在StackOverflow回答的问题，dataframe部分 


######第一个 https://stackoverflow.com/questions/75206062/filling-na-values-conditionally-by-group-and-date/75206239#75206239

import pandas as pd
import numpy as np
import time


# jsonstring = [[22415, 7, '2022-02-15 00:00:00', 'KEY', np.NAN],
#               [22415, 7, '2022-02-24 00:00:00', 'MELOXICA', np.NAN], 
#               [22415, 7, '2022-10-11 00:00:00', 'CEPFR', 12.0], 
#               [22415, 7, '2022-10-11 00:00:00', 'MELOXICA', np.NAN], 
#               [25302, 8, '2022-06-05 00:00:00', 'TOX FL', 11.0],
#                 [25302, 8, '2022-06-05 00:00:00', 'FLUNIX', np.NAN], 
#                 [25302, 8, '2022-06-07 00:00:00', 'FLUNIX', np.NAN], 
#                 [25302, 8, '2022-07-07 00:00:00', 'MAS', np.NAN], 
#                 [25302, 8, '2022-07-07 00:00:00', 'FLUNIX', np.NAN], 
#                 [26662, 8, '2022-07-08 00:00:00', 'FR', 12.0], 
#                 [26662, 8, '2022-07-08 00:00:00', 'FLUNIX', np.NAN], 
#                 [26662, 8, '2022-07-17 00:00:00', 'SFFR', 12.0], 
#                 [26662, 8, '2022-07-17 00:00:00', 'MELOXICA', np.NAN]]

# df = pd.DataFrame(jsonstring)

# df.columns = ['ID', 'LACT','Date','Remark','QUARTER']


# #解决方法
# df['Date'] = pd.to_datetime(df['Date'])
# df = df.sort_values(['ID','LACT','Date'])



# groups = df.groupby(['ID','LACT'])['Date'].diff().dt.days.fillna(0).gt(6).cumsum()
# f = lambda x: x.ffill().bfill()
# df['QUARTER'] = df.groupby(['ID','LACT', groups])['QUARTER'].transform(f)
# print (df)


#第二个  https://stackoverflow.com/questions/67841754/get-values-of-previous-rows-as-list/67842195#67842195

# def some_function_v1(df):
#   df['foo1'] = df.foo.shift(1)
#   df['foo2'] = df.foo.shift(2)
#   df['foo3'] = df.foo.shift(3)


#   df['bar'] = df.apply(lambda x: [x['foo1'],x['foo2'],x['foo3']], axis=1)
#   # print(df)
#   df = df.drop(columns=['foo1','foo2','foo3'])
#   return df

# data = { 'foo':['a','b','c','d','e','f','g']}
# df = pd.DataFrame(data)

# df = some_function_v1(df)
# print(df)



# 第三个 https://stackoverflow.com/questions/73962606/how-to-wrap-cell-value-in-a-dict-maintaining-value-without-using-apply/73962949#73962949 

df=pd.DataFrame()
df['column'] = ['a', 'b', np.NAN, 'c']
print(df)

