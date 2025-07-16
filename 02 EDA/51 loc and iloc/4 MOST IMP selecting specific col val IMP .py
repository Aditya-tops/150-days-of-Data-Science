# Access all veeru recods
# veeru  29 times he done shopping
# value is True we get result
# if our conditions is wrong then we get empty dataframe
import pandas as pd
df = pd.read_csv("sales1.csv")
# print(df["Customer Name"] == "Veeru") ---> relational operator always give boolean value

condition = df["Customer Name"] == "Veeru"
print(df[condition])
print(df[condition].shape)  # (29, 4)

print("=============================================")
print("Les's access Lavanya dataframe")
print()

con = df["Customer Name"] == "Lavanya"
print(df[con])
print(df[con].shape)          # (31, 4)

print("=============================================")
# i want to access total iphone11 records
print()

con = df["Product"] == "iPhone 11"
print(df[con])
print(df[con].shape)          # (29, 4)

print("=============================================")
#  2 conditions 1 veeru record and 2 iphone 11 

condition = (df["Customer Name"] == "Veeru") & (df["Product"] == "iPhone 11")
print(df[condition])
print(df[condition].shape)


