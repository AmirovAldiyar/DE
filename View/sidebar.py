from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QMainWindow


class Sidebar(QWidget):
    def __init__(self, lineedits, checkboxes, button):
        super().__init__()

        self._layout = QVBoxLayout()

        for lineedit in lineedits:
            self._layout.addWidget(lineedit)

        for checkbox in checkboxes:
            self._layout.addWidget(checkbox)

        self._layout.addWidget(button)

        self.setLayout(self._layout)



