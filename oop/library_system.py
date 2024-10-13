class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author

class EBook(Book):
    
    def __init__(self, title, author, file_size):
        super().__init__(title,author)  # Call parent class constructor
        self.file_size = file_size
        
class PrintBook(Book):

    def __init__(self, title, author, page_count):
        super().__init__(title,author)  # Call parent class constructor
        self.page_count = page_count
        
class Library(Book, EBook, PrintBook):

    def __init__(self, books):
        self.books = books
    
    def add_book(self, book):
        return self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"{book}")  