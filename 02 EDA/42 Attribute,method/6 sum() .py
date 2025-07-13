'''
sum()   --> function in python
sum()   --> method in series method
'''

import pandas as pd
a = [10,20,30,40,50,60,70,80,90,100]
s = pd.Series(a)

print(s.sum())
print("-------------------------------")
a = [10,20,30,40,50,60,70,80,90,100,None,None]
s = pd.Series(a)

print(s.sum())