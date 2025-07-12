'''
    python  class

            1.string        Methods

            2.list          Methods
            3.tuple         Methods
            4.set           Methods
            5.dict          Methods
    
    --------------------------------------------

    pandas  class

            1.Series
                        1. Attributes (Instance Variable)
                        2. Methods

            2.DataFrame
                        1. Attributes (Instance Variable)
                        2. Methods

    Series
    ------
        -> It is predefined class having

                    1. Attributes
                    2. Methods

    Series Attrubute
    --------------- 
        -> Attributes return/giving information

'''

class Student:
    def __init__(self,name):
        self.name = name

s = Student("aditya")
print(s.name) # here name is Accessing Attributes
              # we can access objectname.attribute

'''
    Attribute
    --------
    
    --> we can access attribute by using object name,without parenthesis
    --> objectname.attributename

'''
import pandas as pd

a = [10,20,30,40]
s = pd.Series(a)
print(s)
print("----------------------------")
print("Get the data from s object?")
print(s.values)
# attrubete return informations
# values is pre-defiend class in pandas
# value 

'''
How to prove values is existing inside s object?
1. by usinf dir()
2. by using pandas DOcumentation
'''



