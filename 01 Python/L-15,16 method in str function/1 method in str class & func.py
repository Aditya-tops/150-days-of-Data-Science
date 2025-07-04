'''
    Method in str class

        1.str in predefined
        2.class contains methods


    1.str in predefined


    2.class contains methods

'''
# 1. Procedure oriented approach
# write a program by using Procedure

print("Hello")
print("Good evening")

# 2. Function oriented approach
# w a p by using func
''' 
    function
            1. How to create a func
            2. How to call a func

    --> we can create a func by using def keyword

'''

def RHS():
    print("Hello")
    print("Good night")

RHS()


def aditya():
    print("i m aditya")
    print("working in google")
def bony():
    print("i m bony")
    print("working in apple")
def kunal():
    print("i m kunal")
    print("working in Infosys")

aditya()
bony()
kunal()

'''
3. Object Oriented Program
    1.how to create a class
    2.how to create a methods inside of the class
    3.how to create a an object to a class
    4.how to call a method

    class
        method1()      -->     To perform an operation 
        method2()      -->     ... 
        method3()      -->     ...

        NOTE :- if a class contain method method should not call directly
                we need to create a object to the class
                how to create a object LHS=RHS
'''

class aditya:
    def teaching(self):
        print("i like traching very well")

a = aditya()        #  <---- this is object
a.teaching()        #  <---- object name dot method name

'''
        Point to be Noted
        -----------------
            class           -->     Keyword in python
            aditya          -->     Name of the class
            def             -->     Keyword in python
            teaching        -->     Name of the method
            a = aditya()    -->     Object creation
            a               -->     Name of the object
            a.teaching()    -->     calling method

    ---> WE CAN CALL METHOD BY USING NAME OF THE OBJECT
'''
print("-------------------------------------------------------------")
class school:
    def staff(self):
        print("hello")
        print("Pls dont use in school")
        print("Arrey Aditya we like using phone in class")

teachers = school()
teachers.staff()
print("-------------------------------------------------------------")

class bony:
    def coding(self):
        print("At night")
    def gym(self):
        print("gym time")
    def pating(self):
        print("")
    def ss(self):
        print("scrolling time")

b = bony()
b.gym()
b.pating()
b.ss()

'''
    dir() function
    --------------
        --> Predefing function
        -->By using this we can find number of methods in class

            1.with userscore symbol methods       not imp
            1.without userscore symbol methods    imp

'''

car = "hondacivic"
print(car)

print(car.upper())     # here UPPER is a method

