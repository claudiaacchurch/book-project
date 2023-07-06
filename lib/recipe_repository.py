from lib.recipe import Recipe

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM recipes')
        recipes = []
        for row in rows:
            recipe = Recipe(row['id'], row['recipe_name'], row['cooking_time'], row['rating'])
            recipes.append(recipe)
        return recipes
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM recipes WHERE id = %s', [id])
        recipes = []
        for row in rows:
            recipe = Recipe(row['id'], row['recipe_name'], row['cooking_time'], row['rating'])
            recipes.append(recipe)
        return recipes[0]
        