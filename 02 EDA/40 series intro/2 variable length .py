'''
    Backend they created constructor with VARIABLE LENGTH

    Series()
    Series(10)
    Series(10,20)
    Series(10,20,30)
    Series(10,20,30,40)
        
'''
class Student:
    def __init__(self, *k):
        print(k)

s = Student()
s = Student(10)
s = Student(10,20)
s = Student(10,20,30)
s = Student(10,20,30,40)

'''
()
(10,)
(10, 20)
(10, 20, 30)
(10, 20, 30, 40)
'''

print("-----------------------------")

import pandas as pd

a = [10,20,30,"aditya"]
b = pd.Series(a)
print(b)

