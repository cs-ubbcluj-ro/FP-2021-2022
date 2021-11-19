# Application coordinator
# Use dependency injection pattern to asemble the application

from lecture.examples.ex24_gui.controllers.controllers import StudentController
from lecture.examples.ex24_gui.domain.validators import StudentValidator
from lecture.examples.ex24_gui.repository.file import StudentFileRepository
from lecture.examples.ex24_gui.ui.gui import StudentGUI

val = StudentValidator()

# create repository
# repo = StudentRepository()

repo = StudentFileRepository("students.txt")

# create controller and inject dependencies
ctr = StudentController(val, repo)

# create console ui and provide (inject) the controller
# ui = ConsoleUI(ctr)
ui = StudentGUI(ctr)
ui.start()
