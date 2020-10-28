from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QMainWindow
from pyqtgraph import PlotWidget, plot, PlotWindow
import pyqtgraph as pg

class Graph(PlotWindow):
    def __init__(self, lines):
        super().__init__()
        self.replot(lines)
    def replot(self, lines):
        self.clear()
        for line in lines:
            pen = pg.mkPen(color=(line[2][0],line[2][1],line[2][2]), width=2)
            self.plot(line[0], line[1] ,pen=pen)



