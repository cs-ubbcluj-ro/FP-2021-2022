class StudentCRUDException(Exception):
    pass


class ValidationException(StudentCRUDException):
    def __init__(self, msgs):
        """
         Initialise
         msg is a list of strings (errors)
        """
        self.__msgs = msgs

    @property
    def messages(self):
        return self.__msgs

    def __str__(self):
        return str(self.__msgs)


class StudentValidator:
    """
      Class responsible with the validation for students
      GRASP - Protect Variation

    """

    def __init__(self):
        pass

    @staticmethod
    def validate(st):
        """
          Validate student
          raise ValidationException if id, name, or addres is empty
        """
        error_messages = []
        if st.id == "":
            error_messages.append("Id can not be empty")
        if st.name == "":
            error_messages.append("Name can not be empty")
        if st.address is None or st.address.street == "":
            error_messages.append("Address can not be empty")
        # if there is a validation error throw exception
        if len(error_messages) > 0:
            raise ValidationException(error_messages)
