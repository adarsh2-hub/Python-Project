class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def __str__(self):
        return f"Title : {self.title} , Author : {self.author} and Price: {self.price}"
book=Book("Python Basics","John",500)
print(book)