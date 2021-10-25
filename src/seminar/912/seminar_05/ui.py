from functions import functions


class ui:
    def __init__(self):
        self._func = functions()

    def _main_menu(self):
        print("1. Generate circles")
        print("3. Print circles")
        print("4. Exit")

    def _generate_circles(self):
        n = input("How many circles? ")
        self._func.generate_circles(int(n))

    def _print_circles(self):
        circles = self._func.sort_circle_list()
        for c in circles:
            print(str(c))  # no more to_str functions, we use Python provided syntax

    def start(self):
        while True:
            self._main_menu()
            opt = input()
            if opt == "1":
                self._generate_circles()
            elif opt == "3":
                self._print_circles()
            elif opt == "4":
                return
            else:
                print("Bad selection!")


console = ui()

console.start()
