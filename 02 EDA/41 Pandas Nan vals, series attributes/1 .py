'''
    ACESSING VALS FROM SERIES
        1. By using index
        2. for loop

        3. Based on condition (filtring data)
        4. By using loc & iloc
'''
import pandas as pd

v = [14000,20000,50000,90000]
inx = ["nokia","samsung","apple","chiku"]
s = pd.Series(v, name="makes",index=inx)

print(s)
print("--------- accessing val -----------")

print(s[0])
print(s[1])
print(s["chiku"])

print("----------- for loop -----------")

for i in s:
    print(i)

print("----------- for loop in index -----------")

for q in inx:
    print(q)