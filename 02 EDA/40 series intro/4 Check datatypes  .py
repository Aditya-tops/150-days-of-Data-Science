import pandas as pd

a = [10,20,30,40]
s = pd.Series(a)
print(s)
print("-------------------------")

a = [1.23,20.45,30.55,40.55]
s = pd.Series(a)
print(s)
print("-------------------------")

a = ["aditya","bony","honey","bunny"]
s = pd.Series(a)
print(s)
print("-------------------------")

a = [1.23,"bony",True,10]
s = pd.Series(a)
print(s)
print("-------------------------")
