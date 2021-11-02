from lecture.livecoding.lecture_06_08.repo.repository import Repository
from lecture.livecoding.lecture_06_08.services.ingredientService import IngredientService
from lecture.livecoding.lecture_06_08.services.productService import ProductService
from lecture.livecoding.lecture_06_08.ui.ui import UI

"""
The Happy Bakery is a family-run business that produces and sells bakery and confectionary products.
The bakery turns ingredients into delicious products using defined recipes.
They need you, yes you! to help them manage their daily workflow.
What does this entail?
    a. Manage available ingredients, recipes and products that the bakery knows to make
    b. Record a production run. This transforms existing ingredients into product, according to the recipe
    c. Keep the stock for each ingredient and product
    e. Show used ingredients, sorted in descending order of amount used.

domain entities?
    -> Ingredient
        - id, description, stock (default in grams), expiration date
    -> IngredientQuantity
        - ingredient, quantity
    -> Recipe
        - id
        - list of IngredientQuantity
        - list of steps
    -> Product
        - id
        - recipe, stock
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
# what we do here is an early version of dependency injection

# 1. Pick which repository implementation we want to use
ingr_repo = Repository()
prod_repo = Repository()

# 2. Start the service to work with the selected repository
ingr_service = IngredientService(ingr_repo)
prod_service = ProductService(prod_repo)

# 3. Start the UI with the initialized services
ui = UI(ingr_service, prod_service)

# 4. Start the program
ui.start()
