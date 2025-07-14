'''
    DataFrame
    ---------
    1. Access single column
    2. Access multiple columns
'''
'''
    1. Access single column
        --> we can access single column from dataframe
        --> there are two ways to access single columns
            1. By using dot notation(dot symbol)   :(
            2. By using index syntax               :)
        
            Dot Notation    

            -> dot notation works very well if columns name is
               single word
            ->dot notation will not work if columna name having space

            INDEX SYNTAX

            -> we can access single column from datafram by using index syntax
            -> this is good practice :))
'''
import pandas as pd

df = pd.read_csv("dummy.csv")
print(df.Product)
print("----------------------------------")
print(df["Product"])            # this is best way to access column

# 2. Access multiple columns

cols = ["Customer Name","Product"]
print(df[cols])

print("-------------------")
print(df["Quantity"].sum())           
print(df.Quantity.sum())           

# we are using list for speacifiy a column
