'''
    Series
        class

            1. Attribute    ->  Return information
            2. Methods      ->  Perform an operator

    Methods in series class
    -----------------------
    --> series class contains methods
    --> these methods perform an operations
'''
import pandas as pd
a = [10,20,30,40,50,60,70,80,90,100]
s = pd.Series(a)

print(s.head())    # head method by default return top 5 values
print(s.head(8))   # head method return top  values




