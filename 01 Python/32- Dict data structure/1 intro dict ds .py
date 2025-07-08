'''
python 
    1.list ds
    2.Tuple ds
    3.Set ds
    4.Dict ds
'''
print("------------------------------")
d     = {101:"Aditya",102:"kunal"}
# var = {key:value   ,key:value}
print(d)
print(type(d))      # <class 'dict'>
# one key value pair called item here is 2 item

print("---duplicate keys are not allow---")

a = {
        101:"aditya",
        101:"aditya"
}
print(a)            # {101: 'aditya'}
print("---duplicate values are allow---")
a = {
        101:"aditya",
        102:"aditya"
}
print(a)            # {101: 'aditya', 102: 'aditya'}
print("---Insertion order not fixed---")
a = {
        101:"aditya",
        102:"kunal",
        103:"sakshi",
        104:"dhwani",
}
print(a)            # {101: 'aditya', 102: 'kunal', 103: 'sakshi', 104: 'dhwani'}
print("------------------------------")
a = {
        101:"ramesh",
        102:"suresh",
        103:"sakshi",
        104:"dhwani",
}
print(a)
# a[key] = value
a[102] = "tony"
print(a)            # {101: 'ramesh', 102: 'tony', 103: 'sakshi', 104: 'dhwani'}
a[105] = "aditya"
print(a)            # {101: 'ramesh', 102: 'tony', 103: 'sakshi', 104: 'dhwani', 105: 'aditya'}

print("--------IMP intervew question-----------")
a = [10,20,30,40,50]
b ={101:"ramesh"}

a[0]=99
b[0]=99

print(a)            # [99, 20, 30, 40, 50]
print(b)            # {101: 'ramesh', 0: 99}

print("--------IMP intervew question-----------")

d = {
        101:"aditya",
        102:"kunal",
        103:"arjun",
    }
print(d)
print(d[101])           # aditya here is 101 index we can assesss value by using key
print(d[103])           # arjun here is 103 index we can assesss value by using key
# if key does not exits we are getting keyError

print("--------acessing one by one vals--------")

d = {
        101:"aditya",
        102:"kunal",
        103:"arjun",
    }

for i in d:
    print(i) # 101
             # 102
             # 103
for i in d:
    print(i,d[i]) # 101 aditya
                  # 102 kunal
                  # 103 arjun

for i in d:
    print(i,d[i])

print("------------------------------")

a = input("enter value :- ")
b = input("enter value :- ")

c = {a:b}
print(c)


