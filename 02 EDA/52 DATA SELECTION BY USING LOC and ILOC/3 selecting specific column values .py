# create dataframe loading csv file
# select  Veeru from exsting DataFram
import pandas as pd

df = pd.read_csv("sales1.csv")
print(df)

cust_name = df["Customer Name"] == "Veeru"
print(df[cust_name])
shopping = df[cust_name].shape
print(shopping)

# select Macbook Pro Laptop Customer
product_name = df["Product"] == "Macbook Pro Laptop"
print(df[product_name])

