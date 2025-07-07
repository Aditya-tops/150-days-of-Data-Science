'''
    Tuple
    -----
        1. CREATE       -   (),tuple()
        2. STORE        -   same/diff type of vals
        3. ORDER        -   Insertion or der is fixed
        4. SIZE         -   size is not dynamic(bez tuple hv immutable)
        5. DUPLICATES   -   tuple can store duplicates
        6. Immutable    -   tuple having immutable nature
        7. INDEX        -   tuple can use index to store val
        
        mutable --> can be change
        Immutable --> can not be change

'''
print("----------Creating Tuple----------")
a = (10,20,30,40,10.5,40.5,"aditya",True)
print(a)
print(type(a))

print("----------Creating duplicate----------")
b = (10,20,30,10,10,10,10)
print(b)

print("----------List change data type but tuple cant----------")

aa = [10,20,30]
aa[0]=55
print(aa) # [55, 20, 30]

#bb = (10,20,30)
#bb[0]=55
#print(bb) 
'''
  bb[0]=55
    ~~^^^
TypeError: 'tuple' object does not support item assignment
'''
print("----------Index----------")

tup = (10) # 10
print(tup)
print(type(tup)) # <class 'int'>
# 
tupp = (10,) # 10
print(tupp)
print(type(tupp)) # <class 'tuple'>
# A single val tuple should end with comma separator

print("------------------------------------")
c = 10,20,30,40,50
print(c)
print(type(c))
print("------------------------------------")
def m1():
    print("Hi")
    return 10,20,30

a,b,c = m1()
print(a)
print(b)
print(c)
# function can return multiple  values
# if we assign with single variable the it is tuple


# we can convert tuple to list, can change the value then later vonver into tuple agin

               # Original tuple is printed



num = (10, 20, 30, 40)  # Original tuple
num_list = list(num)    # Convert to list
num_list[0] = 99        # Modify the value
num = tuple(num_list)   # Convert back to tuple
print(num)              # Print the modified tuple

