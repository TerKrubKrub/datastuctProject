import sys, os
from PyQt5 import QtWidgets, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, db
import rsrc.rsrc
import rsrc.style.request as style


class Request(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/request.ui", self)
        global reqApp
        reqApp = self
        self.setStyleSheet(style.default)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon("rsrc/img/logo.png"))
        self.submit_btn.clicked.connect(self.submitReq)

    def submitReq(self):
        if self.req_title.text().upper() not in [
            i[1].upper() for i in db.database.books_ll
        ] and self.req_author.text().upper() not in [i[2].upper() for i in db.database.books_ll]:
            if self.req_title.text() and self.req_author.text():
                self.req_info = db.RequestNode(
                    app.id, self.req_title.text(), self.req_author.text()
                )
                db.req_q.enqueue(self.req_info)
                self.req_title.setText("")
                self.req_author.setText("")
                self.msg.setIcon(QtWidgets.QMessageBox.Information)
                self.msg.setWindowTitle("Your request has been sent!")
                self.msg.setText(
                    "Successfully sent your request.\nPlease wait at least 24 hours to see your book!"
                )
                self.msg.exec_()
            else:
                self.msg.setWindowTitle("Request information invalid.")
                self.msg.setIcon(QtWidgets.QMessageBox.Warning)
                self.msg.setText("Book title and Author field is required.")
                self.msg.exec_()
        else:
            self.msg.setWindowTitle("Existed book.")
            self.msg.setIcon(QtWidgets.QMessageBox.Warning)
            self.msg.setText("The Book is already existed.")
            self.msg.exec_()
