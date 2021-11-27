import sys,os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui, uic
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import rsrc.rsrc


class LogIn(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/login.ui", self)
        self.fontDB = QtGui.QFontDatabase()
        self.fontDB.addApplicationFont(":/Font/font/Better Grade/Better Grade.ttf")
        self.fontDB.addApplicationFont(
            ":/Font/font/Product Sans/Product Sans Regular.ttf"
        )
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ext_btn.mousePressEvent = self.exit
        self.min_btn.mousePressEvent = self.minimize
        self.show_pwd.mousePressEvent = self.showPassword
        self.login_btn.mousePressEvent = self.logIn
        self.signup_btn.mousePressEvent = self.signUp
        self.password.textChanged.connect(self.hidePassword)
        self.cur_pos = QtCore.QPoint(1080, 620)
        self.usnErrStyle = "#username { padding-left: 13px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 10px; }"
        self.usnNormStyle = "#username { padding-left: 13px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 14px; }"
        self.pwdErrStyle = "#password { padding-left: 13px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 10px; }"
        self.pwdNormStyle = "#password { padding-left: 13px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 14px; }"

    def mousePressEvent(self, event):
        self.cur_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.cur_pos)
        self.cur_pos = event.globalPos()

    def minimize(self, event):
        self.setWindowState(QtCore.Qt.WindowState.WindowMinimized)

    def exit(self, event):
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
        if (
            self.username.text() == "admin" and self.password.text() == "12345678"
        ):  # if matched
            print(self.username.text())
            print(self.password.text())

            # self.toHome()
        else:
            self.username.clear()
            self.password.clear()
            if self.username.text() == "":
                self.username.setStyleSheet(self.usnErrStyle)
            self.username.textChanged.connect(self.usnChanged)
            self.username.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "LogIn", "⚠ The username or password is incorrect."
                )
            )
            if self.password.text() == "":
                self.password.setStyleSheet(self.pwdErrStyle)
            self.password.textChanged.connect(self.pwdChanged)
            self.password.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "LogIn", "⚠ The username or password is incorrect."
                )
            )
        event.accept()

    def signUp(self, event):
        self.sign_up = SignUp()
        self.sign_up.show()
        self.hide()

    def showPassword(self, event):
        if self.password.echoMode() == QtWidgets.QLineEdit.Normal:
            self.hidePassword()
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)

    def hidePassword(self):
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)


