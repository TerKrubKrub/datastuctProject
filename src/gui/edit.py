import sys, os, sqlite3
from PyQt5 import QtWidgets, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, authen
import rsrc.rsrc
import rsrc.style.edit as style


class Edit(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/edit.ui", self)
        self.back_btn.clicked.connect(self.goToProfile)

    def goToProfile(self):
        authen.mainApp.setWindowTitle("Booque - profile")
        authen.mainApp.app_panel.setCurrentIndex(1)
