"""
Create an application for a car rental business using a console based user interface.
The application must allow keeping records of the company’s list of clients, existing car pool and rental history.
The application must allow its users to manage clients, cars and rentals in the following ways:
    Clients
         Add a new client. Each client is a physical person having a unique ID (driver license series), name, age.
         Update the data for any client.
         Remove a client from active clients. Note that removing a client must not remove existing car rental statistics.
         Search for clients based on ID and name [both at the same time]
         All client operations must undergo proper validation!
    Cars
         Add a new car to the car pool. Each car must have a valid license plate number, a make and model taken from a
        list of makes and models. In addition, each car will have a color.
         Remove a car from the car pool.
         Search for cars based on license number, make and model and color.
            [search with no parameters displays everything, omitting a param disregards it]
            [make = VW, model = Polo, CJ01ABC], [make = VW, model = Polo, CJ01XYZ]
         All car operations must undergo proper validation!
    Rentals
         An existing client can rent one or several cars from the car pool for a determined period. When rented, a car
        becomes unavailable for further renting.
         When a car is returned, it becomes available for renting once again.
         Search the rental history of a given client, car, or all rentals during any given period.
    Statistics
         The list of all cars in the car pool sorted by number of days they were rented.
         The list of clients sorted descending by the number of cars they have rented.

    The application must have support for unlimited undo/redo with cascading.
"""

"""
Plan:
    week 6 -> start the app with clients or cars
    week 7 -> work on statistics
    week 8 -> start the undo/redo implementation
    week 9 -> persist data to text/binary file, settings.properties etc.

What to do for week 6 attendance:
    carrental.domain (1 class to implement) 
        - implement Car OR Client class
            - add the required attributes as properties
            - make sure this class has a read-only id property (getter but no setter)

    carrental.repository (1 class to implement)
        - implement class Repository (application data store)
            - has a list or a dict of Client/Car instances
            - has methods 
                - add -> adds Car/Client to repo, raise RepoException if object with that id already stored
                - delete (by id)
                - get_all (return all instances)

    carrental.service (1 class to implement)
        - implement Car OR Client service (e.g. CarService)
            - methods to add/delete an instance, or return all of them

    carrental.ui (1 class to implement)
        - menu to add a Car/Client

How do these layers work?
    ui -> service (CarService.add_car)          -> repository (Repository.add_car) 
             -> create Car instance                 -> validate id is unique
             -> validate license plate format?       
             -> manage undo/redo? 

Simple Feature-Driven Development
   -> pick one feature (e.g. adding a car) and implement it (ui to repo)

TODO (using Car class as example):
    1. Implement Car class
    2. Implement Repository class + RepoException class (RepoException is raised by the Repository methods)
        - has a (private) list of cars
        - add a car, get_all cars
    3. Implement CarService class
        - has an instance of Repository
        - add a car, get_all cars
    4. Implement the UI
        - add a car
        - print all cars
"""
