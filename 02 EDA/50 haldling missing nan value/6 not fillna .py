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

m = df1['Age'].mean()
print("age avg is",m)                                 # 22

df1['Age'] = df1['Age'].fillna(m)
print()
print(df1)