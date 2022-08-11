# 2022-08-11
# midumn 的例子  https://10mohi6.medium.com/super-easy-python-stock-price-forecasting-using-k-nearest-neighbor-machine-learning-ab6f037f0077
# 用 k-nearest-neighbor 算法预测股市收盘价


import pandas_datareader as pdr
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

df = pdr.get_data_yahoo("AAPL", "2010-11-01", "2020-11-01")

# print(df.head(100))

            # 读取之后 ， 原始数据的形式为：

            #                  High        Low       Open      Close       Volume  Adj Close
            # Date
            # 2010-11-01  10.914286  10.792857  10.793571  10.863571  423889200.0   9.275666
            # 2010-11-02  11.078214  10.964286  10.964286  11.048571  433930000.0   9.433622
            # 2010-11-03  11.174286  11.018929  11.120357  11.171429  508348400.0   9.538523
            # 2010-11-04  11.435000  11.251071  11.266071  11.366786  642488000.0   9.705324
            # 2010-11-05  11.413214  11.312500  11.356786  11.326071  361253200.0   9.670565


df["Diff"] = df.Close.diff()  #新增一列， 值是当前行与上一行 close列的差值
# print(df.head(100))

df["SMA_2"] = df.Close.rolling(2).mean() #新增一列， 值是当前行与上一行 close列的和的平均值 rolling(2)意思是向上一行，如果是rolling(3)就是三行
# print(df.head(100))
df["Force_Index"] = df["Close"] * df["Volume"]
# df["y"] = df["Diff"].apply(lambda x: 1 if x > 0 else 0).shift(-1)  #把新增的y列整体往上提一行
df["y"] = df["Diff"].apply(lambda x: 1 if x > 0 else 0)
# print(df.head(100))

df = df.drop(
   ["Open", "High", "Low", "Close", "Volume", "Diff", "Adj Close"],
   axis=1,
).dropna()
# print(df.head(100))

X = df.drop(["y"], axis=1).values
y = df["y"].values
X_train, X_test, y_train, y_test = train_test_split(
   X,
   y,
   test_size=0.2,
   shuffle=False,   #加这个是为了不改变顺序
)
knn = KNeighborsClassifier(n_neighbors=123)
knn.fit(
   X_train,
   y_train,
)
y_pred = knn.predict(X_test)
print(accuracy_score(y_test, y_pred))
