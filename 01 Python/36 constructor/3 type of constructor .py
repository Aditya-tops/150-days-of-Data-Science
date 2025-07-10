'''
    Type of Constructors
    --------------------
        1. Zero parameterized constructor
        2. Parameter with parameter

    Use of Constructors
    -------------------
        1. to create a variable

'''
# 0.Zero Constructors
class Student:
    def __init__(self):
        print("Zero Para")
s = Student()
print("-------------------------------------------------------------------------")


# 1. Parameter Constructors
# if Constructors having one parameter 
# then while creating an object we need to pass one val

class Student1:
    def __init__(self,sno):
        self.sno = sno                       # Local variable
        print("Student number is : ", self.sno)

s = Student1(10)              
# Student number is :  10

print("-------------------------------------------------------------------------")

# two para
class Student2:
    def __init__(self,sno,name):
        self.sno = sno                       # Local variable
        self.name = name                       # Local variable
        print("Student number is : ", self.sno)
        print("Student name is : ", self.name)


s = Student2(550,"aditya")              
# Student number is :  550
# Student name is :  aditya

print("-------------------------------------------------------------------------")

# three para
class Student3:
    def __init__(self,sno,name,address):
        self.sno = sno                       # Local variable
        self.name = name                       # Local variable
        self.address = address                       # Local variable
        print("Student number is : ", self.sno)
        print("Student name is : ", self.name)
        print("Student address is : ", self.address)


s = Student3(777,"bony","KBHK")              
# Student number is :  777
# Student name is :  bony
# Student address is :  KBHK

print("-------------------------------------------------------------------------")

