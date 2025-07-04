'''
    A function can call another function
'''

def aditya():
    print("hello")
    bony()

def bony():
    print("hi")

aditya()

print("--------------------------------------")

def m1():
    print("first function")
    m2()
def m2():
    print("two function")
    m3()
def m3():
    print("third function")

m1()