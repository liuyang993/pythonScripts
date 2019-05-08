import numpy as np
import matplotlib.pyplot as plt


########################  para 1
#fig, ax = plt.subplots()

#t = np.arange(0.0, 5.0, 0.01)
#s = np.cos(2*np.pi*t)
#line, = ax.plot(t, s, lw=2)

#ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#            arrowprops=dict(facecolor='black', shrink=0.05),
#            )
#ax.set_ylim(-2, 2)
#plt.show()

##############################



plt.axvspan(76, 76, facecolor='g', alpha=1)
plt.annotate('This is awesome!', 
             xy=(76, 0.75),  
             xycoords='data',
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))
plt.show()