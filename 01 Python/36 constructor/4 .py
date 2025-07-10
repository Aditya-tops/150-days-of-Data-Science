class Student3:
    def __init__(self,sno,name,address):
        self.sno = sno                      
        self.name = name                       
        self.address = address   
                           
    def display(self):
            print("Student number is : ", self.sno)
            print("Student name is : ", self.name)
            print("Student address is : ", self.address)

s = Student3(777,"bony","KBHK")   
s.display()