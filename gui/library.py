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
        self.book_rating = []
        self.column = 4
        self.sort = 0
        self.no_match.hide()
        self.updateCatalog(db.database.books_ll)
        self.search_btn.clicked.connect(self.search)
        self.sort_box.activated.connect(lambda x: self.setSort(x))
        self.genre_box.activated.connect(lambda x: self.setGenre(x))
        QtWidgets.QScroller.grabGesture(
            self.scrollArea, QtWidgets.QScroller.LeftMouseButtonGesture
        )

    def goToBook(self, book_id, book_title):
        authen.mainApp.setWindowTitle("Booque - " + book_title)
        authen.mainApp.app_panel.setCurrentIndex(5)
        book.bookApp.setId(int(book_id))

    def clearLayout(self, layout):
        self.book_ids = []
        self.book_titles = []
        self.book_imgs = []
        self.book_authors = []
        self.book_ratings = []
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
            for i in ll:
                self.book_ids.append(i[0])
                self.book_titles.append(i[1])
                self.book_imgs.append(i[2])
                self.book_authors.append(i[3])
                self.book_ratings.append(float(i[7]))
            self.pos = [
                [r, c]
                for r in range(int(len(ll) / self.column) + 1)
                for c in range(self.column)
            ]
            self.button = [
                [[] for c in range(self.column)]
                for r in range(int(len(ll) / self.column) + 1)
            ]
            for pos, id, title, img, author, rating in zip(
                self.pos,
                self.book_ids,
                self.book_titles,
                self.book_imgs,
                self.book_authors,
                self.book_ratings,
            ):
                title_label = QtWidgets.QLabel(self.scrollAreaContents)
                title_label.setText(title)
                title_label.setFont(QtGui.QFont("Product Sans", 12))
                title_label.setWordWrap(True)
                title_label.setAlignment(QtCore.Qt.AlignCenter)
                title_label.setMinimumWidth(250)
                title_label.setMaximumHeight(200)
                author_label = QtWidgets.QLabel(self.scrollAreaContents)
                author_label.setText(author)
                author_label.setFont(QtGui.QFont("Product Sans", 11))
                author_label.setWordWrap(True)
                author_label.setAlignment(QtCore.Qt.AlignCenter)
                author_label.setMinimumWidth(250)
                author_label.setMaximumHeight(30)
                rating_label = QtWidgets.QLabel(self.scrollAreaContents)
                rating_label.setText("⭐ {0:.2f}".format(rating))
                rating_label.setFont(QtGui.QFont("Product Sans", 10))
                rating_label.setWordWrap(True)
                rating_label.setAlignment(QtCore.Qt.AlignCenter)
                rating_label.setMinimumWidth(250)
                rating_label.setMaximumHeight(30)
                button = QtWidgets.QPushButton(self.scrollAreaContents)
                button.setIcon(QtGui.QIcon(QtGui.QPixmap(img)))
                button.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                )
                button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                button.setMinimumSize(250, 380)
                button.setIconSize(button.minimumSize())
                button.clicked.connect(
                    lambda x, id=id, title=title: self.goToBook(id, title)
                )
                book_container = QtWidgets.QVBoxLayout()
                book_container.setSpacing(5)
                book_container.addWidget(button, 0, alignment=QtCore.Qt.AlignCenter)
                book_container.addWidget(title_label, 1)
                book_container.addWidget(author_label, 2)
                book_container.addWidget(rating_label, 3)
                self.book_shelf.addLayout(book_container, *pos)
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
