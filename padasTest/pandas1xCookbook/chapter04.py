import pandas as pd
import numpy as np
college = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/college.csv")

print(college.head(5))

# print(college.info())
# print(college.describe(include=[np.number]).T)


# college.sample(random_state=42)