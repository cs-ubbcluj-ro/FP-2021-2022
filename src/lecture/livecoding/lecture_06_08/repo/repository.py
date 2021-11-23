import unittest

from lecture.livecoding.lecture_06_08.domain.IdObject import IdObject
from lecture.livecoding.lecture_06_08.domain.Ingredient import Ingredient
import pickle


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
        self._data = dict()  # list() set()

    def add(self, entity):
        if isinstance(entity, IdObject) is False:
            raise RepositoryException("Repo can only hold IdObject instances")

        """
        entity is either IdObject or one of its derived types
        """
        if entity.id in self._data:
            raise RepositoryException("Entity with Id " + str(entity.id) + " already in repo")
        self._data[entity.id] = entity

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        return self._data[item]


"""
    File-based Repositor(ies)
        1. save/load program data to/from files
        2. file-backed repos to work exactly like in-memory repos from the service perspective
        3. read data from files ->  on program start-up -> repository constructor
        4. write data to files -> every time we change repository data
        5. want to be able to keep using existing repo class -> inheritance 
"""


class IngredientBinFileRepository(Repository):
    def __init__(self):
        super().__init__()

        self._file_name = "ingredients.bin"
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, "rb")  # rt -> read, binary
        self._data = pickle.load(f)
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self._data, f)
        f.close()

    def add(self, entity):
        """
        1. Do whatever the add method in the base class does
        2. Save the ingredients to file
        """
        super(IngredientBinFileRepository, self).add(entity)
        # super().add(entity)
        self._save_file()


class IngredientTextFileRepository(Repository):
    """
    class TextFileRepository inherits from Repository
        Repository -> base class
        TextFileRepository -> derived class, child class

    what are the effects of this inheritance?
        TextFileRepository has all the non-private methods and fields of Repository
        TextFileRepository has the behaviour of its base class

    what does this mean?
        derived class can do everything that the base class can
        derived class might add some new functionality, or work in a different way
    """

    def __init__(self):
        super().__init__()

        self._file_name = "ingredients.txt"
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, "rt")  # rt -> read, text-mode
        for line in f.readlines():
            _id, description = line.split(maxsplit=1, sep=',')
            self.add(Ingredient(int(_id), description.rstrip()))
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wt")  # wt -> write, text-mode

        for ingr in self._data.values():
            f.write(str(ingr.id) + ',' + ingr.description + "\n")

        f.close()

    def add(self, entity):
        """
        1. Do whatever the add method in the base class does
        2. Save the ingredients to file
        """
        super(IngredientTextFileRepository, self).add(entity)
        # super().add(entity)
        self._save_file()


"""
    Why a unit test framework?
        1. Separate running the program from running the tests
        2. I want to run all the tests, even if some of them fail
        3. I want some nice reports :) (maybe on my email, or twitter)
"""

"""
    object -> root of inheritance hierarchy
    similar to -> C#, Java

    class A(object):
        pass
    
    a = A()
    print(str(a))
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
