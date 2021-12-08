import sys, os
from PyQt5 import QtWidgets, QtCore, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, authen, book, db
import rsrc.rsrc
import rsrc.style.home as style


class Home(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/home.ui", self)
        global homeApp
        homeApp = self
        self.setStyleSheet(style.default)
        self.f_name = [str(i[1]) for i in db.database.users_ll if i[0] == app.id][0]
        self.cur_read = [i[7] for i in db.database.users_ll if i[0] == app.id][0]
        self.updateCurBook(self.cur_read)
        self.welcome_label.setText(
            "Welcome, " + self.f_name + "!\nto BOOQUE, your favorite book app."
        )
        self.quote_label.setText(
            '" The world breaks everyone, and afterward, many are strong at the broken places. "'
        )
        self.credit_label.setText("- Ernest Hemingway, A Farewell to Arms")
        self.welcome_label.resizeEvent = self.resizeWelcome
        self.quote_label.resizeEvent = self.resizeQuote
        self.credit_label.resizeEvent = self.resizeCredit

    def resizeWelcome(self, event):
        if self.rect().width() // 75 > 16:
            font = QtGui.QFont(
                "Helvetica Neue LT Medium Ext", self.rect().width() // 75
            )
        else:
            font = QtGui.QFont("Helvetica Neue LT Medium Ext", 16)
        self.welcome_label.setFont(font)

    def resizeQuote(self, event):
        if self.rect().width() // 40 > 30:
            font = QtGui.QFont(
                "Helvetica Neue LT Black Ext", self.rect().width() // 40 - 8
            )
        else:
            font = QtGui.QFont("Helvetica Neue LT Black Ext", 30)
        self.quote_label.setFont(font)

    def resizeCredit(self, event):
        if self.rect().width() // 75 > 16:
            font = QtGui.QFont(
                "Helvetica Neue LT Light Cond", self.rect().width() // 75
            )
        else:
            font = QtGui.QFont("Helvetica Neue LT Light Cond", 16)
        self.credit_label.setFont(font)

    def goToBook(self, book_id, book_title):
        authen.mainApp.setWindowTitle("Booque - " + book_title)
        authen.mainApp.app_panel.setCurrentIndex(5)
        book.bookApp.setId(int(book_id))

    def updateCurBook(self, book_id):
        if book_id:
            self.cur_label.setText("You are currently reading")
            self.cur_btn.setIcon(
                QtGui.QIcon(
                    QtGui.QPixmap(
                        [
                            i[2]
                            for i in db.database.books_ll
                            if int(i[0]) == int(book_id)
                        ][0]
                    )
                )
            )
            self.cur_btn.clicked.connect(
                lambda: self.goToBook(
                    int(book_id),
                    [i[1] for i in db.database.books_ll if int(i[0]) == int(book_id)][
                        0
                    ],
                )
            )
        else:
            self.cur_label.setText("Recommended for you")
            self.recommended_book = db.database.books_ll.recommended()
            self.cur_btn.setIcon(QtGui.QIcon(QtGui.QPixmap(self.recommended_book[2])))
            self.cur_btn.clicked.connect(
                lambda: self.goToBook(
                    self.recommended_book[0], self.recommended_book[1]
                )
            )
        self.cur_btn.setIconSize(self.cur_btn.size())
