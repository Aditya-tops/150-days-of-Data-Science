'''
Terminolgy 
    def keyword
    name of the func
    parenthesis
    parameters
    colon symbol
    indentation
    bony of the function
    return statement

User defined function
    1. How to a create a function
    2. How to call function

    Functions: Naming conventaion

    A function can call another function

    IMP
    ---
        def aditya():
            print("hello")       <-- valid and highly recommented
        aditya()
    ------------------------------------------------------------'
    def ADITYA():
            print("hello")       <-- not valid and not recommented
        ADITYA()
    ----------------------------------------
    1. function without paramenter 

    def m1():
        print("no parameter")
    m1()
    ----------------------------------------
    2. function with paramenter 

    def m1(a):
        print("with parameter")
    m1(we shold privide value to a)
    ----------------------------------------

    def m1(a):
        print("Hello", a)
    m1(10)
    ----------------------------------------
    function with two para

    def add(a,b):
        print(a + b)
    add(10,20)
    ----------------------------------------
    function with three para
    def add(a,b,c):
        print(a + b)
    add(10,20,30)
    
    '''

def m1(a,b):
    print(a,type(a))
    print(b,type(b))
m1("aditya", 10)

print("--------- Func with two PARA ------------")

def gmail(u, p):
    if u == "aditya":
        print("Welcome to Gmail:", u)
    else:
        print("Invalid username")

user = input("Enter user name: ")
pwd = input("Enter password: ")

gmail(user, pwd)  
