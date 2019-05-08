import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

def distance_cost_plot(distances):
    im = plt.imshow(distances, interpolation='nearest', cmap='Reds') 
    plt.gca().invert_yaxis()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.colorbar()
    #plt.show()


def path_cost(x, y, accumulated_cost, distances):
    path = [[len(x)-1, len(y)-1]]
    cost = 0
    i = len(y)-1
    j = len(x)-1
    while i>0 and j>0:
        if i==0:
            j = j - 1
        elif j==0:
            i = i - 1
        else:
            if accumulated_cost[i-1, j] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
                i = i - 1
            elif accumulated_cost[i, j-1] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
                j = j-1
            else:
                i = i - 1
                j= j- 1
        path.append([j, i])
    path.append([0,0])
    for [y, x] in path:
        cost = cost +distances[x, y]
    return path, cost       

#%matplotlib inline
x=  np.array([1, 1, 2, 3, 2, 0])
y = np.array([0, 1, 1, 2, 3, 2, 1])

plt.plot(x,'r', label='x')
plt.plot(y, 'g', label='y')
plt.legend()

#plt.show()

distances = np.zeros((len(y), len(x)))    #建立一个 len(y) 行 , len(x) 列 的矩阵 ，并初始化为零
#print(distances)

for i in range(len(y)):
    for j in range(len(x)):
        distances[i,j] = (x[j]-y[i])**2    # 计算 y的每个点到 x的距离 

print(distances)        

distance_cost_plot(distances)

# 另一个矩阵
accumulated_cost = np.zeros((len(y), len(x)))
accumulated_cost[0,0] = distances[0,0]

for i in range(1, len(x)):
    accumulated_cost[0,i] = distances[0,i] + accumulated_cost[0, i-1]    

for i in range(1, len(y)):
    accumulated_cost[i,0] = distances[i, 0] + accumulated_cost[i-1, 0]    

for i in range(1, len(y)):
    for j in range(1, len(x)):
        accumulated_cost[i, j] = min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]) + distances[i, j]


distance_cost_plot(accumulated_cost)

#找出最短路径 
path, cost = path_cost(x, y, accumulated_cost, distances)

print(path)
print(cost)
