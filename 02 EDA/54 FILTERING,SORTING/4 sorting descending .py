import pandas as pd
df = pd.read_csv("sales4.csv")
sort_data = df.sort_values(by="Customer_Id",ascending=False)
print(sort_data)