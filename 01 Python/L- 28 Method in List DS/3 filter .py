names = ("aditya","bony",'khushi','pallavi')
r = [ name.upper() for name in names]
j = [ name.title() for name in names]
print(names)
print(r)
print(j)
# ('aditya', 'bony', 'khushi', 'pallavi')
# ['ADITYA', 'BONY', 'KHUSHI', 'PALLAVI']
# ['Aditya', 'Bony', 'Khushi', 'Pallavi']

print("-------condition-----------")
print("-------filter data-----------")

values = [10,20,30,40,50,60,70,80,90]
#  R   =   p1                 p2                 p3
result = [ val         for val in values     if val<50     ]
print(values)
print(result)

#[10, 20, 30, 40, 50, 60, 70, 80, 90]
#[10, 20, 30, 40]

print("----------------------------------------------")

values = [10,20,30,40,50,60,70,80,90]
#  R   =   p1                 p2                 p3
result = [      val         
                for val in values     
                if val>50     
         ]
print(values)
print(result)

# [10, 20, 30, 40, 50, 60, 70, 80, 90]
# [60, 70, 80, 90]

