import pandas as pd
import numpy as np


fueleco = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/vehicles.csv.zip")

# print(fueleco)

# print(fueleco.shape)

# print('***************')

# print(fueleco.mean())

# print('***************')

# print(fueleco.describe())

# print('***************')

# print(fueleco.columns.dtype)

# print(fueleco.info())

# print(fueleco.quantile(
# [0, 0.25, 0.5, 0.75, 1]
# ) 
# )

# print(fueleco.describe(include=object))

# print(fueleco.dtypes) # 显示所有列类型

print(fueleco.dtypes.value_counts()) 