# from pandas import read_csv
# from pandas import DataFrame
# series = read_csv('../../pythonsample/Datasets-master/daily-min-temperatures.csv', header=0, index_col=0,
# parse_dates=True, squeeze=True)

# # print(series)
# # print(series.index[1].month)

# dataframe = DataFrame()
# dataframe['month'] = [series.index[i].month for i in range(len(series))]
# dataframe['day'] = [series.index[i].day for i in range(len(series))]
# dataframe['temperature'] = [series[i] for i in range(len(series))]
# print(dataframe.head(5))


######################################################


from pandas import read_csv
from pandas import DataFrame
from pandas import concat
series = read_csv('../../pythonsample/Datasets-master/daily-min-temperatures.csv', header=0, index_col=0,
parse_dates=True, squeeze=True)
temps = DataFrame(series.values)
dataframe = concat([temps.shift(1), temps], axis=1)
dataframe.columns = ['t', 't+1']
print(dataframe.head(5))




