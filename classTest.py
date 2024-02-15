

class Person:

    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname =lname
        self.age= age
    def print_details(self):
        print(self.fname,self.lname,self.age)

class Employee(Person):
    def fun(self):
        print("Child class")


# emp1 = Employee("mani","j",30)       
# emp1.print_details()
# emp1.fun() 

emp2 = Person("manik","jm",34)
emp2.print_details()
emp2.fun()
        
 
# person_1 = Person("j","mani","20")
# person_1.print_details() 

# person_2 = Person("jm","kmani","230")
# person_2.print_details() 


# class Student(Person):
#     def __init__(self,fname,lname,age,id,mobile):
#         self.id = id
#         self.mobile = mobile
#         Person.__init__(self,fname,lname,age)
    
#     def print_stu_details(self):
#         print(self.id,self.mobile)


# student_1 = Student("juluru","mani",30,123,9160121143)
# student_1.print_details()
# student_1.print_stu_details()