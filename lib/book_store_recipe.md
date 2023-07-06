#model class 
#class Book
#def init: id(int), title(string), author_name(string)

#repository class
#class BookRepository, no args
#def all()
    #executes SQL query
    #SELECT * FROM books;
    #returns list of Book objects

#Book tests
#def test_book_constructs():
    #book object constructs correctly 

#def test_books_are_equal():
    #two variables with the same book details are the same

#BookRepository tests
#def test_get_all_records():
    #all method returns a list of all book table records

#Book repo