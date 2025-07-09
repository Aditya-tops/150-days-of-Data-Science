'''
    class
    -----
        -> Impoetance of the class
        -> a class is a specification of property and action objects
            class -> idea implemented -> object
        -> class is a model to create an object
            --> class doesnot exist physically
            --> object exist physically

        just denifition
        ---------------
                                Template
                                --------
            class                           Purpose

                1. constructor              Initiazation or
                    1. Zero para            Create instance variable
                    2. Para
                    2. variables            To represent the data
                    1. Instance var
                    2. static var
                    3. local var
                3. methods                  To perform an action
                    1. Instance
                    2. static
                    3. class

''' 
a = 10
b = 1.23
c = True
d = "aditya"
e = [10,20,30,40]
f = (10,20,30,40)
g = {10,20,30,40}
h = {101:"aditya",102:"raju"}

def aditya():
    print("hello")

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(aditya))         # <class 'function'>

print("---------------------------------------------------")

class Student:
    print("hello") # below brogram is valid but not much important

