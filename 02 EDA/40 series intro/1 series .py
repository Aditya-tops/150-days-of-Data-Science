'''
    --> series can store single column data
    --> series is predefiend class

    --> Creation
            1. empty series
            2. By using list
            3. By using array
            4. Access single column
'''
import pandas as pd

s = pd.Series()
print(s)                      # Series([], dtype: object)
print(type(s))                # <class 'pandas.core.series.Series'>
print("-----------------------------------")
# series is a pre-defined class
# so let create a object
a = [10,20,30,40]
b = pd.Series(a)
print(b)
'''
0    10
1    20
2    30
3    40
dtype: int64

==> series objects  can display 3 output

        --> here is 0
                    1
                    2
                    3
                        is index

        --> here is 10
                    20
                    30
                    40
                        is data

        --> dtype: int64 this is a datatype

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