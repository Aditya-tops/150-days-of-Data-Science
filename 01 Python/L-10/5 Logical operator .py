'''
        Operators  -->  and, or, not
        Usage      -->  We can create  COMPOUND CONDITION
        Condition  -->  JOING More more than two condition
        Result     -->  Boolean: either True or False 

        LHS     and     RHS     RESULT

        T       and     T       T
        T       and     F       F
        F       and     T       F
        F       and     F       F
    --------------------------------------
        LHS     and     RHS     RESULT

        T       or     T       T
        T       or     F       T
        F       or     T       T
        F       or     F       F
'''

a = 1
b = 2
c = 3

print ( a>b and b>c )
#       1>2 AND 2>3
#     false and false   this is AND GET so
#  Anser is FALSE 
print("-----------------------")

p = True
q = False
print(p and p) # True or 1
print(p or q)  # True or 1
print(not a)   # False

