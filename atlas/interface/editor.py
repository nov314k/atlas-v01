"""Docstring."""

#import keyword
import os
import os.path
import re
#from collections import defaultdict
#from PyQt5.Qsci import (QsciScintilla, QsciLexerPython, QsciLexerHTML, QsciAPIs,
#                        QsciLexerCSS, QsciLexerCustom)
from PyQt5.Qsci import QsciScintilla, QsciLexerCustom
#from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QApplication
from interface.font import Font
from logic import NEWLINE


def language():
    """Docstring."""

    return 'pmd.txt'

def description():
    """Docstring."""

    return 'pmd.txt'

class PmdTxtLexer(QsciLexerCustom):
    """Docstring."""

    def __init__(self, parent):
        """Docstring."""

        super(PmdTxtLexer, self).__init__(parent)
        self.setDefaultColor(QColor('#000000'))
        self.setDefaultPaper(QColor('#ffffff'))
        self.setDefaultFont(QFont('Courier', 8))

        # Initialize colors per style
        self.setColor(QColor('#000000'), 0)   # Black
        self.setColor(QColor('#F70D1A'), 1)   # Ferrari Red
        self.setColor(QColor('#3BB9FF'), 2)   # Deep Sky Blue
        self.setColor(QColor('#CD7F32'), 3)   # Bronze
        self.setColor(QColor('#728C00'), 4)   # Venom Green
        self.setColor(QColor('#008080'), 5)   # Teal Green

        # Initialize paper colors per style
        self.setPaper(QColor('#ffffff'), 0)
        self.setPaper(QColor('#E5E4E2'), 1)    # Platinum
        self.setPaper(QColor('#ffffff'), 2)
        self.setPaper(QColor('#ffffff'), 3)
        self.setPaper(QColor('#ffffff'), 4)

        # Initialize fonts per style
        self.setFont(QFont('Courier', 8), 0)
        self.setFont(QFont('Courier', 8), 1)
        self.setFont(QFont('Courier', 8), 2)
        self.setFont(QFont('Courier', 8), 3)
        self.setFont(QFont('Courier', 8), 4)

    def style_text(self, start, end):
        """Docstring."""

        self.startStyling(start)
        text = self.parent().text()[start:end]
        prec = re.compile(r'[*]\/|\/[*]|\s+|\w+|\W')
        token_list = [(token, len(bytearray(token, 'utf-8')))
                      for token in prec.findall(text)]
        for _, token in enumerate(token_list):
            if token[0] == '#':
                self.setStyling(token[1], 1)
            elif token[0] == '>':
                self.setStyling(token[1], 2)
            elif token[0] in ['dow', 'due', 'rec']:
                self.setStyling(token[1], 4)
            elif token[0] in ['booked', 'daily', 'infra', 'incoming', 'work',
                              'periodic', 'shlist', 'stroth', 'study', 'weekly',
                              'calMaja', 'calCrkveni', 'calPhases',
                              'calAustralia', '+']:
                self.setStyling(token[1], 5)
            elif token[0] in ['dur']:
                self.setStyling(token[1], 3)
            else:
                self.setStyling(token[1], 0)


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
        if self.path:
            self.lexer = PmdTxtLexer(self)
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
        self.setEdgeColumn(79)
        self.setMarginLineNumbers(0, True)
        self.setMarginWidth(0, 25)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)
        self.SendScintilla(QsciScintilla.SCI_SETEDGECOLUMN, 80)
        self.setMarginSensitivity(0, True)
        self.setMarginSensitivity(1, True)
        self.setMarginWidth(4, 8)
        self.setMarginSensitivity(4, True)
        self.selectionChanged.connect(self.selection_change_listener)
        self.set_zoom()

    def set_zoom(self, size='m'):
        """Docstring."""

        sizes = {
            'xs': -4,
            's': -2,
            'm': 1,
            'l': 4,
            'xl': 8,
            'xxl': 16,
            'xxxl': 48,
        }
        self.zoomTo(sizes[size])

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
