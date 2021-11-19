from lecture.examples.ex24_gui.domain.entities import Student, Address


class StudentController:
    """
      Class responsible with the use cases related to Student CRUD
      GRASP Controller
    """

    def __init__(self, val, repo):
        """
          Initialise the controller,
          controller need a validator and a repository to perform the operations
          val - StudentValidator (injected)
          repo - StudentRepository (injected
        """
        self._val = val
        self._repo = repo

    def create(self, id, name, street, nr, city):
        """
          Create validate and store a student
          id,name, street,city- strings
          nr - int
          return Student
          raise ValueEror if the data is invalid, on duplicated id
        """
        # create Student instance
        st = Student(id, name, Address(street, nr, city))
        # validate, raise exception if student is invalid
        self._val.validate(st)
        # store the student, raise exception if duplicated id
        self._repo.store(st)
        return st

    def get_student_count(self):
        """
          Return the number of students
          return int
        """
        return self._repo.size()

    def remove(self, id):
        """
         Remove student with the given id
         id - string, student id
         return Student, the removed Student
         raise ValueError if there is no student with the given id
        """
        return self._repo.remove(id)

    def search(self, criteria):
        """
          Search students with name containing criteria
          criteria string
          return list of students, where the name contains criteria
        """
        all = self._repo.get_all()
        if criteria == "":
            return all

        rez = []
        for st in all:
            if criteria in st.name():
                rez.append(st)
        return rez

    def update(self, id, name, street, nr, city):
        """
          Update student with the given id
          id,name, adr strings
          return the old student
          raise ValueError if the student is invalid, if there is no student with the given id
        """
        newSt = Student(id, name, Address(street, nr, city))

        # validate the student
        self._val.validate(newSt)

        # get the old student
        oldSt = self._repo.find(id)

        # update the student
        self._repo.update(id, newSt)
        return oldSt
