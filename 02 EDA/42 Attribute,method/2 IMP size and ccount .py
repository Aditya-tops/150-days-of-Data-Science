'''
    Q What is the diffrent between size and count() ?
    Size    : Total number of values including missing values
    Count() : Total number of values excluding missing values

    --> size is a attritube
    --> count is a method
    
'''
import  pandas as pd
a = [10,20,None,40]
s = pd.Series(a)

print(s.size)       # 4
print(s.count())    # 3


