# https://machinelearningmastery.com/feature-selection-time-series-forecasting-python/

# # line plot of time series
# from pandas import read_csv
# from matplotlib import pyplot


# # load dataset
# series = read_csv('monthly-car-sales.csv', header=0, index_col=0)
# # display first few rows
# print(series.head(5))
# # line plot of dataset
# series.plot()
# pyplot.show()


# seasonally adjust the time series
from pandas import read_csv
from matplotlib import pyplot
# load dataset
series = read_csv('monthly-car-sales.csv', header=0, index_col=0)
# seasonal difference

print(series.iloc[:24])

shift =  series.shift(12)

differenced = series.diff(12)
# trim off the first year of empty data
differenced = differenced[12:]

# save differenced dataset to file
# differenced.to_csv('seasonally_adjusted.csv', index=False)
# plot differenced dataset


# differenced.plot()
# pyplot.show()

print(shift.iloc[:24])


print(series.iloc[:24] - shift.iloc[:24])
