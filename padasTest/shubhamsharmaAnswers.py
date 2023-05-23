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
# 如何用map


# df=pd.DataFrame()
# df['column'] = ['a', 'b', np.NaN, 'c']
# print(df)

# # df['column'] = df['column'].apply(lambda value: {"key": None} if type(value) == pd._libs.missing.NAType or pd.isna(value) or pd.isnull(value) or value == '' else {"key": value})

# df['column'] = df['column'].replace(['', np.nan], None).map(lambda k: {'key': k})
# print(df)


# 第四个 https://stackoverflow.com/questions/76194779/python-pandas-function-to-replicate-the-creation-of-a-variable

# 根据条件生成 多一列

#Basically aux_35 take data from pdt_050 and assign the value based on the variable tob. For example: when the number of tob is equal to 1 or 0, aux_35 should be the first element of the array pdt_050 and when tob is a number that is higher than the length of elements on pdt_050, aux_35 should be equal to the last element in pdt_050


# df = pd.DataFrame({'pdt_050':[[0.683522, 0.26141],
# [0.683522, 0.26141],
# [0.683522, 0.26141],
# [0.726501, 0.373269, 0.159278],
# [0.726501, 0.373269, 0.159278],
# [0.596246, 0.288327, 0.120612],
# [0.353175, 0.314364, 0.159139],
# [0.595886, 0.25835],
# [0.582035],
# [0.726501, 0.373269, 0.159278],
# [0.583463, 0.366378, 0.262419, 0.19254, 0.1288, 0.064597],
# [0.751279, 0.436349, 0.248187, 0.110235]
# ],

# 'tob': [1, 1,1, 1, 1, 1, 14, 2, 1, 1, 0, 1
# ]
# })

# def indexer(a, i):
#     print(int(i))
#     print(len(a))
#     print(max(1, min(int(i), len(a))))
#     print('*****')
#     # print(max(1, min(int(i), len(a))))
#     return a[max(1, min(int(i), len(a))) - 1]

# df['aux_35'] = df.apply(lambda s: indexer(s['pdt_050'], s['tob']), axis=1)


# print(df)


# 第五个 https://stackoverflow.com/questions/71605971/assign-values-from-numpy-array-to-pandas-dataframe-based-on-almost-matching-unix/71606117#71606117

# arr = np.array([[1648137283, 0],
#                 [1648137284, 1],
#                 [1648137285, 2]])



# df = pd.DataFrame({'unix':[1648137283,
# 1648137285,1648137284
# ],
# 'value': [23,54,25]
# })

# df['index'] = df['unix'].map(dict(arr))
# # dicarr = dict(arr)
# # print(dicarr)
# df['floor'] = df['unix'].floordiv(10).mul(10)

# print(df)

#第六个  https://stackoverflow.com/questions/62808580/rearranging-a-column-based-on-a-list-order-and-then-mapping-the-list-as-a-new-co/62808907#62808907

df_temp = pd.DataFrame({'Name':['ABC',
'EFG','HIJ','ABC'
],
'Class': [1,2,3,4]
})


arr =  ['AbC', 'EfG', 'HiJ']
d = {x.lower():x for x in arr}
df_temp['DB_Name'] = df_temp['Name'].str.lower().map(d)

print(df_temp)