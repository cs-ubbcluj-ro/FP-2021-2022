from lecture.livecoding.lecture_06_08.domain.Ingredient import Ingredient
from lecture.livecoding.lecture_06_08.domain.Recipe import Recipe
from lecture.livecoding.lecture_06_08.domain.Stock import Stock
from lecture.livecoding.lecture_06_08.repo.repository import Repository, \
    IngredientTextFileRepository, IngredientBinFileRepository

"""
The Happy Bakery is a family-run business that produces and sells bakery and confectionary products.
The bakery turns ingredients into delicious products using defined recipes.
They need you, yes you! to help them manage their daily workflow.
What does this entail?
    a. Manage available ingredients, recipes and products that the bakery knows to make
    b. Record a production run. This transforms existing ingredients into product, according to the recipe
    c. Keep the stock for each ingredient and product
    e. Show used ingredients, sorted in descending order of amount used.

domain entities? ( <...> denotes an entire object)
    -> Ingredient
        - id, description
    -> Stock
        - <Ingredient>, quantity, expiration date
    -> Recipe
        - id
        - list of <Stock>
        - list of steps
    -> Product
        - id
        - <Recipe>
"""

"""
Motivation / Recap

~~~
Managing complexity is a big deal in software engineering (SE)
         complexity = what can humans understand
~~~
1. Divide the program into functions (parameters/return/exceptions)
2. Divide the program into modules (+ function)
3. Add our own data types (classes) 
    - we want to represent data/operations our own way
4. We try to combine 1. + 2. + 3. into a well-used design pattern => layered architecture

What layers have we already used?
    -> ui (user interaction)
    -> services (functionality)
    -> repository (data store)
    -> domain (our program's data types)
    
Calls between layers
    ui -> services -> repository -> domain
    ui -> domain

Future work
    services   -> statistics / filters / undo/redo 
    repository -> manage data storage (in-memory -> text-files -> binary files -> SQL/noSQL (opt) )

Modules -> responsible for one thing only (SRP)
        -> independent & interchangeable (text-file storage vs. SQL storage)
"""


# Assemble and start the program
# TODO Make this work
def create_ingredient_repo():
    """
    We should be able to switch between repo implementation without the rest of the
    program knowing or caring about this

    modules = independent AND interchangeable
    """

    # Binary file repository for ingredients
    # repo = IngredientBinFileRepository()

    # Text file repository for ingredients
    repo = IngredientTextFileRepository()

    # in-memory repository for ingredients
    # repo = Repository()
    # repo.add(Ingredient(100, "Bread Flour (White, 550)"))
    # repo.add(Ingredient(101, "Yeast (dry)"))
    # repo.add(Ingredient(102, "Sugar (white)"))
    # repo.add(Ingredient(103, "Salt (regular)"))
    # repo.add(Ingredient(104, "Oil (canola)"))
    # repo.add(Ingredient(105, "Butter"))
    # repo.add(Ingredient(106, "Egg (chicken)"))
    # repo.add(Ingredient(107, "Cake flour"))
    # repo.add(Ingredient(108, "Baking powder"))
    # repo.add(Ingredient(109, "Vanilla (extract)"))

    print(len(repo))
    return repo


def create_bread_recipe(ingredients_repo):
    """
    1 package (1/4 ounce) active dry yeast
    2-1/4 cups warm water (110° to 115°)
    3 tablespoons sugar plus 1/2 teaspoon sugar
    1 tablespoon salt
    2 tablespoons canola oil
    6-1/4 to 6-3/4 cups bread flour
    source: https://www.tasteofhome.com/recipes/basic-homemade-bread/
    """
    recipe = Recipe(500, "Basic Homemade Bread")
    recipe.required_stocks.append(Stock(ingredients_repo[101], 20))
    recipe.required_stocks.append(Stock(ingredients_repo[102], 30))
    recipe.required_stocks.append(Stock(ingredients_repo[103], 5))
    recipe.required_stocks.append(Stock(ingredients_repo[104], 10))
    recipe.required_stocks.append(Stock(ingredients_repo[100], 1000))
    return recipe


def create_cake_recipe(ingredients_repo):
    """
    175g (6oz) margarine or softened butter
    175g (6oz) caster sugar
    3 large eggs
    175g (6oz) self-raising flour, sifted
    1tsp baking powder
    1tsp vanilla extract
    pinch of salt
    source: https://www.houseandgarden.co.uk/recipe/simple-vanilla-cake-recipe
    """
    recipe = Recipe(501, "Tasty Cookies")
    recipe.required_stocks.append(Stock(ingredients_repo[105], 175))
    recipe.required_stocks.append(Stock(ingredients_repo[102], 175))
    recipe.required_stocks.append(Stock(ingredients_repo[106], 3))
    recipe.required_stocks.append(Stock(ingredients_repo[107], 175))
    recipe.required_stocks.append(Stock(ingredients_repo[108], 5))
    recipe.required_stocks.append(Stock(ingredients_repo[109], 5))
    recipe.required_stocks.append(Stock(ingredients_repo[103], 2))
    return recipe


"""
    Repository
    in-memory implementation
        + able to store program data
        + has a single responsibility
        - it should handle persistence, but it doesn't
        
        persistence = keep data from previous program runs
        how do we persist data?
            -> files (text OR binary)
            -> files (+ relational algebra sprinked on top = SQL database)
            -> files (+ something else = NoSQL database) 
    
    
"""
ingredient_repo = create_ingredient_repo()
recipe_repo = Repository()
recipe_repo.add(create_bread_recipe(ingredient_repo))
recipe_repo.add(create_cake_recipe(ingredient_repo))

print("Recipe repo size - ", str(len(recipe_repo)))
