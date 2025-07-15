'''
--> this topic is v IMP 
--> recap  about last session with one example
'''
#  we can rename columns name in datafrme
# we can rename cols names by usnig rename() method
# rename() method will cretae new object new object with updates
# Separate memory allocation is done for new object

# i dont want new object  i want to perform changes on existing object
# then we need to use inplace parameter
import pandas as pd

df = pd.read_csv("sales3.csv")
print(df.head(3))
print("----------------------------")
d = {
        "ord id":"Order_Id",
        "cust name":"Customer_Name",
        "cust id":"Customer_ID",
        "prod name":"Product_Name",
        "prod cost":"Product_Cost",
}

data = df.rename(columns=d)
print(data.head(3))

