def naresh():
    print("Hello")


class Aditya:
    def teaching(self):
        print("Good moring")

print(naresh) # <function naresh at 0x000001DE073D1440>
# func called directly
d = Aditya()
print(d.teaching) # <bound method Aditya.teaching of <__main__.Aditya object at 0x00000232F8FA7230>>
#  method is called u should by object