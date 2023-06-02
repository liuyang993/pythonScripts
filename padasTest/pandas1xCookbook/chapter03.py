# Creating DataFrames from scratch

import pandas as pd
import numpy as np

# fname = ["Paul", "John", "Richard", "George"]
# lname = ["McCartney", "Lennon", "Starkey", "Harrison"]
# birth = [1942, 1940, 1940, 1943]

# people = {"first": fname, "last": lname, "birth": birth}

# beatles = pd.DataFrame(people)

# print(beatles)



# diamond= pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/diamonds.csv")
# print(diamond.info())


diamonds2 = pd.read_csv(
    "../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/diamonds.csv",
    nrows=1000,
    dtype={
    "carat": np.float32,
    "depth": np.float32,
    "table": np.float32,
    "x": np.float32,
    "y": np.float32,
    "z": np.float32,
    "price": np.int16,
    },
)

print(diamonds2.describe())
