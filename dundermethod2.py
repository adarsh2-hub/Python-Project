class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def __str__(self):
        return f"Name : {self.name} , Age : {self.age} and Course: {self.course}"
student=Student("Adarsh",21,"BCA")
print(student)