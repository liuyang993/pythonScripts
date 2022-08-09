# import matplotlib.pyplot as plt
# from pylab import *
# import numpy as np

# x = np.linspace(0, 2*np.pi, 400)
# y = np.sin(x**2)

# subplots_adjust(hspace=0.000)
# number_of_subplots=3

# for i,v in enumerate(range(number_of_subplots)):
#     v = v+1
#     ax1 = subplot(number_of_subplots,1,v)
#     ax1.plot(x,y)

# plt.show()


#######################################################


# import matplotlib.pyplot as plt

# # Start with one
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot([1,2,3])

# # Now later you get a new subplot; change the geometry of the existing
# n = len(fig.axes)
# for i in range(n):
#     fig.axes[i].change_geometry(n+1, 1, i+1)

# # Add the new
# ax = fig.add_subplot(n+1, 1, n+1)
# ax.plot([4,5,6])

# plt.show() 



import math
import matplotlib.pylab as plt

nrows = int(math.ceil(len(subsl) / 2.))

fig, axs = plt.subplots(nrows, 2)

ylim = 100000, 600000
for ax, subsm in zip(axs.flat, subsl):
    H7, subsm = sumsubdesc2(table, subsm)
    H7.plot(ax=ax, title='Rolling 4q mean %s' % subsm)
    ax.set_ylim(ylim)
    