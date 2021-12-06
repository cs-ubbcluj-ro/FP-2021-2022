from datetime import date

from seminar.group_912.seminar_09.domain.Car import Car
from seminar.group_912.seminar_09.domain.Client import Client
from seminar.group_912.seminar_09.domain.Rental import Rental
from seminar.group_912.seminar_11.repository.Repository import Repository

alice = Client(101, "2801010266699", "Alice")
bob = Client(102, "1800101248899", "Bob")
carol = Client(103, "2670511035588", "Carol")
sophia = Client(104, "2990511035588", "Sophia")

hyundai_tucson = Car(201, "CJ 02 TWD", "Hyundai", "Tucson")
toyota_corolla = Car(202, "CJ 02 FWD", "Toyota", "Corolla")
dacia_sandero = Car(203, "IS 99 RTY", "Dacia", "Sandero")

# TODO Make sure that after reading from input files, Rentals are still linked to Car & Client objects
#   Persist the client and car ID when writing rentals to file
#   When loading rentals from file, we should have cars & clients already available
rental_sophia_toyota = Rental(302, sophia, hyundai_tucson, date(2016, 12, 1), date(2016, 12, 31))
rental_sophia_tucson = Rental(301, sophia, hyundai_tucson, date(2016, 11, 1), date(2016, 11, 30))
rental_bob_dacia = Rental(303, bob, dacia_sandero, date(2021, 12, 1), date(2021, 12, 31))

"""
    1. Use in-memory Repository
"""
car_repo = Repository()
car_repo.store(hyundai_tucson)
car_repo.store(toyota_corolla)
car_repo.store(dacia_sandero)

client_repo = Repository()
client_repo.store(alice)
client_repo.store(bob)
client_repo.store(carol)
client_repo.store(sophia)

rental_repo = Repository()
rental_repo.store(rental_bob_dacia)
rental_repo.store(rental_sophia_toyota)
rental_repo.store(rental_sophia_tucson)

# TODO Implement 2. and test it as a PyUnit test
# TODO Pass file name as a __init__ parameter
"""
    2. Use text file Repository
    
    class CarTextFileRepo(Repository)
        pass
    
    class ClientTextFileRepo(Repository)
        pass
    
    class RentalTextFileRepo(Repository)
        pass
"""

# TODO Implement 3. and test it as a PyUnit test
"""
    3. Use binary file Repositories
    
    class BinaryFileRepo(Repository)
        pass
"""

# TODO Implement 4. and test it as a PyUnit test
"""
   4. Use a single text-file Repository
   
    class TextFileRepo(Repository):
        pass 
        
    implement a pair of functions for each domain entity:
        car_to_file(car) -> str
        file_to_car(str) -> Car
        
    pass these functions as __init__ parameters

"""
