import pandas as pd
import timeit
import numpy as np

# 问题一  怎么join 俩个dataframe :  https://stackoverflow.com/questions/40468069/merge-two-dataframes-by-index/40468090#40468090
 
# df1 = pd.DataFrame({'a':range(6),
#                     'b':[5,3,6,9,2,4]}, index=list('abcdef'))

# print (df1)

# df2 = pd.DataFrame({'c':range(4),
#                     'd':[10,20,30, 40]}, index=list('abhi'))

# print (df2)


# # a和b都有的 inner join
# df3 = pd.merge(df1, df2, left_index=True, right_index=True)
# print (df3)

# # left join
# df4 = df1.join(df2)
# print (df4)

# #out join
# df5 = pd.concat([df1, df2], axis=1)
# print (df5)



#问题二 把一列分割为两列 ： https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns/35491399#35491399

# df = pd.DataFrame({"teams": [["SF", "NYG"] for _ in range(7)]})
# print(df)

# df3 = pd.DataFrame(df['teams'].to_list(), columns=['team1','team2'])
# print (df3)

# # %timeit df2['teams'].apply(pd.Series) 这句是运行在jupter的


#问题三 单算某一列的sum https://stackoverflow.com/questions/41286569/get-total-of-pandas-column/41286607#41286607

# df1 = pd.DataFrame({'a':range(6),
#                     'MyColumn':[84,76,28,28,19,84]})

# print(df1)

# # df1.loc['Total'] = df1['MyColumn'].sum()
# # print(df1)

# df1.at['Total', 'MyColumn'] = df1['MyColumn'].sum()
# print(df1)


#问题四 按照两列group 计算总数 https://stackoverflow.com/questions/38309729/count-unique-values-per-groups-with-pandas/38309823#38309823

# df = pd.DataFrame({'ID':[123,123,123,456,456,456,456,789,789],
#                     'domain':['vk.com','vk.com','twitter.com','vk.com','facebook.com','vk.com','google.com','twitter.com','vk.com']}
#                     )
# # print(df.domain.value_counts())

# df = df.groupby('domain')['ID'].nunique()

# print(df)


#问题五  如何把离散数据分桶  https://stackoverflow.com/questions/45273731/binning-a-column-with-pandas/45273750#45273750 
#例子把数据分在 [0,1] , [1,5] , [5,10]等区间

# df = pd.DataFrame({'percentage':[46.5,44.2,100.0,42.12]})

# bins = [0, 1, 5, 10, 25, 50, 100]
# df['binned'] = pd.cut(df['percentage'], bins)
# print (df)


# 问题六 如何按星期分组 https://stackoverflow.com/questions/45281297/group-by-week-in-pandas/45281439#45281439


# df = pd.DataFrame({'Name':['Apple','orange','Aapple','orange','Apple'],
#                     'Date':['07/11/17','07/14/17','07/14/17','07/25/17','07/20/17'],
#                     'Quan':[20,20,70,40,30]}
#                     )

# df['Date'] = pd.to_datetime(df['Date']) - pd.to_timedelta(7, unit='d') #减去7天是为了把日期包括在前一个星期，比如7月11记在7.10这个星期而不是7-17

# print(df)

# df = df.groupby(['Name', pd.Grouper(key='Date', freq='W-MON')])['Quan'].sum().reset_index().sort_values('Date')
# print (df)


#问题七  把某一列从float转到int64

# df = pd.DataFrame({'column name':[7500000.0,7500000.0, np.nan]})
# print (df['column name'])

# df['column name'] = df['column name'].astype('Int64')
# print(df)

#问题八 找出所有列中包含nan的行  https://stackoverflow.com/questions/43424199/display-rows-with-one-or-more-nan-values-in-pandas-dataframe/43424223#43424223

# d = {'filename': ['M66_MI_NSRh35d32kpoints.dat', 'F71_sMI_DMRI51d.dat', 'F62_sMI_St22d7.dat', 'F41_Car_HOC498d.dat', 'F78_MI_547d.dat'], 'alpha1': [0.8016, 0.0, 1.721, 1.167, 1.897], 'alpha2': [0.9283, 0.0, 3.833, 2.809, 5.459], 'gamma1': [1.0, np.nan, 0.23748000000000002, 0.36419, 0.095319], 'gamma2': [0.074804, 0.0, 0.15, 0.3, np.nan], 'chi2min': [39.855990000000006, 1e+25, 10.91832, 7.966335000000001, 25.93468]}
# df = pd.DataFrame(d).set_index('filename')
# print(df)

# df1 = df[df.isna().any(axis=1)]

# print(df1)


#问题九 找出所有 cycle列包括整数的行，比如1.0  ，  2.0 . 不要 0.2  ， 0.8

# #Create dataset
# data = {'id': [1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1,
#                2, 2, 2, 2, 2, 2, 2,
#                3, 3, 3, 3, 3, 3, 3,3,
#                4, 4, 4, 4, 4,4,
#                5, 5, 5, 5, 5, 5,5, 5, 5,5,     5,5, 5,5, 5, 5,5],
#         'cycle': [0.0, 0.2,0.4, 0.6, 0.8, 1,1.2,1.4,1.6,1.8,2.0,2.2,
#                   0.0, 0.2,0.4, 0.6,0.8,1.0,1.2,
#                   0.0, 0.2,0.4, 0.6, 0.8,1.0,1.2,1.4,
#                   0.0, 0.2,0.4, 0.6, 0.8,1.0,
#                   0.0, 0.2,0.4, 0.6, 0.8, 1.0,1.2,1.4,1.6,1.8,   2.0,2.2,2.4,2.6,2.8,3.0,3.2],
#         'Salary': [6, 7, 7, 7,8,9,10,11,12,13,14,15,
#                    3, 4, 4, 4,4,5,6,
#                    2, 8,9,10,11,12,13,14,
#                    1, 8,9,10,11,12,
#                    6, 7, 7,9,10,11,12,13,14,15, 9,10,11,12,13,14,15],
#         'Children': ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No','No', 'Yes', 'Yes', 'Yes', 'No',
#                      'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 
#                      'Yes', 'No','Yes', 'Yes', 'No','No', 'Yes','Yes',
#                      'Yes', 'Yes', 'No','Yes', 'Yes','Yes',
#                      'Yes', 'No',  'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No',    'No',  'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes'],
#         'Days': [141, 123, 128, 66, 66, 120, 141, 52,96, 120, 141, 52,
#                  141, 96, 120,120, 141, 52,96,
#                  141,  15,123, 128, 66, 120, 141, 141,
#                  141, 141,123, 128, 66,67,
#                  141, 123, 128, 66, 123, 128, 66, 120, 141, 52,   123, 128, 66, 123, 128, 66, 120,],
#         }

# #Convert to dataframe
# df = pd.DataFrame(data)
# print(df)

# out=df[df['cycle'].ne(0) & df['cycle'].astype(int).eq(df['cycle'])].reset_index(drop=True)
# print (out)



# 问题十 。 去掉string的空格 

# import pandas as pd

# df = pd.DataFrame([['  a  ', 10], ['  c  ', 5]])
# print (df)
# df_obj = df.select_dtypes(['object'])
# # print (df_obj)


# df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
# print (df)
# print(df[0][0])


