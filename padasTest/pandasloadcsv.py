from pandas import read_csv
from pandas import DataFrame
from matplotlib import pyplot
series = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0,
parse_dates=True, squeeze=True)



# dataframe = DataFrame()
# dataframe['month'] = [series.index[i].month for i in range(len(series))]
# dataframe['day'] = [series.index[i].day for i in range(len(series))]
# dataframe['temperature'] = [series[i] for i in range(len(series))]
# print(dataframe.head(5))


series.plot()
pyplot.show()

