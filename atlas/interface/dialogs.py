"""Contains all dialogs used in the application.

Contains classes: PrepareDayDialog, LogProgressDialog, LogExpenseDialog,
AddAdhocTaskDialog.

"""

import json
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
#from PyQt5.QtWidgets import (QCheckBox, QComboBox, QDialog, QDialogButtonBox,
#                             QLabel, QLineEdit, QVBoxLayout)


class PrepareDayDialog(QDialog):
    """Docstring."""

    def __init__(self, parent=None):
        """Initialize PrepareDayDialog."""

        super().__init__(parent)

    def setup(self, target_day=None, target_month=None, target_year=None):
        """Set up the dialog for preparing a day plan.
        
        The dialog gets from the user the date (separately day, month, and year)
        for which to prepare a day plan.
        
        """

        self.setMinimumSize(200, 200)
        self.setWindowTitle("Enter target")
        widget_layout = QVBoxLayout()
        self.setLayout(widget_layout)
        
        self.target_day_term = QLineEdit()
        target_day_label = QLabel("Target day:")
        self.target_day_term.setText(target_day)
        widget_layout.addWidget(target_day_label)
        widget_layout.addWidget(self.target_day_term)
        
        self.target_month_term = QLineEdit()
        target_month_label = QLabel("Target month:")
        self.target_month_term.setText(target_month)
        widget_layout.addWidget(target_month_label)
        widget_layout.addWidget(self.target_month_term)

        self.target_year_term = QLineEdit()
        target_year_label = QLabel("Target year:")
        self.target_year_term.setText(target_year)
        widget_layout.addWidget(target_year_label)
        widget_layout.addWidget(self.target_year_term)
        
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        widget_layout.addWidget(button_box)

    def target_day(self):
        """Return month-day of the date for which to prepare a day plan."""

        return int(self.target_day_term.text())

    def target_month(self):
        """Return month of the date for which to prepare a day plan."""

        return int(self.target_month_term.text())

    def target_year(self):
        """Return year of the date for which to prepare a day plan."""

        return int(self.target_year_term.text())


class LogProgressDialog(QDialog):
    """Dialog for logging progress (the main log)."""

    def __init__(self):
        """Docstring."""

        self.log_entry_term = QLineEdit()

    def setup(self):
        """Docstring."""

        self.setMinimumSize(600, 100)
        self.setWindowTitle("Log Progress")
        widget_layout = QVBoxLayout()
        self.setLayout(widget_layout)
        log_entry_label = QLabel("Log entry:")
        widget_layout.addWidget(log_entry_label)
        widget_layout.addWidget(self.log_entry_term)
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        widget_layout.addWidget(button_box)

    def log_entry(self):
        """Docstring."""

        return self.log_entry_term.text()

class LogExpenseDialog(QDialog):
    """Docstring."""

    def __init__(self):
        """Docstring."""

        self.log_date_term = QLineEdit("2019-11-18")
        self.income_term = QCheckBox("This is an income", self)
        self.second_acct_term = QCheckBox("Charge to second account", self)
        self.log_amount_a_term = QLineEdit()
        self.log_amount_b_term = QLineEdit()
        self.log_desc_term = QLineEdit()
        self.log_cat_term = QComboBox()
        self.log_new_cat_term = QLineEdit()

    def setup(self):
        """Docstring."""

        with open('settings-private/settings.json') as settings_file:
            settings = json.load(settings_file)
            expense_categories = settings['expense_categories']

        self.setMinimumSize(600, 100)
        self.setWindowTitle("Log Expense")

        widget_layout = QVBoxLayout()
        self.setLayout(widget_layout)
        log_date_label = QLabel("Date:")
        widget_layout.addWidget(log_date_label)
        widget_layout.addWidget(self.log_date_term)
        widget_layout.addWidget(self.income_term)
        widget_layout.addWidget(self.second_acct_term)
        log_amount_a_label = QLabel("Amount A:")
        widget_layout.addWidget(log_amount_a_label)
        widget_layout.addWidget(self.log_amount_a_term)
        log_amount_b_label = QLabel("Amount B (transaction processing fee):")
        widget_layout.addWidget(log_amount_b_label)
        widget_layout.addWidget(self.log_amount_b_term)
        log_desc_label = QLabel("Description:")
        widget_layout.addWidget(log_desc_label)
        widget_layout.addWidget(self.log_desc_term)
        log_cat_label = QLabel("Category:")
        for ecat in expense_categories:
            self.log_cat_term.addItem(ecat)
        widget_layout.addWidget(log_cat_label)
        widget_layout.addWidget(self.log_cat_term)
        log_new_cat_label = QLabel("New category:")
        widget_layout.addWidget(log_new_cat_label)
        widget_layout.addWidget(self.log_new_cat_term)
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        widget_layout.addWidget(button_box)

    def log_entry(self):
        """Docstring."""

        return self.log_entry_term.text()


class AddAdhocTaskDialog(QDialog):
    """Docstring."""

    def __init__(self, parent=None):
        """Initialize AddAdhocTask Dialog.
        
        Notes
        -----
        Do not remove `super().__init__(parent)`.
        
        """

        super().__init__(parent)

    def setup(self):
        """Set up the dialog to add an ad hoc task."""

        self.setMinimumSize(600, 100)
        self.setWindowTitle("Add an ad hoc task")
        widget_layout = QVBoxLayout()
        self.setLayout(widget_layout)
        
        adhoc_task_label = QLabel("Ad hoc task:")
        widget_layout.addWidget(adhoc_task_label)
        
        self.adhoc_task_term = QLineEdit()
        widget_layout.addWidget(self.adhoc_task_term)
        self.adhoc_task_term.setFocus()
        
        duration_label = QLabel("dur:")
        widget_layout.addWidget(duration_label)
        
        self.duration_term = QLineEdit()
        widget_layout.addWidget(self.duration_term)
        self.duration_term.setText("0")
        
        self.finished_term = QCheckBox("Task aready finished", self)
        widget_layout.addWidget(self.finished_term)
        
        self.plus_work_term = QCheckBox("This is a +work task", self)
        widget_layout.addWidget(self.plus_work_term)
        
        tags_label = QLabel("Tags (please include '+'):")
        widget_layout.addWidget(tags_label)
        
        self.tags_term = QLineEdit()
        self.tags_term.setText("+adhoc")
        widget_layout.addWidget(self.tags_term)
        
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        widget_layout.addWidget(button_box)

    def adhoc_task(self):
        """Get entered values from the add an ad hoc task dialog."""

        return [self.adhoc_task_term.text(), self.duration_term.text(),
                self.tags_term.text(), self.finished_term.isChecked(),
                self.plus_work_term.isChecked()]
