class library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def addbook(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)
    
    def info(self):
        print(f"The no of books in library is {self.no_of_books} books. The books are ")
        for book in self.books:
            print(book)


l = library()
l.addbook("Think and grow rich")
l.addbook("Cant hurt me")
l.addbook("Do epic shit")
l.info()

