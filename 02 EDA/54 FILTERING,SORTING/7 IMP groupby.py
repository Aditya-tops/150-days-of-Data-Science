'''
    Steps in groupby() method
        1. Splitting the data
        2. Applying an operation
        3. Combining the result

    Very IMP points
    ---------------
    
    --> groupby() method returns GroupBy object
    
    --> df.head() method returns DataFrame 
    --> df.tail() method returns DataFrame
    
    --> map() Function returns (giving result as) map object
    --> filter function rerurns (giving result as) filter object

    --> groupby() method return GroupBy object
    
'''

import pandas as pd
d = {
        "Product": ["Samsung","Nokia","Samsung","Motorola","Nokia","Samsung","Samsung"],
        "Order"  : [2,4,3,4,6,7,3]
    }

df = pd.DataFrame(d)
print(df)
print("----------------------------------------")

result = df.groupby("Product")
# print(result)       # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000020B895206E0>

final_result = result.sum()
print(final_result)