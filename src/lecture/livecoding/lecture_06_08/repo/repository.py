import unittest

from lecture.livecoding.lecture_06_08.domain.IdObject import IdObject
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
        if isinstance(entity, IdObject) is False:
            raise RepositoryException("Repo can only hold IdObject instances")

        """
        entity is either IdObject or one of its derived types
        """
        if entity.id in self.__data:
            raise RepositoryException("Entity with Id " + str(entity.id) + " already in repo")
        self.__data[entity.id] = entity

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, item):
        return self.__data[item]


"""
    Why a unit test framework?
        1. Separate running the program from running the tests
        2. I want to run all the tests, even if some of them fail
        3. I want some nice reports :) (maybe on my email, or twitter)
"""

# def test_repo_again():
#     # TODO Some testing code
#     pass
#
#
# def test_repository():
#     # signal "kilroy was here"
#     repo = Repository()
#     assert len(repo) == 0
#
#     repo.add(Ingredient(100, "White flour 550"))
#     assert len(repo) == 1
#
#     yeast = Ingredient(101, "Yeast (dry)")
#     repo.add(yeast)
#     repo.add(Ingredient(102, "Sugar (white)"))
#     assert len(repo) == 3
#     assert repo[101] == yeast
#
#     try:
#         x = repo[103]
#         assert False
#     except RepositoryException:
#         pass
#
#     del repo[102]
#     assert len(repo) == 2
#
#     try:
#         del repo[102]
#         assert False
#     except RepositoryException:
#         pass

# test_repository()
# test_repo_again()
