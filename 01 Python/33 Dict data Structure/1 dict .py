'''

'''
# we can access value and key
d = {
        10:"aditya",
        11:"dhwani",
        12:"bony",
}
print(d[10])
print(d[11])
print(d[12])
print("------------------------------------------")
for i in d:
    print(i)
print("------------------------------------------")
for i in d:
    print(i,d[i])
print("------------- Update dict (add) ----------------")
# case : 1 Can we add key and value in dict
d = {
        101:"ramesh",
        102:"suresh",
        103:"aditya",
}
print(d)

d[104] = "prasad"
print(d)            # {101: 'ramesh', 102: 'suresh', 103: 'aditya', 104: 'prasad'}
# if no key is existing in dict then  only new key and val pair added
print("------------- Update dict () ----------------")
# case : 2
d = {
        101:"ramesh",
        102:"suresh",
        103:"aditya",
}
print(d)
d[101] = "bony"
print(d)            # {101: 'bony', 102: 'suresh', 103: 'aditya'}
# old val is replace with new vals duplate keys are not allow in dict

print("------------- Update dict remove or del ----------------")
# In python we do have del kieyword
# By using this keyword we can deleted vals/objects
a = 10
print(a)    # 10
#del a       # ONCE YOU CAN DEL AND PRINT YOU GIVE ERROR this error is nameError
#print(a)
'''
    print(a)
          ^
NameError: name 'a' is not defined
'''
print("------------------------------------------")
a = [10,20,30,40]
print(a)        # [10,20,30,40]
del (a[0])
print(a)        # [20, 30, 40]
# deleting speacific val
print("----------------------------------")
# deleing item form dict
d = {
        101:"aditya",
        102:"bony",
        103:"kunal",
}
del d[101]
print(d)        # {102: 'bony', 103: 'kunal'}
print("------------clear()------------------")
# CLEAR IS REMOVE ALL ITEMS AND GIVE EMPTY DICT
d.clear()
print(d)        # {}
print("------------len()------------------------")
a = [ 10,20,30,40,50]
b = ( 10,20,30,10,50)
c = {
        101:"aditya",
        102:"bony",
    }

print(len(a))               # 5
print(len(b))               # 5
print(len(c))               # 2 here is total number of items
print("------------------------------------------")









