from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QMainWindow, QCheckBox
from pyqtgraph import PlotWidget, plot
from .graph import Graph
from .sidebar import Sidebar
from .namedLE import NamedLineEdit

class Page(QWidget):
    def __init__(self, graphs, lineedits, checkboxes, button):
        super().__init__()

        self._graph_layout = QVBoxLayout()

        for graph in graphs:
            self._graph_layout.addWidget(graph)

        self._graph_widget = QWidget()
        self._graph_widget.setLayout(self._graph_layout)

        self._sidebar = Sidebar(lineedits=lineedits, checkboxes=checkboxes, button=button)

        self._layout = QHBoxLayout()
        self._layout.addWidget(self._graph_widget)
        self._layout.addWidget(self._sidebar)

        self.setLayout(self._layout)


