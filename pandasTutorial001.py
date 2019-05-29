import numpy as np
import pandas as pd


#s = pd.Series([1, 3, 5, np.nan, 6, 8])
#print(s)

#np.random.seed(1234)
#d1 = pd.Series(np.random.normal(size = 100))

d1 = pd.Series(np.random.randint(low=1, high=100, size=4))    

print(d1)

print('index of min is ' , d1.idxmin())
print('index of max is ' , d1.idxmax())

print('average value is ', d1.mean())


