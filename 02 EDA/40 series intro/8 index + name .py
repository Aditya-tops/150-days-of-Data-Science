import pandas as pd 

v = [14000,15000,38000,13000]
i = ["nokia","samsung","Oppo","iphone6"]
s = pd.Series(v, name='counts',index=i)
print(s)