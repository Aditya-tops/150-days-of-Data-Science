'''
    DataFrame Attributes
    --------------------

    --> df is a predefined class
    --> df
            1.Attribute ->  Giving information about object
            2.Methods   ->  Perform an operation
'''
import pandas as pd

df = pd.read_csv("sales1.csv")
print(len(df))                  # 600