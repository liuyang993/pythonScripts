import pandas as pd
import numpy as np
movie = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/movie.csv",index_col="movie_title")

# print(movie[["duration"]].head())

movie_2_hours = movie["duration"] > 120
# print(movie_2_hours)

print(movie_2_hours.mean() * 100)
