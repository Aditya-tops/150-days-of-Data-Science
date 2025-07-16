# replace have 2 para replace(np.nan, yr value)
import pandas as pd
import numpy as np

data = [
            ["rajat",26,40000],
            ["Daniel",16,20000],
            ["veeru",np.nan,60000],
            ["aditya",np.nan,25000],
            ["bony",24,40000],
            ["tony",np.nan,44000],
       ]

df1 = pd.DataFrame(data,columns=['Name','Age','Salary'])
print(df1)
print()
#         replace(para1,para2)
df2 = df1.replace(np.nan,0)
print(df2)