'''
    Function creating
        1. by using def keyword
        2. by using lambda keyword

    function using def       --->    Normal Function   100%
    Function using lambda    --->    Lambda function   5%

    function    def     usage :- Reusable component
                                 We can call any number of time
    Function    lambda           One time purpose

'''
# def
def aditya():
    print("hi")

aditya()
print(aditya) # <function aditya at 0x00000227631C1440>

print("----------------------")
# lambda  syntax :- var = lambda LHS : RHS
result = lambda x : x + 1
print(result) #  <function <lambda> at 0x000001BDE8FF3EC0>

result1 = lambda y : y + 1
print(result1) # <function <lambda> at 0x0000025FA6DECCC0>

# lambda is a keyword in python
# Lambda func is also called anonymous function 
# anonymous mean no name
# A func without a name called as anonymous function








