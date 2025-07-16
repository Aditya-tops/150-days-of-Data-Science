import pandas as pd

data = pd.read_csv("fruits1.csv")
data.dropna(inplace=True)

print(data)