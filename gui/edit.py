import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, authen, db, home
import rsrc.rsrc
import rsrc.style.edit as style
import rsrc.style.authen as authenStyle


class Edit(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/edit.ui", self)
        global editApp
        editApp = self
        self.setStyleSheet(style.default)
        self.old_prof = [str(i[6]) for i in db.database.users_ll if i[0] == app.id][0]
        self.prof_img.setPixmap(QtGui.QPixmap(self.old_prof))
        self.prof_img.setScaledContents(True)
        self.img_frame.setPixmap(QtGui.QPixmap("rsrc/img/frame_big.png"))
        self.img_frame.setScaledContents(True)
        self.back_btn.clicked.connect(self.goToHome)
        self.upload_btn.clicked.connect(self.uploadImage)
        self.restore_btn.clicked.connect(self.restoreProfile)
        self.save_btn.clicked.connect(self.saveChanges)
        self.delete_account.clicked.connect(self.delAcc)
        self.edit_label.resizeEvent = self.resizeEdit
        self.old_username = [str(i[3]) for i in db.database.users_ll if i[0] == app.id][
            0
        ]
        self.old_f_name = [str(i[1]) for i in db.database.users_ll if i[0] == app.id][0]
        self.old_l_name = [str(i[2]) for i in db.database.users_ll if i[0] == app.id][0]
        self.old_email = [i[5] for i in db.database.users_ll if i[0] == app.id][0]
        self.old_password = [str(i[4]) for i in db.database.users_ll if i[0] == app.id][
            0
        ]
        self.cur_read = [i[7] for i in db.database.users_ll if i[0] == app.id][0]
        if self.cur_read:
            self.cur_read_title = [
                str(i[1])
                for i in db.database.books_ll
                if int(i[0]) == int(self.cur_read)
            ][0]
        else:
            self.cur_read_title = None
        self.cur_read_box.addItems([None] + [i[1] for i in db.database.books_ll])
        self.old_cur_read_index = self.cur_read_box.findText(self.cur_read_title)
        self.restoreProfile()
        self.new_prof = None
        self.file = None
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon("rsrc/img/logo.png"))

    def goToHome(self):
        self.prof_img.setPixmap(QtGui.QPixmap(self.old_prof))
        self.restoreProfile()
        authen.mainApp.setWindowTitle("Booque - Home")
        authen.mainApp.home_btn.show()
        authen.mainApp.prof_btn.show()
        authen.mainApp.prof.show()
        authen.mainApp.app_panel.setCurrentIndex(0)
        self.file = None
        self.new_prof = None

    def resizeEdit(self, event):
        if self.rect().width() // 35 > 35:
            font = QtGui.QFont("Helvetica Neue LT Black Ext", self.rect().width() // 35)
        else:
            font = QtGui.QFont("Helvetica Neue LT Black Ext", 35)
        self.edit_label.setFont(font)

    def delAcc(self):
        self.msg.setIcon(QtWidgets.QMessageBox.Question)
        self.msg.setWindowTitle("Confirm deletion.")
        self.msg.setText("Are you sure to delete this account?")
        self.msg.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel
        )
        self.msg.buttonClicked.connect(self.delete)
        self.msg.exec_()

    def delete(self, signal):
        if signal.text() == "&Yes":
            db.database.curs.execute("DELETE FROM current_user")
            db.database.db.commit()
            db.database.curs.execute("DELETE FROM users WHERE user_id=" + str(app.id))
            db.database.db.commit()
            db.database.curs.execute(
                "DELETE FROM comments WHERE user_id=" + str(app.id)
            )
            db.database.db.commit()
            db.database.curs.execute("DELETE FROM ratings WHERE user_id=" + str(app.id))
            db.database.db.commit()
            db.database.updateDatabase(False, True, False, True)

            self.log_in = authen.LogIn()
            self.log_in.show()
            authen.mainApp.close()


    def uploadImage(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Save File",
            "C:/",
            "Images (*.png *.jpeg *.jpg)",
        )
        if self.file[0]:
            self.new_prof = "rsrc/db/userimg/" + self.file[0].split("/")[-1]
            self.prof_img.setPixmap(QtGui.QPixmap(self.file[0]))
        else:
            self.file = None
            self.new_prof = None
            self.prof_img.setPixmap(QtGui.QPixmap(self.old_prof))

    def saveChanges(self):
        if not self.f_name.text():
            self.f_name.setStyleSheet(authenStyle.error)
            self.f_name.textChanged.connect(self.fnChanged)
            self.f_name.setPlaceholderText("⚠ First name is required.")

        if not self.l_name.text():
            self.l_name.setStyleSheet(authenStyle.error)
            self.l_name.textChanged.connect(self.lnChanged)
            self.l_name.setPlaceholderText("⚠ Last name is required.")

        if not self.username.text():
            self.username.setStyleSheet(authenStyle.error)
            self.username.textChanged.connect(self.usnChanged)
            self.username.setPlaceholderText("⚠ Username is required.")

        if self.username.text() in [
            str(i[3]) for i in db.database.users_ll if i[3] != self.old_username
        ]:
            if self.username.text() == "":
                self.username.setStyleSheet(authenStyle.error)
            self.username.textChanged.connect(self.usnChanged)
            self.username.setPlaceholderText("⚠ The username is already taken.")
            self.username.clear()

        if self.email.text() in [
            str(i[5]) for i in db.database.users_ll if i[5] != self.old_email
        ]:
            if self.email.text() == "":
                self.email.setStyleSheet(authenStyle.error)
            self.email.textChanged.connect(self.emlChanged)
            self.email.setPlaceholderText("⚠ This email is already in use.")
            self.email.clear()

        if self.password.text() and len(self.password.text()) < 8:
            self.password.clear()
            self.re_password.clear()
            self.password.setStyleSheet(authenStyle.error)
            self.password.textChanged.connect(self.pwdChanged)
            self.password.setPlaceholderText("⚠ Password must be 8 or more charactors.")

        if self.re_password.text() and self.re_password.text() != self.password.text():
            self.password.clear()
            self.re_password.clear()
            self.password.setStyleSheet(authenStyle.error)
            self.password.textChanged.connect(self.pwdChanged)
            self.password.setPlaceholderText("⚠ Password is unmatched.")
            self.re_password.setStyleSheet(authenStyle.error)
            self.re_password.textChanged.connect(self.rpwdChanged)
            self.re_password.setPlaceholderText("⚠ Password is unmatched.")

        if (
            self.f_name.text()
            and self.l_name.text()
            and self.username.text()
            and self.username.text()
            not in [
                str(i[3]) for i in db.database.users_ll if i[3] != self.old_username
            ]
            and self.email.text()
            not in [str(i[5]) for i in db.database.users_ll if i[5] != self.old_email]
            and not (
                self.f_name.text() == self.old_f_name
                and self.l_name.text() == self.old_l_name
                and self.username.text() == self.old_username
                and self.email.text() == self.old_email
                and self.cur_read_box.currentIndex() == self.old_cur_read_index
                and not self.new_prof
            )
        ):
            if self.new_prof and self.file:
                QtCore.QFile.copy(self.file[0], self.new_prof)
                self.old_prof = self.new_prof
                authen.mainApp.prof.setPixmap(QtGui.QPixmap(self.new_prof))
                self.new_prof = None
                self.file = None
            if self.cur_read_box.currentText():
                self.cur_book_id = [
                    i[0]
                    for i in db.database.books_ll
                    if i[1] == self.cur_read_box.currentText()
                ][0]
            else:
                self.cur_book_id = 0
            db.database.curs.execute(
                "UPDATE users SET f_name=?, l_name=?, username=?, password=?, email=?, user_img=?, cur_read=? WHERE user_id=?",
                [
                    self.f_name.text(),
                    self.l_name.text(),
                    self.username.text(),
                    self.password.text() if self.password.text() else self.old_password,
                    self.email.text() if self.email.text() else None,
                    self.new_prof if self.new_prof else self.old_prof,
                    self.cur_book_id,
                    app.id,
                ],
            )
            db.database.db.commit()
            db.database.updateDatabase(False, True, False, False)
            home.homeApp.updateCurBook(self.cur_book_id)
            self.old_username = self.username.text()
            self.old_f_name = self.f_name.text()
            self.old_l_name = self.l_name.text()
            self.old_email = self.email.text()
            self.password.setText("")
            self.re_password.setText("")
            self.old_cur_read_index = self.cur_read_box.currentIndex()
            self.password.setPlaceholderText("Password must be 8 or more charactors")
            self.password.setStyleSheet(authenStyle.input)
            self.re_password.setStyleSheet(authenStyle.input)
            self.msg.setWindowTitle("Profile edited.")
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setText("Successfully edit your profile.")
            self.msg.exec_()

    def restoreProfile(self):
        self.username.setText(self.old_username)
        self.f_name.setText(self.old_f_name)
        self.l_name.setText(self.old_l_name)
        self.email.setText(self.old_email)
        self.cur_read_box.setCurrentIndex(self.old_cur_read_index)
        self.prof_img.setPixmap(QtGui.QPixmap(self.old_prof))
        self.file = None
        self.new_prof = None

    def fnChanged(self, txt):
        if not txt:
            self.f_name.setStyleSheet(authenStyle.error)
        else:
            self.f_name.setStyleSheet(authenStyle.input)

    def lnChanged(self, txt):
        if not txt:
            self.l_name.setStyleSheet(authenStyle.error)
        else:
            self.l_name.setStyleSheet(authenStyle.input)

    def usnChanged(self, txt):
        if not txt:
            self.username.setStyleSheet(authenStyle.error)
        else:
            self.username.setStyleSheet(authenStyle.input)

    def emlChanged(self, txt):
        if not txt:
            self.email.setStyleSheet(authenStyle.error)
        else:
            self.email.setStyleSheet(authenStyle.input)

    def pwdChanged(self, txt):
        if not txt:
            self.password.setStyleSheet(authenStyle.error)
        else:
            self.password.setStyleSheet(authenStyle.input)

    def rpwdChanged(self, txt):
        if not txt:
            self.re_password.setStyleSheet(authenStyle.error)
        else:
            self.re_password.setStyleSheet(authenStyle.input)
