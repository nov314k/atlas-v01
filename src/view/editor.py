"""Docstring."""

import os
import os.path
import re
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QApplication

from view.font import Font
from logic import NEWLINE


#def language():
#    """Docstring."""
#
#    return 'pmd.txt'
#
#
#def description():
#    """Docstring."""
#
#    return 'pmd.txt'


class EditorPane(QsciScintilla):
    """Docstring."""

    open_file = pyqtSignal(str)

    def __init__(self, path, text, newline=NEWLINE):
        """Docstring."""

        super().__init__()
        self.setUtf8(True)
        self.path = path
        self.setText(text)
        self.newline = newline
        self.previous_selection = {
            'line_start': 0, 'col_start': 0, 'line_end': 0, 'col_end': 0
        }
        self.setModified(False)
        # ~ self.breakpoint_handles = set()
        self.setMarginLineNumbers(0, True)
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor('#ffe4e4'))
        self.configure()

    def wheel_event(self, event):
        """Docstring."""

        if not QApplication.keyboardModifiers():
            super().wheelEvent(event)

    def configure(self):
        """Docstring."""

        font = Font().load()
        self.setFont(font)
        self.setUtf8(True)
        self.setAutoIndent(True)
        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)
        self.setIndentationGuides(True)
        self.setBackspaceUnindents(True)
        self.setTabWidth(4)
        self.setEdgeColumn(119)
        self.setEdgeMode(1)
#        self.setEdgeColor(data.QColor(180, 180, 180, alpha=250))
        self.setMarginLineNumbers(0, True)
        self.setMarginWidth(0, 25)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)
#        self.SendScintilla(QsciScintilla.SCI_SETEDGECOLUMN, 80)
        self.setMarginSensitivity(0, True)
        self.setMarginSensitivity(1, True)
        self.setMarginWidth(4, 8)
        self.setMarginSensitivity(4, True)
        self.selectionChanged.connect(self.selection_change_listener)

    @property
    def label(self):
        """Docstring."""

        if self.path:
            label = os.path.basename(self.path).split('.')[0]
        else:
            label = 'untitled'
        if self.isModified():
            return label + ' *'
        return label

    def selection_change_listener(self):
        """Docstring."""

        line_from, index_from, line_to, index_to = self.getSelection()
        if self.previous_selection['col_end'] != index_to or \
                self.previous_selection['col_start'] != index_from or \
                self.previous_selection['line_start'] != line_from or \
                self.previous_selection['line_end'] != line_to:
            self.previous_selection['line_start'] = line_from
            self.previous_selection['col_start'] = index_from
            self.previous_selection['line_end'] = line_to
            self.previous_selection['col_end'] = index_to
            # Highlight matches
            # ~ self.reset_search_indicators()
            # ~ self.highlight_selected_matches()