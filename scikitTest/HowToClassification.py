# import pyspark
# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName("answers").getOrCreate()

# path = "../../pythonsample/pima-indians-diabetes.csv"

# df = spark.read.option("header",'False').option('delimiter', ',').csv(path)
# df.printSchema()



# from pyspark.sql import SparkSession

# spark = SparkSession.builder

# df = spark.read.format("csv") \
#     .option("header", "false") \
#     .option("inferSchema", "true") \
#     .load("../../pythonsample/pima-indians-diabetes.csv")



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("../../pythonsample/pima-indians-diabetes.csv")

# df.info()
# print(df)
# print(df.describe().transpose())

# sampled_data = df.drop("Class" ,axis=1)
# print(sampled_data)


# sampled_data = df.drop("Class" ,axis=1).sample(replace=False, frac=0.8)


# axs = pd.plotting.scatter_matrix(sampled_data, figsize=(10, 10))

# num_cols = len(sampled_data.columns)
# for cur_col in range(num_cols):
#     ax = axs[cur_col, 0]
#     ax.yaxis.label.set_rotation(0)
#     ax.yaxis.label.set_ha('right')
#     ax.set_yticks(())
#     h = axs[num_cols-1, cur_col]
#     h.xaxis.label.set_rotation(90)
#     h.set_xticks(())

# plt.show()


X = df.iloc[:,:-1].values
y = df.iloc[:, -1].values
# print(X)
# print(y)

X_train, X_test, y_train, y_test = \
        train_test_split( \
                         X, y, \
                         test_size = 0.25, \
                         random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# 使用线性回归分类 

lr = LogisticRegression(random_state = 0)
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)

cm_lr = confusion_matrix(y_test, y_pred_lr)
print(cm_lr)
acc_lr = accuracy_score(y_test, y_pred_lr)
print (acc_lr)
