class Bookshelf:
    def __init__(self):
        self.shelf=["Python","Java","HTML"]
    def __len__(self):
        return len(self.shelf)
bookself=Bookshelf()
print(len(bookself))