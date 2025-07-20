'''
    --> Groupby is very common operation
    --> Based on gernder, location, education(Gard, PG) etc

    GroupBy
    -------

    --> Operation1: Splitting the data 
    --> Operation2: Applying an operation
    --> Operation3: Combine the result

    IMP Point
    ---------
    -> GroupBy method return groupby object

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