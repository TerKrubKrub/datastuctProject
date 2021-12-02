import sys, os,sqlite3
from PyQt5 import QtWidgets, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, authen
import rsrc.rsrc
import rsrc.style.book as style


class Book(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/book.ui", self)
        self.rating.valueChanged.connect(self.ratingStars)

    def ratingStars(self):
        print(self.rating.value())
