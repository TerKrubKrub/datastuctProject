import sys, os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app
import rsrc.rsrc
import rsrc.style.request as style


class Request(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/request.ui", self)
        global reqApp
        reqApp = self
        self.setStyleSheet(style.default)
        self.db = sqlite3.connect("rsrc/db/data.db")
        self.curs = self.db.cursor()
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon(":/Image/img/logo.png"))
        self.submit_btn.clicked.connect(self.submitReq)

    def submitReq(self):
        if self.req_title.text() and self.req_author.text():
            self.req_info = [
                app.id,
                self.req_title.text(),
                self.req_author.text(),
            ]
            self.curs.execute(
                "INSERT INTO requests (user_id, title, author) VALUES (?,?,?)",
                self.req_info,
            )
            self.db.commit()
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
