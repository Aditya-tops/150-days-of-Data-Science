import pandas as pd

df = pd.read_csv("sales2.csv")
print(df)

print("----------------------")
# i want to remove bydefault index 
# add index to Customer id

df.set_index("Customer id",inplace=True)
print(df)