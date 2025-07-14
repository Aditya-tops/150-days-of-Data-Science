# this method giving statistical information about the DataFrame
import pandas as pd

df = pd.read_csv("dummy.csv")
print(df.describe())

'''
            Order ID    Quantity
count     590.000000  600.000000
mean   167127.516949    1.491667
std       162.188227    0.705285
min    166846.000000    1.000000
25%    166987.250000    1.000000
50%    167124.500000    1.000000
75%    167268.000000    2.000000
max    167409.000000    5.000000

'''