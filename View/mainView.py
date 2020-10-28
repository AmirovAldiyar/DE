from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QMainWindow, QCheckBox, QTabWidget
from pyqtgraph import PlotWidget, plot
from .graph import Graph
from .page import Page
from .sidebar import Sidebar
from .namedLE import NamedLineEdit

class MainPage(QTabWidget):
    def __init__(self, controller):
        super().__init__()
        self._controller = controller

        self._solution_lineedits=[NamedLineEdit('x_0'),NamedLineEdit('X'),NamedLineEdit('y_0'),NamedLineEdit('N')]
        self._solution_checkboxes=[QCheckBox('Euler method(red)'),QCheckBox('Improved Euler method(green)'),QCheckBox('Runge-Kutta method(blue)')]

        self._solution_button = QPushButton('Plot')


        self._solution_graphs = [Graph(self._controller.solution_get_graphs()), Graph(self._controller.solution_get_lte())]



        def onPushPlot():
            self._controller.solution_recalculate(x_0=self._solution_lineedits[0].text(), X=self._solution_lineedits[1].text(), y_0=self._solution_lineedits[2].text(), step=self._solution_lineedits[3].text())
            graphs=self._controller.solution_get_graphs()
            errors=self._controller.solution_get_lte()
            cnt = 0
            for checkbox in self._solution_checkboxes:
                if not checkbox.isChecked():
                    print(checkbox.isChecked())
                    graphs[cnt if cnt == 0 else cnt+1]=[[],[],[0,0,0]]
                    errors[cnt]=[[],[],[0,0,0]]
                cnt+=1
            self._solution_graphs[0].replot(graphs)
            self._solution_graphs[1].replot(errors)

        self._solution_button.clicked.connect(onPushPlot)

        self._solution_lines = self._controller.solution_get_graphs()

        # self._error_graphs = controller.get_error_graphs()
        print(self._controller.solution_get_graphs())

        self._solution_page = Page(graphs=self._solution_graphs, lineedits=self._solution_lineedits, checkboxes=self._solution_checkboxes, button=self._solution_button)

        self._error_graphs=[Graph(self._controller.error_get_graphs(5, 10))]
        self._error_lineedits=[NamedLineEdit('n_0'), NamedLineEdit('N')]
        self._error_checkboxes=[]
        self._error_button=QPushButton('Plot')

        def onPush():
            self._error_graphs[0].replot(self._controller.error_get_graphs(int(self._error_lineedits[0].text()), int(self._error_lineedits[1].text())))

        self._error_button.clicked.connect(onPush)

        self._error_page = Page(graphs=self._error_graphs, lineedits=self._error_lineedits, checkboxes=[], button=self._error_button)

        self.addTab(self._solution_page, "Solution")
        self.addTab(self._error_page, "Error")


