'''
Instance methods
----------------
    --> we can cteate instance variable inside constructor
    --> we need to use those variables inside instance method
    --> instance variables and methods having relation eachother
    --> we can access instance method by using object name
'''


class Student:
    def __init__(self,sno,name,location):
        self.sno = sno
        self.name = name
        self.location = location

       

s1 = Student(101, "aditya" ,"KBHK")
s2 = Student(102, "bony" ,"KBHK")
s3 = Student(103, "dhwani" ,"KBHK")

print(s1.sno)
print(s1.name)
print(s1.location)
print("-----------------------")

print(s2.sno)
print(s2.name)
print(s2.location)
print("-----------------------")

print(s3.sno)
print(s3.name)
print(s3.location)