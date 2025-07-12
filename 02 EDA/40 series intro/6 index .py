# index means the position of val where it stores
# index is assigned to everyvals
# generic name of an index is an axis
# index is starts from 0,1,2,3,4,....,ect
# base on requirements we can customise this index
# these are called as axis labels

'''
    Q can i change the index in series?
    A Based on requirement we can do that :))

    for example

'''
import pandas as pd 
a = [10,20,30,40,50]
inx = [11,22,33,44,55]    # this our index number
s = pd.Series(a, index= inx)
print(s)

# while changing the index, data length and index length
# should be match, otherwise we will get an error