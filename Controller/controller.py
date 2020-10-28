from Model import SolutionPageData
from PyQt5.QtWidgets import QMainWindow, QApplication
from View import MainPage
from tabulate import tabulate

class controller:
    def __init__(self):
        self.solution_data = SolutionPageData(10.0, 1.0, 5.0, 2.0)


    def solution_recalculate(self, step, x_0, X, y_0):
        self.solution_data.set_params(step=step, X=X, x_0=x_0, y_0=y_0)
        self.solution_data.recalculate()

    def solution_get_graphs(self):
        return self.solution_data.get_lineedits()

    def solution_get_lte(self):
        return self.solution_data.get_lte()

    def error_get_graphs(self, n_0, N):
        return self.solution_data.get_gte(n_0, N)

    def run_app(self):
        class Window(QMainWindow):

            def __init__(self):
                super(Window, self).__init__()
                self.setGeometry(50, 50, 1000, 1000)
                self.setWindowTitle("Differential Equation!")
                self.controller = controller()
                self.page = MainPage(self.controller)
                self.setCentralWidget(self.page)
                self.show()

        app = QApplication([])
        gui = Window()
        app.exec_()
