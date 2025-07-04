'''
Predefinend function
    1.Map(p1,p2)
    2.Filter(p1,p2)
    3.Reduce(p1,p2)

    1. Map(p1,p2)

        ---> map function alwawys return map object
        ---> we are converting into list data structures

        price = [100,200,300,400,500]
        # midnight 12am MOdiji GST, +2
        res =   [102,202,302,402,502]
'''
prices = [100, 200, 300, 400, 500]
# var = map(       p1      ,p2)  here p1 is lambda func,p2 is alwas exection shooting variable
m     = map(lambda p: p + 2,prices)
print(m)            # map function always return MAP OBJECT <map object at 0x000001C73CC25090>
print(list(m))

print("-------------------------------")


names = ["aditya","bony","sabby"]
m = map(lambda name : name.upper(),names )
print(list(m))

print("-------------------------------")
names1 = ["aditya","bony","sabby"]
for i in names1:
    c = i.upper()
    print(c)

print("-------------------------------")





