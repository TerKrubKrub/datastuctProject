import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)

        # self.loginbutton ตั้งไว้ใน Qt Design
        self.loginbutton.clicked.connect(self.loginfunction)

        # set password invisible
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):

        # self.email, self.password ตั้งไว้ใน Qt Design (Line Edit)
        email = self.email.text() # เก็บค่าที่พิมพ์ลงในช่อง email (ใน ui) ลงตัวแปร email
        pasword = self.password.text()
        print("successfully email:", email, "passwor:", pasword)

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("create-Acc.ui", self)

        self.signupbutton.clicked.connect(self.createaccfunction)

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            print("successfully created acc with email:", email, "and password:", password)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)


app = QApplication(sys.argv)

mainwindow = Login()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)

# user can't resize window
widget.setFixedWidth(480)
widget.setFixedHeight(620)

widget.show()

app.exec_()