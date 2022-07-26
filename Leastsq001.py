import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimization

plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data
data = pd.read_csv('exportData.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]

#plt.scatter(X, Y)
#plt.show()

# Initial guess.
x0    = np.array([0.0, 0.0, 0.0])

sigma = np.array([1.0,1.0,1.0,1.0,1.0,1.0])

def func(x, a, b, c):
    return a + b*x + c*x*x

#print(optimization.curve_fit(func, X, Y, x0, sigma))
print(optimization.curve_fit(func, X, Y))
