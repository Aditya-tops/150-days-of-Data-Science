'''
    print = (object.methodname())

    Method
    ------  
        1. count
        2. append
        3. insert
        4. remove
        5. reverse
        6. sort
        7. 
        8.

        Math operatiors
        ---------------
            +   ->  add over number
            *   ->  mul over numbs

            +   ->  concatenating/joining two lists
            *   ->  REPEATING THE VALS IN LIST

'''
print("---------------count--------------------")
a = [10,20,30,40,50,10,10,10]
print(a)
print(a.count(10))              # 4
print(a.count(99))              # 0
print("---------------append--------------------")
a.append(23)
print(a)                        # [10, 20, 30, 40, 50, 10, 10, 10, 23]
a.append("aditya")
print(a)                        # [10, 20, 30, 40, 50, 10, 10, 10, 23, 'aditya']
# append method add a value in last position
print("---------------insert--------------------")
b = [10,20,30,40]
print(b)                        #[10, 20, 30, 40]
#var.insert(position,value)
b.insert(0,99)
print(b)                        #[99, 10, 20, 30, 40]
b.insert(2,1000)
print(b)                        #[99, 10, 1000, 20, 30, 40]
# we can insert a value specific position
print("---------------remove--------------------")
bb = [10,20,30,40]
print(bb)                       #[10, 20, 30, 40]
bb.remove(10)
print(bb)                       #[20, 30, 40]
print("---------------reverse--------------------")
p = [1,2,3,4,5]
print(p)
p.reverse()
print(p)                        # [5, 4, 3, 2, 1]
print("---------------sort--------------------")

k = [40,10,90,80,60,70,50,30]
k.sort()
print(k)                        # [10, 30, 40, 50, 60, 70, 80, 90]
print("-----------------------------------")
frt = ["banana","apple","orange"]
frt.sort()
print(frt)                      # ['apple', 'banana', 'orange']
# we should not provide diff type of value
print("---------------sort--------------------")

aa = [50,60,44,00,77,55,10,55]
aa.sort()
print(aa)                       # [0, 10, 44, 50, 55, 55, 60, 77]
aa.sort(reverse=True)           # this is a keyword argu
print(aa)                       #[77, 60, 55, 55, 50, 44, 10, 0]


print("---------------Math Operators--------------------")

mon = [10,20,30]
tue = [40,50,60]

total = mon + tue
print(total)          # [10, 20, 30, 40, 50, 60]
print(sum(total))     #  210

# here sum is predefind function

print("---------------Reapt Operators--------------------")

g = [10,20,30]
print(g*3)

print("---------------memebership Operators--------------------")

vals = [10,30,40,20]
print(30 in vals)   # True

if 30 in vals:
    print("value avalible")
else:
    print("value is not existing")

# value avalible
print("--------------fun example--------------------")

users = ["aditya", "bony", "dhwani"]
prime_users = ["bony", "aditya"]

for user in users:
    if user in prime_users:
        print(f"{user}: Assign benefits")
    else:
        print(f"{user}: Normal user")




