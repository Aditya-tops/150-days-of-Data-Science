import pandas as pd
import numpy as np

data = [
        ['aditya',21,4000],
        ['bony',22,6000],
        ['veeru',25,4400],
        ['jay',19,8500],
        ['suman',2,99900],
        [np.nan,21,4000],
        ['aditi',21,4000],
     ]

c = ['Name','Age','Salary']

df = pd.DataFrame(data,columns=c)
print(df)
print(df.shape)
print("==================================")
d = df['Name'].notnull()
print(df[d])
print(df[d].shape)





