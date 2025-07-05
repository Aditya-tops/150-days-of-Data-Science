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
    
        
'''
# -->  CREATE   ->   [],list()
print("------------ [],list() --------------")
a = [10,20,30,40]
print("[10,20,30,40] is ",type(a))

print("------ Checking all data type -------")
b = [10,20.22,True,'aditya']
print("[10,20.22,True,'aditya'] is ",type(b))

for i in b:
    print(type(i))

print("---- Size increases dynamically -----")
from sys import getsizeof
c = [12,13,30,40]
print(getsizeof(c))
f = [12,13,30,40,50]
print(getsizeof(f))
i = [12,13,30,40,50,60]
print(getsizeof(i))

print("------ INSERTION ORDER(Order Sequesnce follw) -----")

u = [10,20,30,40]
v = {10,20,30,40}

print("List Data Structure :- ",u)
print("Dict Data Structure :- ",v)


