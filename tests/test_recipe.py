from lib.recipe import Recipe

def test_recipe_construction():
    recipe1 = Recipe(1, 'pasta', 50, 4)
    assert recipe1.id == 1
    assert recipe1.recipe_name == 'pasta'
    assert recipe1.cooking_time == 50
    assert recipe1.rating == 4

def test_formats_as_a_string():
    recipe1 = Recipe(1, 'pasta', 50, 4)
    assert str(recipe1) == "Recipe(1, pasta, 50, 4)"

def test_two_recipes_are_the_same():
    recipe1 = Recipe(1, 'pasta', 50, 4)
    recipe2 = Recipe(1, 'pasta', 50, 4)
    assert recipe1 == recipe2