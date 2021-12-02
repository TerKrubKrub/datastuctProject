import sys, os, sqlite3
from PyQt5 import QtWidgets, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, authen
import rsrc.rsrc
import rsrc.style.library as style


class Library(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/library.ui", self)
        self.book_btn.clicked.connect(self.goToBook)

    def goToBook(self):
        authen.mainApp.setWindowTitle("Booque - ")
        authen.mainApp.app_panel.setCurrentIndex(6)
