# import pandas as pd
# import numpy as np


# college = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/college.csv")

# print(college.head(5))

# print(college.info())
# print(college.describe(include=[np.number]).T)


# college.sample(random_state=42)


# df = pd.read_csv("../../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/college_data_dictionary.csv")
# print(df.to_numpy())

###########################################


import datetime
import pandas_datareader.data as web
import requests_cache

session = requests_cache.CachedSession(
    cache_name="cache",
    backend="sqlite",
    expire_after=datetime.timedelta(days=90),
    )

tsla = web.DataReader(
    "tsla",
    data_source="yahoo",
    start="2023-1-1",
    session=session,
)

print(tsla.head(8))