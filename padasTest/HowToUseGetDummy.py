# https://www.sharpsightlabs.com/blog/pandas-get-dummies/

import pandas as pd
import numpy as np

sales_data = pd.DataFrame({"name":["William","Emma","Sofia","Markus","Edward","Thomas","Ethan","Olivia","Arun","Anika","Paulo"]
                           ,"sales":[50000,52000,90000,34000,42000,72000,49000,55000,67000,65000,67000]
                           ,"region":["East","North","East","South","West","West","South","West","West","East",np.nan]
                           }
                          )

print(sales_data)

region = sales_data.region
print(region)

print(pd.get_dummies(region))

print(pd.get_dummies(sales_data, columns = ['region']))

print(pd.get_dummies(sales_data
               ,columns = ['region']
               ,prefix = 'sales_region'
               ))

