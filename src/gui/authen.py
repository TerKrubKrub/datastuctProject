import sys, os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import rsrc.rsrc
import rsrc.style.authen as style


class LogIn(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/login.ui", self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.fontDB = QtGui.QFontDatabase()
        self.fontDB.addApplicationFont(":/Font/font/Better Grade/Better Grade.ttf")
        self.fontDB.addApplicationFont(
            ":/Font/font/Product Sans/Product Sans Regular.ttf"
        )
        self.db = sqlite3.connect("rsrc/db/data.db")
        self.curs = self.db.cursor()
        self.setStyleSheet(style.default)
        self.ext_btn.mousePressEvent = self.exit
        self.min_btn.mousePressEvent = self.minimize
        self.show_pwd.mousePressEvent = self.showPassword
        self.login_btn.mousePressEvent = self.logIn
        self.create_btn.mousePressEvent = self.signUp
        self.password.textChanged.connect(self.hidePassword)
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
            self.username.setStyleSheet(style.error)
        else:
            self.username.setStyleSheet(style.input)

    def pwdChanged(self, txt):
        if not txt:
            self.password.setStyleSheet(style.error)
        else:
            self.password.setStyleSheet(style.input)

    def logIn(self, event):
        self.curs.execute("SELECT username FROM users")
        self.users_db = self.curs.fetchall()
        self.usn_db = [i[0] for i in self.users_db]
        self.curs.execute("SELECT email FROM users")
        self.emails_db = self.curs.fetchall()
        self.eml_db = [i[0] for i in self.emails_db]
        if self.username.text() in self.usn_db or self.username.text() in self.eml_db:
            self.curs.execute(
                'SELECT password FROM users WHERE username="'
                + self.username.text()
                + '" OR email="'
                + self.username.text()
                + '"'
            )
            self.pwd_db = self.curs.fetchone()[0]
            print(self.pwd_db)
            if self.password.text() == self.pwd_db:
                self.curs.execute(
                    'SELECT user_id FROM users WHERE username="'
                    + self.username.text()
                    + '" OR email="'
                    + self.username.text()
                    + '"'
                )
                self.user_id = self.curs.fetchone()[0]
                print("\nusername:", self.username.text())
                print("password:", self.password.text())
                print("id:", self.user_id)
                print("\nSuccessfully logged in!")

                # to home
                self.close()
            else:
                self.password.clear()
                if self.password.text() == "":
                    self.password.setStyleSheet(style.error)
                self.password.textChanged.connect(self.pwdChanged)
                self.password.setPlaceholderText(
                    QtCore.QCoreApplication.translate(
                        "LogIn", "⚠ Password is incorrect."
                    )
                )
        else:
            self.username.clear()
            if self.username.text() == "":
                self.username.setStyleSheet(style.error)
            self.username.textChanged.connect(self.usnChanged)
            self.username.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "LogIn", "⚠ The username does not exist."
                )
            )
            self.password.clear()
            if self.password.text() == "":
                self.password.setStyleSheet(style.error)
            self.password.textChanged.connect(self.pwdChanged)
            self.password.setPlaceholderText(
                QtCore.QCoreApplication.translate("LogIn", "⚠ Password is incorrect.")
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
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.fontDB = QtGui.QFontDatabase()
        self.fontDB.addApplicationFont(":/Font/font/Better Grade/Better Grade.ttf")
        self.fontDB.addApplicationFont(
            ":/Font/font/Product Sans/Product Sans Regular.ttf"
        )
        self.db = sqlite3.connect("rsrc/db/data.db")
        self.curs = self.db.cursor()
        self.setStyleSheet(style.default)
        self.ext_btn.mousePressEvent = self.login
        self.min_btn.mousePressEvent = self.minimize
        self.signup_btn.mousePressEvent = self.signUp
        self.back_btn.mousePressEvent = self.login
        self.show_pwd.mousePressEvent = self.showPassword
        self.show_repwd.mousePressEvent = self.showRePassword
        self.password.textChanged.connect(self.hidePassword)
        self.re_password.textChanged.connect(self.hideRePassword)
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

    def fnChanged(self, txt):
        if not txt:
            self.f_name.setStyleSheet(style.error)
        else:
            self.f_name.setStyleSheet(style.input)

    def lnChanged(self, txt):
        if not txt:
            self.l_name.setStyleSheet(style.error)
        else:
            self.l_name.setStyleSheet(style.input)

    def usnChanged(self, txt):
        if not txt:
            self.username.setStyleSheet(style.error)
        else:
            self.username.setStyleSheet(style.input)

    def emlChanged(self, txt):
        if not txt:
            self.email.setStyleSheet(style.error)
        else:
            self.email.setStyleSheet(style.input)

    def pwdChanged(self, txt):
        if not txt:
            self.password.setStyleSheet(style.error)
        else:
            self.password.setStyleSheet(style.input)

    def rpwdChanged(self, txt):
        if not txt:
            self.re_password.setStyleSheet(style.error)
        else:
            self.re_password.setStyleSheet(style.input)

    def signUp(self, event):
        self.usn_query = "SELECT username FROM users"
        self.curs.execute(self.usn_query)
        self.users_db = self.curs.fetchall()
        self.usn_db = [i[0] for i in self.users_db]
        self.eml_query = "SELECT email FROM users"
        self.curs.execute(self.eml_query)
        self.emails_db = self.curs.fetchall()
        self.eml_db = [i[0] for i in self.emails_db]
        if not self.f_name.text():
            self.f_name.setStyleSheet(style.error)
            self.f_name.textChanged.connect(self.fnChanged)
            self.f_name.setPlaceholderText(
                QtCore.QCoreApplication.translate("SignUp", "⚠ First name is required.")
            )
        if not self.l_name.text():
            self.l_name.setStyleSheet(style.error)
            self.l_name.textChanged.connect(self.lnChanged)
            self.l_name.setPlaceholderText(
                QtCore.QCoreApplication.translate("SignUp", "⚠ Last name is required.")
            )
        if not self.username.text():
            self.username.setStyleSheet(style.error)
            self.username.textChanged.connect(self.usnChanged)
            self.username.setPlaceholderText(
                QtCore.QCoreApplication.translate("SignUp", "⚠ Username is required.")
            )
        if not self.password.text():
            self.password.setStyleSheet(style.error)
            self.password.textChanged.connect(self.pwdChanged)
            self.password.setPlaceholderText(
                QtCore.QCoreApplication.translate("SignUp", "⚠ Password is required.")
            )
        if not self.re_password.text():
            self.re_password.setStyleSheet(style.error)
            self.re_password.textChanged.connect(self.rpwdChanged)
        if self.username.text() in self.usn_db:
            if self.username.text() == "":
                self.username.setStyleSheet(style.error)
            self.username.textChanged.connect(self.usnChanged)
            self.username.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ The username is already taken."
                )
            )
            self.username.clear()
        if self.email.text() in self.eml_db:
            if self.email.text() == "":
                self.email.setStyleSheet(style.error)
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
            self.password.setStyleSheet(style.error)
            self.password.textChanged.connect(self.pwdChanged)
            self.password.setPlaceholderText(
                QtCore.QCoreApplication.translate(
                    "SignUp", "⚠ Password must be 8 or more charactors."
                )
            )
        if self.re_password.text() != self.password.text():
            self.password.clear()
            self.re_password.clear()
            self.password.setStyleSheet(style.error)
            self.password.textChanged.connect(self.pwdChanged)
            self.password.setPlaceholderText(
                QtCore.QCoreApplication.translate("SignUp", "⚠ Password is unmatched.")
            )
            self.re_password.setStyleSheet(style.error)
            self.re_password.textChanged.connect(self.rpwdChanged)
            self.re_password.setPlaceholderText(
                QtCore.QCoreApplication.translate("SignUp", "⚠ Password is unmatched.")
            )
        if (
            self.f_name.text()
            and self.l_name.text()
            and self.username.text()
            and self.password.text()
            and self.re_password.text()
            and self.username.text() not in self.usn_db
            and self.email.text() not in self.eml_db
            and len(self.password.text()) >= 8
            and self.re_password.text() == self.password.text()
        ):
            user_info = [
                self.f_name.text(),
                self.l_name.text(),
                self.username.text(),
                self.password.text(),
                self.email.text() if self.email.text() else None,
            ]
            self.curs.execute(
                "INSERT INTO users (fname, lname, username, password, email) VALUES (?,?,?,?,?)",
                user_info,
            )
            self.db.commit()
            self.db.close()

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
