'''
    1.Attributes
        -> return/giving info about series objes
        ->Access: by using object name, without parenthesisi

            -> s.attributes1
            -> s.attributes2
            -> s.values
            -> s.index
            
'''
# values and index attribute

import pandas as pd

a = [10,20,30,40]
s = pd.Series(a)

print("cretae series object: s")
print("get data from s object")
print()
print(s.values)                         # [10 20 30 40]
print(s.index)                          # RangeIndex(start=0, stop=4, step=1)
print("Get data type of data",s.dtypes) # int64

'''
-> i wanted to see, .values, .index, .dtypes attributes in s object
    1. by using dir() function
    2. by using documentation
'''

print("----------------------------------------")
a = [10,20,30,40]
s = pd.Series(a)
# print(dir(s))   # or




