'''
    oop
        class                       Purpose
            1.Constructor           Initialization/
                1.zero para             Createing instance vars
                2.para  
            2. Variable             To represent the data
                1.Instance
            3. Method               To perform an operation
                1.Instance
'''
class Student:
    def __init__(self,sno,name,location):
        self.sno = sno
        self.name = name
        self.location = location
        print("Student number:", self.sno)
        print("Student number:", self.name)
        print("Student number:", self.location)
        print("-----------------------")

s1 = Student(101, "aditya" ,"KBHK")
s2 = Student(102, "bony" ,"KBHK")
s3 = Student(103, "dhwani" ,"KBHK")

'''
1. How to create instance
    --> Inside constructor
    --> self is required
2.How to Access
    1.Within the class we can access by using self
    2.How to access outside of the class
        --> by using object name


'''