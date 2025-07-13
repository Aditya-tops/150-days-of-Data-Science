'''
    Different between count() from pandas and pandas

    count()     -->     method      ->      str         python
                                            list
                                            tuple
  
    count()     -->     Method      ->      series      pandas

'''

# python count()
a = [10,2,0,30,10,40,50,60,70,10,10,20,50,40,10,75]
print(a.count(10))          # 5

# pandas count()
import pandas as pd
marks = [56,45,67,None,86,None,"aditya",None]
s = pd.Series(marks)
print(s.count())            # 4