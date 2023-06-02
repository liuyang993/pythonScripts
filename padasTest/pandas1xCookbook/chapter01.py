import pandas as pd
import numpy as np
movies = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/movie.csv")

# print(movies)

# print(movies.columns)
# index = movies.index

# movies = movies.set_index(['director_name'])
# print(movies)

# print(columns)
# print(index)

# data = movies.to_numpy()
# print(data)


# print(index.to_numpy())

# print(movies.dtypes)




# print(movies["director_name"])
# print(movies.director_name)

# print(movies.director_name.head(100))

# print(movies.director_name.value_counts())

# print(movies.movie_facebook_likes.describe())


# print(movies.loc[:, "director_name"])

# print(movies.iloc[:, 0])

imdb_score = movies["imdb_score"]

print(imdb_score.gt(7))