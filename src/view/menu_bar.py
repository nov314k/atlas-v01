"""Docstring."""

from PyQt5.QtWidgets import QDesktopWidget, QMenuBar


def screen_size():
    """Docstring."""

    screen = QDesktopWidget().screenGeometry()
    return screen.width(), screen.height()


class MenuBar(QMenuBar):
    """Docstring."""

    def __init__(self, parent):
        """Docstring."""

        super().__init__(parent)

    def setup(self):
        """Docstring."""

        self.addMenu("&Portfolio")
        self.addMenu("la&File")
        self.addMenu("&Task")
        self.addMenu("&Log")
