'''
return
------
            --> return is a keyword in python
            --> we can apply only on two functions
                    1. Function
                    2. Method
Combinations
------------

        if       +    else        -->     Valid
        for      +    in          -->     Valid
        return   +    function    -->     Valid
        return   +    method      -->     Valid
        return                    -->     Invalid

    1.function ,no return
    ---------------------
    def balance():
        print("hello")
    balance()

    2.function + return
    ---------------------
    def balance():
        return -10

    b = balance()
    if b == 0:
        print("Balance is :",b)
    elif b < 0:
        print("Boss its negetive ,plz dep some money,otherwise some charges ",b)
    
'''

def balance():
    print("balance is :- ")
    return 100000

print(balance())
# this is valid but not recommented

print("-------------------------------")

def m1():
    print("Hi")
def m2():
    print("Hey")
    return 10
def m3():
    print("Hello")

m1()
a = m2()
print(a)
m3()

'''
m1()    -> Func call
        -> no,pera
        -> no return

m2(10)  -> Func call
        -> one para
        -> No return

m3()    -> Func call
        -> No para
        -> Having return

'''
print("-------------------------------")
a = "Hello"
b = len(a)
print(b)
'''
 --> FUNC CALL
 --> ONE PARA
 --> HAVING RETURN
'''
print("------IMPORTING INTERVIEW QUES--------------")

def m6():
    print("Hello")
    return 100

b = m6()
print(b)

print("-------------------------------")

def m66():
    print("heelo")

a = m66()
print(a)
# Answer is None Datatype
# function and method can return NONE data type

print("-------------------------------")

def m99():
    print("Hello")
    a = 1000
    return a

b = m99()
print(b)

print("---func is return One value----")
# func is return one value 

def a1():
    print("yoooooooo")
    a = 66
    return a

x = a1()
print(x)

print("----func is return two value----")
# if a func is retunning two vals the func call we need assing 2 variabls like x,y=function name  
def q1():
    print("hellu")
    a = 10 
    b = 20
    return a,b

x , y = q1()
print(x)
print(y)

print("----func is return three value----")
# if a func is retunning three vals the func call we need assing 3 variabls like p,q,r=function name  
def c1():
    print("hellu")
    a = 1000
    b = 2000
    c = 3000
    return a,b,c

p , q, r = c1()
print(p)
print(q)
print(r)

print("----interview question----")
# FUNC IS RETURNING 3 VALS
# THEN WE NEED TO ASSING FUNC CALL WITH 3 VLAS
# IF WE ASSIGN WITH ONLY ONE CARIABLE THEN VARIABLE BEHAVES LIKE TUPLE
def z1():
    print("hellu")
    p = 100000000
    q = 200000000
    r = 300000000
    return p,q,r

t = z1()
print(t)

print("--- A FUCNCTION CAN MULTIPLE VALUES ----")
'''
Counter question why tuple is here 

'''










