from lib.book import *

def test_book_constructs():
    book = Book(1, "Lord of the Rings", "Tolkein")
    assert book.id == 1
    assert book.title == "Lord of the Rings"
    assert book.author_name == "Tolkein"

def test_books_are_equal():
    book1 = Book(1, "Lord of the Rings", "Tolkein")
    book2 = Book(1, "Lord of the Rings", "Tolkein")
    assert book1 == book2 

def test_book_formats_as_string():
    book1 = Book(1, "Lord of the Rings", "Tolkein")
    assert str(book1) == "Book(1, Lord of the Rings, Tolkein)"