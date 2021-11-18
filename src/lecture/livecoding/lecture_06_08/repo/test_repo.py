import unittest

from lecture.livecoding.lecture_06_08.domain.Ingredient import Ingredient
from lecture.livecoding.lecture_06_08.repo.repository import RepositoryException, Repository


class RepositoryTest(unittest.TestCase):
    """
    class RepositoryTest "is a" unittest.TestCase
    RepositoryTest has all the methods that TestCase has
    """

    def setUp(self) -> None:
        """
        Runs before every test method
        """
        self._repo = Repository()

    def tearDown(self) -> None:
        """
        Runs after every test method
        """
        pass

    def test_empty_repo(self):
        self.assertEqual(len(self._repo), 0)
        # assert len(repo) == 0

    def test_repo_add_one(self):
        self._repo.add(Ingredient(100, "White flour 550"))
        # assert len(repo) == 1
        self.assertEqual(len(self._repo), 1)

    def test_repo_exception(self):
        self._repo.add(Ingredient(100, "White flour 550"))

        with self.assertRaises(RepositoryException):
            self._repo.add(Ingredient(100, "White flour 550"))

    def test_repository(self):
        yeast = Ingredient(101, "Yeast (dry)")
        self._repo.add(yeast)
        self._repo.add(Ingredient(102, "Sugar (white)"))
        # assert len(repo) == 3
        self.assertEqual(len(self._repo), 2)
        # assert repo[101] == yeast
        self.assertEqual(self._repo[101], yeast)

        # try:
        #     x = repo[103]
        #     assert False
        # except RepositoryException:
        #     pass

        # self.assertRaises(RepositoryException,self.__getItem__,103)
        with self.assertRaises(RepositoryException) as re:
            x = self._repo[103]
        self.assertEqual(str(re.exception), "Item with ID not found")

        del self._repo[102]
        # assert len(repo) == 2
        self.assertEqual(len(self._repo), 2)

        # try:
        #     del repo[102]
        #     assert False
        # except RepositoryException:
        #     pass

        with self.assertRaises(RepositoryException):
            x = self._repo[102]
