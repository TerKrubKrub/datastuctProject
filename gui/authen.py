import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtGui import QMovie

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, db
import rsrc.rsrc
import rsrc.style.authen as style


class LogIn(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/login.ui", self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=5, yOffset=5)
        )
        self.usn_db = [str(i[3]) for i in db.database.users_ll]
        self.eml_db = [str(i[5]) for i in db.database.users_ll]
        self.user_id = db.database.cur_user[0]
        self.rmb = db.database.cur_user[1]
        if self.rmb:
            self.f_name = [
                str(i[1]) for i in db.database.users_ll if i[0] == self.user_id
            ][0]
            self.showRmb()
        else:
            self.showNotRmb()
        self.setStyleSheet(style.default)
        self.close_btn.clicked.connect(self.exit)
        self.min_btn.clicked.connect(self.minimize)
        self.show_pwd.clicked.connect(self.showPassword)
        self.login_btn.clicked.connect(self.logIn)
        self.continue_btn.clicked.connect(self.logIn)
        self.create_btn.clicked.connect(self.signUp)
        self.unrmb_btn.clicked.connect(self.notYou)
        self.password.textChanged.connect(self.hidePassword)
        self.cur_pos = QtCore.QPoint(1080, 620)

    def mousePressEvent(self, event):
        self.cur_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.cur_pos)
        self.cur_pos = event.globalPos()

    def minimize(self):
        self.setWindowState(QtCore.Qt.WindowState.WindowMinimized)

    def exit(self):
        sys.exit(0)

    def showRmb(self):
        self.rmb_welcome.setText("Welcome back,\n" + self.f_name + "!")
        self.rmb_welcome.show()
        self.continue_btn.show()
        self.unrmb_btn.show()
        self.login_label.hide()
        self.username.hide()
        self.password.hide()
        self.show_pwd.hide()
        self.login_btn.hide()
        self.remember.hide()
        self.create_btn.hide()

    def showNotRmb(self):
        self.rmb_welcome.hide()
        self.continue_btn.hide()
        self.unrmb_btn.hide()
        self.login_label.show()
        self.username.show()
        self.password.show()
        self.show_pwd.show()
        self.login_btn.show()
        self.remember.show()
        self.create_btn.show()

    def notYou(self):
        self.showNotRmb()
        self.user_id = self.rmb = None
        db.database.curs.execute("DELETE FROM current_user")
        db.database.db.commit()
        db.database.updateDatabase(False, False, True, False)

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

    def logIn(self):
        global mainApp
        if self.rmb:
            mainApp = app.App(self.user_id)
            mainApp.show()
            self.close()
        else:
            if (
                self.username.text() in self.usn_db
                or self.username.text() in self.eml_db
            ):
                self.user_db = db.database.curs.fetchone()
                self.pwd_db = [
                    str(i[4])
                    for i in db.database.users_ll
                    if i[3] == self.username.text() or i[5] == self.username.text()
                ][0]
                self.user_id = [
                    str(i[0])
                    for i in db.database.users_ll
                    if i[3] == self.username.text() or i[5] == self.username.text()
                ][0]
                if self.password.text() == self.pwd_db:
                    self.cur_user = [self.user_id, self.remember.isChecked()]
                    db.database.curs.execute(
                        "INSERT INTO current_user (id, rmb) VALUES (?,?)",
                        self.cur_user,
                    )
                    db.database.db.commit()
                    db.database.updateDatabase(False, False, True, False)

                    mainApp = app.App(self.user_id)
                    mainApp.show()
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
                    QtCore.QCoreApplication.translate(
                        "LogIn", "⚠ Password is incorrect."
                    )
                )

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
        self.usn_db = [str(i[3]) for i in db.database.users_ll]
        self.eml_db = [str(i[5]) for i in db.database.users_ll]
        self.setStyleSheet(style.default)
        self.close_btn.mousePressEvent = self.exit
        self.min_btn.mousePressEvent = self.minimize
        self.signup_btn.mousePressEvent = self.signUp
        self.back_btn.mousePressEvent = self.login
        self.show_pwd.mousePressEvent = self.showPassword
        self.show_repwd.mousePressEvent = self.showRePassword
        self.password.textChanged.connect(self.hidePassword)
        self.re_password.textChanged.connect(self.hideRePassword)
        self.cur_pos = QtCore.QPoint(1080, 620)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon("rsrc/img/logo.png"))

    def mousePressEvent(self, event):
        self.cur_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.cur_pos)
        self.cur_pos = event.globalPos()

    def minimize(self, event):
        self.setWindowState(QtCore.Qt.WindowState.WindowMinimized)

    def exit(self, event):
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
            self.user_info = [
                self.f_name.text(),
                self.l_name.text(),
                self.username.text(),
                self.password.text(),
                self.email.text() if self.email.text() else None,
            ]
            db.database.curs.execute(
                "INSERT INTO users (f_name, l_name, username, password, email) VALUES (?,?,?,?,?)",
                self.user_info,
            )
            db.database.db.commit()
            db.database.updateDatabase(True, False, False, False)
            self.msg.setWindowTitle("Account created.")
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setText(
                "Your account is successfully created!\nYou can now log in."
            )
            self.msg.exec_()

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
