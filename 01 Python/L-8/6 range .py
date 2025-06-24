a = [ 10,20,30,40]
# a = [ 60,70,50,80,40]
b = { 60,70,50,80,40}

print(a)
print(type(a))
print("----------------------------------")
print(b)
print(type(b))

# range is data type 
# it is sequence means it can store grp of vls
# range data type having start and end values
'''
whats range
 a = 100            --->    single ValueError
 b = [10,20,30]     --->    10,20,30 

 range of values
    start value
    end value

 1 to 10
             for exp 
                    1,2,3,4,5,6,7,8,9,10

  start --> 1
  end   --> 10

'''

a = 10 # int
b = 1.32 # float 
c = [10,20,30] # list

# d = range of values? we can create nw 

'''
    THRE ARE 3 PARA IN RANGE 

        1. RANGE (P)
        2. RANGE (START,END)
        3. RANEG (START,END,STEP)

        there are two type to create range func

            1. by using INDEX               not using 
                ---> the position of value, where it store

            2. by using FOR loop            more using
                ---> Accessing the range of value  by using loop
                ---> by using for loop we can access ONE BY ONE from seq....

                        for LHS in RHS:
                            print()
'''

num = range(10) # start --> 0 , end --> 10-1 = 9
print(num) # (0,10)

num2 = range(10,15) # start --> 10 , end --> 15-1 = 14
print(num2) # (10,15)

print("--------------------index syntax (range)-----------------")

r = range(10,15) # start --> 10 , end --> 15-1 = 14

print(r) # (10,15)
print(r[0])
print(r[1])
print(r[2])
print(r[3])
print(r[4])


print("-------------------- using for loop (range)-----------------")

n = range(0,15)

for i in n :
    print(i)







