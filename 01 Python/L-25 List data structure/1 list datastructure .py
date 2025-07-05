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
'''
print("------------ Duplication values are allow --------------")
a = [10,20,30,40,10,20]
b = {10,20,30,40,10,20}
print("[10,20,30,40,10,20] is ",a,type(a)) # list can store duplicate vals
print("{10,20,30,40,10,20} is ",b,type(b)) # set can remove duplicate vals

print("------------ List data structure allow mutable --------------")
c = [10,20,30,40]               #[10, 20, 30, 40]
print(c)

c[0] = 99                       #[99, 20, 30, 40]
print(c)

print("------------ INDEX --------------")

d = [10,20,30,40]               #[10, 20, 30, 40]
print(d[3])                     #40
print(d[2])                     #30

print("------------ Add data in LIST --------------")

q = []                          # this is empty list
print(q)
print(type(q))

q.append(11)                       #[11]
q.append(22)                       #[11,22]
q.append(33)                       #[11,22,33]
q.append(44)                       #[11,22,33,44]

print(q)                        #

