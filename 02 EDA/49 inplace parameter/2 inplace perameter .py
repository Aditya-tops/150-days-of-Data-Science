# i dont want new object  i want to perform changes on existing object
# then we need to use inplace parameter
import pandas as pd

data = pd.read_csv("sales3.csv")
d = {
        "ord id":"Order_Id",
        "cust name":"Customer_Name",
        "cust id":"Customer_ID",
        "prod name":"Product_Name",
        "prod cost":"Product_Cost",
    }

data.rename(columns=d,inplace=True)
print(data.head())