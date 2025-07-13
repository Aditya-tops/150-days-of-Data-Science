'''
    CREATE DATAFRAME
    ----------------

        1. single list
                    single column DataFrame
        2. Nested list
                    Dataframe, rows and columns
'''
# single list
import pandas as pd

a  = [10,20,30,40]
df = pd.DataFrame(a)

print(df)

'''
    0
0  10
1  20
2  30
3  40

--> Series cannot give name of the column
--> DataFrame can give by default name 0
'''

print("----------------------------------")
# Nested list
# A list inside list is called a nested list

a = [
        ["aditya",21],
        ["bony",17],
        ["kunal",14],
    ]
print(a)

df = pd.DataFrame(a)
print(df)
'''
[['aditya', 21], ['bony', 17], ['kunal', 14]]


        0   1 <--  name of the colomn
0  aditya  21   
1    bony  17   Data
2   kunal  14
^
|
index

'''

print("-----------------------------------")

name = ["aditya","dhwani", "bony", "kunal", "tony", "prisha"]
df = pd.DataFrame(name)
print(df)

'''
        0
0  aditya
1  dhwani
2    bony
3   kunal
4    tony
5  prisha
'''
print("-----------------------------------")


a = [
        ["aditya",20,10000],
        ["bony",21,20000],
        ["tony",25,110000],
        ["bunny",7,50000],
        ["gony",30,12200],
        ["kunal",25,23000],
        ["kunali",32,27000],
    ]
cols = ["Name","Age","Salary"]
inx  = ["a","b","c","d","f","g","h"]
df = pd.DataFrame(a,index=inx,columns=cols)
print(df)


print("--------------------------------")

d = {
        "name":["aditya","bony","tony"],
        "age" :[16,17,18],
    }

print(d)        # {'name': ['aditya', 'bony', 'tony'], 'age': [16, 17, 18]}
df = pd.DataFrame(d)
print(df)

'''
     name  age
0  aditya   16
1    bony   17
2    tony   18
'''
# if you are using dict keys behaves like name of the columns

