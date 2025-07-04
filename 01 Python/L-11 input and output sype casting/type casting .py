# convert one data type into other data type is called type casting


a = 10 
b = 20 
print("a + b = ",a + b)         #30

p = "10"
q = "20"
print("p + q = ", p + q)         #1020 

product1 = input("Enter price 1 :- ")
product2 = input("Enter price 2 :- ")

total = product1 + product2
print(type(total))
print("your bill is :- ", total) 

'''
Enter price 1 :- 50
Enter price 2 :- 50
your bill is :-  5050
'''

print("---------------welcome to waltmart--------------")

prod1 = int(input("Enter price 1 :- "))
prod2 = int(input("Enter price 2 :- "))

total1 = prod1 + prod2
print(type(total1))
print("your bill is :- ", total1) 