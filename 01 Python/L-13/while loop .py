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

    
print("---------continue  statement---------------------")

for i in nums:
    if i == 50:
        continue
    print(i)

