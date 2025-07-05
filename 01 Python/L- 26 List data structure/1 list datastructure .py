'''
    --?   Why we learn about data structures?
    -->  Companies are generating the --> DATA

    COIN     =      H              +   T
    DATA     =     Store the data  +   Process the data
             =     [10,20,30,40]   +   min val 10
                                       max val 40
                                       sum     100
                                       length  4

    Python Data Structure
    ---------------------
        1. List Data Structure
        2. Tuple Data Structure
        3. Set Data Structure
        4. Dictionary Data Structure
    
    1.List Data Structure
    ---------------------
        Real time operation

    Data Structure :- If you wanted to store,
                      a group of individual values,
                      in a single entity/object,
                      then you should go for data structures.
    Normal Def :-
        --> 5 years old
        --> Mother, getting ready to go veg market
        --> getting ready...
        --> carry BAG(BIG), folding, folding.....small
        --> Shop-1
            ------
                -> Potato   -  1kg
                -> Tomoato  -  1kg
                -> Onions   -  1kg

            --> Carry bag is data structure

        C         U           R            D
        Create    Update      Retrive      Delete  

    
    -->  CREATE             ->   [],list()
    -->  STORE              ->   Same, diffrent data
    -->  SIZE               ->   Size increases dynamically
    -->  INSERTION ORDER    ->   Fixed
    -->  DUPLICATIOn        ->   List can store duplication vals
    -->  INDEX              ->   list can use index to store vals

    List Comprehension
    ------------------
'''
a = ""
b = []

print(a)                        #
print(b)
print()
print(type(a))                        #
print(type(b))                        #

aa = [10,20,30,40,10,10,10]
bb = {10,20,30,40,10,10,10,1,True}
print(len(aa))
print(len(bb))


r = range(10,20)
lst = list(r)
print(lst)

'''
    List having mutable nature

    Once list is created then

        1. adding a value    ->      valid
        2. delete a value    ->      valid
        3. replace a value   ->      valid

    Accessing values from list
        1. Index  --> The position of value where it stores
        2. Slicing
        3. for loop   *** mostly use
'''

f = [10,20,30,40,60,60,40,50,80]
print("INDEXING")
print(f[2])
print(f[5])
print(f[-3])
print(f[-1])
print("SLICING")
print(f[0:3])
print(f[2:5])
print(f[-7:-1])
print("For loop")
for val in f:
    print(val)
print("---------Taking multple value in runtime----------")
num = []

for val in range(3):
    i = int(input("Enter value :- "))
    num.append(i)

print(num)

print("------------List Comprehension----------")

'''
Method in list DATA STRUCTURE
    Method in str class

    Method in list class
    Method in tuple class
    Method in set class
    Method in Dict class

    Method in Series class
    Method in DataFrame class

    Method in LinearRegrsession class

    1. list is predefined class
    2. class contains methods
        class
            mehtod

        humanbody
            hear()
            brain
'''
print("----list is predefined class-----")
vals = [10,20,3,4,0]
print(type(vals))   #<class 'list'>
print("----2. class contains methods-----")







