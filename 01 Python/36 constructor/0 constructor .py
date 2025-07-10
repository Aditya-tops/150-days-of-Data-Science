'''
    constructor
    -----------
        --> constructor is special kind of method
        --> we can create a constructor by using def keyword

        --> def is keyword 
                1. we can create a function
                2. we can create a method
                3. we can create a constructor
    
        --> def
                1. Function
                2. Method
                3. Constructor

        --> method name can be anything
            m1(), m2(), m3()......

    --> Constructor name SHOULD BE,
            __init__(self)

    --> Purpose: To create instance variables
                        or
                Initialization purpose

'''
class Student:
    def __init__(self):
        print("Hello")

s = Student()
# during object creation constructor will execute
# by default __init__ is execute
# we no need to call constructor

class Student:
    def __init__(self):
        print("Constuructor")
    
    def display(self):
        print("Method")

s = Student()           # Constuructor
#s.display()             # Method

# method we need to call explicitely
# constructor will execute automatilly during object creation
