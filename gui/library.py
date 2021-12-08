import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import authen, book, db
import rsrc.rsrc
import rsrc.style.library as style


class Library(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/library.ui", self)
        global libApp
        libApp = self
        self.setStyleSheet(style.default)
        self.book_ids = []
        self.book_titles = []
        self.book_imgs = []
        self.book_authors = []
        self.column = 4
        self.sort = 0
        self.no_match.hide()
        self.updateCatalog(db.database.books_ll)
        self.search_btn.clicked.connect(self.search)
        self.sort_box.activated.connect(lambda x: self.setSort(x))
        self.genre_box.activated.connect(lambda x: self.setGenre(x))

    def goToBook(self, book_id, book_title):
        authen.mainApp.setWindowTitle("Booque - " + book_title)
        authen.mainApp.app_panel.setCurrentIndex(5)
        book.bookApp.setId(int(book_id))

    def clearLayout(self, layout):
        self.book_ids = []
        self.book_titles = []
        self.book_imgs = []
        self.book_authors = []
        self.pos = []
        self.button = []
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clearLayout(child.layout())

    def updateCatalog(self, ll, type=None):
        self.clearLayout(self.book_shelf)
        if not type:
            self.cur_ll = ll
        if ll:
            self.no_match.hide()
            for i in range(len(ll)):
                self.book_ids.append(ll[i][0])
                self.book_titles.append(ll[i][1])
                self.book_imgs.append(ll[i][2])
                self.book_authors.append(ll[i][3])
            self.pos = [
                [r, c]
                for r in range(int(len(ll) / self.column) + 1)
                for c in range(self.column)
            ]
            self.button = [
                [[] for c in range(self.column)]
                for r in range(int(len(ll) / self.column) + 1)
            ]
            for pos, id, title, img, author in zip(
                self.pos,
                self.book_ids,
                self.book_titles,
                self.book_imgs,
                self.book_authors,
            ):
                self.title_label = QtWidgets.QLabel()
                self.title_label.setText(title)
                self.title_label.setFont(QtGui.QFont("Product Sans", 12))
                self.title_label.setWordWrap(True)
                self.title_label.setAlignment(QtCore.Qt.AlignCenter)
                self.title_label.setMaximumWidth(250)
                self.author_label = QtWidgets.QLabel()
                self.author_label.setText(author)
                self.author_label.setFont(QtGui.QFont("Product Sans", 10))
                self.author_label.setWordWrap(True)
                self.author_label.setAlignment(QtCore.Qt.AlignCenter)
                self.author_label.setMaximumWidth(250)
                self.button = QtWidgets.QPushButton()
                self.button.setIcon(QtGui.QIcon(QtGui.QPixmap(img)))
                self.button.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                )
                self.button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.button.setMinimumSize(250, 380)
                self.button.setIconSize(self.button.minimumSize())
                self.button.clicked.connect(
                    lambda x, id=id, title=title: self.goToBook(id, title)
                )
                self.book_container = QtWidgets.QVBoxLayout()
                self.book_container.setSpacing(4)
                self.book_container.addWidget(
                    self.button, 0, alignment=QtCore.Qt.AlignCenter
                )
                self.book_container.addWidget(self.title_label, 1)
                self.book_container.addWidget(self.author_label, 2)
                self.book_shelf.addLayout(self.book_container, *pos)
        else:
            self.no_match.show()

    def search(self):
        if self.search_bar.text():
            temp = self.cur_ll.search(self.search_bar.text())
            self.updateCatalog(temp, 1)
        else:
            self.updateCatalog(self.cur_ll)

    def setSort(self, index):
        self.search_bar.setText("")
        self.sort = index
        self.updateCatalog(self.cur_ll.sort(self.sort))

    def setGenre(self, index):
        self.search_bar.setText("")
        if index == 0:
            self.updateCatalog(db.database.books_ll.sort(self.sort))
        elif index == 1:
            self.updateCatalog(db.database.fictions_ll.sort(self.sort))
        elif index == 2:
            self.updateCatalog(db.database.thrillers_ll.sort(self.sort))
        elif index == 3:
            self.updateCatalog(db.database.fantasies_ll.sort(self.sort))
        elif index == 4:
            self.updateCatalog(db.database.romances_ll.sort(self.sort))
        elif index == 5:
            self.updateCatalog(db.database.biographies_ll.sort(self.sort))
        elif index == 6:
            self.updateCatalog(db.database.comedies_ll.sort(self.sort))
        elif index == 7:
            self.updateCatalog(db.database.horrors_ll.sort(self.sort))
        elif index == 8:
            self.updateCatalog(db.database.poetries_ll.sort(self.sort))
