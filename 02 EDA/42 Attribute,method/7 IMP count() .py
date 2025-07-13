'''
count() --> It count total number of values excluding missing 
-------     values(ingnoring missing values)
'''
import pandas as pd

marks = [56,45,67,None,86]
s = pd.Series(marks)

print(s.count())        # 4
print(s.size)        # 4
