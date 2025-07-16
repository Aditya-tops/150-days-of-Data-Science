'''
    # age never be zero
    # here we shouldnt use

    student1    ->      21
    student2    ->      19  
    student3    ->      0   
    student4    ->      30
'''
import pandas as pd
import numpy as np

data = [
            ["rajat",26,40000],
            ["Daniel",16,20000],
            ["veeru",36,60000],
            ["aditya",26,25000],
            ["bony",np.nan,40000],
            ["tony",26,44000],
       ]

df = pd.DataFrame(data,columns=['Name','Age','Salary'])
print(df)

print("----------------")

newdata = df.fillna(18)
print(newdata)