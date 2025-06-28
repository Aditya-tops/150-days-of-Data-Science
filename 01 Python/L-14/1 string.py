'''
        String

            Python          ->  print("hello world")
            "hello world"   ->  this is string
                            ->  A grp of characters enclosed within 
                                quotes(single/double/triple)

'''
a = 'aditya'
b = "aditya"
c = '''aditya'''
d = """aditya"""

print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("----------------------------")

address = ''' jalaram nagar, "balasinor", 'mahisagar', gujarat'''
name = "aditya"
gender = 'male'
print(name)
print(gender)
print(address)

print("---------Indixing-------------")
'''
        h   e   l   l   o       w   o   r   l   d
        0   1   2   3   4   5   6   7   8   9   10   <--- Positive index
      -11 -10  -9  -8  -7  -6  -5  -4  -3  -2   -1   <--- Nagetive index
        index :- the position of character where it stores
'''
p = "hello world"
print(p)
print(p[6])
print(p[5])
print(p[1])
print(p[-1])

print("---------Hello world print characters-------------")

st = "hello world"

for s in st:
    print(s)

'''
    index    -> by using this we can access single character
    slicing  -> by using this we can access grp of character

    print(a[start:end])

    1. what is stg?
    2. how many ways to create a stg?
    3. how to access stg 
                            -index
                            -slicing
                            -for loop
'''
print("---------Hello world print slicing characters-------------")

st1 = "hello world"
print(st1[0:4])  # hell   
print(st1[0:5])  # hello
print(st1[:5])  # hello


