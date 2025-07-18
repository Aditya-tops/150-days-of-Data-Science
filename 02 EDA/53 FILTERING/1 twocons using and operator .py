import pandas as pd

df = pd.read_csv("sales4.csv")

con1 = df['Product_Cost'] > 50000
con2 = df['Product_Cost'] < 60000

result = df[con1 & con2]
print(result)               # [74794 rows x 5 columns]

'''
    kind info

    Python      -->     and operator
    Pandas      -->     & symbol
'''