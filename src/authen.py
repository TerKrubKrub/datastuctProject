import sys
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from rsrc import rsrc


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
        self.usnErrStyle = "#username { padding-left: 10px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 13px; }"
        self.usnNormStyle = "#username { padding-left: 10px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 16px; }"
        self.pwdErrStyle = "#password { padding-left: 10px;  border-radius: 10px; background-color: rgb(255, 228, 184); color: red; font-size: 13px; }"
        self.pwdNormStyle = "#password { padding-left: 10px; border-radius: 10px; background-color: rgb(255, 228, 184); color: black; font-size: 16px; }"
        self.password.textEdited.connect(self.hidePassword)
        self.cur_pos = QtCore.QPoint(1080, 620)

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
        self.sign_up = SignUp()
        self.sign_up.show()
        self.close()

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
        self.ext_btn.mousePressEvent = self.exit
        self.min_btn.mousePressEvent = self.minimize
        self.signup_btn.mousePressEvent = self.signUp
        self.show_pwd.mousePressEvent = self.showPassword
        self.show_repwd.mousePressEvent = self.showRePassword
        self.password.textEdited.connect(self.hidePassword)
        self.re_password.textEdited.connect(self.hideRePassword)
        self.cur_pos = QtCore.QPoint(1080, 620)

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

    def signUp(self, event):
        # to database
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
