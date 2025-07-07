'''
    []      -->        list
    ()      -->        tuple
    {}      -->        set      -->     dict



    Set
    --- 
            1. CREATE           -       {} with vals, set()
            2. STORE            -       same,diff type of vals
            3. SIZE             -       increase dynamically
            4. INSERTION ORDER  -       not fixed
            5. DUPLICATE        -       set cannot store
            6. MUTABLE          -       set having mutable nature
            7. INDEX            -       set cannot follow indexing
            
    ---> we can create empty set by set() predefined function

'''


a = {10,20,30}
print(a)                        # {10,20,30}
print(type(a))                  # <class 'set'>
# INSERTION ORDER IS NOT FIX
print("---------------------------------")
a = {10,1.23,"aditya"}
print(a)                        # {10,1.23,"aditya"}
print(type(a))                  # <class 'set'>
print("----------INSERTION ORDER----------")
a = [10,20,30,40]
b = (10,20,30,40)
c = {10,20,30,40}
print(a)                        # [10,20,30,40]
print(b)                        # (10,20,30,40)
print(c)                        # {40, 10, 20, 30}
print("--------------DUPLICATE-----------")
a = [10,20,30,10,1,10,10]
c = {10,20,30,10,1,10,10}
print(a)                        # [10, 20, 30, 10, 1, 10, 10]
print(c)                        # {1, 10, 20, 30}
print(len(a))                   #  7
print(len(c))                   #  4

print("-------------MUTABLE----------------")
a = {10,20,3,40,50,60}
print(a)                        # {50, 3, 20, 40, 10, 60}
a.add(99)   
print(a)                        # {50, 3, 20, 99, 40, 10, 60}

print("------------------------")
a = [ 10,20,30,40]
b = set(a)
print(b)                        # {40, 10, 20, 30}

print("------------RANGE------------")
a = range (10,15)
b = set(a)
print(b)                        # {10, 11, 12, 13, 14}
print("-----------Empty Set--------------")

a = []
b = ()
c = {}
d = set()   
print(a)                        # []
print(b)                        # ()    
print(c)                        # {}
print(d)                        # set()               
print(type(a))                  # <class 'list'>
print(type(b))                  # <class 'tuple'>
print(type(c))                  # <class 'dict'>
print(type(d))                  # <class 'set'>
# we can create empty set by set() predefined function






