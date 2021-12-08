import sys, os
from PyQt5 import QtWidgets, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import authen, book, db
import rsrc.rsrc
import rsrc.style.chart as style


class Chart(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/chart.ui", self)
        global chartApp
        chartApp = self
        self.setStyleSheet(style.default)
        self.all_btn.toggled.connect(lambda: self.setGenre(self.all_btn.text()))
        self.fiction_btn.toggled.connect(lambda: self.setGenre(self.fiction_btn.text()))
        self.thriller_btn.toggled.connect(
            lambda: self.setGenre(self.thriller_btn.text())
        )
        self.fantasy_btn.toggled.connect(lambda: self.setGenre(self.fantasy_btn.text()))
        self.rom_btn.toggled.connect(lambda: self.setGenre(self.rom_btn.text()))
        self.bio_btn.toggled.connect(lambda: self.setGenre(self.bio_btn.text()))
        self.com_btn.toggled.connect(lambda: self.setGenre(self.com_btn.text()))
        self.horror_btn.toggled.connect(lambda: self.setGenre(self.horror_btn.text()))
        self.poetry_btn.toggled.connect(lambda: self.setGenre(self.poetry_btn.text()))
        self.no1 = db.database.books_ll.sort(0)[0]
        self.no2 = db.database.books_ll.sort(0)[1]
        self.no3 = db.database.books_ll.sort(0)[2]
        self.no1_btn.setIcon(QtGui.QIcon(QtGui.QPixmap(self.no1[2])))
        self.no1_btn.setIconSize(self.no1_btn.size())
        self.no1_btn.clicked.connect(lambda: self.goToBook(self.no1[0], self.no1[1]))
        self.no1_rating.setText("⭐ {0:.2f}".format(float(self.no1[7])))
        self.no2_btn.setIcon(QtGui.QIcon(QtGui.QPixmap(self.no2[2])))
        self.no2_btn.setIconSize(self.no2_btn.size())
        self.no2_btn.clicked.connect(lambda: self.goToBook(self.no2[0], self.no2[1]))
        self.no2_rating.setText("⭐ {0:.2f}".format(float(self.no2[7])))
        self.no3_btn.setIcon(QtGui.QIcon(QtGui.QPixmap(self.no3[2])))
        self.no3_btn.setIconSize(self.no3_btn.size())
        self.no3_btn.clicked.connect(lambda: self.goToBook(self.no3[0], self.no3[1]))
        self.no3_rating.setText("⭐ {0:.2f}".format(float(self.no3[7])))

    def setGenre(self, genre):
        self.genre_label.setText(genre)
        if genre == "All Genre":
            self.no1 = db.database.books_ll.sort(0)[0]
            self.no2 = db.database.books_ll.sort(0)[1]
            self.no3 = db.database.books_ll.sort(0)[2]
        elif genre == "Fiction":
            self.no1 = db.database.fictions_ll.sort(0)[0]
            self.no2 = db.database.fictions_ll.sort(0)[1]
            self.no3 = db.database.fictions_ll.sort(0)[2]
        elif genre == "Thriller":
            self.no1 = db.database.thrillers_ll.sort(0)[0]
            self.no2 = db.database.thrillers_ll.sort(0)[1]
            self.no3 = db.database.thrillers_ll.sort(0)[2]
        elif genre == "Fantasy":
            self.no1 = db.database.fantasies_ll.sort(0)[0]
            self.no2 = db.database.fantasies_ll.sort(0)[1]
            self.no3 = db.database.fantasies_ll.sort(0)[2]
        elif genre == "Romance":
            self.no1 = db.database.romances_ll.sort(0)[0]
            self.no2 = db.database.romances_ll.sort(0)[1]
            self.no3 = db.database.romances_ll.sort(0)[2]
        elif genre == "Biography":
            self.no1 = db.database.biographies_ll.sort(0)[0]
            self.no2 = db.database.biographies_ll.sort(0)[1]
            self.no3 = db.database.biographies_ll.sort(0)[2]
        elif genre == "Comedy":
            self.no1 = db.database.comedies_ll.sort(0)[0]
            self.no2 = db.database.comedies_ll.sort(0)[1]
            self.no3 = db.database.comedies_ll.sort(0)[2]
        elif genre == "Horror":
            self.no1 = db.database.horrors_ll.sort(0)[0]
            self.no2 = db.database.horrors_ll.sort(0)[1]
            self.no3 = db.database.horrors_ll.sort(0)[2]
        elif genre == "Poetry":
            self.no1 = db.database.poetries_ll.sort(0)[0]
            self.no2 = db.database.poetries_ll.sort(0)[1]
            self.no3 = db.database.poetries_ll.sort(0)[2]
        self.no1_btn.setIcon(QtGui.QIcon(QtGui.QPixmap(self.no1[2])))
        self.no2_btn.setIcon(QtGui.QIcon(QtGui.QPixmap(self.no2[2])))
        self.no3_btn.setIcon(QtGui.QIcon(QtGui.QPixmap(self.no3[2])))

    def goToBook(self, book_id, book_title):
        authen.mainApp.setWindowTitle("Booque - " + book_title)
        authen.mainApp.app_panel.setCurrentIndex(5)
        book.bookApp.setId(int(book_id))
