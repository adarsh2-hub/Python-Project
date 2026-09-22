class ShopingCart:
    def __init__(self):
        self.cart=["laptop","mouse","keyboard","headphones"]
    def __len__(self):
        return len(self.cart)
shopingcart=ShopingCart()
print(len(shopingcart))