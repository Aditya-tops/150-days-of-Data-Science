'''
    --> Comma Separated value
    --> sales1.cvs

    ----------------------------------------------

    sales1.cvs      -->     pandas      -->     DataFrame
'''
import pandas as pd

df = pd.read_csv("sales1.csv")
print(df)

print("-------------------------------------------------")

# here is read_csv is function
print(pd.read_csv)          # <function read_csv at 0x000001AB05A67CE0>