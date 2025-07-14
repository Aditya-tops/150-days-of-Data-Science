import pandas as pd

data1 = pd.DataFrame()
data2 = pd.read_csv("sales1.csv")


print("Created DataFrame: df")
print("Check either its empty or loaded with data")

print()
print(data1.empty)           # True
print(data2.empty)          # False

'''
data1 = pd.dataframe()
        --> Object creation
        --> no return statement

data2 = pd.read_cvs("sales1.csv")
        --> function calling
        --> having return
'''