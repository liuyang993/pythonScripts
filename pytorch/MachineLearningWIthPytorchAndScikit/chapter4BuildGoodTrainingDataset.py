import pandas as pd
from io import StringIO
import sys

# csv_data = \
# '''A,B,C,D
# 1.0,2.0,3.0,4.0
# 5.0,6.0,,8.0
# 10.0,11.0,12.0,'''

# # If you are using Python 2.7, you need
# # to convert the string to unicode:

# if (sys.version_info < (3, 0)):
#     csv_data = unicode(csv_data)

# df = pd.read_csv(StringIO(csv_data))
# print(df)

# # print(df.values)

# # df=df.dropna(axis=0)
# # print(df)


# # from sklearn.impute import SimpleImputer
# # import numpy as np

# # imr = SimpleImputer(missing_values=np.nan, strategy='mean')
# # imr = imr.fit(df.values)
# # imputed_data = imr.transform(df.values)
# # print(imputed_data)

# df = df.fillna(df.mean())
# print(df)

#######################################################

df = pd.DataFrame([['green', 'M', 10.1, 'class2'],
                   ['red', 'L', 13.5, 'class1'],
                   ['blue', 'XL', 15.3, 'class2']])

df.columns = ['color', 'size', 'price', 'classlabel']
print(df)

size_mapping = {'XL': 3,
                'L': 2,
                'M': 1}

df['size'] = df['size'].map(size_mapping)
print(df)
