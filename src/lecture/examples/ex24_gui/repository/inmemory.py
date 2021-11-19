from lecture.examples.ex24_gui.domain.validators import StudentCRUDException


class RepositoryException(StudentCRUDException):
    """
      Base class for the exceptions in the repository
    """

    def __init__(self, msg):
        self.__msg = msg

    def messages(self):
        return self.__msg

    def __str__(self):
        return self.__msg


class DuplicatedIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Duplicate student ID")


class StudentRepository:
    """
      Class responsible for managing a list of students (store, retrieve , update, etc)
      GRASP - Pure Fabrication -  Repository Pattern
    """

    def __init__(self):
        self._students = {}

    def store(self, st):
        """
          Store a student
          st - student
          raise DuplicatedIDException for duplicated id
        """
        if st.id in self._students:
            raise DuplicatedIDException()
        self._students[st.id] = st

    def size(self):
        """
          return the number of students in the repository
        """
        return len(self._students)

    def remove(self, id):
        """
          remove a student from the repository
          id - string, the id of the student to be removed
          return student
          post: the repository not contains student with the given id
          raise ValueError if there is no student with the given id
        """
        if id not in self._students:
            raise ValueError("No student for the id:" + id)
        st = self._students[id]
        del self._students[id]
        return st

    def remove_all(self):
        """
          Remove all the students from the repository
        """
        self._students = {}

    def get_all(self):
        """
          Retrive all the students
          return a list with students
        """
        return self._students.values()

    def update(self, id, st):
        """
          Update student in the repository
          id - string, the id of the student to be updated
          st - Student, the updated student
          raise ValueError if there is no student with the given id
        """
        # remove the old student (this will raise exception if there is no student
        self.remove(id)
        # store the student
        self.store(st)

    def find(self, id):
        """
          Find the student for a given id
          id - string
          return student with the given id or None if there is no student with the given id
        """
        if id not in self._students:
            return None
        return self._students[id]
