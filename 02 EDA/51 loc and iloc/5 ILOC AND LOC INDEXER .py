'''
    1 creted a Dataframe

    select the data
    ---------------

            Top 5 rows        ->        df.head()
                              ->        by using loc & iloc

    a = [10,20,30,40]
    a[0]                # accessing value by using index
                        # Indexer

    LOC AND ILOC INDEXER
        1.EXAMPLE
        2.THEORY

    Suntax 1
    --------
        df.iloc[singlevalue]
        df.iloc[0]
    
        --> iloc cantake only interger value
        --> else typeError

    Suntax 2
    --------

        def.iloc[   LHS      ,       RHS        ]
        def.iloc[   rows     ,       columns    ]
        def.iloc[    :       ,       0          ]

    Suntax 3
    --------

        df.iloc[0:5]

        --> if comma sup you want specific column
        --> if no comma then you will get all columns

    Suntax 4
    --------

        def.iloc[        :       ,          :          ]
        def.iloc[       LHS      ,         RHS         ]
        def.iloc[       rows     ,       columns       ]
                     all rows            all cols


        --> if comma sup you want specific column
        --> if no comma then you will get all columns
'''
# select single row 
import pandas as pd

df = pd.read_csv("sales2.csv")
s = df.iloc[0]
print(s)
print("===============iloc==================")
df1 = pd.read_csv("sales2.csv")
s = df1.iloc[99]
print(s)
print("===============iloc==================")
df2 = pd.read_csv("sales2.csv")
s = df2.iloc[-1]
print(s)

print("================ Syntax-2 ================")
df = pd.read_csv("sales2.csv")
s = df.iloc[:,0]
print(s)
print("================ Syntax-2 ================")
df = pd.read_csv("sales2.csv")
s = df.iloc[0:15,0]
print(s)
print("================ Syntax-2 ================")
df = pd.read_csv("sales2.csv")
s = df.iloc[0:16,1]
print(s)

print("================ Syntax-3 ================")
df = pd.read_csv("sales2.csv")
s = df.iloc[55:60]
print(s)
print("------------------------")
s = df.head()
print(s)

# iloc is use for between records
# head() is start from 0

print("================ Syntax-4 ================")
df = pd.read_csv("sales2.csv")
s = df.iloc[:,:]
print(s)
print("================ Syntax-4 ================")
df = pd.read_csv("sales2.csv")
s = df.iloc[0:7,:]
print(s)
print("================ Syntax-4 ================")
df = pd.read_csv("sales2.csv")
s = df.iloc[0:5,:3]
print(s)
print("================ Syntax-4 ================")
df = pd.read_csv("sales2.csv")
s = df.iloc[50:55,:3]
print(s)