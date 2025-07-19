# a = [40,50,88,99,7,1,51]
# a.sort()
# print(a)

import pandas as pd
df = pd.read_csv("sales4.csv")
# print(df)
sort_data = df.sort_values(by="Product_Cost")
print(sort_data)