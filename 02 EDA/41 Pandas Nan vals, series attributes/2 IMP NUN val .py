'''
                                                    DataType

    Python      ->      None        empty object    NoneType
    Pandas      ->      NaN         missing value   float

    NaN Value
    ---------

        --> Nun is datatype 
        --> NaN mean "Not a Number"

        student come for DEMO
        ---------------------

    student     mobile no     Normal terminology      pandas
        1       123456789                               
        2       235689741
        3                         no value              NaN
        4       251436987       
        5                         no value              NaN
        6       123654789                               

        NUN mean missing value
        -----------------------
        
'''
import pandas as pd

a = [10,20,30,40]
s = pd.Series(a)
print(s)
print("----------------------------------")

# creating series with NAN val
a = [10,None,30,40]
s = pd.Series(a)
print(s)

'''
0    10.0
1     NaN
2    30.0
3    40.0
dtype: float64
'''
# NaN with string

names = ["aditya","chiku",None,"bony"]
s = pd.Series(names)
print(s)

'''
0    aditya
1     chiku
2      None
3      bony
dtype: object
'''
import numpy as np

names = ["aditya","chiku",np.nan,"bony"]
s = pd.Series(names)
print(s)

'''
0    aditya
1     chiku
2       NaN
3      bony
dtype: object
'''