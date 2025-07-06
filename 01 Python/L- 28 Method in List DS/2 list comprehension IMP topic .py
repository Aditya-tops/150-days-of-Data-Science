'''
    List Comprehension
    ------------------
        Comprehension   -->     Big para / essay

    List Comprehension Syntax

        LHS = RHS

        variable = [ part1  part2   part3]
        part1    = variable/expression
        part2    = for loop
        part3    = condition(optional)

        variable = [
                        variable/expression 
                        forloop 
                        condition
                   ]
    
'''

vals = [100,200,300,400,500]
# var  = [    p1           p2       ]  exxution always start frm p2
result = [val + 10   for val in vals] 
print(result)
# [110, 210, 310, 410, 510]


print("---------------------------------------------")

values = [1000, 2000, 3000, 4000]
results = [
    value + 100
    for value in values
]
print("Results after adding 100:", results)

print("---------------------------------------------")

names = ["aditya", "kunal", "krish"]
namesinupper = [
    name.upper()
    for name in names
]
print("Names in uppercase:", namesinupper)






