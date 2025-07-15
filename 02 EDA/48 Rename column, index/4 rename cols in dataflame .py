'''
    rename cols in df
    -----------------
        1. by using rename() method 
        2. by using cols attribute

    How to change index or rename index in a df 
'''
import pandas as pd

d = {
    "order_id": [11, 22, 33],
    "customer_name": ["aditya", "bony", "kunal"],
    "product": ["iphone", "HTC", "Macbook"],
}

i = {0: 77, 1: 88, 2: 99}

df1 = pd.DataFrame(d)
df2 = df1.rename(index={1: 88})

print(df1)
print("-----------------------")
print(df2)
