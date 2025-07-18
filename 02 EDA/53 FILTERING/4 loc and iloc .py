import pandas as pd

df = pd.read_csv("sales4.csv")

con1 = df.Product_Name  == "iPhone 11"
con2 = df.Customer_Name == "Shahid"

result = df.loc[con1 & con2]
print(result)                   # [594 rows x 5 columns]