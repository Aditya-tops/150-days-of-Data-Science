'''
    describe()  ->  perform static about the data

    this method is giving 8 output
        1   count
        2   mean
        3   std (standdivision)
        4   min
        5   25%
        6   50%
        7   75%
        8   max
'''
import pandas as pd

a = [10,None,20,30,40] 
s = pd.Series(a)
print(s.describe())
print("------------------------------")
print(s.describe().round(3))
print("------------------------------")


'''
count     4.000000
mean     25.000000
std      12.909944
min      10.000000
25%      17.500000
50%      25.000000
75%      32.500000
max      40.000000
dtype: float64
------------------------------
count     4.00
mean     25.00
std      12.91
min      10.00
25%      17.50
50%      25.00
75%      32.50
max      40.00
dtype: float64

'''