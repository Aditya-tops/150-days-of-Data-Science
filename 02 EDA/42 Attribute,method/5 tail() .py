import pandas as pd
a = [10,20,30,40,50,60,70,80,90,100]
s = pd.Series(a)

print(s.tail())    # head method by default return last 5 values
print(s[3:5])
'''
5     60
6     70
7     80
8     90
9    100
dtype: int64
'''
'''
3    40
4    50
dtype: int64
'''
