from scipy.stats import frechet_r
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)

F=frechet_r(loc=17.440  ,scale= 8.153, c=   0.198)              
x=np.arange(0.01,120,0.01)
ax.plot(x, F.pdf(x), 'k-', lw=2)

plt.show()