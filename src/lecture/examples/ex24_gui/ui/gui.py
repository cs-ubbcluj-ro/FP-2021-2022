from tkinter import *
from tkinter import messagebox


class StudentGUI:
    """
      Implement the graphic user interface for add/list students
    """

    def __init__(self, ctrl):
        self.frame = None
        self.tk = Tk()
        self.ctrl = ctrl

    def start(self):
        self.tk.title("Student CRUD")

        frame = Frame(self.tk)
        frame.pack()
        self.frame = frame

        lbl = Label(frame, text="ID:")
        lbl.pack(side=LEFT)

        self.idtf = Entry(frame, {})
        self.idtf.pack(side=LEFT)

        lbl = Label(frame, text="Name:")
        lbl.pack(side=LEFT)

        self.nametf = Entry(frame, {})
        self.nametf.pack(side=LEFT)

        lbl = Label(frame, text="Street:")
        lbl.pack(side=LEFT)

        self.streettf = Entry(frame, {})
        self.streettf.pack(side=LEFT)

        lbl = Label(frame, text="Nr.:")
        lbl.pack(side=LEFT)

        self.nrtf = Entry(frame, {})
        self.nrtf.pack(side=LEFT)

        lbl = Label(frame, text="City:")
        lbl.pack(side=LEFT)

        self.citytf = Entry(frame, {})
        self.citytf.pack(side=LEFT)

        self.storeBtn = Button(frame, text="Store", command=self._store_pressed)
        self.storeBtn.pack(side=LEFT)

        self.listBtn = Button(frame, text="List", command=self._list_students)
        self.listBtn.pack(side=LEFT)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.tk.mainloop()

    def _store_pressed(self):
        """
          Handler method for store button pressed
          Store the student
          Show error messages on exceptions
        """
        try:
            st = self.ctrl.create(self.idtf.get(), self.nametf.get(), self.streettf.get(), self.nrtf.get(),
                                  self.citytf.get())
            messagebox.showinfo("Stored", "Student %s saved.." % st.name)
        except Exception as e:
            messagebox.showinfo("Error", "Error saving student - " + str(e))

    def _list_students(self):
        """
          Handler method for list button
          Show all the students
        """
        sts = self.ctrl.search("")
        txt = "ID".ljust(5) + "Name".ljust(15) + "Address\n"
        for st in sts:
            txt += st.id.ljust(5) + st.name.ljust(15) + str(st.address)
            txt += "\n"
        messagebox.showinfo("List students", txt)
