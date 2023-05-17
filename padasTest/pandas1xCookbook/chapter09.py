import pandas as pd
import numpy as np


flights = pd.read_csv("../../pythonsample/Pandas-Cookbook-Second-Edition-master/data/flights.csv")
# print(flights.head())

print(flights['AIRLINE'])

print(flights.groupby('AIRLINE').agg({'ARR_DELAY':'mean'}))
