import unittest

from seminar.group_912.seminar_06_09.domain.car import Car
from seminar.group_912.seminar_06_09.repository.repository_exception import RepositoryException


class CarRepository:
    # TODO Finish implementation
    def __init__(self):
        self._data = {}

    def add(self, car):
        if car.id in self._data.keys():
            raise RepositoryException("Duplicate Car id")
        self._data[car.id] = car

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


def test_car_repository():
    repo = CarRepository()
    # TODO Implement the len operation for car repository -> __len__
    # repo length is how many cars it holds
    assert len(repo) == 0

    car_100 = Car('100', 'CJ 10 WER', 'Dacia', 'Sandero', 'green')
    repo.add(car_100)
    repo.add(Car('101', 'CJ 10 WER', 'Dacia', 'Sandero', 'red'))
    repo.add(Car('102', 'CJ 10 TOY', 'Toyota', 'RAV4', 'blue'))
    repo.add(Car('103', 'CJ 10 WER', 'Dacia', 'Sandero', 'red'))
    assert len(repo) == 4

    try:
        repo.add(Car('100', 'CJ 10 WER', 'Dacia', 'Sandero', 'green'))
        assert False, 'There should have been a RepoException raised here!'
    except RepositoryException:
        pass

    # TODO Implement the [...] operator for car repository -> __getItem__
    assert repo['100'] == car_100

    try:
        # TODO Make sure the [...] operator raises exception when it has to
        x = repo['200']
        assert False, 'There should have been a RepoException raised here!'
    except RepositoryException:
        pass


"""
    Let's turn the code above into a proper PyUnit unit test
    
    We need to "tell" unittest test runner which are the tests
"""


class CarRepositoryTestDummy(unittest.TestCase):
    def test_dummy(self):
        pass


class CarRepositoryTest(unittest.TestCase):
    def setUp(self):
        """
        Runs before any of the tests
        Used to set up the class so that tests can be run

        :return: None
        """
        self._repo = CarRepository()
        self._car_100 = Car('100', 'CJ 10 WER', 'Dacia', 'Sandero', 'green')
        self._repo.add(self._car_100)

    '''
    Define test functions (test cases) using functions named test_*
    '''

    def test_repo_elements(self):
        # assert len(self._repo) == 0
        self.assertEqual(len(self._repo), 1)

        self._repo.add(Car('101', 'CJ 10 WER', 'Dacia', 'Sandero', 'red'))
        self._repo.add(Car('102', 'CJ 10 TOY', 'Toyota', 'RAV4', 'blue'))
        self._repo.add(Car('103', 'CJ 10 WER', 'Dacia', 'Sandero', 'red'))
        # assert len(self._repo) == 4
        self.assertEqual(len(self._repo), 4)

    def test_repo_exception(self):
        self.assertRaises(RepositoryException, self._repo.add, Car('100', 'CJ 10 WER', 'Dacia', 'Sandero', 'green'))
        # try:
        #     self._repo.add(Car('100', 'CJ 10 WER', 'Dacia', 'Sandero', 'green'))
        #     assert False, 'There should have been a RepoException raised here!'
        # except RepositoryException:
        #     pass

        # TODO Implement the [...] operator for car repository -> __getItem__
        # assert self._repo['100'] == self._car_100
        self.assertEqual(self._repo['100'], self._car_100)

        # try:
        #     # TODO Make sure the [...] operator raises exception when it has to
        #     x = self._repo['200']
        #     assert False, 'There should have been a RepoException raised here!'
        # except RepositoryException:
        #     pass
        with self.assertRaises(RepositoryException):
            x = self._repo['200']

    def tearDown(self) -> None:
        """
        Runs after all the tests have completed
        Used to close the test environment (clase files, DB connections, deallocate memory)

        :return: None
        """
        self._repo = None


"""
    Why aren't these tests good enough? :) 
        1. Testing stops with the first assert == False !
        2. We don't have a testing report (get an email every morning with test reports)
        3. We don't separate running tests from running the program
        
    unittest module (and many other similar ones) solve these issues
"""
# test_car_repository()
unittest.main()