import numpy as np
from sklearn.linear_model import LinearRegression
import torch
import torch.optim as optim
import torch.nn as nn

true_b = 1
true_w = 2
N = 100

# Data Generation
np.random.seed(42)
x = np.random.rand(N, 1)
epsilon = (.1 * np.random.randn(N, 1))
y = true_b + true_w * x + epsilon


# Shuffles the indices
idx = np.arange(N)
np.random.shuffle(idx)

# Uses first 80 random indices for train
train_idx = idx[:int(N*.8)]
# Uses the remaining indices for validation
val_idx = idx[int(N*.8):]

# Generates train and validation sets
x_train, y_train = x[train_idx], y[train_idx]
x_val, y_val = x[val_idx], y[val_idx]


scalar = torch.tensor(3.14159)
vector = torch.tensor([1, 2, 3])
matrix = torch.ones((2, 3), dtype=torch.float)
tensor = torch.randn((2, 3, 4), dtype=torch.float)
# print(scalar)
# print(vector)
# print(matrix)
# print(tensor)


# We get a tensor with a different shape but it still is
# the SAME tensor
same_matrix = matrix.view(1, 6)
# print(same_matrix)


# If we change one of its elements...
same_matrix[0, 1] = 2.
# It changes both variables: matrix and same_matrix
# print(matrix)
# print(same_matrix)

# We can use "new_tensor" method to REALLY copy it into a new one
different_matrix = matrix.new_tensor(matrix.view(1, 6))
# Now, if we change one of its elements...
different_matrix[0, 1] = 3.
# The original tensor (matrix) is left untouched!
# But we get a "warning" from PyTorch telling us
# to use "clone()" instead!
# print(matrix)
# print(different_matrix)


# Lets follow PyTorch's suggestion and use "clone" method
another_matrix = matrix.view(1, 6).clone().detach()
# Again, if we change one of its elements...
another_matrix[0, 1] = 4.
# The original tensor (matrix) is left untouched!
# print(matrix)
# print(another_matrix)


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)


x_train_tensor = torch.as_tensor(x_train).float().to(device)
y_train_tensor = torch.as_tensor(y_train).float().to(device)

# Here we can see the difference - notice that .type() is more
# useful since it also tells us WHERE the tensor is (device)
print(type(x_train), type(x_train_tensor), x_train_tensor.type())

back_to_numpy = x_train_tensor.numpy()


# FIRST
# Initializes parameters "b" and "w" randomly, ALMOST as we
# did in Numpy since we want to apply gradient descent on
# these parameters we need to set REQUIRES_GRAD = TRUE
torch.manual_seed(42)
b = torch.randn(1, requires_grad=True, dtype=torch.float)
w = torch.randn(1, requires_grad=True, dtype=torch.float)
print(b, w)


# Step 1 - Computes our model's predicted output - forward pass
yhat = b + w * x_train_tensor
# Step 2 - Computes the loss
# We are using ALL data points, so this is BATCH gradient
# descent. How wrong is our model? That's the error!
error = (yhat - y_train_tensor)
# It is a regression, so it computes mean squared error (MSE)
loss = (error ** 2).mean()
# Step 3 - Computes gradients for both "b" and "w" parameters
# No more manual computation of gradients!
# b_grad = 2 * error.mean()
# w_grad = 2 * (x_tensor * error).mean()
loss.backward()

print(error.requires_grad, yhat.requires_grad, \
  b.requires_grad, w.requires_grad)
print(y_train_tensor.requires_grad, x_train_tensor.requires_grad)

print(b.grad, w.grad)




# Step 0 - Initializes parameters "b" and "w" randomly
torch.manual_seed(42)
b = torch.randn(1, requires_grad=True, \
dtype=torch.float, device=device)
w = torch.randn(1, requires_grad=True, \
dtype=torch.float, device=device)

# Defines number of epochs
n_epochs = 1000
# Sets learning rate - this is "eta" ~ the "n"-like Greek letter
lr = 0.1

for epoch in range(n_epochs):
  # Step 1 - Computes model's predicted output - forward pass
  yhat = b + w * x_train_tensor

  # Step 2 - Computes the loss
  # We are using ALL data points, so this is BATCH gradient
  # descent. How wrong is our model? That's the error!
  error = (yhat - y_train_tensor)
  # It is a regression, so it computes mean squared error (MSE)
  loss = (error ** 2).mean()

  # Step 3 - Computes gradients for both "b" and "w"
  # parameters. No more manual computation of gradients!
  # b_grad = 2 * error.mean()
  # w_grad = 2 * (x_tensor * error).mean()
  # We just tell PyTorch to work its way BACKWARDS
  # from the specified loss!
  loss.backward()

  # Step 4 - Updates parameters using gradients and
  # the learning rate. But not so fast...
  # FIRST ATTEMPT - just using the same code as before
  # AttributeError: 'NoneType' object has no attribute 'zero_'
  # b = b - lr * b.grad
  # w = w - lr * w.grad
  # print(b)

  # SECOND ATTEMPT - using in-place Python assingment
  # RuntimeError: a leaf Variable that requires grad
  # has been used in an in-place operation.
  # b -= lr * b.grad ②
  # w -= lr * w.grad ②

  # THIRD ATTEMPT - NO_GRAD for the win!
  # We need to use NO_GRAD to keep the update out of
  # the gradient computation. Why is that? It boils
  # down to the DYNAMIC GRAPH that PyTorch uses...
  with torch.no_grad():
    b -= lr * b.grad
    w -= lr * w.grad

# PyTorch is "clingy" to its computed gradients, we
# need to tell it to let it go...
b.grad.zero_()
w.grad.zero_()

print(b, w)