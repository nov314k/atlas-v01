"""Docstring."""

from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import (QAction, QDesktopWidget, QWidget, QVBoxLayout,
                             QTabWidget, QFileDialog, QMessageBox, QMainWindow,
                             QStatusBar, QShortcut, QMenuBar)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtGui import QIcon
from pkg_resources import resource_filename
from view.prepare_day_dialog import PrepareDayDialog
from view.log_progress_dialog import LogProgressDialog
from view.add_adhoc_task_dialog import AddAdhocTaskDialog
from view.editor_pane import EditorPane


def screen_size():
    """Docstring."""

    screen = QDesktopWidget().screenGeometry()
    return screen.width(), screen.height()


class MenuBar(QMenuBar):
    """Docstring."""

    def __init__(self, parent):
        """Docstring."""

#        super().__init__(parent)
        pass

    def setup(self):
        """Docstring."""

        self.addMenu("&Portfolio")
        self.addMenu("la&File")
        self.addMenu("&Task")
        self.addMenu("&Log")

