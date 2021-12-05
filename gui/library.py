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
        self.updateCatalog(db.database.books_ll)
        self.search_btn.clicked.connect(self.search)
        self.sort_box.activated.connect(lambda x: self.handleSortBox(x))
        self.genre_box.activated.connect(lambda x: self.handleGenreBox(x))

    def goToBook(self, book_id):
        authen.mainApp.setWindowTitle("Booque - ")
        authen.mainApp.app_panel.setCurrentIndex(6)
        book.bookApp.setId(int(book_id))

    def search(self):
        db.database.books_ll.search(self.search_bar.text())

    def updateCatalog(self, ll):
        self.cur_ll = ll
        self.clearLayout(self.book_shelf)
        for i in range(len(self.cur_ll)):
            self.book_ids.append(self.cur_ll[i][0])
            self.book_titles.append(self.cur_ll[i][1])
            self.book_imgs.append(self.cur_ll[i][2])
            self.book_authors.append(self.cur_ll[i][3])
        self.pos = [
            [r, c]
            for r in range(int(len(self.cur_ll) / self.column) + 1)
            for c in range(self.column)
        ]
        self.button = [
            [[] for c in range(self.column)]
            for r in range(int(len(self.cur_ll) / self.column) + 1)
        ]
        for [r, c], id, title, img, author in zip(
            self.pos, self.book_ids, self.book_titles, self.book_imgs, self.book_authors
        ):
            self.title_label = QtWidgets.QLabel()
            self.title_label.setText(title)
            self.title_label.setFont(QtGui.QFont("Product Sans", 14))
            self.title_label.setWordWrap(True)
            self.title_label.setAlignment(QtCore.Qt.AlignCenter)
            self.author_label = QtWidgets.QLabel()
            self.author_label.setText(author)
            self.author_label.setFont(QtGui.QFont("Product Sans", 10))
            self.author_label.setWordWrap(True)
            self.author_label.setAlignment(QtCore.Qt.AlignCenter)
            self.button[r][c] = QtWidgets.QPushButton()
            self.pixmap = QtGui.QPixmap(img)
            self.button[r][c].setIcon(QtGui.QIcon(self.pixmap))
            self.button[r][c].setSizePolicy(
                QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
            )
            self.button[r][c].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.button[r][c].setMinimumSize(250, 380)
            self.button[r][c].setIconSize(QtCore.QSize(250, 380))
            self.button[r][c].clicked.connect(lambda x, id=id: self.goToBook(id))
            self.book_container = QtWidgets.QVBoxLayout()
            self.book_container.setSpacing(5)
            self.book_container.addWidget(self.button[r][c], 0)
            self.book_container.addWidget(self.title_label, 1)
            self.book_container.addWidget(self.author_label, 2)
            self.book_shelf.addLayout(self.book_container, *[r, c])

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

    def handleSortBox(self, index):
        if index == 0:
            print("a-z")
        elif index == 1:
            print("z-a")
        elif index == 2:
            print("Rating (most)")
        elif index == 3:
            print("Rating (least)")

    def handleGenreBox(self, index):
        if index == 0:
            self.updateCatalog(db.database.books_ll)
        elif index == 1:
            temp = []
            for i in range(len(db.database.books_ll)):
                if db.database.books_ll[i][6] == "fiction":
                    temp.append(db.database.books_ll[i])
            self.updateCatalog(temp)
        elif index == 2:
            temp = []
            for i in range(len(db.database.books_ll)):
                if db.database.books_ll[i][6] == "thriller":
                    temp.append(db.database.books_ll[i])
            self.updateCatalog(temp)
        elif index == 3:
            print("Fantasy")
        elif index == 4:
            print("Romance")
        elif index == 5:
            print("Biography")
        elif index == 6:
            print("Comedy")
        elif index == 7:
            print("Horror")
        elif index == 8:
            print("Adventure")
