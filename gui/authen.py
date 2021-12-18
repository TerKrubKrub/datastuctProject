import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, db
import rsrc.style.authen as style


class LogIn(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=5, yOffset=5)
        )
        self.setupUi()
        self.setStyleSheet(style.default)
        self.setWindowTitle("Log in to continue.")
        db.database.updateDatabase(False, True, False, True)
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
        self.close_btn.clicked.connect(self.exit)
        self.min_btn.clicked.connect(self.minimize)
        self.show_pwd.toggled.connect(self.showPassword)
        self.login_btn.clicked.connect(self.logIn)
        self.continue_btn.clicked.connect(self.logIn)
        self.create_btn.clicked.connect(self.signUp)
        self.unrmb_btn.clicked.connect(self.notYou)
        self.password.textChanged.connect(self.hidePassword)
        self.password.textChanged.connect(lambda: self.show_pwd.setChecked(False))
        self.remember.toggled.connect(self.isRemembered)
        self.cur_pos = QtCore.QPoint(1080, 620)

    def setupUi(self):
        self.setObjectName("LogIn")
        self.setEnabled(True)
        self.resize(1200, 800)
        self.setMinimumSize(QtCore.QSize(1200, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("rsrc/img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On
        )
        self.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.login_panel = QtWidgets.QFrame(self)
        self.login_panel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_panel.sizePolicy().hasHeightForWidth())
        self.login_panel.setSizePolicy(sizePolicy)
        self.login_panel.setMinimumSize(QtCore.QSize(480, 720))
        self.login_panel.setMaximumSize(QtCore.QSize(480, 720))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.login_panel.setFont(font)
        self.login_panel.setFrameShape(QtWidgets.QFrame.Panel)
        self.login_panel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_panel.setObjectName("login_panel")
        self.gridLayout = QtWidgets.QGridLayout(self.login_panel)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.remember = QtWidgets.QPushButton(self.login_panel)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remember.sizePolicy().hasHeightForWidth())
        self.remember.setSizePolicy(sizePolicy)
        self.remember.setMinimumSize(QtCore.QSize(75, 0))
        self.remember.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        self.remember.setFont(font)
        self.remember.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remember.setStyleSheet(
            "#remember {\n"
            "    background-color: rgba(255, 255, 255, 0);\n"
            "}\n"
            "#remember:hover {\n"
            "    background-color: rgba(255, 255, 255, 0);\n"
            "}\n"
            "#remember:active {\n"
            "    background-color: rgba(255, 255, 255, 0);\n"
            "}"
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("rsrc/img/unchecked.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        icon1.addPixmap(
            QtGui.QPixmap("rsrc/img/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.On
        )
        self.remember.setIcon(icon1)
        self.remember.setIconSize(QtCore.QSize(15, 15))
        self.remember.setCheckable(True)
        self.remember.setChecked(False)
        self.remember.setObjectName("remember")
        self.horizontalLayout_3.addWidget(self.remember)
        spacerItem = QtWidgets.QSpacerItem(
            5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem)
        self.create_btn = QtWidgets.QPushButton(self.login_panel)
        self.create_btn.setMinimumSize(QtCore.QSize(75, 0))
        self.create_btn.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        font.setUnderline(True)
        self.create_btn.setFont(font)
        self.create_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_btn.setFlat(True)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_3.addWidget(self.create_btn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 1, 1, 1)
        self.login_label = QtWidgets.QLabel(self.login_panel)
        self.login_label.setMinimumSize(QtCore.QSize(300, 40))
        self.login_label.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("")
        self.login_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setWordWrap(False)
        self.login_label.setObjectName("login_label")
        self.gridLayout.addWidget(self.login_label, 2, 1, 1, 1)
        self.logo = QtWidgets.QLabel(self.login_panel)
        self.logo.setMinimumSize(QtCore.QSize(350, 160))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.logo.setFont(font)
        self.logo.setPixmap(QtGui.QPixmap("rsrc/img/logo_full.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 1, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.login_panel)
        self.username.setMinimumSize(QtCore.QSize(300, 40))
        self.username.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.username.setText("")
        self.username.setMaxLength(1000)
        self.username.setFrame(False)
        self.username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem2, 10, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 12, 15, -1)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem3)
        self.min_btn = QtWidgets.QPushButton(self.login_panel)
        self.min_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.min_btn.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.min_btn.setFont(font)
        self.min_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min_btn.setObjectName("min_btn")
        self.horizontalLayout.addWidget(self.min_btn)
        self.close_btn = QtWidgets.QPushButton(self.login_panel)
        self.close_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.close_btn.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Extended")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.close_btn.setFont(font)
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 3, 1, 1)
        self.rmb_welcome = QtWidgets.QLabel(self.login_panel)
        self.rmb_welcome.setEnabled(True)
        self.rmb_welcome.setMinimumSize(QtCore.QSize(480, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rmb_welcome.setFont(font)
        self.rmb_welcome.setText("")
        self.rmb_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.rmb_welcome.setObjectName("rmb_welcome")
        self.gridLayout.addWidget(self.rmb_welcome, 3, 0, 1, 4)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem6, 5, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem7, 8, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem8, 2, 3, 1, 1)
        self.login_btn = QtWidgets.QPushButton(self.login_panel)
        self.login_btn.setMinimumSize(QtCore.QSize(300, 50))
        self.login_btn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.login_btn.setCheckable(False)
        self.login_btn.setFlat(True)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 8, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem9, 5, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem10, 4, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem11, 6, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem12, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.continue_btn = QtWidgets.QPushButton(self.login_panel)
        self.continue_btn.setEnabled(True)
        self.continue_btn.setMinimumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.continue_btn.setFont(font)
        self.continue_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.continue_btn.setFlat(True)
        self.continue_btn.setObjectName("continue_btn")
        self.horizontalLayout_4.addWidget(self.continue_btn)
        self.unrmb_btn = QtWidgets.QPushButton(self.login_panel)
        self.unrmb_btn.setEnabled(True)
        self.unrmb_btn.setMinimumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.unrmb_btn.setFont(font)
        self.unrmb_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.unrmb_btn.setFlat(True)
        self.unrmb_btn.setObjectName("unrmb_btn")
        self.horizontalLayout_4.addWidget(self.unrmb_btn)
        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem13, 2, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem14, 8, 0, 1, 1)
        self.pwd_frame = QtWidgets.QFrame(self.login_panel)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwd_frame.sizePolicy().hasHeightForWidth())
        self.pwd_frame.setSizePolicy(sizePolicy)
        self.pwd_frame.setMinimumSize(QtCore.QSize(300, 40))
        self.pwd_frame.setMaximumSize(QtCore.QSize(300, 40))
        self.pwd_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pwd_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pwd_frame.setObjectName("pwd_frame")
        self.password = QtWidgets.QLineEdit(self.pwd_frame)
        self.password.setGeometry(QtCore.QRect(0, 0, 300, 40))
        self.password.setMinimumSize(QtCore.QSize(300, 40))
        self.password.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(10)
        font.setItalic(False)
        self.password.setFont(font)
        self.password.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setMaxLength(1000)
        self.password.setFrame(False)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setCursorPosition(0)
        self.password.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.password.setDragEnabled(True)
        self.password.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.password.setObjectName("password")
        self.show_pwd = QtWidgets.QPushButton(self.pwd_frame)
        self.show_pwd.setGeometry(QtCore.QRect(270, 12, 15, 15))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_pwd.sizePolicy().hasHeightForWidth())
        self.show_pwd.setSizePolicy(sizePolicy)
        self.show_pwd.setMinimumSize(QtCore.QSize(15, 15))
        self.show_pwd.setMaximumSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_pwd.setFont(font)
        self.show_pwd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_pwd.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("rsrc/img/eyeon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        icon2.addPixmap(
            QtGui.QPixmap("rsrc/img/eyeoff.png"), QtGui.QIcon.Normal, QtGui.QIcon.On
        )
        self.show_pwd.setIcon(icon2)
        self.show_pwd.setIconSize(QtCore.QSize(15, 15))
        self.show_pwd.setCheckable(True)
        self.show_pwd.setFlat(True)
        self.show_pwd.setObjectName("show_pwd")
        self.gridLayout.addWidget(self.pwd_frame, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.login_panel, 0, 0, 1, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.min_btn, self.close_btn)
        self.setTabOrder(self.close_btn, self.username)
        self.setTabOrder(self.username, self.password)
        self.setTabOrder(self.password, self.remember)
        self.setTabOrder(self.remember, self.create_btn)
        self.setTabOrder(self.create_btn, self.continue_btn)
        self.setTabOrder(self.continue_btn, self.unrmb_btn)
        self.setTabOrder(self.unrmb_btn, self.login_btn)
        self.setTabOrder(self.login_btn, self.show_pwd)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.remember.setToolTip(
            _translate(
                "LogIn", "<html><head/><body><p>Keep me sign in</p></body></html>"
            )
        )
        self.remember.setText(_translate("LogIn", "Keep me in"))
        self.create_btn.setToolTip(
            _translate(
                "LogIn", "<html><head/><body><p>Create an account?</p></body></html>"
            )
        )
        self.create_btn.setText(_translate("LogIn", "SIGN UP >"))
        self.login_label.setText(_translate("LogIn", "Log in to continue."))
        self.username.setToolTip(
            _translate(
                "LogIn",
                "<html><head/><body><p>Your username or e-mail</p></body></html>",
            )
        )
        self.username.setPlaceholderText(_translate("LogIn", "E-mail or Username"))
        self.min_btn.setToolTip(
            _translate("LogIn", "<html><head/><body><p>Minimize</p></body></html>")
        )
        self.min_btn.setText(_translate("LogIn", "-"))
        self.close_btn.setToolTip(
            _translate("LogIn", "<html><head/><body><p>Close</p></body></html>")
        )
        self.close_btn.setText(_translate("LogIn", "X"))
        self.login_btn.setToolTip(
            _translate("LogIn", "<html><head/><body><p>Log in</p></body></html>")
        )
        self.login_btn.setText(_translate("LogIn", "LOG IN"))
        self.continue_btn.setToolTip(
            _translate("LogIn", "<html><head/><body><p>Continue</p></body></html>")
        )
        self.continue_btn.setText(_translate("LogIn", "CONTINUE"))
        self.unrmb_btn.setToolTip(
            _translate(
                "LogIn", "<html><head/><body><p>Back to log in</p></body></html>"
            )
        )
        self.unrmb_btn.setText(_translate("LogIn", "Not You?"))
        self.password.setToolTip(
            _translate(
                "LogIn",
                "<html><head/><body><p>Password must be 8 or more charactors</p><p>Password is required</p></body></html>",
            )
        )
        self.password.setPlaceholderText(_translate("LogIn", "Password"))
        self.show_pwd.setToolTip(
            _translate(
                "LogIn", "<html><head/><body><p>Reveal/hide password</p></body></html>"
            )
        )

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
        db.database.updateDatabase(False, False, False, True)

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

    def isRemembered(self):
        return self.remember.isChecked()

    def startApp(self):
        global mainApp
        self.close()
        db.database.updateDatabase(True, False, True, False)
        mainApp = app.App(self.user_id)
        mainApp.show()

    def logIn(self):
        if self.rmb:
            LoadingScreen()
            self.timer = QtCore.QTimer
            self.timer.singleShot(1, self.startApp)
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
                    self.cur_user = [self.user_id, self.isRemembered()]
                    db.database.curs.execute(
                        "INSERT INTO current_user (id, rmb) VALUES (?,?)",
                        self.cur_user,
                    )
                    db.database.db.commit()
                    db.database.updateDatabase(False, False, False, True)

                    LoadingScreen()
                    self.timer = QtCore.QTimer
                    self.timer.singleShot(1, self.startApp)
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

    def signUp(self):
        self.sign_up = SignUp()
        self.sign_up.show()
        self.close()

    def showPassword(self):
        if self.password.echoMode() == QtWidgets.QLineEdit.Normal:
            self.hidePassword()
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)

    def hidePassword(self):
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)


