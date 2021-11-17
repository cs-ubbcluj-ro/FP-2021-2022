import unittest

from lecture.livecoding.lecture_06_08.domain.Ingredient import Ingredient


class RepositoryException(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass


class Repository:
    """
    You have two choices:
        1. Implement a separate Repo class for each entity
        2. Implement a single Repo class with different objects for each entity

    Lecture -> we try approach 2
    Lab -> both work fine (approach 1 is easier, but there's more code :) )
    """

    def __init__(self):
        self.__data = dict()  # list() set()

    def add(self, entity):
        if entity.id in self.__data:
            raise RepositoryException("Entity with Id " + str(entity.id) + " already in repo")
        self.__data[entity.id] = entity

    def __getitem__(self, item):
        return self.__data[item]


def test_repository():
    repo = Repository()

    repo.add(Ingredient(100, "White flour 550", 100))
    repo[100].stock += 50
    assert repo[100].stock == 150

    # repo.add(Ingredient(100, "White flour 550", 100))

# test_repository()
