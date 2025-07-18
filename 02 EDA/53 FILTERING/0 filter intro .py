'''
    Data:   1,23,4,5,6,7,8,9,10

            
    filter1:1,2,3,4,5       -->     value<6
    filter2:7,8,9,10        -->     value>6
    filter3:4,5,6,7,8       -->     x>3, 9>x

    --> we can use filter 

            - By using relational operators
                    - single condition
                    - multiple condition

            - By using loc & iloc indexers 

'''
import pandas as pd

df = pd.read_csv("sales4.csv")
# print(df)

# filtring data by using single conduction
con = df["Product_Cost"] == 65000       # [19054 rows x 5 columns]
print(df[con])

con = df["Product_Cost"] > 65000        # [112280 rows x 5 columns]
print(df[con])



