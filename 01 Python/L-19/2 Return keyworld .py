'''
    --> return is keyword in python
    --> program by using return keyword : you shold use func topic

    valid combinations
    ------------------

    for     +   in      -->     Valid
    return  +   func    -->     Valid
    for                 -->     Invalid

    print("hello")
    return 100        Invalid Syntax error

    func   --> no return
    func   --> having return

'''
# Func with out return
def balance():
    print("My balance is :- ")
balance()

print("--------------------------")
# func with return state
def bal():
    print("My balance is :- ")
    return 100000
b = bal()
print(b)
# IMP note :- if a function contain return statement that function calling u need to assing into variable

print("---------for int value--------------")

def c1():
    print("hello")
    return 10

a = c1()
print(a)

print("---------for float value-------------")

def d1():
    print("hello")
    return 10.50

d = d1()
print(d)

print("---------for string value-----------")
def m5():
    print("aditya")
    return "patel"
x = m5()
print(x)

'''
    Que Why fuinction calll we call we need to assign into a variable?
    --> By using WE CAN BUSINESS LOGIC (Re-using Code)

    Que What is BUSINESS LOGIC?

'''
print("--------- BUSINESS LOGIC 1 --------------")
def jamarashee():
    return 0

money = jamarashee()
if money == 0:
    print("your balace is",money)

print("--------- BUSINESS LOGIC 2 --------------")
def jamarashee1():
    return -100

money2 = jamarashee1()
if money2 == 0:
    print("your balace is",money2)
elif money2 < 0:
    print("Boss your balance is negative" , money2)

print("--------- BUSINESS LOGIC 3 --------------")
def jamarashee3():
    return 1000000

money3 = jamarashee3()
if money3 == 0:
    print("your balace is",money3)
elif money3 < 0:
    print("Boss your balance is negative" , money3)
else:
    print("Hoorreeyy your balance is ", money3)






