# recap last session
# rename method always create new object
import pandas as pd

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
'''
--> we can rename cols name in dataframe
--> we can rename columns name by using rename() method
--> rename() method will cretae new object with updates
--> separate memory allocation is done for new object

 # I dont want new objce, i wanted to perform changes on
   existing object then we need to use inplace
'''
print("-------------------------------")
print("-------------------------------")

# 2 inplace.py