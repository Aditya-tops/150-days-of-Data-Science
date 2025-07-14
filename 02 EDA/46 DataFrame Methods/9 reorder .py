import pandas as pd

df = pd.read_csv("dummy.csv")
print(df[["Product", "Customer Name", "Quantity", "Order ID"]])
 