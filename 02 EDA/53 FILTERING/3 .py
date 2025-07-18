import pandas as pd

df = pd.read_csv("sales4.csv")

con1 = df['Product_Name']  == 'iPhone 11'
con2 = df['Customer_Name'] == 'Nireekshan'

result = df[con1 & con2]
print(result)                   # [581 rows x 5 columns]