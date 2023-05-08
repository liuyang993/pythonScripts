import pandas as pd
import numpy as np
movies = pd.read_csv("../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/movie.csv")
# print(movies)

columns = movies.columns
index = movies.index
data = movies.to_numpy()

# print(columns)
print(index)
# print(data)
