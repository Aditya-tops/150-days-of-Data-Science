'''
    --> set is predefined class
    --> class contains methods
    --> To see the methods, dir() function
    
    dir()
        1. with userscore symbol methods
        2. without userscore sysbol method
'''
print("------METHOD IN SET CLASS---------")

import builtins as b
print(dir(b))              
# to display all predefined methods, class etc....

'''
    add() method
    add() is predefined METHOD in set class
    We should ACCESS this method by using set object
    By using this method we can add value to set

    IMP set methods
    --------------
        1. add()
        2. clear()
        3. remove()
'''
a = [10,20,30,40]
b = {10,20,30,40}

print(a)
print(b)
a.append(99)        # append is for append if use add u got error
b.add(99)

print(a)            # [10, 20, 30, 40, 99]
print(b)            # {99, 40, 10, 20, 30}

print("------------------------------")

a = [10,10,10,10]
b = {10,10,10,10}
print(a.count(10))
# print(b.count(10))      # AttributeError: 'set' object has no attribute 'count'

print("------------------------------")

a = {10,20,1,True,1}
print(a)                  #{1, 10, 20}

print("----------remove-------------")
a = {10,20,30,40}
a.remove(20)
print(a)                   # {40, 10, 30}

print("------------clear()----------")
a = {10,30,30,40,40,50,60,70}
a.clear()
print(a)                   #set()

print("------------------------------")
a = {10,20,30,40}
val = 10

if val in a:
    print("Existing",val)
else:
    print("Not Existing",val)

# Existing 10

print("---------set comprehensions-----------")
'''
    syntax
    ------
        LHS = RHS
        var = {part1    part2   part3}
        part1 = variable/expression
        part2 = for loop
        part3 = condition(optional)
        result = {variable/expression   for loop    conditions}
                            or
        result = {  variable/expression   
                    for loop    
                    conditions
                  }
                
'''
values = [10,20,30,40,50]
result = [val+2  for val in values]
print(result)                   # [12, 22, 32, 42, 52]
print("------------------------------")
a = [10,10,20,10,10]
b = set(a)
print(b)                        # {10, 20}


