# creating series and give a name


import pandas as pd

marks = [56,78,90,94,36,65]
s = pd.Series(marks, name = "aditya")
print(s)

'''
0    56
1    78
2    90
3    94
4    36
5    65
Name: aditya, dtype: int64


--->  name = "aditya" is keyword argument
'''