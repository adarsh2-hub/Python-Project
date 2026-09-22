class Classroom:
    def __init__(self):
        self.clss=["Adarsh","Rahul","Kiran","Vijay","Ravi"]
    def __len__(self):
        return len(self.clss)
room=Classroom()
print(len(room))