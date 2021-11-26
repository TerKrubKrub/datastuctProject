import sys
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtWidgets import *
from rsrc import rsrc


class LogIn(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/login.ui", self)
        fontDB = QtGui.QFontDatabase()
        fontDB.addApplicationFont(":/Font/font/Better Grade/Better Grade.ttf")
        fontDB.addApplicationFont(":/Font/font/Product Sans/Product Sans Regular.ttf")
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ext_btn.clicked.connect(self.exit)
        self.min_btn.clicked.connect(self.minimize)
        self.show_pwd.clicked.connect(self.showPassword)
        self.login_btn.clicked.connect(self.logIn)
        self.signup_btn.clicked.connect(self.signUp)
        self.usnErrStyle = "#username { padding-left: 10px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 13px; }"
        self.usnNormStyle = "#username { padding-left: 10px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 16px; }"
        self.pwdErrStyle = "#password { padding-left: 10px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 13px; }"
        self.pwdNormStyle = "#password { padding-left: 10px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 16px; }"

    def mousePressEvent(self, event):
        self.cur_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.cur_pos)
        self.cur_pos = event.globalPos()
        event.accept()

    def minimize(self):
        self.setWindowState(QtCore.Qt.WindowState.WindowMinimized)

    def exit(self):
        sys.exit(0)

    def usnChanged(self, txt):
        if not txt:
            self.username.setStyleSheet(self.usnErrStyle)
        else:
            self.username.setStyleSheet(self.usnNormStyle)

    def pwdChanged(self, txt):
        if not txt:
            self.password.setStyleSheet(self.pwdErrStyle)
        else:
            self.password.setStyleSheet(self.pwdNormStyle)

    def logIn(self, event):
        self.username.clear()
        self.password.clear()
        if self:  # if matched
            # to database
            self.toHome()
        else:
            if self.username.text() == "":
                self.username.setStyleSheet(self.usnErrStyle)
            if self.password.text() == "":
                self.password.setStyleSheet(self.pwdErrStyle)
            self.username.textChanged.connect(self.usnChanged)
            self.password.textChanged.connect(self.pwdChanged)
            self.username.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "LogIn", "⚠ The username or password is incorrect."
                )
            )
            self.password.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "LogIn", "⚠ The username or password is incorrect."
                )
            )
        event.accept()

    def signUp(self, event):
        self.toSignUp()

    def toSignUp(self):
        self.sign_up = SignUp()
        self.sign_up.show()
        self.close()

    def showPassword(self):
        if self.password.echoMode() == QLineEdit.Normal:
            self.password.setEchoMode(QLineEdit.Password)
        else:
            self.password.setEchoMode(QLineEdit.Normal)


class SignUp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/signup.ui", self)
        fontDB = QtGui.QFontDatabase()
        fontDB.addApplicationFont(":/Font/font/Better Grade/Better Grade.ttf")
        fontDB.addApplicationFont(":/Font/font/Product Sans/Product Sans Regular.ttf")
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ext_btn.mousePressEvent = self.exit
        self.min_btn.mousePressEvent = self.minimize
        self.signup_btn.clicked.connect(self.signUp)
        self.show_pwd.clicked.connect(self.showPassword)
        self.show_repwd.clicked.connect(self.showRePassword)

    def mousePressEvent(self, event):
        self.cur_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.cur_pos)
        self.cur_pos = event.globalPos()
        event.accept()

    def minimize(self, event):
        self.setWindowState(QtCore.Qt.WindowState.WindowMinimized)
        event.accept()

    def exit(self, event):
        event.accept()
        sys.exit(0)

    def toLogIn(self):
        self.log_in = LogIn()
        self.log_in.show()
        self.close()

    def signUp(self):
        # to database
        self.toLogIn()

    def showPassword(self):
        if self.password.echoMode() == QLineEdit.Normal:
            self.password.setEchoMode(QLineEdit.Password)
        else:
            self.password.setEchoMode(QLineEdit.Normal)

    def showRePassword(self):
        if self.re_password.echoMode() == QLineEdit.Normal:
            self.re_password.setEchoMode(QLineEdit.Password)
        else:
            self.re_password.setEchoMode(QLineEdit.Normal)
