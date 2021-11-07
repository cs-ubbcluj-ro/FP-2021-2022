from functions import functions


class console:
    def __init__(self):
        self._func = functions()

    def _show_menu(self):
        print("1. Generate rectangles")
        print("2. View rectangles")
        print("3. Exit")

    def _generate_rectangles(self):
        n = input("n=")
        self._func.generate_rectangles(int(n))

    def _show_rectangles(self):
        rectangles = self._func.sort_rectangles()
        for rect in rectangles:
            print(str(rect))

    def start(self):
        while True:
            self._show_menu()
            opt = input("")

            if opt == '1':
                self._generate_rectangles()
            elif opt == '2':
                self._show_rectangles()
            elif opt == '3':
                return
            else:
                print("Invalid menu choice")


ui = console()
ui.start()
