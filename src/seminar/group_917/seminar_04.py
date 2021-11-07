"""
Write a program that manages rectangles. Each rectangle is defined by two of its opposing corners, having coordinates
(x1,y1) and (x2,y2) (for example, points (0,0) and (1,1) define a 'unit rectangle').

Functionalities will be available using a menu or commands:

1. Generate 'n' rectangles
    random.randint(a,b) -> use to generate random integers

    - n is a positive integer read from the keyboard.
    - program generates and stores n distinct rectangles (distinct = at least one different corner),
    - each rectangle is completely enclosed in the square defined by corners (0,0) and (20,20)

2. Display all rectangle data, sorted descending by area
    rectangle: (0,0) - (10,10) -> area is 100 (0,0), (0,10), (10,0), (10,10)
    rectangle: (14,15) - (18,18) -> area is 12

    - display area and coordinates for each rectangle, using right justification (str.rjust)

3. Delete all rectangles that have at least one corner below the line x = y

Requirements:
    - handle input errors with exceptions
    - specification for all noi-UI functions (except getters and setters)
    - unit test for 3. delete

Required modules:
    rectangle.py    (functions that work directly with rectangles)
    functions.py (implement program functionalities)
    console.py   (user interface)

Function calls between modules:
    console -> functions -> rectangle
    console -> rectangle
"""