import pandas as pd
import numpy as np

# college = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/college.csv")
# print(college.dtypes)

college = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/college.csv", index_col="INSTNM")

# print(college)

city = college["CITY"]   # 如果前面带 index_col="INSTNM" ， 这里就是选出2列 ，city 和 INSTNM

print(city)

# print(city["Alabama A & M University"])  #按这个index找 

# print( city.loc["Alabama A & M University"])

# print( city.loc[5])      #这样是错的

# print( city.iloc[0])

# print(city[
#         [
#         "Alabama A & M University",
#         "Alabama State University",
#         ]
#     ]
#     )

print(city.iloc[[0, 4]])       #第0和第4