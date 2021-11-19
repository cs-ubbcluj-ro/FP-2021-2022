from lecture.examples.ex24_gui.domain.entities import Student, Address
from lecture.examples.ex24_gui.repository.inmemory import StudentRepository, RepositoryException


class StudentFileRepository(StudentRepository):
    """
      Store/retrieve students from file
    """

    def __init__(self, file_name):
        """
          initialise repository
          fileName - string, file path where the students are stored
          post: students are loaded from the file
        """
        # properly initialise the base class
        StudentRepository.__init__(self)
        self._fName = file_name
        # load student from the file
        self._load_file()

    def _load_file(self):
        """
          Load students from file
          raise CorruptedFileException if there is an error when reading from the file
        """
        try:
            f = open(self._fName, "r")
        except IOError:
            raise RepositoryException("Input file not found")
        line = f.readline().strip()
        while line != "":
            attrs = line.split(";")
            st = Student(attrs[0], attrs[1], Address(attrs[2], attrs[3], attrs[4]))
            StudentRepository.store(self, st)
            line = f.readline().strip()
        f.close()

    def store(self, st):
        """
          Store the student to the file.Overwrite store
          st - student
          Post: student is stored to the file
          raise DuplicatedIdException for duplicated id
        """
        StudentRepository.store(self, st)
        self._save_file()

    def update(self, id, st):
        """
          Update student in the repository
          id - string, the id of the student to be updated
          st - Student, the updated student
          raise ValueError if there is no student with the given id
        """
        StudentRepository.update(self, id, st)
        self._save_file()

    def remove(self, id):
        """
          remove a student from the repository
          id - string, the id of the student to be removed
          return student
          post: the repository not contains student with the given id
          raise ValueError if there is no student with the given id
        """
        st = StudentRepository.remove(self, id)
        self._save_file()
        return st

    def _save_file(self):
        """
         Store all the students  in to the file
         raise CorruptedFileException if we can not store to the file
        """
        # open file (rewrite file)
        f = open(self._fName, "w")
        sts = StudentRepository.get_all(self)
        for st in sts:
            strf = st.id + ";" + st.name + ";"
            strf = strf + st.address.street + ";" + str(st.address.number) + ";" + st.address.city
            strf = strf + "\n"
            f.write(strf)
        f.close()

    def remove_all(self):
        """
          Remove all the students from the repository
          post: the repository is empty
        """
        StudentRepository.remove_all(self)
        self._save_file()
