from abc import ABC,abstractmethod
class Vehicle:
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car is starting..")
car=Car()
car.start()