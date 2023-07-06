from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

def test_all_returns_list_of_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repo = RecipeRepository(db_connection)
    result = repo.all()
    assert result == [
        Recipe(1, 'Pizza', 50, 4),
        Recipe(2, 'Pasta', 90, 2),
        Recipe(3, 'Curry', 20, 5),
        Recipe(4, 'Salad', 10, 3)
    ]

def test_find_returns_single_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repo = RecipeRepository(db_connection)
    result = repo.find(1)
    print(type(result))
    assert result == Recipe(1, 'Pizza', 50, 4)