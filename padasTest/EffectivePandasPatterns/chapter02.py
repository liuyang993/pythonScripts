import pandas as pd

df = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/vehicles.csv.zip")

# print(df.head())

city_mpg = df.city08
highway_mpg = df.highway08

print(city_mpg)
