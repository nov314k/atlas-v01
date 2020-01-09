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


class FileTabs(QTabWidget):
    """Docstring."""

    def __init__(self):
        """Docstring."""

        super(FileTabs, self).__init__()
        self.setStyleSheet("""
            font-size: 12px;
        """)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.removeTab)
        self.currentChanged.connect(self.change_tab)

    def remove_tab(self, tab_idx):
        """Remove tab with index `tab_idx`."""

        super(FileTabs, self).removeTab(tab_idx)

    def change_tab(self, tab_id):
        """Docstring."""

        current_tab = self.widget(tab_id)
        window = self.nativeParentWidget()
        if current_tab:
            window.update_title(current_tab.label)
        else:
            window.update_title(None)

