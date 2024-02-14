class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __gt__(book1, book2):
        if(book1.publication_year > book2.publication_year):
            return True
        else:
            return False
        
book1 = Book('book1', 'author', 2008)
book2 = Book('book2', 'auth2', 2023)
if(book1>book2):
    print(f"{book1.title} written by {book1.author} published on {book1.publication_year} is greater than book2")
else:
    print(f"{book2.title} written by {book2.author} published on {book2.publication_year} is greater than book1")