import unittest

from seminar.group_917.seminar_06_09.domain.car import Car
from seminar.group_917.seminar_06_09.repository.repository_exception import RepositoryException


class CarRepository:
    # TODO Finish implementation
    def __init__(self):
        self._data = {}

    def add(self, car):
        if car.id in self._data.keys():
            raise RepositoryException("Duplicate Car id")
        self._data[car.id] = car

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        try:
            return self._data[item]
        except KeyError:
            raise RepositoryException("Car id not found")

    def filter(self, license=None, make=None, model=None, color=None):
        """
        Filter cars by their parameters

        e.g.
        repo.filter()
        repo.filter(color='red')
        repo.filter(color='black',make = 'Audi')
        repo.filter(make = 'Skoda',model='Fabia')
        repo.filter(license='CJ 01 ABC',make = 'Skoda',model='Fabia',color='blue')

        Implementation
            - ignore all fields that are None
            - filter by those which are not None


        :param license:
        :param make:
        :param model:
        :param color:
        :return: List of filtered cars
        """

        result = []
        for car in self._data:
            # TODO Check that car passes filter
            # result.append(car)
            pass

        return result


def test_car_repo():
    r = CarRepository()

    r.add(Car('100', 'CJ 11 WER', 'Dacia', 'Sandero', 'red'))
    r.add(Car('101', 'CJ 12 WTP', 'Dacia', 'Sandero', 'blue'))

    car_102 = Car('102', 'CJ 13 WER', 'Dacia', 'Sandero', 'red')
    r.add(car_102)
    r.add(Car('103', 'CJ 14 TOY', 'Toyota', 'Avansis', 'red'))
    r.add(Car('104', 'CJ 15 WER', 'Dacia', 'Sandero', 'black'))
    r.add(Car('105', 'CJ 16 ABC', 'Dacia', 'Sandero', 'red'))

    assert len(r) == 6
    # get car with id '102'
    assert r['102'] == car_102
    # also check with __str__
    assert str(r['104']) == str(Car('104', 'CJ 15 WER', 'Dacia', 'Sandero', 'black'))

    # raise RepositoryException
    try:
        assert r['200'] is None
    except RepositoryException as re:
        # test pass
        pass
    except Exception as exc:
        assert False


class CarRepositoryAnotherTest(unittest.TestCase):
    def test_car_dummy(self):
        pass


class CarRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        """
        Runs before any of the defined tests
        """
        self._r = CarRepository()

        self._r.add(Car('100', 'CJ 11 WER', 'Dacia', 'Sandero', 'red'))
        self._r.add(Car('101', 'CJ 12 WTP', 'Dacia', 'Sandero', 'blue'))

        self._car_102 = Car('102', 'CJ 13 WER', 'Dacia', 'Sandero', 'red')
        self._r.add(self._car_102)
        self._r.add(Car('103', 'CJ 14 TOY', 'Toyota', 'Avansis', 'red'))
        self._r.add(Car('104', 'CJ 15 WER', 'Dacia', 'Sandero', 'black'))
        self._r.add(Car('105', 'CJ 16 ABC', 'Dacia', 'Sandero', 'red'))

    def test_repo_elems(self):
        # assert len(self._r) == 6, 'Lengths not equal!'
        self.assertEqual(len(self._r), 6, 'Lengths not equal!' + str(self._r))

        # get car with id '102'
        # assert self._r['102'] == self._car_102
        self.assertEqual(self._r['102'], self._car_102)
        # also check with __str__
        # assert str(self._r['104']) == str(Car('104', 'CJ 15 WER', 'Dacia', 'Sandero', 'black'))
        self.assertEqual(str(self._r['104']), str(Car('104', 'CJ 15 WER', 'Dacia', 'Sandero', 'black')))

    def test_repo_exception(self):
        # raise RepositoryException
        # try:
        #     assert self._r['200'] is None
        # except RepositoryException as re:
        #     # test pass
        #     pass
        # except Exception as exc:
        #     assert False

        # self._r.__getItem__ ?
        # self.assertRaises(RepositoryException, self._r['200'], '200')

        with self.assertRaises(RepositoryException):
            self._r['200']

    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass


"""
    Why don't we stick with this way of writing tests?
    1. They can be all over the place -> have a test module 
    2. First False assertion stops all tests
    3. Separate running the program from running tests
    4. Have a nicer way of reporting test results (more flex with test results)
"""
# test_car_repo()

"""
    Alternative to run unittest code 
"""
# unittest.main()
