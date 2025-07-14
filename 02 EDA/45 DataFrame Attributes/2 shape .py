import pandas as pd

data = pd.read_csv("sales1.csv")
print(data.shape)                        # (600, 4)
print(data.shape[0])                        # 600
print(data.shape[1])                        # 4

# shape is use for show total number of row & column
