'''
    list    comprehension   result          list
    set     comprehension   result          set
    dict    comprehension   result          dict

    tuple   comprehension   result          not a tuple generator :))

    LHS = RHS
    var = {p1          p2         p3}
    p1  = var/expression with dict syntax
    p2  = for loop
    p3  = condition
                        or
    var = { 
            p1          
            p2 
            p3
          }
'''

a = [1,2,3,4]
result = {
            i : i**2
            for i in a
         }
print(result)
# {1: 1, 2: 4, 3: 9, 4: 16}
print("--------------------------------")
names = ["aditya","bony","subham"]

result1 = {
            i:i.upper()
            for i in names
          }
print(result1)
# {'aditya': 'ADITYA', 'bony': 'BONY', 'subham': 'SUBHAM'}
print("--------------------------------")

names = ["aditya", "bony", "subham"]

result1 = {
    name: len(name)
    for name in names
}
print(result1)
# {'aditya': 6, 'bony': 4, 'subham': 6}
print("--------------------------------")

squares = {
            a:a*a
            for a in range(1,6)
          }
print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