class SignUp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/signup.ui", self)
        self.fontDB = QtGui.QFontDatabase()
        self.fontDB.addApplicationFont(":/Font/font/Better Grade/Better Grade.ttf")
        self.fontDB.addApplicationFont(
            ":/Font/font/Product Sans/Product Sans Regular.ttf"
        )
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ext_btn.mousePressEvent = self.login
        self.min_btn.mousePressEvent = self.minimize
        self.signup_btn.mousePressEvent = self.signUp
        self.back_btn.mousePressEvent = self.login
        self.show_pwd.mousePressEvent = self.showPassword
        self.show_repwd.mousePressEvent = self.showRePassword
        self.password.textChanged.connect(self.hidePassword)
        self.re_password.textChanged.connect(self.hideRePassword)
        self.cur_pos = QtCore.QPoint(1080, 620)
        self.fnErrStyle = "#f_name { padding-left: 13px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 10px; }"
        self.fnNormStyle = "#f_name { padding-left: 13px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 14px; }"
        self.lnErrStyle = "#l_name { padding-left: 13px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 10px; }"
        self.lnNormStyle = "#l_name { padding-left: 13px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 14px; }"
        self.usnErrStyle = "#username { padding-left: 13px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 10px; }"
        self.usnNormStyle = "#username { padding-left: 13px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 14px; }"
        self.emlErrStyle = "#email { padding-left: 13px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 10px; }"
        self.emlNormStyle = "#email { padding-left: 13px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 14px; }"
        self.pwdErrStyle = "#password { padding-left: 13px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 10px; }"
        self.pwdNormStyle = "#password { padding-left: 13px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 14px; }"
        self.rpwdErrStyle = "#re_password { padding-left: 13px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 10px; }"
        self.rpwdNormStyle = "#re_password { padding-left: 13px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 14px; }"

    def mousePressEvent(self, event):
        self.cur_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.cur_pos)
        self.cur_pos = event.globalPos()

    def minimize(self, event):
        self.setWindowState(QtCore.Qt.WindowState.WindowMinimized)

    def exit(self, event):
        event.accept()
        sys.exit(0)

    def fnChanged(self, txt):
        if not txt:
            self.f_name.setStyleSheet(self.fnErrStyle)
        else:
            self.f_name.setStyleSheet(self.fnNormStyle)

    def lnChanged(self, txt):
        if not txt:
            self.l_name.setStyleSheet(self.lnErrStyle)
        else:
            self.l_name.setStyleSheet(self.lnNormStyle)

    def usnChanged(self, txt):
        if not txt:
            self.username.setStyleSheet(self.usnErrStyle)
        else:
            self.username.setStyleSheet(self.usnNormStyle)

    def emlChanged(self, txt):
        if not txt:
            self.email.setStyleSheet(self.emlErrStyle)
        else:
            self.email.setStyleSheet(self.emlNormStyle)

    def pwdChanged(self, txt):
        if not txt:
            self.password.setStyleSheet(self.pwdErrStyle)
        else:
            self.password.setStyleSheet(self.pwdNormStyle)

    def rpwdChanged(self, txt):
        if not txt:
            self.re_password.setStyleSheet(self.rpwdErrStyle)
        else:
            self.re_password.setStyleSheet(self.rpwdNormStyle)

    def signUp(self, event):
        if self.f_name.text() == "":
            self.f_name.setStyleSheet(self.fnErrStyle)
            self.f_name.textChanged.connect(self.fnChanged)
            self.f_name.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ You must enter your first name."
                )
            )
        if self.l_name.text() == "":
            self.l_name.setStyleSheet(self.lnErrStyle)
            self.l_name.textChanged.connect(self.lnChanged)
            self.l_name.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ You must enter your last name."
                )
            )
        if self.username.text() == "":
            self.username.setStyleSheet(self.usnErrStyle)
            self.username.textChanged.connect(self.usnChanged)
            self.username.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ You must enter your username."
                )
            )
        if self.password.text() == "":
            self.password.setStyleSheet(self.pwdErrStyle)
            self.password.textChanged.connect(self.pwdChanged)
            self.password.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ You must enter your password."
                )
            )
        if self.re_password.text() == "":
            self.re_password.setStyleSheet(self.rpwdErrStyle)
            self.re_password.textChanged.connect(self.rpwdChanged)
        if self.username.text() == "admin":  # if exists
            if self.username.text() == "":
                self.username.setStyleSheet(self.usnErrStyle)
            self.username.textChanged.connect(self.usnChanged)
            self.username.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ Th username is already taken."
                )
            )
            self.username.clear()
        if self.email.text() == "admin@kmitl.ac.th":  # if exists
            if self.email.text() == "":
                self.email.setStyleSheet(self.emlErrStyle)
            self.email.textChanged.connect(self.emlChanged)
            self.email.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ This email is already in use."
                )
            )
            self.email.clear()
        if len(self.password.text()) < 8:
            self.password.clear()
            self.re_password.clear()
            self.password.setStyleSheet(self.pwdErrStyle)
            self.password.textChanged.connect(self.pwdChanged)
            self.password.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ Password must be 8 or more charactors."
                )
            )
        if self.re_password.text() != self.password.text():
            self.password.clear()
            self.re_password.clear()
            self.password.setStyleSheet(self.pwdErrStyle)
            self.password.textChanged.connect(self.pwdChanged)
            self.password.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ Password is not matched."
                )
            )
            self.re_password.setStyleSheet(self.rpwdErrStyle)
            self.re_password.textChanged.connect(self.rpwdChanged)
            self.re_password.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ Password is not matched."
                )
            )
        if (
            self.f_name.text() != ""
            and self.l_name.text() != ""
            and self.username.text() != ""
            and self.password.text() != ""
            and self.re_password.text() != ""
            and self.username.text() != "admin"
            and self.email.text() != "admin@kmitl.ac.th"
            and len(self.password.text()) >= 8
            and self.re_password.text() == self.password.text()
        ):  # if valid
            print(self.f_name.text())
            print(self.l_name.text())
            print(self.username.text())
            if self.email.text() != "":
                print(self.email.text())
            print(self.password.text())

            self.log_in = LogIn()
            self.log_in.show()
            self.close()

    def login(self, event):
        self.log_in = LogIn()
        self.log_in.show()
        self.close()

    def showPassword(self, event):
        if self.password.echoMode() == QtWidgets.QLineEdit.Normal:
            self.hidePassword()
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)

    def showRePassword(self, event):
        if self.re_password.echoMode() == QtWidgets.QLineEdit.Normal:
            self.hideRePassword()
        else:
            self.re_password.setEchoMode(QtWidgets.QLineEdit.Normal)

    def hidePassword(self):
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def hideRePassword(self):
        self.re_password.setEchoMode(QtWidgets.QLineEdit.Password)
