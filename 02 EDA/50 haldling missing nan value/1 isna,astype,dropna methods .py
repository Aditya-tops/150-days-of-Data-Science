# dropping missing values
# converting into float to int
import pandas as pd

data = pd.read_csv("fruits1.csv")
print(data.columns)
print("--------------------------------")
print(data.shape)
print("--------------------------------")

del_missing_vals = data.dropna()  # its deleted missing values data
print(del_missing_vals)

print("----------------------------------------")

print(data.isna().sum())
print(del_missing_vals.isna().sum())
print(del_missing_vals.astype(int)) # astype is use for values convert float to int
