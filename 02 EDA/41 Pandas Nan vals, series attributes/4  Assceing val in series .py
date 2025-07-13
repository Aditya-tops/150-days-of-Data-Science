import pandas as pd

a = [10,20,30,40]
i = ["a","b","c","d"]
s = pd.Series(a, index=i)
print("Created Series object: s")
print("Get the data from s object")
print()
print(s.values)
print("--------------------------")
print(s.index)