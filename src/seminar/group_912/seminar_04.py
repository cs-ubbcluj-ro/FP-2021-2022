"""
Write a program that manages circles. Each circle has an (x,y) center (x,y - integers) and a the radius r
(r > 0, r is an integer). Functionalities will be available using a command-based UI:

1. Generate 'n' circles.
    - n is a positive integer read from the keyboard.
    - program generates and stores n distinct, random circles (distinct = at least one of x,y,radius must differ) ,
        each completely enclosed in the square defined by corners (0,0) and (40,40)

2. Delete all circles from a given rectangle
    - read rectangle data (x, y, width, height) # rect corner coordinates  (x,y) - (x + width, y + height)
    - delete all circles that are fully enclosed in this rectangle

3. Display all circle data on the console, sorted descending by radius

4. Exit

Requirements:
    - handle input errors with exceptions
    - unit test for 2. delete

Required modules:
    circle.py    (functions that work directly with circles)
    functions.py (implement program functionalities)
    console.py   (user interface)

    function calls
    console.py -> function.py -> circle.py
               -> circle.py
"""