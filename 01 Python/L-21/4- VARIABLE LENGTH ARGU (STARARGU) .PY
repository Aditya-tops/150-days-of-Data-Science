'''
    * args or Variable length arguments
    -----------------------------------

    --> *arguments / *args
    --> Variable length args
    
'''
'''
def shopping(p1,p2):
    print("first product price ", p1)
    print("first product price ", p2)

shopping(888,999,444,666,777)
# TypeError: shopping() takes 2 positional arguments but 5 were given
# kushma shoping :- how to fix this problema
# this proble is solve by varable lenth args
'''

def shopping(*p):
    print("All prices :- ",p)
shopping(777,888,999,888,111)

# output is in tuple data structure
print("-----------------------------")
# i want perform some operation

def shopping1(*p):
    print("All prices :- ",p)
    print("Total bill is :- ",sum(p))
shopping1(777,888,999,888,111)







