from datetime import date

from seminar.group_917.seminar_09.domain.Car import Car
from seminar.group_917.seminar_09.domain.Client import Client
from seminar.group_917.seminar_09.domain.Rental import Rental
from seminar.group_917.seminar_11.repository.Repository import Repository

alice = Client(101, "2801010266699", "Alice")
bob = Client(102, "1800101248899", "Bob")
carol = Client(103, "2670511035588", "Carol")
sophia = Client(104, "2990511035588", "Sophia")

hyundai_tucson = Car(201, "CJ 02 TWD", "Hyundai", "Tucson")
toyota_corolla = Car(202, "CJ 02 FWD", "Toyota", "Corolla")
dacia_sandero = Car(203, "IS 99 RTY", "Dacia", "Sandero")

"""
    !!!!
    Rental objects hold the entire Client and Car object
"""
rental_sophia_tucson = Rental(301, sophia, hyundai_tucson, date(2016, 11, 1), date(2016, 11, 30))
rental_sophia_toyota = Rental(302, sophia, hyundai_tucson, date(2016, 12, 1), date(2016, 12, 31))
rental_bob_dacia = Rental(303, bob, dacia_sandero, date(2021, 12, 1), date(2021, 12, 31))

"""
    1. Use in-memory repos
"""
car_repo = Repository()
car_repo.store(hyundai_tucson)
car_repo.store(toyota_corolla)
car_repo.store(dacia_sandero)

client_repo = Repository()
client_repo.store(sophia)
client_repo.store(alice)

rental_repo = Repository()
rental_repo.store(rental_bob_dacia)
rental_repo.store(rental_sophia_toyota)
rental_repo.store(rental_sophia_tucson)

# Do the same for clients and rentals

# TODO Implement the requirements below
"""
    2. Use text-file repos
    
        class CarTextFileRepo(Repository):
            pass 

        class ClientTextFileRepo(Repository):
            pass
            
        class RentalTextFileRepo(Repository):
            pass

    Add entities to them, save & load from file
"""
# TODO Implement PyUnit test case

"""
    3. Use Pickle repos        
        Can we implement a single class (BinaryFileRepo) or do we need more?
        
        class BinaryFileRepo(Repository):
            pass
"""
# TODO Implement PyUnit test case

"""
    4. Imeplement a single text-file repo that works for each entity
    
    class TextFileRepo(Repository):
        # function references
        # call when saving to/loading from file
        file_line_to_entity = None
        entity_to_file_line = None

    client_repo = TextFileRepo(...)
    car_repo = TextFileRepo(...)
    rental_repo = TextFileRepo(...)
    
    -> we need two functions:
        file_line_to_<entity>
        <entity>_to_file_line
        
    e.g.
        file_line_to_car
        car_to_file_line(car) -> str
        
        file_line_to_client
        client_to_file_line
"""
# TODO Implement PyUnit test case
