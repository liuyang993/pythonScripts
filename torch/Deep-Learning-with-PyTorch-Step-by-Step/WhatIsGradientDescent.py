import numpy as np
import torch
import torch.nn as nn
from chapter0 import *

true_b = 1
true_w = 2
N = 100

# Data Generation
np.random.seed(42)
x = np.random.rand(N, 1)
# print(x)

epsilon = (.1 * np.random.randn(N, 1))
# print(epsilon)
y = true_b + true_w * x + epsilon
# print(y)

# Shuffles the indices
idx = np.arange(N)
np.random.shuffle(idx)   # shuffle mean 洗牌

print(idx)
# Uses first 80 random indices for train
train_idx = idx[:int(N*.8)]
# Uses the remaining indices for validation
val_idx = idx[int(N*.8):]
# Generates train and validation sets
x_train, y_train = x[train_idx], y[train_idx]
x_val, y_val = x[val_idx], y[val_idx]

# print(x[val_idx])
# figure1(x_train, y_train, x_val, y_val)
# plt.show()

# # Step 0 - Initializes parameters "b" and "w" randomly
# np.random.seed(42)
# b = np.random.randn(1)
# w = np.random.randn(1)
# # print(b, w)

# # Step 1 - Computes our model's predicted output - forward pass
# yhat = b + w * x_train

# # Step 2 - Computing the loss
# # We are using ALL data points, so this is BATCH gradient
# # descent. How wrong is our model? That's the error!
# error = (yhat - y_train)
# # It is a regression, so it computes mean squared error (MSE)
# loss = (error ** 2).mean()
# # print(loss)

# ###########################

# # Reminder:
# # true_b = 1
# # true_w = 2
# # we have to split the ranges in 100 evenly spaced intervals each
# b_range = np.linspace(true_b - 3, true_b + 3, 101)
# w_range = np.linspace(true_w - 3, true_w + 3, 101)

# # print(b_range)
# # print(w_range)


# # nx, ny = (3, 2)
# # print(nx,ny)
# # x = np.linspace(0, 1, nx)
# # print(x)
# # y = np.linspace(0, 1, ny)
# # print(y)
# # xv, yv = np.meshgrid(x, y)
# # print(xv)
# # print(yv)




# # meshgrid is a handy function that generates a grid of b and w
# # values for all combinations
# bs, ws = np.meshgrid(b_range, w_range)
# print(bs.shape, ws.shape)

# all_predictions = np.apply_along_axis(
#   func1d=lambda x: bs + ws * x,
#   axis=1,
#   arr=x_train,
# )
# print(all_predictions.shape)


# print(y_train)
# all_labels = y_train.reshape(-1, 1, 1)
# print(all_labels)