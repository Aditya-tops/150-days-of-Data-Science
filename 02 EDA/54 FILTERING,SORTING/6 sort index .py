import pandas as pd

d = {
        'Order id' : [11,21,31],
        'Customer name' : ["kedar","nireekshan","aditya"],
        'Order id' : ["iphone 11",'htc','macbook'],
    }

i = [777,666,222]

df = pd.DataFrame(d,index=i)
print(df)
print("------------------------------")
df1 = df.sort_index()
print(df1)