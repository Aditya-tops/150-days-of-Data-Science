import pandas as pd 

v = [145,142,38,13]
i = ["A","B","C","D"]
s = pd.Series(v, name='counts',index=i)
print(s)