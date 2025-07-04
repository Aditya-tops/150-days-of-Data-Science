'''
'''

monday = [100,200,300,400,500]
print(sum(monday))

print("------------------------------")

from functools import reduce

friday = [500, 600, 400, 300]
r = reduce(lambda x, y: x + y, friday)
print(r)




