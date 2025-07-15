'''
we can rename columns in DF in two ways
    1. by using rename() method
    2. by using columns attribute
'''
import pandas as pd

df1 = pd.read_csv("sales3.csv")
print(df1.columns)
print("---------------------------------------")

df1.columns = ["order_id","customer_name",
               "customer_id","product_name","product_cost"]
print(df1.head())

print("------------------------------")
'''
    can we know length of this sales file?
    -> yes
        1. len() func
        2. df.shape
'''
print(df1.shape)


