'''
        1.Intialization
        2.Condition
        3.Increment/Decrement

        print the vals
            1......................................10
            start                                 End
'''

ranya_main = 1

while ranya_main <=10 :
    print("ranya " + str(ranya_main))
    ranya_main = ranya_main +1

# same output we can still get by using range data type
'''
    --> break is keyworld in python
    --> Based on condition, I wanted to stop the loop, 
        then we need to use break keyword
    --> break key we should only on loops
    --> break keyworld we should appy only on loops
    --> break 
                for
                while
'''
print("--------------Break statement-------------")
nums = [10,20,30,40,50,60,70,80,90,100]

for i in nums:
    if i == 50:
        break
    print(i)

for i in nums:
    if i == 50:
        continue
    print(i)

print("--------- continue  statement ---------------------")
'''
    Continue
            --> Keyword in python
            --> We can skip the value(s) from loop
            --> continue keyword we shold use loops only

    a = [10,20,30,40,50,60]

    for loop......
    10
    20
    30
    40

    --> i wanted to skin 30, then we need to use continue key
'''
a = [10,20,30,40,50,60]

for i in a :
    if i ==30: # 30 is skip
        continue
    print(i)

value1 = [10,20,30,40,50,1,60,70,90]
value2 = [30,50]

for val in value1:
    if val in a :
        continue
    print(val)

print("----------- 500 skip in cart --------------")

cart = [10,20,500,600,700,800,1000]

for item in cart :
    if item == 500:
        continue
    print(item)

'''
pass
 -> pass is a keyword 
 -> we can pass funtion
'''