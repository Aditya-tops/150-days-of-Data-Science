'''
    1) while     2) for     

    --> Staetments will be execute based on condition
    --> Condition 
                Result
                        True  -> True block will be exeucte
                                    or
                        False -> False block will be exeucte 
    
    if condition1:
        if blockstatements
    elif condition2:
        elif blockstatements
    elif condition3:
        elif blockstatements
    else:
         blockstatements        

'''

marks = int(input("Please enter your marks: "))

if 90 <= marks <= 100:
    print("You have A group :)) ")
elif 80 <= marks < 90:
    print("You have B group :)) ")
elif 70 <= marks < 80:
    print("You have C group :)) ")
elif 35 <= marks < 70:
    print("You have D group :)) ")
elif 0 <= marks < 35:
    print("Sorry, you are fail")
else:
    print("Invalid input. Please enter marks between 0 and 100.")

print("-------------------------------------")
marks = int(input("Please enter your marks: "))

if marks <= 100 and marks >= 90:
    print("You have A group :))")
elif marks < 90 and marks >= 80:
    print("You have B group :))")
elif marks < 80 and marks >= 70:
    print("You have C group :))")
elif marks < 70 and marks >= 35:
    print("You have D group :))")
elif marks < 35 and marks >= 0:
    print("Sorry, you are fail")
else:
    print("Invalid input. Please enter marks between 0 and 100.")



print("----------------------------")
''' 
    Sequence  ->    variable
                    this can store grp of vals
                    i wanted to print ONE BY ONE val frm grp of vals
                    then we need to looping of kind execution

'''

a = [10,20,30,40,50]
print(a)
print(type(a))



