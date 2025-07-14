'''
    --> info method give u 7 results

            1. type of object
            2. range of object
            3. number of columns
            4. number of rows
            5. the data type of each column
            6. number of data types
            7. total memory usage
            8. 
'''

import pandas as pd

df = pd.read_csv("dummy.csv")
print(df.info())

'''
--> before

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 600 entries, 0 to 599
Data columns (total 4 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Order ID       600 non-null    int64  
 1   Customer Name  600 non-null    object 
 2   Product        600 non-null    object 
 3   Quantity       597 non-null    float64
dtypes: float64(1), int64(1), object(2)
memory usage: 18.9+ KB
None

--> 10 vals delted after 

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 600 entries, 0 to 599
Data columns (total 4 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Order ID       590 non-null    float64
 1   Customer Name  600 non-null    object 
 2   Product        600 non-null    object 
 3   Quantity       597 non-null    float64
dtypes: float64(2), object(2)
memory usage: 18.9+ KB
None
'''