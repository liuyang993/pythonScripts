import pandas as pd
import numpy as np
movies = pd.read_csv("../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/movie.csv")
# print(movies)

columns = movies.columns
index = movies.index
data = movies.to_numpy()

# print(columns)
# print(index)
# print(data)


# print(index.to_numpy())

# print(movies["director_name"])
# print(movies.director_name)

# print(movies.director_name.head(100))

# print(movies.director_name.value_counts())

print(movies.movie_facebook_likes.describe())


