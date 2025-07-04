#import foldername
import module

# print (filename.varname)
print(module.a)
print(module.b)

print("---------------------------------")
import wish

print(wish.x)
print(wish.wish())

'''
    import
    ------
        --> keyword in python
        --> Usage We can import the module
        --> after importing module, we can access member of the module

'''

print("-1----import----------")
import addmul 

addmul.add(10,20)
addmul.mul(2,6)

print("-2----import--as---Alices------") 
# we can rename the module
import addmul  as am

am.add(20,30)
am.mul(3,7)



