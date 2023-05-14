from pandas import read_csv
series = read_csv('../../pythonsample/Datasets-master/daily-total-female-births.csv', header=0, index_col=0, parse_dates=True,
squeeze=True)

# series = read_csv('../../pythonsample/Datasets-master/daily-total-female-births.csv', header=0, index_col=0, parse_dates=True)

# series = read_csv('../../pythonsample/Datasets-master/daily-total-female-births.csv')


# print(type(series))
# print(series.head())

print(series.size)