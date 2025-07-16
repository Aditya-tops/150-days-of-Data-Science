'''
    fillna :- we need to fill up some values in NaN
    but we are mosty use zero number only like fillna(0)



'''

import pandas as pd

df1 = pd.read_csv("fruits1.csv")
df2 = df1.fillna(0)

print(df1)
print()
print(df2)
print("--------------------------")
print(df2.astype(int))






