from datetime import date

from seminar.group_912.seminar_09.domain.Car import Car
from seminar.group_912.seminar_09.domain.Client import Client
from seminar.group_912.seminar_09.domain.Rental import Rental

alice = Client(101, "2801010266699", "Alice")
bob = Client(102, "1800101248899", "Bob")
carol = Client(103, "2670511035588", "Carol")
sophia = Client(104, "2990511035588", "Sophia")

hyundai_tucson = Car(201, "CJ 02 TWD", "Hyundai", "Tucson")
toyota_corolla = Car(202, "CJ 02 FWD", "Toyota", "Corolla")
dacia_sandero = Car(203, "IS 99 RTY", "Dacia", "Sandero")

rental_sophia_tucson = Rental(301, sophia, hyundai_tucson, date(2016, 11, 1), date(2016, 11, 30))
rental_sophia_toyota = Rental(302, sophia, hyundai_tucson, date(2016, 12, 1), date(2016, 12, 31))
rental_bob_dacia = Rental(303, bob, dacia_sandero, date(2021, 12, 1), date(2021, 12, 31))
