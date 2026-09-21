class Laptop:
    def __init__(self,brand,ram,storage):
        self.brand=brand
        self.ram=ram
        self.storage=storage
    def __str__(self):
        return f"brand:{self.brand} , ram:{self.ram} and storage:{self.storage}"
laptop=Laptop("Dell","8GB","512GB")
print(laptop)