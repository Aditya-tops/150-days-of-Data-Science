import pandas as pd
marks = [10,10,20,10,10,20,34,1,5,40,10]
s = pd.Series(marks)
print(s.unique())         # [10 20 34  1  5 40]
print(s.nunique())        # 6