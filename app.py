from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.book_repository import BookRepository
from lib.album_repository import AlbumRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/book_store.sql")

# Retrieve all artists
book_repository = BookRepository(connection)
books = book_repository.all()

# List them out
for book in books:
    print(f"{book.id}-{book.title}-{book.author_name}")


album_repo = AlbumRepository(connection)
result = album_repo.find(1)
print(result)
