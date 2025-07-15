import pandas as pd

'''
sales3csv   -->     Dataflame
            -->     5 cols

Reanaming name of the columns
    1. single column
    2. multiple column
'''
# 1. single column
old_data = pd.read_csv("sales3.csv")
d = {
        "ord id":"Order Id"
    }
new_data = old_data.rename(columns=d)    # columns=d is keyword args
print(new_data.head())

print("------------------------------------------")
# chaing multple columns name
old_data = pd.read_csv("sales3.csv")
d = {
        "ord id":"Order_Id",
        "cust name":"Customer_Name",
        "cust id":"Customer_ID",
        "prod name":"Product_Name",
        "prod cost":"Product_Cost",
    }
new_data = old_data.rename(columns=d)    
print(new_data.head())
