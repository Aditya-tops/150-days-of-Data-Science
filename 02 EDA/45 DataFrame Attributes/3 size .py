# size attribute using for show number of elements/values in df

import pandas as pd

data = pd.read_csv("sales1.csv")
print(data.size)                    # 2400
# 600 row x 4 columns


print("Number of elements in dataframe",data.size)
print("Number of elements in dataframe",data.shape[0]*data.shape[1])
