import unittest

from seminar.group_911.seminar_06_09.domain.car import Car
from seminar.group_911.seminar_06_09.repository.repository_exception import RepositoryException


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

    # TODO Implement the __len__ function for this
    assert len(repo) == 0  # no cars added to repository

    repo.add(Car('100', 'CJ 10 WER', 'Dacia', 'Sandero', 'red'))
    car_101 = Car('101', 'CJ 10 TOY', 'Toyota', 'RAV4', 'red')
    repo.add(car_101)
    repo.add(Car('102', 'CJ 10 AUD', 'Audi', 'Q4', 'blue'))
    assert len(repo) == 3  # 3 cars in the repo

    # TODO Implement __getItem__ function for subscipt operator [...]
    assert repo['101'] == car_101

    try:
        # TODO Raise exception if car with given id was not found
        x = repo['200']
        assert False, 'This should have raised an exception'
    except RepositoryException:
        pass
    except Exception:
        assert False, 'This should have raised a RepoException specifically!'


"""
    PyUnit unit test below
    1. Tell the test runner that this is a test case
"""

class CarRepositoryDummyTest(unittest.TestCase):
    def test_dummy(self):
        pass


class CarRepositoryTest(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment (Create objects/files/data bases/connections etc)
        It runs before any of the tests
        """
        self._repo = CarRepository()

    """
    Test functions are run between the call to setUp and the call to tearDown
    They have to be named test_*
    """

    def test_repo_exceptions(self):
        # try:
        #     # TODO Raise exception if car with given id was not found
        #     x = self._repo['200']
        #     assert False, 'This should have raised an exception'
        # except RepositoryException:
        #     pass
        # except Exception:
        #     assert False, 'This should have raised a RepoException specifically!'

        with self.assertRaises(RepositoryException):
            '''
            Test fails:
                Element with id '200' not in dictionary
            When does the test fail:
                - No exception is being raised
                - Raise a different Exception type
            '''
            x = self._repo['200']



    def test_repo_elements(self):
        # assert len(repo) == 0  # no cars added to repository
        self.assertEqual(len(self._repo), 0)

        self._repo.add(Car('100', 'CJ 10 WER', 'Dacia', 'Sandero', 'red'))
        car_101 = Car('101', 'CJ 10 TOY', 'Toyota', 'RAV4', 'red')
        self._repo.add(car_101)
        self._repo.add(Car('102', 'CJ 10 AUD', 'Audi', 'Q4', 'blue'))
        # assert len(self._repo) == 3  # 3 cars in the repo
        self.assertEqual(len(self._repo), 3)

        # TODO Implement __getItem__ function for subscipt operator [...]
        # assert self._repo['101'] == car_101
        self.assertEqual(self._repo['101'], car_101)

    def tearDown(self) -> None:
        """
        Tear down the test environment (deallocate objects/delete files/close databases etc)
        Runs after all test functions
        """
        self._repo = None


"""
    What could we improve on the way we run tests?
        1. Easier/shorter way to write test cases
        2. Try to run all the tests, even when some of them fail
        3. Report results of testing nicely (nicely= GUI report, HTML, send me an email, etc...)
        4. Separate running tests from running the program
            running tests = during evelopment, clients should not see it/be exposed to it
            running the program = tests have already passed, so no reason to keep running them
            
    unittest tries to provide an answer for all of these...
"""

# test_car_repository()
