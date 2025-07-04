'''
Filter
------
    data = [1,2,3,4,5,6,7,8,9,10]

    filter the data
    To filter data we need condition

    Value < 7
    result = [1,2,3,4,5,6]
'''
data = [1,2,3,4,5,6,7,8,9,10]
# var  = filter(p1,p2)
result = filter(lambda value : value < 7 , data)
result1 = filter(lambda value : value > 5 , data)
print(result)      # <filter object at 0x0000021FEA7B5000>
print(list(result))
print(list(result1))



