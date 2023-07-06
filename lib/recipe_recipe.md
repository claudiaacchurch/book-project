"""
Modal class:

def__init__(self, id, recipe_name, cooking_time, rating):

def__repr__(self)
    - formats object as a string

def__eq__(self, other):
    - check that two objects are the same
'
tests:

def test_recipe_construction():
    - creates instance of recipe 
    - asserts attributes are set

def test_formats_as_a_string():
    - creates instance of recipe
    - asserts str(recipe) formats nicely

def test_two_recipes_are_the_same():
    - creates two instances of the recipe which are the same
    - asserts both instances are the same 

Repository class:

def all(self):
    - returns a list of all the recipes
    - loops through data from PG and creates Recipe objects 
    - SQL query: SELECT * FROM recipes;

def find(self):
    - returns one Recipe object
    - gets data from PG and filters based on id
    - SQL query: 'SELECT * FROM recipes WHERE id = %s'[id] 

tests:

def test_all_returns_list_of_recipes():

def test_find_returns_single_recipe():

"""
