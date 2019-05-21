import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt

# Generate random experimental data
x = np.random.random(15)
y = np.random.random(15)



exp_data = np.zeros((15, 2))
exp_data[:, 0] = x
exp_data[:, 1] = y

#tdArray=[]
#for  i in range(0,14) :
    #tdArray.append([])
    #tdArray[i].append(x[i])
    #tdArray[i].append(y[i])

tdArray = np.zeros((len(x), 2))
tdArray[:, 0] = x
tdArray[:, 1] = y


minX = np.min(tdArray[:, 0])



# Generate random numerical data
x = np.random.random(15)
y = np.random.random(15)
num_data = np.zeros((15, 2))
num_data[:, 0] = x
num_data[:, 1] = y




minX = np.min(exp_data[:, 0])

# quantify the difference between the two curves using PCM
pcm = similaritymeasures.pcm(exp_data, num_data)

# quantify the difference between the two curves using
# Discrete Frechet distance
df = similaritymeasures.frechet_dist(exp_data, num_data)

# quantify the difference between the two curves using
# area between two curves
area = similaritymeasures.area_between_two_curves(exp_data, num_data)

# quantify the difference between the two curves using
# Curve Length based similarity measure
cl = similaritymeasures.curve_length_measure(exp_data, num_data)

# quantify the difference between the two curves using
# Dynamic Time Warping distance
dtw, d = similaritymeasures.dtw(exp_data, num_data)

# print the results
print(pcm, df, area, cl, dtw)

# plot the data
plt.figure()
plt.plot(exp_data[:, 0], exp_data[:, 1])
plt.plot(num_data[:, 0], num_data[:, 1])
plt.show()