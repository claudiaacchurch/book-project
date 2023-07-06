from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.book_repository import BookRepository
from lib.album_repository import AlbumRepository
from lib.recipe_repository import RecipeRepository

#Application layer
class Application():
    def __init__ (self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")
    
    def run(self):
        print("Welcome to the music library manager!")
        print("What would you like to do?\n1 - List all albums\n2 - List all artists")
        while True:
            user_action = input("Enter your choice: ")
            if user_action == '1':
                album_repo = AlbumRepository(self._connection)
                albums = album_repo.all()
                for album in albums:
                    print(f"{album.id}: {album.title}, {album.release_year}, {album.artist_id}")
                break
            elif user_action == '2':
                artist_repo = ArtistRepository(self._connection)
                artists = artist_repo.all()
                for artist in artists:
                    print(f"{artist.id}: {artist.name}, {artist.genre}")
                break
            else:
                print("Not a valid option please enter 1 or 2")
                continue

    
if __name__ == '__main__':
    app = Application()
    app.run()



"""# Connect to the database
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


connection.seed("seeds/recipes.sql")
recipe_repo = RecipeRepository(connection)
recipes = recipe_repo.all()

for recipe in recipes:
    print(recipe)"""

