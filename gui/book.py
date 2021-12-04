import sys, os
from PyQt5 import QtWidgets, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, authen
import rsrc.rsrc
import rsrc.style.book as style


class Book(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/book.ui", self)
        global bookApp
        bookApp = self
        self.rating.valueChanged.connect(self.ratingStars)

    def ratingStars(self):
        print(self.rating.value())

    def setId(self, id):
        self.book_id = id
        self.id_label.setText(str(self.book_id))