class SignUp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setWindowTitle("Create an account.")
        self.setStyleSheet(style.default)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=5, yOffset=5)
        )
        self.usn_db = [str(i[3]) for i in db.database.users_ll]
        self.eml_db = [str(i[5]) for i in db.database.users_ll]
        self.close_btn.clicked.connect(self.exit)
        self.min_btn.clicked.connect(self.minimize)
        self.signup_btn.clicked.connect(self.signUp)
        self.back_btn.clicked.connect(self.login)
        self.show_pwd.toggled.connect(self.showPassword)
        self.show_repwd.toggled.connect(self.showRePassword)
        self.password.textChanged.connect(self.hidePassword)
        self.password.textChanged.connect(lambda: self.show_pwd.setChecked(False))
        self.re_password.textChanged.connect(self.hideRePassword)
        self.re_password.textChanged.connect(lambda: self.show_repwd.setChecked(False))
        self.cur_pos = QtCore.QPoint(1080, 620)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon("rsrc/img/logo.png"))

    def setupUi(self):
        self.setObjectName("SignUp")
        self.resize(1200, 800)
        self.setMinimumSize(QtCore.QSize(1200, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("rsrc/img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On
        )
        self.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.signup_panel = QtWidgets.QFrame(self)
        self.signup_panel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signup_panel.sizePolicy().hasHeightForWidth())
        self.signup_panel.setSizePolicy(sizePolicy)
        self.signup_panel.setMinimumSize(QtCore.QSize(480, 720))
        self.signup_panel.setMaximumSize(QtCore.QSize(480, 720))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.signup_panel.setFont(font)
        self.signup_panel.setFrameShape(QtWidgets.QFrame.Panel)
        self.signup_panel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.signup_panel.setObjectName("signup_panel")
        self.gridLayout = QtWidgets.QGridLayout(self.signup_panel)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem2, 8, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem3, 11, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem4, 8, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem5, 4, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem6, 5, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem7, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem8, 1, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem9, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem10, 4, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem11, 9, 0, 1, 1)
        self.f_name = QtWidgets.QLineEdit(self.signup_panel)
        self.f_name.setMinimumSize(QtCore.QSize(300, 40))
        self.f_name.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(10)
        self.f_name.setFont(font)
        self.f_name.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.f_name.setText("")
        self.f_name.setMaxLength(1000)
        self.f_name.setFrame(False)
        self.f_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.f_name.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.f_name.setObjectName("f_name")
        self.gridLayout.addWidget(self.f_name, 3, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem12, 9, 3, 1, 1)
        self.signup_label = QtWidgets.QLabel(self.signup_panel)
        self.signup_label.setMinimumSize(QtCore.QSize(300, 100))
        self.signup_label.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setFamily("Better Grade")
        font.setPointSize(72)
        self.signup_label.setFont(font)
        self.signup_label.setStyleSheet("")
        self.signup_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.signup_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_label.setWordWrap(False)
        self.signup_label.setObjectName("signup_label")
        self.gridLayout.addWidget(self.signup_label, 1, 1, 1, 1)
        self.back_btn = QtWidgets.QPushButton(self.signup_panel)
        self.back_btn.setMinimumSize(QtCore.QSize(100, 35))
        self.back_btn.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        font.setUnderline(True)
        self.back_btn.setFont(font)
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.back_btn.setShortcut("")
        self.back_btn.setDefault(False)
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout.addWidget(self.back_btn, 10, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem13, 3, 3, 1, 1)
        self.username = QtWidgets.QLineEdit(self.signup_panel)
        self.username.setMinimumSize(QtCore.QSize(300, 40))
        self.username.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.username.setText("")
        self.username.setMaxLength(1000)
        self.username.setFrame(False)
        self.username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 5, 1, 1, 1)
        self.signup_btn = QtWidgets.QPushButton(self.signup_panel)
        self.signup_btn.setMinimumSize(QtCore.QSize(300, 50))
        self.signup_btn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.signup_btn.setFont(font)
        self.signup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.signup_btn.setCheckable(False)
        self.signup_btn.setFlat(True)
        self.signup_btn.setObjectName("signup_btn")
        self.gridLayout.addWidget(self.signup_btn, 11, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem14, 11, 3, 1, 1)
        self.email = QtWidgets.QLineEdit(self.signup_panel)
        self.email.setMinimumSize(QtCore.QSize(300, 40))
        self.email.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.email.setText("")
        self.email.setMaxLength(1000)
        self.email.setFrame(False)
        self.email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.email.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 6, 1, 1, 1)
        self.l_name = QtWidgets.QLineEdit(self.signup_panel)
        self.l_name.setMinimumSize(QtCore.QSize(300, 40))
        self.l_name.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(10)
        self.l_name.setFont(font)
        self.l_name.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.l_name.setInputMask("")
        self.l_name.setText("")
        self.l_name.setMaxLength(1000)
        self.l_name.setFrame(False)
        self.l_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.l_name.setCursorPosition(0)
        self.l_name.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.l_name.setDragEnabled(True)
        self.l_name.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.l_name.setObjectName("l_name")
        self.gridLayout.addWidget(self.l_name, 4, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem15, 6, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 12, 15, -1)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem16 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem16)
        self.min_btn = QtWidgets.QPushButton(self.signup_panel)
        self.min_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.min_btn.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(11)
        self.min_btn.setFont(font)
        self.min_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min_btn.setObjectName("min_btn")
        self.horizontalLayout.addWidget(self.min_btn)
        self.close_btn = QtWidgets.QPushButton(self.signup_panel)
        self.close_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.close_btn.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Extended")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.close_btn.setFont(font)
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem17 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem17)
        self.gridLayout.addLayout(self.verticalLayout, 0, 3, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem18, 12, 1, 1, 1)
        self.pwd_frame = QtWidgets.QFrame(self.signup_panel)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwd_frame.sizePolicy().hasHeightForWidth())
        self.pwd_frame.setSizePolicy(sizePolicy)
        self.pwd_frame.setMinimumSize(QtCore.QSize(300, 40))
        self.pwd_frame.setMaximumSize(QtCore.QSize(300, 40))
        self.pwd_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pwd_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pwd_frame.setObjectName("pwd_frame")
        self.password = QtWidgets.QLineEdit(self.pwd_frame)
        self.password.setGeometry(QtCore.QRect(0, 0, 300, 40))
        self.password.setMinimumSize(QtCore.QSize(300, 40))
        self.password.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.password.setText("")
        self.password.setMaxLength(1000)
        self.password.setFrame(False)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.password.setObjectName("password")
        self.show_pwd = QtWidgets.QPushButton(self.pwd_frame)
        self.show_pwd.setGeometry(QtCore.QRect(270, 12, 15, 15))
        self.show_pwd.setMinimumSize(QtCore.QSize(15, 15))
        self.show_pwd.setMaximumSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_pwd.setFont(font)
        self.show_pwd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_pwd.setAcceptDrops(False)
        self.show_pwd.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("rsrc/img/eyeon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        icon1.addPixmap(
            QtGui.QPixmap("rsrc/img/eyeoff.png"), QtGui.QIcon.Normal, QtGui.QIcon.On
        )
        self.show_pwd.setIcon(icon1)
        self.show_pwd.setIconSize(QtCore.QSize(15, 15))
        self.show_pwd.setCheckable(True)
        self.show_pwd.setChecked(False)
        self.show_pwd.setFlat(True)
        self.show_pwd.setObjectName("show_pwd")
        self.gridLayout.addWidget(self.pwd_frame, 8, 1, 1, 1)
        self.repwd_frame = QtWidgets.QFrame(self.signup_panel)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repwd_frame.sizePolicy().hasHeightForWidth())
        self.repwd_frame.setSizePolicy(sizePolicy)
        self.repwd_frame.setMinimumSize(QtCore.QSize(300, 40))
        self.repwd_frame.setMaximumSize(QtCore.QSize(300, 40))
        self.repwd_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.repwd_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.repwd_frame.setObjectName("repwd_frame")
        self.re_password = QtWidgets.QLineEdit(self.repwd_frame)
        self.re_password.setGeometry(QtCore.QRect(0, 0, 300, 40))
        self.re_password.setMinimumSize(QtCore.QSize(300, 40))
        self.re_password.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(10)
        self.re_password.setFont(font)
        self.re_password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.re_password.setText("")
        self.re_password.setMaxLength(1000)
        self.re_password.setFrame(False)
        self.re_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.re_password.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.re_password.setObjectName("re_password")
        self.show_repwd = QtWidgets.QPushButton(self.repwd_frame)
        self.show_repwd.setGeometry(QtCore.QRect(270, 12, 15, 15))
        self.show_repwd.setMinimumSize(QtCore.QSize(15, 15))
        self.show_repwd.setMaximumSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_repwd.setFont(font)
        self.show_repwd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_repwd.setText("")
        self.show_repwd.setIcon(icon1)
        self.show_repwd.setIconSize(QtCore.QSize(15, 15))
        self.show_repwd.setCheckable(True)
        self.show_repwd.setFlat(True)
        self.show_repwd.setObjectName("show_repwd")
        self.gridLayout.addWidget(self.repwd_frame, 9, 1, 1, 1)
        self.gridLayout_2.addWidget(self.signup_panel, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.min_btn, self.close_btn)
        self.setTabOrder(self.close_btn, self.f_name)
        self.setTabOrder(self.f_name, self.l_name)
        self.setTabOrder(self.l_name, self.username)
        self.setTabOrder(self.username, self.email)
        self.setTabOrder(self.email, self.password)
        self.setTabOrder(self.password, self.re_password)
        self.setTabOrder(self.re_password, self.back_btn)
        self.setTabOrder(self.back_btn, self.signup_btn)
        self.setTabOrder(self.signup_btn, self.show_pwd)
        self.setTabOrder(self.show_pwd, self.show_repwd)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.f_name.setToolTip(
            _translate(
                "SignUp", "<html><head/><body><p>Your first name</p></body></html>"
            )
        )
        self.f_name.setPlaceholderText(_translate("SignUp", "First name"))
        self.signup_label.setText(_translate("SignUp", "Sign Up"))
        self.back_btn.setToolTip(
            _translate(
                "SignUp", "<html><head/><body><p>Back to log in</p></body></html>"
            )
        )
        self.back_btn.setText(_translate("SignUp", "< BACK"))
        self.username.setToolTip(
            _translate(
                "SignUp", "<html><head/><body><p>Unique username</p></body></html>"
            )
        )
        self.username.setPlaceholderText(_translate("SignUp", "Username"))
        self.signup_btn.setToolTip(
            _translate(
                "SignUp", "<html><head/><body><p>Confirm signing up</p></body></html>"
            )
        )
        self.signup_btn.setText(_translate("SignUp", "CONFIRM"))
        self.email.setToolTip(
            _translate("SignUp", "<html><head/><body><p>Your e-mail</p></body></html>")
        )
        self.email.setPlaceholderText(_translate("SignUp", "Email (optional)"))
        self.l_name.setToolTip(
            _translate(
                "SignUp", "<html><head/><body><p>Your last name</p></body></html>"
            )
        )
        self.l_name.setPlaceholderText(_translate("SignUp", "Last name"))
        self.min_btn.setToolTip(
            _translate("SignUp", "<html><head/><body><p>Minimize</p></body></html>")
        )
        self.min_btn.setText(_translate("SignUp", "-"))
        self.close_btn.setToolTip(
            _translate("SignUp", "<html><head/><body><p>Close</p></body></html>")
        )
        self.close_btn.setText(_translate("SignUp", "X"))
        self.password.setToolTip(
            _translate(
                "SignUp",
                "<html><head/><body><p>Password must be 8 or more charactors</p><p>Password is required</p></body></html>",
            )
        )
        self.password.setPlaceholderText(_translate("SignUp", "Password"))
        self.show_pwd.setToolTip(
            _translate(
                "SignUp", "<html><head/><body><p>Reveal/hide password</p></body></html>"
            )
        )
        self.re_password.setToolTip(
            _translate(
                "SignUp",
                "<html><head/><body><p>Password must be 8 or more charactors</p><p>Password is required</p></body></html>",
            )
        )
        self.re_password.setPlaceholderText(
            _translate("SignUp", "Confirm your password")
        )
        self.show_repwd.setToolTip(
            _translate(
                "SignUp", "<html><head/><body><p>Reveal/hide password</p></body></html>"
            )
        )

    def mousePressEvent(self, event):
        self.cur_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.cur_pos)
        self.cur_pos = event.globalPos()

    def minimize(self):
        self.setWindowState(QtCore.Qt.WindowState.WindowMinimized)

    def exit(self):
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

    def signUp(self):
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
            db.database.updateDatabase(False, True, False, False)
            self.msg.setWindowTitle("Account created.")
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setText(
                "Your account is successfully created!\nYou can now log in."
            )
            self.msg.exec_()

            self.log_in = LogIn()
            self.log_in.show()
            self.close()

    def login(self):
        self.log_in = LogIn()
        self.log_in.show()
        self.close()

    def showPassword(self):
        if self.password.echoMode() == QtWidgets.QLineEdit.Normal:
            self.hidePassword()
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)

    def showRePassword(self):
        if self.re_password.echoMode() == QtWidgets.QLineEdit.Normal:
            self.hideRePassword()
        else:
            self.re_password.setEchoMode(QtWidgets.QLineEdit.Normal)

    def hidePassword(self):
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def hideRePassword(self):
        self.re_password.setEchoMode(QtWidgets.QLineEdit.Password)


class LoadingScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        global loading
        loading = self
        self.setFixedSize(240, 240)
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.loading = QtWidgets.QLabel(self)
        self.loading.setFixedSize(240, 240)
        self.loading.setPixmap(QtGui.QPixmap("rsrc/img/loading.png"))
        self.loading.setScaledContents(True)
        self.loading.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.show()
