import pandas as pd
import timeit

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


df = pd.DataFrame({'ID':[123,123,123,456,456,456,456,789,789],
                    'domain':['vk.com','vk.com','twitter.com','vk.com','facebook.com','vk.com','google.com','twitter.com','vk.com']}
                    )
# df.set_index('ID', inplace=True)

print(df)
