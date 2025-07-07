a = [10,20,30]
b = tuple(a)
print(b)            # (10, 20, 30)
print(a)            # [10, 20, 30]

print("-------slice----------")
aa = (10,20,30,40,50,60,70,80)
print(aa)
print(aa[0])        # 10
print(aa[1:5])      # (20, 30, 40, 50)

for i in aa:
    print(i)

t = (10,20,30)
t2 = (40,50,60)
t3 = t + t2
print(t3)     # (10, 20, 30, 40, 50, 60)

print("---------------------------------")

# class, method, object, method calling
class Aditya:
    def eating(self):
        print("I like chicken biriyani")

a = Aditya()
a.eating()


z = (10,20,30,[40,50],60,70)
print(z)
# can i chage this ? ans no but we change list vals
print(z[0])
print(z[1])
print(z[2])
print(z[3][0])
print(z[3][1])
z[3][1] = 99
print(z[3][1])
z[3].append(69)
print(z)
