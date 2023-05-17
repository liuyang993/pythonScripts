import pandas as pd
import numpy as np

# fname = ["Paul", "John", "Richard", "George"]
# lname = ["McCartney", "Lennon", "Starkey", "Harrison"]
# birth = [1942, 1940, 1940, 1943]

# people = {"first": fname, "last": lname, "birth": birth}

# beatles = pd.DataFrame(people)

# print(beatles)

diamond= pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/diamonds.csv")
print(diamond.info())