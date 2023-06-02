import pandas as pd
import numpy as np
movies = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/movie.csv")


# movie_actor_director = movies[
#         [
#         "actor_1_name",
#         "actor_2_name",
#         "actor_3_name",
#         "director_name",
#         ]
#     ]


# print(movie_actor_director.head())

# print(movies["director_name"])

# print(movies.shape)    #显示有多少行，多少列

# print(movies.size)    #显示一共有多少元素，就是行乘列

# print(movies.ndim) 

# print(len(movies)) 

# print(movies.count())   #显示每一列的值的总个数，除了缺失的

# print(movies.min())   #显示每一列的值的总个数，除了缺失的

# print(movies.describe())

def shorten(col):
    return (
    str(col)
    .replace("facebook_likes", "fb")
    .replace("_for_reviews", "")
    )

movies = movies.rename(columns=shorten)
print(movies.columns)