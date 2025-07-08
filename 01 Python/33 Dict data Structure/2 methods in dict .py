'''
    --> dict is predefined class
    --> class contains method

    class
        method1()
        method2()
        method3()

    body
        heart()
        brain()

    --> methods can perform a task

    class      method
    -----      ------
    str        upper(),lower,strip(),replace(),count(),slip()
    list       append(),count(),insert(),remove(),reverse()
    tuple      count(),index()
    set        add(),remove(),clear()
    dict       keys(),values(),items()




'''
print("------------------------------------------")
d = {
        101:None,
        102:"aditya",
    }
print(d) #{101: None, 102: 'aditya'}
# values assign with NONE data type
print("------------keys() method----------------")
d = {
        1:"aditya",
        2:"kavan",
        3:"juned",
    }
print(d)                # {1: 'aditya', 2: 'kavan', 3: 'juned'}
print(d.keys())         # dict_keys([1, 2, 3])
print(list(d.keys()))   # [1, 2, 3]
print("------------------------------------------")
print(d.values())       # dict_values(['aditya', 'kavan', 'juned'])
print(list(d.values())) # ['aditya', 'kavan', 'juned']
print("------------------------------------------")
print("------------------------------------------")

print("----------items() method------------")
#items() method
#item method it can return list of tuple
d = {
        1:"aditya",
        2:"kavan",
        3:"juned",
    }
print(d.items())  # dict_items([(1, 'aditya'), (2, 'kavan'), (3, 'juned')])
print(list(d.items()))  # dict_items([(1, 'aditya'), (2, 'kavan'), (3, 'juned')])
print("------------------------------------------")
a = [10, 20, 30, 40]
for i in a:
    print(i, end=' ')  # 10 20 30 40

print()
print("------------------------------------------")
d = {
        1:"aditya",
        2:"kavan",
        3:"juned",
    }

for val in d.items() :
    print(val)

# (1, 'aditya')
# (2, 'kavan')
# (3, 'juned')

print("------------------------------------------")
for val in d.values() :
    print(val)
# aditya
# kavan
# juned
print("------------------------------------------")
for val in d.keys() :
    print(val)
# 1
# 2
# 3

