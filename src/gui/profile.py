import sys, os, sqlite3
from PyQt5 import QtWidgets, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, authen
import rsrc.rsrc
import rsrc.style.profile as style


class Profile(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/profile.ui", self)
        self.edit_btn.clicked.connect(self.goToEdit)

    def goToEdit(self):
        authen.mainApp.setWindowTitle("Booque - edit profile")
        authen.mainApp.app_panel.setCurrentIndex(2)
