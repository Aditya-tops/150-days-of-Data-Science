# create grp of vals by using range() func
r = range(100,201)

for val in r:
    print(val)

print("-----------------------")
# creating Series by using range data type

import pandas as pd
a = range(100,201)
s = pd.Series(a)
print(s)

# if Series having more vals then by default it can display
# top 5 and bottom 5 vals