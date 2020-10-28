from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QMainWindow

class NamedLineEdit(QWidget):
    def __init__(self, title):
        super().__init__()

        self._layout=QHBoxLayout()

        self._lineEdit=QLineEdit()

        self._layout.addWidget(QLabel(title))
        self._layout.addWidget(self._lineEdit)

        self.setLayout(self._layout)

    def text(self):
        return self._lineEdit.text()



