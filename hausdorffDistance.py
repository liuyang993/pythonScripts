from scipy.spatial.distance import directed_hausdorff
import numpy as np
#u = np.array([(1.0, 0.0),(0.0, 1.0),(-1.0, 0.0),(0.0, -1.0)])
#v = np.array([(2.0, 0.0),(0.0, 2.0),(-2.0, 0.0),(0.0, -4.0)])

#u = np.array([(1.0, 0.0),(2.0, 0.0),(3.0, 0.0),(4.0, 0.0)])
#v = np.array([(1.0, 4.0),(2.0, 4.0),(3.0, 4.0),(4.0, 4.0)])


u = np.array([(1.0, 4032.8),(2.0, 4033.0),(3.0, 4033.0),(4.0, 4033.2),(5.0, 4033.2),(6.0, 4035.2),(7.0, 4035.0),(8.0, 4034.0),(9.0, 4035.0),(10.0, 4035.6)])
v = np.array([(1.0, 4011.0),(2.0, 4010.0),(3.0, 4010.0),(4.0, 4006.8),(5.0, 4008.4),(6.0, 4008.8),(7.0, 4008.6),(8.0, 4034.0),(9.0, 4009.0),(10.0, 4009.6)])

print(directed_hausdorff(u, v)[0])
print(directed_hausdorff(v, u)[0])
print(max(directed_hausdorff(u, v)[0], directed_hausdorff(v, u)[0]))
print(directed_hausdorff(v, u)[1:])