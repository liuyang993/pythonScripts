import numpy as np
import pandas as pd

# x = pd.Series([1, 2, 2, np.nan], index=['p', 'q', 'r', 's'])
# x = pd.Series([3660], index=['2020-1-1 09:00:00'])
# print(x)


df = pd.DataFrame( columns=['date','value'])
df=df.append({'date':'2020-1-1 09:00:00','value':'3600'}, ignore_index=True)



# df['date'].append('2020-1-1 09:00:00')
# df['value'].append(3660)
print(df.head())

