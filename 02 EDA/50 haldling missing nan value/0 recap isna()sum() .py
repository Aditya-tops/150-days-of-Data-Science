'''
    recap
    -----
        1. Data(.csv)
        2. DataFrame
        3. Apply some basic operations(shape, columns, head(), tail() etc)
        4. Checking missing values in DataFrame 
            
            During check

            if DataFrame having no missing values
                    No need to do anything
            If DataFrame having missing values
                    Then we need to handle

                    df
                    df.isna().sum()

'''     
import pandas as pd

data = pd.read_csv("fruits1.csv")
missingdata = data.isna().sum()
print(missingdata)


'''
    1.  data
    2.  df
    3.  df.isna()
    4.  df.isna().sum()
    5.  df.dropna()
    6.  df.dropna(inplace = True)
    7.  df.astype(int)
    8.  df.fillna(p)
    9.  df.fillna(df["Age"].mean())
    10. df.replace(p1,p2)
'''