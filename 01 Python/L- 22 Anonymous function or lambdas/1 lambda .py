'''
    syntax
    ------

    LHS = RHS
    var = lambdas lhs        : rhs
    var = lambdas variables  : expression with variable

'''
print("-----Lambda Func with one para--------")

# var = lambdas variables  : expression with variable
add   = lambda x : x + 1
result = add(10)
print(result)

print("-----Lambda Func with two para--------")
# var   = lambdas variables  : expression with variable
add1    = lambda   p,q       : p + q
result1 = add1(10,20)
print(result1)

print("-----Lambda Func with three para--------")
# var   = lambdas variables  : expression with variable
add3    = lambda   x,y,z       : x + y +z
result3 = add3(10,20,30)
print(result3)


print("------- lowecase to upper case--------")
a = lambda x:x.upper()
res = a("aditya")
print(res)

# we can apply only specific operation Not for regular operation
s = lambda g : g*g
x = s(100)
print(x)










