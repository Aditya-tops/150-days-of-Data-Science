import pandas as pd

vdata = pd.read_csv("sales1.csv")
odata = vdata.tail()

print(odata)