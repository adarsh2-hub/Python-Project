class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def __str__(self):
        return f"brand:{self.brand} and model:{self.model}"
car=Car("Toyota","Innova")
print(car)