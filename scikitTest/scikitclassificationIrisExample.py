from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd
import numpy as np



iris = load_iris()

# print('The data matrix:\n',iris['data'])
# print('The classification target:\n',iris['target'])
# print('The names of the dataset columns:\n',iris['feature_names'])
# print('The names of target classes:\n',iris['target_names'])
# print('The full description of the dataset:\n',iris['DESCR'])
# print('The path to the location of the data:\n',iris['filename'])

# df = pd.DataFrame(
#     iris['data'], columns=iris['feature_names']
# ).assign(Species=iris['target_names'][iris['target']])

# print("Target names:{}".format(iris['target_names']))


# with pd.option_context('expand_frame_repr', False):
#     print(df.to_string())

# print(df.to_string())

# print(df.describe())

# print(df.groupby('Species').size())

# train, test = train_test_split(df, test_size = 0.4, stratify = df['Species'], random_state = 42)
# print(train)
# print(test)

X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)


X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_new)
print("Prediction :{}".format(prediction))
print("Predicted target name:{}".format(iris['target_names'][prediction]))

# 第五步：评估模型
y_pred = knn.predict(X_test)
print("Test set predictions:\n{}".format(y_pred))
print("Test set score:{:.2f}".format(knn.score(X_test, y_test)))
