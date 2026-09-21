class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def __str__(self):
        return f"brand:{self.brand} , model:{self.model} and price:{self.price}"
mobile=Mobile("Redmi","Note 11",12000)
print(mobile)