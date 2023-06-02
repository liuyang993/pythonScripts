# Beginning Data Analysis

import pandas as pd
import numpy as np


college = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/college.csv")

# print(college.head(5))

# print(college.info())
# print(college.describe(include=[np.number]).T)


# print(college.sample(random_state=42))
# print(college.shape)

# print(college.describe(include=[np.number]).T)
# print(college.describe(include=[np.object0]).T)


print(college.describe(
include=[np.number],
    percentiles=[
        0.01,
        0.05,
        0.10,
        0.25,
        0.5,
        0.75,
        0.9,
        0.95,
        0.99,
        ],
).T)

# df = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/college_data_dictionary.csv")
# print(df.to_numpy())

###########################################


# import datetime
# import pandas_datareader.data as web
# import requests_cache

# session = requests_cache.CachedSession(
#     cache_name="cache",
#     backend="sqlite",
#     expire_after=datetime.timedelta(days=90),
#     )

# tsla = web.DataReader(
#     "tsla",
#     data_source="yahoo",
#     start="2023-1-1",
#     session=session,
# )

# print(tsla.head(8))