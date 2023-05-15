# from scipy.io import loadmat
# import matplotlib
# import matplotlib.pyplot as plt

# mnist = loadmat("../../pythonsample/mnist-original.mat")
# # mnist_data = mnist["data"].T

# print(mnist)

# X,y= mnist["data"],mnist["label"]
# # print(X.shape)
# # print(y.shape)


# yourDigit = X[36000]
# Your_image = your_image.reshape(26, 26)
# plt.imshow(Your_image, cmap = matplotlib.cm.binary,
# interpolation="nearest")
# plt.axis("off")
# plt.show()




# 例子 从 https://www.datatechnotes.com/2020/09/sgd-classification-example-with-sgdclassifier-in-python.html


# from sklearn.linear_model import SGDClassifier
# from sklearn.datasets import load_iris
# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import classification_report
# from sklearn.preprocessing import scale

# x, y = make_classification(n_samples=5000, n_features=10, 
#                            n_classes=3, 
#                            n_clusters_per_class=1)
# # print(x)

# xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.15)

# sgdc = SGDClassifier(max_iter=1000, tol=0.01)
# # print(sgdc)
 
# sgdc.fit(xtrain, ytrain)

# score = sgdc.score(xtrain, ytrain)
# print("Training score: ", score) 

# ypred = sgdc.predict(xtest)

# cm = confusion_matrix(ytest, ypred)
# # print(cm) 


# cr = classification_report(ytest, ypred)
# print(cr)



# import numpy as np
# from sklearn.linear_model import SGDClassifier
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import make_pipeline
# X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
# Y = np.array([1, 1, 2, 2])
# # Always scale the input. The most convenient way is to use a pipeline.
# clf = make_pipeline(StandardScaler(),
#                     SGDClassifier(max_iter=1000, tol=1e-3))
# clf.fit(X, Y)


# print(clf.predict([[-0.8, -1]]))

# 原版例子

import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
Y = np.array([1, 1, 2, 2])
# Always scale the input. The most convenient way is to use a pipeline.
clf = make_pipeline(StandardScaler(),
                    SGDClassifier(max_iter=1000, tol=1e-3))
clf.fit(X, Y)


print(clf.predict([[-0.8, -1]]))
