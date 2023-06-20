import numpy as np
import torch
import torch.nn as nn
from chapter0 import *

true_b = 1
true_w = 2
N = 100

# Data Generation
np.random.seed(42)
x = np.random.rand(N, 1)    #生成100个0，1之间的数字。1维,第二次运行 np.random.rand(N, 1) 会不一样
# print(x[:5])



epsilon = (.1 * np.random.randn(N, 1))
# print(epsilon[:5])


y = true_b + true_w * x + epsilon
# # print(y)

# Shuffles the indices
idx = np.arange(N)
# print(idx[:5])

np.random.shuffle(idx)   # shuffle mean 洗牌，打乱idx的顺序
# print(idx[:5])

# Uses first 80 random indices for train
train_idx = idx[:int(N*.8)]
# print(train_idx[:5])


# Uses the remaining indices for validation
val_idx = idx[int(N*.8):]
# Generates train and validation sets
x_train, y_train = x[train_idx], y[train_idx]
x_val, y_val = x[val_idx], y[val_idx]



# print(x[val_idx])
# figure1(x_train, y_train, x_val, y_val)
# plt.show()

# Step 0 - Initializes parameters "b" and "w" randomly
np.random.seed(42)
b = np.random.randn(1)
w = np.random.randn(1)
# print(b, w)     # b实为1，w是2，这里先随意假设b和w

# Step 1 - Computes our model's predicted output - forward pass
yhat = b + w * x_train

# figure2(x_train, y_train, b, w)
# plt.show()

# Step 2 - Computing the loss
# We are using ALL data points, so this is BATCH gradient
# descent. How wrong is our model? That's the error!
error = (yhat - y_train)
# It is a regression, so it computes mean squared error (MSE)
loss = (error ** 2).mean()
# print(loss)

# ###########################

# Reminder:
# true_b = 1
# true_w = 2
# we have to split the ranges in 100 evenly spaced intervals each

# b_range = np.linspace(0, 1, 3)
# print(b_range)


#为什么这里是101， 因为是以true_b，true_w为中点的平均分布，总数必须是奇数，这样才能把中间正确的点包含进来
b_range = np.linspace(true_b - 3, true_b + 3, 101)
w_range = np.linspace(true_w - 3, true_w + 3, 101)

# print(b_range)
# print(w_range)


# nx, ny = (3, 2)
# print(nx,ny)
# x = np.linspace(0, 1, nx)
# print(x)
# y = np.linspace(0, 1, ny)
# print(y)
# xv, yv = np.meshgrid(x, y)
# print(xv)
# print(yv)




# meshgrid is a handy function that generates a grid of b and w
# values for all combinations
bs, ws = np.meshgrid(b_range, w_range)
print(bs.shape, ws.shape)

all_predictions = np.apply_along_axis(
  func1d=lambda x: bs + ws * x,
  axis=1,
  arr=x_train,
)
print(all_predictions.shape)


# print(y_train)
all_labels = y_train.reshape(-1, 1, 1)
print(all_labels.shape)


all_errors = (all_predictions - all_labels)

all_losses = (all_errors ** 2).mean(axis=0)
# figure4(x_train, y_train, b, w, bs, ws, all_losses)
# plt.show()

# Step 3 - Computes gradients for both "b" and "w" parameters

b_grad = 2 * error.mean()     #计算b的偏导数
w_grad = 2 * (x_train * error).mean()
print(b_grad, w_grad)

# figure7(b, w, bs, ws, all_losses)
# plt.show()


# Sets learning rate - this is "eta" ~ the "n" like Greek letter
lr = 0.1
print(b, w)
# Step 4 - Updates parameters using gradients and the
# learning rate
b = b - lr * b_grad
w = w - lr * w_grad
print(b, w)


