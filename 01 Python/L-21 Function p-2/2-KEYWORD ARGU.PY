'''
    Most IMP topic
    --------------
        1. Keywords
        2. Keyword arguments

    --> There is no relation in between abouve two topic
    
'''
def m1(a,b):
    print("First value is :- ",a)
    print("Second value is :- ",b)

m1(a = 10, b = 20)  # a = 10  <-- keyword args to pass vals

'''
def -> keyword
m1()->Name of the func
a,b -> Parameter
m1(a =10, b=20)-> keyword args to pass vals
'''
print("------------------------------------------")

def cart(product, price):
    print("Product is :- ",product)
    print("Cost is :- ",price)

cart(product="Pizza",price=20)

print("-----------------------------------------")

def m2(a = 50, b = 70):
    print("First value is :- ",a)
    print("Second value is :- ",b)

m2()

print("-----------------------------------------")

def m2(a = 50):  # a = 50 is old value
    print("First value is :- ",a)

m2(70) # this is new value

print("-----------------------------------------")










