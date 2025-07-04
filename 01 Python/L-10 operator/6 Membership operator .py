'''
    Rule1 -->  work : sequence is require

        operators  -->  in, not in
        Usage      -->  checking purpose 
        Result     -->  Boolean, either True or False

        syntax :- print( LHS in RHS)

'''


names = ["aditya","bony","prisha","dhwani","aditi","kunal"]
print("Our List is :- ",names)

print("prisha" in names)  # True
print("niyati" in names)  # False

values = [10,20,3,0,30,40,50,60]
print( 10 in values)  # True
print( 55 in values)  # False

text = "Welcome to python programming "
print("Welcome" in text) # True
print("welcome" in text) # False
print("aditya" in text) # False
print("aditya" not in text) # True

print("-------Login Program------")

users = ["aditya", "bony", "prisha", "dhwani", "aditi", "kunal"]
prime_users = ["sita", "mita", "bony", "gita", "chinny", "vinny", "bunny", "prisha"]

for user in users:
    if user in prime_users:
        print("this user is prime user :- ",user)

# Answer is bony,prisha
# this is a nested loop 





