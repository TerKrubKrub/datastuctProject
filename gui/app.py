import sys, os, datetime
from PyQt5 import QtWidgets, QtGui, QtCore

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import authen, db
from rsrc.style import (
    app as appStyle,
    authen as authenStyle,
    book as bookStyle,
    chart as chartStyle,
    edit as editStyle,
    home as homeStyle,
    library as libStyle,
    request as reqStyle,
    setting as settingStyle,
)


LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo


class App(QtWidgets.QWidget):
    def __init__(self, user_id):
        super().__init__()
        global app
        app = self
        self.id = int(user_id)
        self.dark = False
        authen.loading.close()
        self.setupUi()
        self.setWindowTitle("Booque - Home")
        self.setStyleSheet(appStyle.default)
        self.app_panel.setCurrentIndex(0)
        self.home_btn.clicked.connect(self.goToHome)
        self.prof_img = [i[6] for i in db.database.users_ll if i[0] == self.id][0]
        self.prof.setPixmap(self.prof_img)
        self.prof.setScaledContents(True)
        self.prof_btn.setIcon(QtGui.QIcon("rsrc/img/frame.png"))
        self.menu = QtWidgets.QMenu("menu_list", self)
        self.menu.setFont(QtGui.QFont("Product Sans", 10))
        self.menu.triggered.connect(lambda x: self.handleMenu(x.text()))
        self.menu.addAction("Library").setIcon(QtGui.QIcon("rsrc/img/library.ico"))
        self.menu.addAction("Chart").setIcon(QtGui.QIcon("rsrc/img/trophy.png"))
        self.menu.addAction("Request").setIcon(QtGui.QIcon("rsrc/img/request.png"))
        self.menu.addAction("Edit Profile").setIcon(QtGui.QIcon("rsrc/img/prof.png"))
        self.menu.addAction("Setting").setIcon(QtGui.QIcon("rsrc/img/gear.png"))
        self.menu.addAction("Log out").setIcon(QtGui.QIcon("rsrc/img/logout.png"))
        self.menu.setProperty("hide", True)
        self.prof_btn.setMenu(self.menu)

    def setupUi(self):
        self.setObjectName("booque")
        self.resize(1200, 800)
        self.setMinimumSize(QtCore.QSize(1200, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("rsrc/img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On
        )
        self.setWindowIcon(icon)
        self.setWindowOpacity(1.0)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.navbar = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbar.sizePolicy().hasHeightForWidth())
        self.navbar.setSizePolicy(sizePolicy)
        self.navbar.setMinimumSize(QtCore.QSize(0, 110))
        self.navbar.setMaximumSize(QtCore.QSize(16777215, 110))
        self.navbar.setObjectName("navbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.navbar)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(30, 0, 40, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.home_btn = QtWidgets.QPushButton(self.navbar)
        self.home_btn.setMinimumSize(QtCore.QSize(230, 110))
        self.home_btn.setMaximumSize(QtCore.QSize(230, 110))
        self.home_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_btn.setStyleSheet(
            "#home_btn:hover {\n" "    background-color: rgba(255, 255, 255, 0);\n" "}"
        )
        self.home_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("rsrc/img/logo_full.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On,
        )
        self.home_btn.setIcon(icon1)
        self.home_btn.setIconSize(QtCore.QSize(250, 65))
        self.home_btn.setFlat(True)
        self.home_btn.setObjectName("home_btn")
        self.horizontalLayout.addWidget(self.home_btn)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.profile = QtWidgets.QVBoxLayout()
        self.profile.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.profile.setSpacing(0)
        self.profile.setObjectName("profile")
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.profile.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.navbar)
        self.frame.setMinimumSize(QtCore.QSize(50, 50))
        self.frame.setMaximumSize(QtCore.QSize(70, 70))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.prof = QtWidgets.QLabel(self.frame)
        self.prof.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.prof.setMinimumSize(QtCore.QSize(50, 50))
        self.prof.setMaximumSize(QtCore.QSize(50, 50))
        self.prof.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prof.setObjectName("prof")
        self.prof_btn = QtWidgets.QPushButton(self.frame)
        self.prof_btn.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.prof_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.prof_btn.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.prof_btn.setFont(font)
        self.prof_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prof_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.prof_btn.setStyleSheet(
            "#prof_btn:hover {\n" "    background-color: rgba(255, 255, 255, 0);\n" "}"
        )
        self.prof_btn.setText("")
        self.prof_btn.setIconSize(QtCore.QSize(50, 50))
        self.prof_btn.setFlat(True)
        self.prof_btn.setObjectName("prof_btn")
        self.profile.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.profile.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.profile)
        self.gridLayout.addWidget(self.navbar, 1, 0, 1, 1)
        self.app_panel = QtWidgets.QStackedWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_panel.sizePolicy().hasHeightForWidth())
        self.app_panel.setSizePolicy(sizePolicy)
        self.app_panel.setMinimumSize(QtCore.QSize(1200, 690))
        self.app_panel.setObjectName("app_panel")
        self.home_page = Home()
        self.home_page.setObjectName("home_page")
        self.app_panel.addWidget(self.home_page)
        self.edit_page = Edit()
        self.edit_page.setObjectName("edit_page")
        self.app_panel.addWidget(self.edit_page)
        self.library_page = Library()
        self.library_page.setObjectName("library_page")
        self.app_panel.addWidget(self.library_page)
        self.request_page = Request()
        self.request_page.setObjectName("request_page")
        self.app_panel.addWidget(self.request_page)
        self.setting_page = Setting()
        self.setting_page.setObjectName("setting_page")
        self.app_panel.addWidget(self.setting_page)
        self.book_page = Book()
        self.book_page.setObjectName("book_page")
        self.app_panel.addWidget(self.book_page)
        self.chart_page = Chart()
        self.chart_page.setObjectName("chart_page")
        self.app_panel.addWidget(self.chart_page)
        self.gridLayout.addWidget(self.app_panel, 2, 0, 1, 1)
        self.app_panel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def goToHome(self):
        self.setWindowTitle("Booque - Home")
        self.app_panel.setCurrentIndex(0)

    def handleMenu(self, action):
        if action == "Edit Profile":
            self.setWindowTitle("Booque - Edit Profile")
            self.home_btn.hide()
            self.prof_btn.hide()
            self.prof.hide()
            self.app_panel.setCurrentIndex(1)
        elif action == "Library":
            self.setWindowTitle("Booque - Library")
            libApp.reset()
            self.app_panel.setCurrentIndex(2)
        elif action == "Request":
            self.setWindowTitle("Booque - Request")
            self.app_panel.setCurrentIndex(3)
        elif action == "Setting":
            self.setWindowTitle("Booque - Setting")
            self.app_panel.setCurrentIndex(4)
        if action == "Chart":
            self.setWindowTitle("Booque - Charts")
            chartApp.reset()
            self.app_panel.setCurrentIndex(6)
        elif action == "Log out":
            db.database.curs.execute("DELETE FROM current_user")
            db.database.db.commit()
            db.database.updateDatabase(False, False, False, True)
            db.database.exit(1)

            self.log_in = authen.LogIn()
            self.log_in.show()
            self.close()


class Book(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        global bookApp
        bookApp = self
        self.setupUi()
        self.setStyleSheet(bookStyle.default)
        self.book_id = None
        self.rating = 0.00
        self.btn05.toggled.connect(lambda: self.updateStar(float(self.btn05.text())))
        self.star05.setPixmap(db.database.star_off)
        self.star05.setScaledContents(True)
        self.btn1.toggled.connect(lambda: self.updateStar(float(self.btn1.text())))
        self.star1.setPixmap(db.database.star_off_latter)
        self.star1.setScaledContents(True)
        self.btn15.toggled.connect(lambda: self.updateStar(float(self.btn15.text())))
        self.star15.setPixmap(db.database.star_off)
        self.star15.setScaledContents(True)
        self.btn2.toggled.connect(lambda: self.updateStar(float(self.btn2.text())))
        self.star2.setPixmap(db.database.star_off_latter)
        self.star2.setScaledContents(True)
        self.btn25.toggled.connect(lambda: self.updateStar(float(self.btn25.text())))
        self.star25.setPixmap(db.database.star_off)
        self.star25.setScaledContents(True)
        self.btn3.toggled.connect(lambda: self.updateStar(float(self.btn3.text())))
        self.star3.setPixmap(db.database.star_off_latter)
        self.star3.setScaledContents(True)
        self.btn35.toggled.connect(lambda: self.updateStar(float(self.btn35.text())))
        self.star35.setPixmap(db.database.star_off)
        self.star35.setScaledContents(True)
        self.btn4.toggled.connect(lambda: self.updateStar(float(self.btn4.text())))
        self.star4.setPixmap(db.database.star_off_latter)
        self.star4.setScaledContents(True)
        self.btn45.toggled.connect(lambda: self.updateStar(float(self.btn45.text())))
        self.star45.setPixmap(db.database.star_off)
        self.star45.setScaledContents(True)
        self.btn5.toggled.connect(lambda: self.updateStar(float(self.btn5.text())))
        self.star5.setPixmap(db.database.star_off_latter)
        self.star5.setScaledContents(True)
        self.user_img.setScaledContents(True)
        self.user_frame.setScaledContents(True)
        self.star_btn.clicked.connect(self.resetStar)
        self.submit_btn.clicked.connect(self.submitReview)
        QtWidgets.QScroller.grabGesture(
            self.scrollArea, QtWidgets.QScroller.LeftMouseButtonGesture
        )
        self.user_frame.setPixmap(QtGui.QPixmap("rsrc/img/frame.png"))
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon("rsrc/img/logo.png"))

    def setupUi(self):
        self.setObjectName("Book")
        self.resize(1200, 640)
        self.setMinimumSize(QtCore.QSize(1200, 640))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(30, 40, 30, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(10)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContents = QtWidgets.QWidget()
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 1140, 1494))
        self.scrollAreaContents.setObjectName("scrollAreaContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaContents)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 30)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(100)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem, 3, 8, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem1, 4, 0, 1, 1)
        self.review_section = QtWidgets.QFrame(self.scrollAreaContents)
        self.review_section.setObjectName("review_section")
        self.review_container = QtWidgets.QGridLayout(self.review_section)
        self.review_container.setContentsMargins(0, 0, 0, 30)
        self.review_container.setSpacing(20)
        self.review_container.setObjectName("review_container")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.review_container.addItem(spacerItem2, 1, 6, 1, 1)
        self.stars = QtWidgets.QFrame(self.review_section)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stars.sizePolicy().hasHeightForWidth())
        self.stars.setSizePolicy(sizePolicy)
        self.stars.setMinimumSize(QtCore.QSize(150, 30))
        self.stars.setMaximumSize(QtCore.QSize(150, 30))
        self.stars.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stars.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stars.setObjectName("stars")
        self.star05 = QtWidgets.QLabel(self.stars)
        self.star05.setGeometry(QtCore.QRect(0, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star05.sizePolicy().hasHeightForWidth())
        self.star05.setSizePolicy(sizePolicy)
        self.star05.setMinimumSize(QtCore.QSize(15, 30))
        self.star05.setMaximumSize(QtCore.QSize(15, 30))
        self.star05.setText("")
        self.star05.setObjectName("star05")
        self.star1 = QtWidgets.QLabel(self.stars)
        self.star1.setGeometry(QtCore.QRect(15, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star1.sizePolicy().hasHeightForWidth())
        self.star1.setSizePolicy(sizePolicy)
        self.star1.setMinimumSize(QtCore.QSize(15, 30))
        self.star1.setMaximumSize(QtCore.QSize(15, 30))
        self.star1.setText("")
        self.star1.setObjectName("star1")
        self.star15 = QtWidgets.QLabel(self.stars)
        self.star15.setGeometry(QtCore.QRect(30, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star15.sizePolicy().hasHeightForWidth())
        self.star15.setSizePolicy(sizePolicy)
        self.star15.setMinimumSize(QtCore.QSize(15, 30))
        self.star15.setMaximumSize(QtCore.QSize(15, 30))
        self.star15.setText("")
        self.star15.setObjectName("star15")
        self.star2 = QtWidgets.QLabel(self.stars)
        self.star2.setGeometry(QtCore.QRect(45, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star2.sizePolicy().hasHeightForWidth())
        self.star2.setSizePolicy(sizePolicy)
        self.star2.setMinimumSize(QtCore.QSize(15, 30))
        self.star2.setMaximumSize(QtCore.QSize(15, 30))
        self.star2.setText("")
        self.star2.setObjectName("star2")
        self.star25 = QtWidgets.QLabel(self.stars)
        self.star25.setGeometry(QtCore.QRect(60, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star25.sizePolicy().hasHeightForWidth())
        self.star25.setSizePolicy(sizePolicy)
        self.star25.setMinimumSize(QtCore.QSize(15, 30))
        self.star25.setMaximumSize(QtCore.QSize(15, 30))
        self.star25.setText("")
        self.star25.setObjectName("star25")
        self.star3 = QtWidgets.QLabel(self.stars)
        self.star3.setGeometry(QtCore.QRect(75, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star3.sizePolicy().hasHeightForWidth())
        self.star3.setSizePolicy(sizePolicy)
        self.star3.setMinimumSize(QtCore.QSize(15, 30))
        self.star3.setMaximumSize(QtCore.QSize(15, 30))
        self.star3.setText("")
        self.star3.setObjectName("star3")
        self.star35 = QtWidgets.QLabel(self.stars)
        self.star35.setGeometry(QtCore.QRect(90, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star35.sizePolicy().hasHeightForWidth())
        self.star35.setSizePolicy(sizePolicy)
        self.star35.setMinimumSize(QtCore.QSize(15, 30))
        self.star35.setMaximumSize(QtCore.QSize(15, 30))
        self.star35.setText("")
        self.star35.setObjectName("star35")
        self.star4 = QtWidgets.QLabel(self.stars)
        self.star4.setGeometry(QtCore.QRect(105, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star4.sizePolicy().hasHeightForWidth())
        self.star4.setSizePolicy(sizePolicy)
        self.star4.setMinimumSize(QtCore.QSize(15, 30))
        self.star4.setMaximumSize(QtCore.QSize(15, 30))
        self.star4.setText("")
        self.star4.setObjectName("star4")
        self.star45 = QtWidgets.QLabel(self.stars)
        self.star45.setGeometry(QtCore.QRect(120, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star45.sizePolicy().hasHeightForWidth())
        self.star45.setSizePolicy(sizePolicy)
        self.star45.setMinimumSize(QtCore.QSize(15, 30))
        self.star45.setMaximumSize(QtCore.QSize(15, 30))
        self.star45.setText("")
        self.star45.setObjectName("star45")
        self.star5 = QtWidgets.QLabel(self.stars)
        self.star5.setGeometry(QtCore.QRect(135, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star5.sizePolicy().hasHeightForWidth())
        self.star5.setSizePolicy(sizePolicy)
        self.star5.setMinimumSize(QtCore.QSize(15, 30))
        self.star5.setMaximumSize(QtCore.QSize(15, 30))
        self.star5.setText("")
        self.star5.setObjectName("star5")
        self.btn05 = QtWidgets.QRadioButton(self.stars)
        self.btn05.setGeometry(QtCore.QRect(0, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn05.sizePolicy().hasHeightForWidth())
        self.btn05.setSizePolicy(sizePolicy)
        self.btn05.setMinimumSize(QtCore.QSize(15, 30))
        self.btn05.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(1000)
        self.btn05.setFont(font)
        self.btn05.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn05.setObjectName("btn05")
        self.btn1 = QtWidgets.QRadioButton(self.stars)
        self.btn1.setGeometry(QtCore.QRect(15, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setMinimumSize(QtCore.QSize(15, 30))
        self.btn1.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(1000)
        self.btn1.setFont(font)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1.setObjectName("btn1")
        self.btn15 = QtWidgets.QRadioButton(self.stars)
        self.btn15.setGeometry(QtCore.QRect(30, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn15.sizePolicy().hasHeightForWidth())
        self.btn15.setSizePolicy(sizePolicy)
        self.btn15.setMinimumSize(QtCore.QSize(15, 30))
        self.btn15.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(1000)
        self.btn15.setFont(font)
        self.btn15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn15.setObjectName("btn15")
        self.btn2 = QtWidgets.QRadioButton(self.stars)
        self.btn2.setGeometry(QtCore.QRect(45, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setMinimumSize(QtCore.QSize(15, 30))
        self.btn2.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(1000)
        self.btn2.setFont(font)
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn2.setObjectName("btn2")
        self.btn25 = QtWidgets.QRadioButton(self.stars)
        self.btn25.setGeometry(QtCore.QRect(60, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn25.sizePolicy().hasHeightForWidth())
        self.btn25.setSizePolicy(sizePolicy)
        self.btn25.setMinimumSize(QtCore.QSize(15, 30))
        self.btn25.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(1000)
        self.btn25.setFont(font)
        self.btn25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn25.setObjectName("btn25")
        self.btn35 = QtWidgets.QRadioButton(self.stars)
        self.btn35.setGeometry(QtCore.QRect(90, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn35.sizePolicy().hasHeightForWidth())
        self.btn35.setSizePolicy(sizePolicy)
        self.btn35.setMinimumSize(QtCore.QSize(15, 30))
        self.btn35.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(1000)
        self.btn35.setFont(font)
        self.btn35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn35.setObjectName("btn35")
        self.btn4 = QtWidgets.QRadioButton(self.stars)
        self.btn4.setGeometry(QtCore.QRect(105, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setMinimumSize(QtCore.QSize(15, 30))
        self.btn4.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(1000)
        self.btn4.setFont(font)
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn4.setObjectName("btn4")
        self.btn45 = QtWidgets.QRadioButton(self.stars)
        self.btn45.setGeometry(QtCore.QRect(120, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn45.sizePolicy().hasHeightForWidth())
        self.btn45.setSizePolicy(sizePolicy)
        self.btn45.setMinimumSize(QtCore.QSize(15, 30))
        self.btn45.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(1000)
        self.btn45.setFont(font)
        self.btn45.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn45.setObjectName("btn45")
        self.btn5 = QtWidgets.QRadioButton(self.stars)
        self.btn5.setGeometry(QtCore.QRect(135, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        self.btn5.setMinimumSize(QtCore.QSize(15, 30))
        self.btn5.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(1000)
        self.btn5.setFont(font)
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn5.setObjectName("btn5")
        self.btn3 = QtWidgets.QRadioButton(self.stars)
        self.btn3.setGeometry(QtCore.QRect(75, 0, 15, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(25)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setMinimumSize(QtCore.QSize(15, 30))
        self.btn3.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(1000)
        self.btn3.setFont(font)
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3.setObjectName("btn3")
        self.review_container.addWidget(self.stars, 1, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.review_section)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(50, 50))
        self.frame.setMaximumSize(QtCore.QSize(50, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.user_img = QtWidgets.QLabel(self.frame)
        self.user_img.setGeometry(QtCore.QRect(0, 0, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_img.sizePolicy().hasHeightForWidth())
        self.user_img.setSizePolicy(sizePolicy)
        self.user_img.setMinimumSize(QtCore.QSize(50, 50))
        self.user_img.setMaximumSize(QtCore.QSize(50, 50))
        self.user_img.setText("")
        self.user_img.setObjectName("user_img")
        self.user_frame = QtWidgets.QLabel(self.frame)
        self.user_frame.setGeometry(QtCore.QRect(0, 0, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_frame.sizePolicy().hasHeightForWidth())
        self.user_frame.setSizePolicy(sizePolicy)
        self.user_frame.setMaximumSize(QtCore.QSize(50, 50))
        self.user_frame.setSizeIncrement(QtCore.QSize(50, 50))
        self.user_frame.setText("")
        self.user_frame.setObjectName("user_frame")
        self.review_container.addWidget(self.frame, 1, 1, 1, 1)
        self.comment_section = QtWidgets.QVBoxLayout()
        self.comment_section.setContentsMargins(0, 30, -1, 100)
        self.comment_section.setSpacing(40)
        self.comment_section.setObjectName("comment_section")
        self.review_container.addLayout(self.comment_section, 0, 1, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.review_container.addItem(spacerItem3, 3, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.review_container.addItem(spacerItem4, 3, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.review_container.addItem(spacerItem5, 2, 0, 1, 1)
        self.comment = QtWidgets.QTextEdit(self.review_section)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comment.sizePolicy().hasHeightForWidth())
        self.comment.setSizePolicy(sizePolicy)
        self.comment.setMinimumSize(QtCore.QSize(600, 200))
        self.comment.setMaximumSize(QtCore.QSize(600, 200))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.comment.setFont(font)
        self.comment.setObjectName("comment")
        self.review_container.addWidget(self.comment, 2, 2, 1, 4)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.review_container.addItem(spacerItem6, 0, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.review_container.addItem(spacerItem7, 0, 0, 1, 1)
        self.submit_btn = QtWidgets.QPushButton(self.review_section)
        self.submit_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.submit_btn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.submit_btn.setFont(font)
        self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_btn.setObjectName("submit_btn")
        self.review_container.addWidget(self.submit_btn, 3, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.review_container.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.review_container.addItem(spacerItem9, 2, 6, 1, 1)
        self.star_btn = QtWidgets.QPushButton(self.review_section)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.star_btn.sizePolicy().hasHeightForWidth())
        self.star_btn.setSizePolicy(sizePolicy)
        self.star_btn.setMinimumSize(QtCore.QSize(60, 30))
        self.star_btn.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.star_btn.setFont(font)
        self.star_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.star_btn.setObjectName("star_btn")
        self.review_container.addWidget(self.star_btn, 1, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.review_container.addItem(spacerItem10, 1, 4, 1, 1)
        self.gridLayout_3.addWidget(self.review_section, 5, 1, 1, 6)
        spacerItem11 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem11, 4, 8, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem12, 5, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem13, 5, 8, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(
            0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem14, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 10, 0, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.book_img = QtWidgets.QLabel(self.scrollAreaContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_img.sizePolicy().hasHeightForWidth())
        self.book_img.setSizePolicy(sizePolicy)
        self.book_img.setMinimumSize(QtCore.QSize(360, 550))
        self.book_img.setMaximumSize(QtCore.QSize(360, 550))
        self.book_img.setText("")
        self.book_img.setObjectName("book_img")
        self.verticalLayout_2.addWidget(self.book_img)
        spacerItem15 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem15)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.book_title = QtWidgets.QLabel(self.scrollAreaContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_title.sizePolicy().hasHeightForWidth())
        self.book_title.setSizePolicy(sizePolicy)
        self.book_title.setMinimumSize(QtCore.QSize(600, 0))
        self.book_title.setMaximumSize(QtCore.QSize(1800, 16777215))
        font = QtGui.QFont()
        font.setFamily("Freight")
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.book_title.setFont(font)
        self.book_title.setScaledContents(True)
        self.book_title.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.book_title.setWordWrap(True)
        self.book_title.setObjectName("book_title")
        self.verticalLayout.addWidget(self.book_title)
        self.book_author = QtWidgets.QLabel(self.scrollAreaContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_author.sizePolicy().hasHeightForWidth())
        self.book_author.setSizePolicy(sizePolicy)
        self.book_author.setMinimumSize(QtCore.QSize(600, 0))
        self.book_author.setMaximumSize(QtCore.QSize(1800, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Medium")
        font.setPointSize(20)
        self.book_author.setFont(font)
        self.book_author.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.book_author.setWordWrap(True)
        self.book_author.setObjectName("book_author")
        self.verticalLayout.addWidget(self.book_author)
        self.book_rating = QtWidgets.QLabel(self.scrollAreaContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_rating.sizePolicy().hasHeightForWidth())
        self.book_rating.setSizePolicy(sizePolicy)
        self.book_rating.setMinimumSize(QtCore.QSize(600, 0))
        self.book_rating.setMaximumSize(QtCore.QSize(1800, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Medium")
        font.setPointSize(16)
        self.book_rating.setFont(font)
        self.book_rating.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.book_rating.setWordWrap(True)
        self.book_rating.setObjectName("book_rating")
        self.verticalLayout.addWidget(self.book_rating)
        spacerItem16 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 5, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setSpacing(50)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.synop_label = QtWidgets.QLabel(self.scrollAreaContents)
        font = QtGui.QFont()
        font.setFamily("Freight")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.synop_label.setFont(font)
        self.synop_label.setObjectName("synop_label")
        self.verticalLayout_3.addWidget(self.synop_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line = QtWidgets.QFrame(self.scrollAreaContents)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.book_synop = QtWidgets.QLabel(self.scrollAreaContents)
        font = QtGui.QFont()
        font.setFamily("Palatino")
        font.setPointSize(18)
        self.book_synop.setFont(font)
        self.book_synop.setWordWrap(True)
        self.book_synop.setObjectName("book_synop")
        self.horizontalLayout_2.addWidget(self.book_synop)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 4, 5, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.btn05.setText(_translate("Book", "0.5"))
        self.btn1.setText(_translate("Book", "1"))
        self.btn15.setText(_translate("Book", "1.5"))
        self.btn2.setText(_translate("Book", "2"))
        self.btn25.setText(_translate("Book", "2.5"))
        self.btn35.setText(_translate("Book", "3.5"))
        self.btn4.setText(_translate("Book", "4"))
        self.btn45.setText(_translate("Book", "4.5"))
        self.btn5.setText(_translate("Book", "5"))
        self.btn3.setText(_translate("Book", "3"))
        self.comment.setPlaceholderText(_translate("Book", "Write Something..."))
        self.submit_btn.setText(_translate("Book", "Submit"))
        self.star_btn.setText(_translate("Book", "Reset"))
        self.synop_label.setText(_translate("Book", "Synopsis"))

    def setId(self, id):
        self.book_id = id
        self.currentRating = QtWidgets.QRadioButton()
        self.scrollArea.verticalScrollBar().setValue(0)
        self.resetId()
        self.book_title.setText(
            [i[1] for i in db.database.books_ll if i[0] == self.book_id][0]
        )
        self.book_author.setText(
            [i[3] for i in db.database.books_ll if i[0] == self.book_id][0]
        )
        self.book_rating.setText(
            "⭐ {0:.2f}".format(
                ([float(i[7]) for i in db.database.books_ll if i[0] == self.book_id][0])
            )
        )
        self.book_img.setPixmap(
            [i[2] for i in db.database.books_ll if i[0] == self.book_id][0]
        )
        self.book_img.setScaledContents(True)
        self.book_synop.setText(
            [i[5] for i in db.database.books_ll if i[0] == self.book_id][0].replace(
                "\n", "\n\n"
            )
        )
        self.user_img.setPixmap(
            [i[6] for i in db.database.users_ll if i[0] == app.id][0]
        )

        try:
            self.past_rating = [
                x[3]
                for x in db.database.ratings_ll
                if x[1] == self.book_id and x[2] == app.id
            ][0]
        except:
            self.past_rating = 0
        self.updateStar(self.past_rating)
        self.updateComment()

    def resetId(self):
        self.currentRating.setAutoExclusive(False)
        self.currentRating.setChecked(False)
        self.currentRating.setAutoExclusive(True)
        self.updateStar(0)
        self.updateComment()

    def resetStar(self):
        if self.rating != 0:
            self.past_rating = 0
            self.rating = 0
            db.database.curs.execute(
                "DELETE FROM ratings WHERE book_id="
                + str(self.book_id)
                + " and user_id="
                + str(app.id)
            )
            db.database.db.commit()
            db.database.updateDatabase(True, False, False, False)
            ratings = []
            for i in db.database.ratings_ll:
                if i[1] == self.book_id:
                    ratings.append(i[3])
            if ratings:
                db.database.curs.execute(
                    "UPDATE books SET rating="
                    + str(float(sum(ratings) / len(ratings)))
                    + " WHERE book_id="
                    + str(self.book_id)
                )
            else:
                db.database.curs.execute(
                    "UPDATE books SET rating="
                    + str(0.0)
                    + " WHERE book_id="
                    + str(self.book_id)
                )
            db.database.db.commit()
            db.database.updateDatabase(False, False, True, False)
            self.resetId()

    def updateStar(self, id):
        self.rating = id
        if self.rating == 0:
            self.star05.setPixmap(db.database.star_off)
            self.star1.setPixmap(db.database.star_off_latter)
            self.star15.setPixmap(db.database.star_off)
            self.star2.setPixmap(db.database.star_off_latter)
            self.star25.setPixmap(db.database.star_off)
            self.star3.setPixmap(db.database.star_off_latter)
            self.star35.setPixmap(db.database.star_off)
            self.star4.setPixmap(db.database.star_off_latter)
            self.star45.setPixmap(db.database.star_off)
            self.star5.setPixmap(db.database.star_off_latter)
        elif self.rating == 0.5:
            self.currentRating = self.btn05
            self.star05.setPixmap(db.database.star)
            self.star1.setPixmap(db.database.star_off_latter)
            self.star15.setPixmap(db.database.star_off)
            self.star2.setPixmap(db.database.star_off_latter)
            self.star25.setPixmap(db.database.star_off)
            self.star3.setPixmap(db.database.star_off_latter)
            self.star35.setPixmap(db.database.star_off)
            self.star4.setPixmap(db.database.star_off_latter)
            self.star45.setPixmap(db.database.star_off)
            self.star5.setPixmap(db.database.star_off_latter)
        elif self.rating == 1:
            self.currentRating = self.btn1
            self.star05.setPixmap(db.database.star)
            self.star1.setPixmap(db.database.star_latter)
            self.star15.setPixmap(db.database.star_off)
            self.star2.setPixmap(db.database.star_off_latter)
            self.star25.setPixmap(db.database.star_off)
            self.star3.setPixmap(db.database.star_off_latter)
            self.star35.setPixmap(db.database.star_off)
            self.star4.setPixmap(db.database.star_off_latter)
            self.star45.setPixmap(db.database.star_off)
            self.star5.setPixmap(db.database.star_off_latter)
        elif self.rating == 1.5:
            self.currentRating = self.btn15
            self.star05.setPixmap(db.database.star)
            self.star1.setPixmap(db.database.star_latter)
            self.star15.setPixmap(db.database.star)
            self.star2.setPixmap(db.database.star_off_latter)
            self.star25.setPixmap(db.database.star_off)
            self.star3.setPixmap(db.database.star_off_latter)
            self.star35.setPixmap(db.database.star_off)
            self.star4.setPixmap(db.database.star_off_latter)
            self.star45.setPixmap(db.database.star_off)
            self.star5.setPixmap(db.database.star_off_latter)
        elif self.rating == 2:
            self.currentRating = self.btn2
            self.star05.setPixmap(db.database.star)
            self.star1.setPixmap(db.database.star_latter)
            self.star15.setPixmap(db.database.star)
            self.star2.setPixmap(db.database.star_latter)
            self.star25.setPixmap(db.database.star_off)
            self.star3.setPixmap(db.database.star_off_latter)
            self.star35.setPixmap(db.database.star_off)
            self.star4.setPixmap(db.database.star_off_latter)
            self.star45.setPixmap(db.database.star_off)
            self.star5.setPixmap(db.database.star_off_latter)
        elif self.rating == 2.5:
            self.currentRating = self.btn25
            self.star05.setPixmap(db.database.star)
            self.star1.setPixmap(db.database.star_latter)
            self.star15.setPixmap(db.database.star)
            self.star2.setPixmap(db.database.star_latter)
            self.star25.setPixmap(db.database.star)
            self.star3.setPixmap(db.database.star_off_latter)
            self.star35.setPixmap(db.database.star_off)
            self.star4.setPixmap(db.database.star_off_latter)
            self.star45.setPixmap(db.database.star_off)
            self.star5.setPixmap(db.database.star_off_latter)
        elif self.rating == 3:
            self.currentRating = self.btn3
            self.star05.setPixmap(db.database.star)
            self.star1.setPixmap(db.database.star_latter)
            self.star15.setPixmap(db.database.star)
            self.star2.setPixmap(db.database.star_latter)
            self.star25.setPixmap(db.database.star)
            self.star3.setPixmap(db.database.star_latter)
            self.star35.setPixmap(db.database.star_off)
            self.star4.setPixmap(db.database.star_off_latter)
            self.star45.setPixmap(db.database.star_off)
            self.star5.setPixmap(db.database.star_off_latter)
        elif self.rating == 3.5:
            self.currentRating = self.btn35
            self.star05.setPixmap(db.database.star)
            self.star1.setPixmap(db.database.star_latter)
            self.star15.setPixmap(db.database.star)
            self.star2.setPixmap(db.database.star_latter)
            self.star25.setPixmap(db.database.star)
            self.star3.setPixmap(db.database.star_latter)
            self.star35.setPixmap(db.database.star)
            self.star4.setPixmap(db.database.star_off_latter)
            self.star45.setPixmap(db.database.star_off)
            self.star5.setPixmap(db.database.star_off_latter)
        elif self.rating == 4:
            self.currentRating = self.btn4
            self.star05.setPixmap(db.database.star)
            self.star1.setPixmap(db.database.star_latter)
            self.star15.setPixmap(db.database.star)
            self.star2.setPixmap(db.database.star_latter)
            self.star25.setPixmap(db.database.star)
            self.star3.setPixmap(db.database.star_latter)
            self.star35.setPixmap(db.database.star)
            self.star4.setPixmap(db.database.star_latter)
            self.star45.setPixmap(db.database.star_off)
            self.star5.setPixmap(db.database.star_off_latter)
        elif self.rating == 4.5:
            self.currentRating = self.btn45
            self.star05.setPixmap(db.database.star)
            self.star1.setPixmap(db.database.star_latter)
            self.star15.setPixmap(db.database.star)
            self.star2.setPixmap(db.database.star_latter)
            self.star25.setPixmap(db.database.star)
            self.star3.setPixmap(db.database.star_latter)
            self.star35.setPixmap(db.database.star)
            self.star4.setPixmap(db.database.star_latter)
            self.star45.setPixmap(db.database.star)
            self.star5.setPixmap(db.database.star_off_latter)
        elif self.rating == 5:
            self.currentRating = self.btn5
            self.star05.setPixmap(db.database.star)
            self.star1.setPixmap(db.database.star_latter)
            self.star15.setPixmap(db.database.star)
            self.star2.setPixmap(db.database.star_latter)
            self.star25.setPixmap(db.database.star)
            self.star3.setPixmap(db.database.star_latter)
            self.star35.setPixmap(db.database.star)
            self.star4.setPixmap(db.database.star_latter)
            self.star45.setPixmap(db.database.star)
            self.star5.setPixmap(db.database.star_latter)

        self.book_rating.setText(
            "⭐ {0:.2f}".format(
                [float(i[7]) for i in db.database.books_ll if i[0] == self.book_id][0]
            )
        )

    def updateComment(self):
        self.clearLayout(self.comment_section)
        self.comment_id = [
            i[0] for i in db.database.comments_ll if i[1] == self.book_id
        ]
        rev_book_id = []
        rev_user_id = []
        if self.comment_id:
            self.pos = [i for i in range(len(self.comment_id))]
            for i in self.comment_id:
                rev_book_id.append(
                    [x[1] for x in db.database.comments_ll if x[0] == i][0]
                )
                rev_user_id.append(
                    [x[2] for x in db.database.comments_ll if x[0] == i][0]
                )
                self.rev_comment.append(
                    [x[3] for x in db.database.comments_ll if x[0] == i][0]
                )
                self.rev_date.append(
                    [x[4] for x in db.database.comments_ll if x[0] == i][0]
                )
            for i in rev_user_id:
                self.rev_fname.append(
                    [x[1] for x in db.database.users_ll if x[0] == i][0]
                )
                self.rev_lname.append(
                    [x[2] for x in db.database.users_ll if x[0] == i][0]
                )
                self.rev_username.append(
                    [x[3] for x in db.database.users_ll if x[0] == i][0]
                )
                self.rev_userimg.append(
                    [x[6] for x in db.database.users_ll if x[0] == i][0]
                )
            for i, j in zip(rev_book_id, rev_user_id):
                try:
                    self.rev_rating.append(
                        [
                            float(x[3])
                            for x in db.database.ratings_ll
                            if x[1] == i and x[2] == j
                        ][0]
                    )
                except:
                    self.rev_rating.append(None)

            for pos, id, comment, rating, date, fname, lname, username, userimg in zip(
                self.pos,
                self.comment_id,
                self.rev_comment,
                self.rev_rating,
                self.rev_date,
                self.rev_fname,
                self.rev_lname,
                self.rev_username,
                self.rev_userimg,
            ):
                user_container = QtWidgets.QHBoxLayout()
                user_container.setSpacing(10)
                user_frame = QtWidgets.QFrame()
                user_frame.setSizePolicy(
                    QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                    )
                )
                user_frame.setMinimumSize(QtCore.QSize(50, 50))
                user_frame.setMaximumSize(QtCore.QSize(50, 50))
                user_img = QtWidgets.QLabel(user_frame)
                user_img.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                )
                user_img.setMaximumSize(50, 50)
                user_img.setPixmap(QtGui.QPixmap(userimg))
                user_img.setGeometry(QtCore.QRect(0, 0, 50, 50))
                user_img.setScaledContents(True)
                frame = QtWidgets.QLabel(user_frame)
                frame.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                )
                frame.setMaximumSize(50, 50)
                if app.dark:
                    frame.setPixmap(QtGui.QPixmap("rsrc/img/frame_dark.png"))
                else:
                    frame.setPixmap(QtGui.QPixmap("rsrc/img/frame.png"))
                frame.setGeometry(QtCore.QRect(0, 0, 50, 50))
                frame.setScaledContents(True)
                user_container.addWidget(user_frame)
                user_name = QtWidgets.QLabel(self.review_section)
                if (
                    fname + " " + lname
                    == [i[1] for i in db.database.users_ll if i[0] == app.id][0]
                    + " "
                    + [i[2] for i in db.database.users_ll if i[0] == app.id][0]
                ):
                    user_name.setText("You")
                else:
                    user_name.setText(fname + " " + lname)
                user_name.setFont(QtGui.QFont("Product Sans", 12))
                user_name.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                )
                user_container.addWidget(user_name)
                user_username = QtWidgets.QLabel(self.review_section)
                user_username.setText("@" + username)
                user_username.setFont(QtGui.QFont("Product Sans", 12))
                user_username.setStyleSheet("color: grey;")
                user_container.addWidget(user_username)
                if rating:
                    user_rating = QtWidgets.QLabel(self.review_section)
                    user_rating.setText("⭐ {0:.1f}".format(rating))
                    user_rating.setFont(QtGui.QFont("Product Sans", 12))
                    user_container.addWidget(user_rating)
                spacerItem = QtWidgets.QSpacerItem(
                    5,
                    5,
                    QtWidgets.QSizePolicy.Expanding,
                    QtWidgets.QSizePolicy.Minimum,
                )
                user_container.addItem(spacerItem)
                if (
                    fname + " " + lname
                    == [i[1] for i in db.database.users_ll if i[0] == app.id][0]
                    + " "
                    + [i[2] for i in db.database.users_ll if i[0] == app.id][0]
                ):
                    del_comment = QtWidgets.QPushButton("-", self.review_section)
                    del_comment.setFont(QtGui.QFont("Helvetica Neue LT", 6))
                    del_comment.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                    )
                    del_comment.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    del_comment.setMinimumSize(14, 14)
                    del_comment.setIconSize(del_comment.minimumSize())
                    del_comment.setStyleSheet("border-radius: 7px; ")
                    del_comment.clicked.connect(lambda x, id=id: self.delComment(id))
                    user_container.addWidget(del_comment)
                comment_label = QtWidgets.QLabel(self.review_section)
                comment_label.setText(comment)
                comment_label.setFont(QtGui.QFont("Product Sans", 12))
                comment_label.setStyleSheet(
                    """
                    background-color: rgb(255, 231, 203);
                    border-radius: 15px;
                    margin-left: 60px;
                    padding: 10px 15px;
                    color: black;
                """
                )
                comment_label.setSizePolicy(
                    QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
                    )
                )
                comment_label.setMaximumHeight(100)
                comment_label.setAlignment(QtCore.Qt.AlignTop)
                comment_label.setWordWrap(True)
                comment_date = QtWidgets.QLabel(self.review_section)
                comment_date.setText(date)
                comment_date.setFont(QtGui.QFont("Product Sans", 10))
                comment_date.setStyleSheet("margin-left: 60px;")
                comment_date.setWordWrap(True)
                comment_container = QtWidgets.QVBoxLayout()
                comment_container.setSpacing(5)
                comment_container.addLayout(user_container, 0)
                comment_container.addWidget(comment_label, 1)
                comment_container.addWidget(comment_date, 2)
                self.comment_section.addLayout(comment_container, pos)

    def clearLayout(self, layout):
        self.comment_id = []
        self.rev_comment = []
        self.rev_rating = []
        self.rev_date = []
        self.rev_fname = []
        self.rev_lname = []
        self.rev_username = []
        self.rev_userimg = []
        self.pos = []
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clearLayout(child.layout())

    def submitReview(self):
        submitted = False
        date_created = datetime.datetime.now(LOCAL_TIMEZONE).strftime(
            "%a, %d %b %Y at %I:%M %p"
        )

        if self.comment.toPlainText():
            db.database.curs.execute(
                "INSERT INTO Comments (book_id, user_id, comment, date_created) VALUES (?,?,?,?)",
                [
                    self.book_id,
                    app.id,
                    self.comment.toPlainText(),
                    date_created,
                ],
            )
            db.database.db.commit()
            db.database.updateDatabase(True, False, False, False)
            self.comment.clear()
            submitted = True

        if self.rating != self.past_rating and self.rating != 0:
            self.past_rating = self.rating
            try:
                past_rating = [
                    x[3]
                    for x in db.database.ratings_ll
                    if x[1] == self.book_id and x[2] == app.id
                ][0]
            except:
                past_rating = None
            if not past_rating:
                db.database.curs.execute(
                    "INSERT INTO ratings (book_id, user_id, rating) VALUES (?,?,?)",
                    [self.book_id, app.id, self.rating],
                )
            else:
                db.database.curs.execute(
                    "UPDATE ratings SET rating="
                    + str(self.rating)
                    + " WHERE book_id="
                    + str(self.book_id)
                    + " and user_id="
                    + str(app.id)
                )
            db.database.db.commit()
            db.database.updateDatabase(True, False, False, False)
            ratings = []
            for i in db.database.ratings_ll:
                if i[1] == self.book_id:
                    ratings.append(i[3])
            db.database.curs.execute(
                "UPDATE books SET rating="
                + str(float(sum(ratings) / len(ratings)))
                + " WHERE book_id="
                + str(self.book_id)
            )
            db.database.db.commit()
            db.database.updateDatabase(False, False, True, False)
            self.book_rating.setText(
                "⭐ {0:.2f}".format(
                    [float(i[7]) for i in db.database.books_ll if i[0] == self.book_id][
                        0
                    ]
                )
            )
            submitted = True

        if submitted:
            submitted = False
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setWindowTitle("Review submitted")
            self.msg.setText("Your review is submitted.")
            self.msg.exec_()

        self.updateComment()

    def delComment(self, comment_id):
        self.msg.setIcon(QtWidgets.QMessageBox.Question)
        self.msg.setWindowTitle("Confirm deletion.")
        self.msg.setText("Are you sure to delete this comment?")
        self.msg.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel
        )
        self.msg.buttonClicked.connect(lambda x, id=comment_id: self.delete(x, id))
        self.msg.exec_()

    def delete(self, signal, comment_id):
        if signal.text() == "&Yes":
            db.database.curs.execute("DELETE FROM comments WHERE id=" + str(comment_id))
            db.database.db.commit()
            db.database.updateDatabase(True, False, False, False)
            self.updateComment()


class Chart(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        global chartApp
        chartApp = self
        self.setupUi()
        self.setStyleSheet(chartStyle.default)
        self.all_btn.toggled.connect(lambda: self.updateGenre(self.all_btn.text()))
        self.fiction_btn.toggled.connect(
            lambda: self.updateGenre(self.fiction_btn.text())
        )
        self.thriller_btn.toggled.connect(
            lambda: self.updateGenre(self.thriller_btn.text())
        )
        self.fantasy_btn.toggled.connect(
            lambda: self.updateGenre(self.fantasy_btn.text())
        )
        self.rom_btn.toggled.connect(lambda: self.updateGenre(self.rom_btn.text()))
        self.bio_btn.toggled.connect(lambda: self.updateGenre(self.bio_btn.text()))
        self.com_btn.toggled.connect(lambda: self.updateGenre(self.com_btn.text()))
        self.horror_btn.toggled.connect(
            lambda: self.updateGenre(self.horror_btn.text())
        )
        self.poetry_btn.toggled.connect(
            lambda: self.updateGenre(self.poetry_btn.text())
        )
        self.no1_btn.clicked.connect(lambda: self.goToBook(self.no1[0], self.no1[1]))
        self.no2_btn.clicked.connect(lambda: self.goToBook(self.no2[0], self.no2[1]))
        self.no3_btn.clicked.connect(lambda: self.goToBook(self.no3[0], self.no3[1]))
        self.no1_btn.setIconSize(self.no1_btn.size())
        self.no2_btn.setIconSize(self.no2_btn.size())
        self.no3_btn.setIconSize(self.no3_btn.size())
        self.updateGenre("All Genre")

    def setupUi(self):
        self.setObjectName("chart")
        self.resize(1200, 640)
        self.setMinimumSize(QtCore.QSize(1200, 640))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.genre_box = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genre_box.sizePolicy().hasHeightForWidth())
        self.genre_box.setSizePolicy(sizePolicy)
        self.genre_box.setMinimumSize(QtCore.QSize(200, 0))
        self.genre_box.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.genre_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.genre_box.setObjectName("genre_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.genre_box)
        self.verticalLayout_4.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(
            20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_4.addItem(spacerItem)
        self.all_btn = QtWidgets.QRadioButton(self.genre_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all_btn.sizePolicy().hasHeightForWidth())
        self.all_btn.setSizePolicy(sizePolicy)
        self.all_btn.setMinimumSize(QtCore.QSize(250, 55))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        self.all_btn.setFont(font)
        self.all_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.all_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.all_btn.setStyleSheet("")
        self.all_btn.setChecked(True)
        self.all_btn.setObjectName("all_btn")
        self.verticalLayout_4.addWidget(self.all_btn)
        self.fiction_btn = QtWidgets.QRadioButton(self.genre_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fiction_btn.sizePolicy().hasHeightForWidth())
        self.fiction_btn.setSizePolicy(sizePolicy)
        self.fiction_btn.setMinimumSize(QtCore.QSize(250, 55))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        self.fiction_btn.setFont(font)
        self.fiction_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fiction_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.fiction_btn.setObjectName("fiction_btn")
        self.verticalLayout_4.addWidget(self.fiction_btn)
        self.thriller_btn = QtWidgets.QRadioButton(self.genre_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thriller_btn.sizePolicy().hasHeightForWidth())
        self.thriller_btn.setSizePolicy(sizePolicy)
        self.thriller_btn.setMinimumSize(QtCore.QSize(250, 55))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        self.thriller_btn.setFont(font)
        self.thriller_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.thriller_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.thriller_btn.setObjectName("thriller_btn")
        self.verticalLayout_4.addWidget(self.thriller_btn)
        self.fantasy_btn = QtWidgets.QRadioButton(self.genre_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fantasy_btn.sizePolicy().hasHeightForWidth())
        self.fantasy_btn.setSizePolicy(sizePolicy)
        self.fantasy_btn.setMinimumSize(QtCore.QSize(250, 55))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        self.fantasy_btn.setFont(font)
        self.fantasy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fantasy_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.fantasy_btn.setObjectName("fantasy_btn")
        self.verticalLayout_4.addWidget(self.fantasy_btn)
        self.rom_btn = QtWidgets.QRadioButton(self.genre_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rom_btn.sizePolicy().hasHeightForWidth())
        self.rom_btn.setSizePolicy(sizePolicy)
        self.rom_btn.setMinimumSize(QtCore.QSize(250, 55))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        self.rom_btn.setFont(font)
        self.rom_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rom_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rom_btn.setObjectName("rom_btn")
        self.verticalLayout_4.addWidget(self.rom_btn)
        self.bio_btn = QtWidgets.QRadioButton(self.genre_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bio_btn.sizePolicy().hasHeightForWidth())
        self.bio_btn.setSizePolicy(sizePolicy)
        self.bio_btn.setMinimumSize(QtCore.QSize(250, 55))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        self.bio_btn.setFont(font)
        self.bio_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bio_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.bio_btn.setObjectName("bio_btn")
        self.verticalLayout_4.addWidget(self.bio_btn)
        self.com_btn = QtWidgets.QRadioButton(self.genre_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_btn.sizePolicy().hasHeightForWidth())
        self.com_btn.setSizePolicy(sizePolicy)
        self.com_btn.setMinimumSize(QtCore.QSize(250, 55))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        self.com_btn.setFont(font)
        self.com_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.com_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.com_btn.setObjectName("com_btn")
        self.verticalLayout_4.addWidget(self.com_btn)
        self.horror_btn = QtWidgets.QRadioButton(self.genre_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horror_btn.sizePolicy().hasHeightForWidth())
        self.horror_btn.setSizePolicy(sizePolicy)
        self.horror_btn.setMinimumSize(QtCore.QSize(250, 55))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        self.horror_btn.setFont(font)
        self.horror_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horror_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.horror_btn.setObjectName("horror_btn")
        self.verticalLayout_4.addWidget(self.horror_btn)
        self.poetry_btn = QtWidgets.QRadioButton(self.genre_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.poetry_btn.sizePolicy().hasHeightForWidth())
        self.poetry_btn.setSizePolicy(sizePolicy)
        self.poetry_btn.setMinimumSize(QtCore.QSize(250, 55))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        self.poetry_btn.setFont(font)
        self.poetry_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.poetry_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.poetry_btn.setObjectName("poetry_btn")
        self.verticalLayout_4.addWidget(self.poetry_btn)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_4.addItem(spacerItem1)
        self.gridLayout.addWidget(self.genre_box, 1, 0, 1, 1)
        self.rank = QtWidgets.QFrame(self)
        self.rank.setStyleSheet("")
        self.rank.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rank.setObjectName("rank")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.rank)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.genre_label = QtWidgets.QLabel(self.rank)
        self.genre_label.setMinimumSize(QtCore.QSize(250, 100))
        self.genre_label.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        font.setPointSize(36)
        self.genre_label.setFont(font)
        self.genre_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.genre_label.setObjectName("genre_label")
        self.gridLayout_2.addWidget(self.genre_label, 0, 1, 1, 5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_6.addItem(spacerItem2)
        self.first_label = QtWidgets.QLabel(self.rank)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        font.setPointSize(18)
        self.first_label.setFont(font)
        self.first_label.setAlignment(QtCore.Qt.AlignCenter)
        self.first_label.setObjectName("first_label")
        self.verticalLayout_6.addWidget(self.first_label)
        self.no1_btn = QtWidgets.QPushButton(self.rank)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no1_btn.sizePolicy().hasHeightForWidth())
        self.no1_btn.setSizePolicy(sizePolicy)
        self.no1_btn.setMinimumSize(QtCore.QSize(300, 460))
        self.no1_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.no1_btn.setText("")
        self.no1_btn.setObjectName("no1_btn")
        self.verticalLayout_6.addWidget(self.no1_btn)
        self.no1_rating = QtWidgets.QLabel(self.rank)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        self.no1_rating.setFont(font)
        self.no1_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.no1_rating.setObjectName("no1_rating")
        self.verticalLayout_6.addWidget(self.no1_rating)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_6.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 3, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_5.addItem(spacerItem4)
        self.second_label = QtWidgets.QLabel(self.rank)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        self.second_label.setFont(font)
        self.second_label.setAlignment(QtCore.Qt.AlignCenter)
        self.second_label.setObjectName("second_label")
        self.verticalLayout_5.addWidget(self.second_label)
        self.no2_btn = QtWidgets.QPushButton(self.rank)
        self.no2_btn.setMinimumSize(QtCore.QSize(250, 380))
        self.no2_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.no2_btn.setText("")
        self.no2_btn.setObjectName("no2_btn")
        self.verticalLayout_5.addWidget(self.no2_btn)
        self.no2_rating = QtWidgets.QLabel(self.rank)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        self.no2_rating.setFont(font)
        self.no2_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.no2_rating.setObjectName("no2_rating")
        self.verticalLayout_5.addWidget(self.no2_rating)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_5.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 2, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_7.addItem(spacerItem6)
        self.third_label = QtWidgets.QLabel(self.rank)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        self.third_label.setFont(font)
        self.third_label.setAlignment(QtCore.Qt.AlignCenter)
        self.third_label.setObjectName("third_label")
        self.verticalLayout_7.addWidget(self.third_label)
        self.no3_btn = QtWidgets.QPushButton(self.rank)
        self.no3_btn.setMinimumSize(QtCore.QSize(245, 375))
        self.no3_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.no3_btn.setText("")
        self.no3_btn.setObjectName("no3_btn")
        self.verticalLayout_7.addWidget(self.no3_btn)
        self.no3_rating = QtWidgets.QLabel(self.rank)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        self.no3_rating.setFont(font)
        self.no3_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.no3_rating.setObjectName("no3_rating")
        self.verticalLayout_7.addWidget(self.no3_rating)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_7.addItem(spacerItem7)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_2.addItem(spacerItem8, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_2.addItem(spacerItem9, 1, 5, 1, 1)
        self.gridLayout.addWidget(self.rank, 0, 3, 3, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.all_btn.setText(_translate("chart", "All Genre"))
        self.fiction_btn.setText(_translate("chart", "Fiction"))
        self.thriller_btn.setText(_translate("chart", "Thriller"))
        self.fantasy_btn.setText(_translate("chart", "Fantasy"))
        self.rom_btn.setText(_translate("chart", "Romance"))
        self.bio_btn.setText(_translate("chart", "Biography"))
        self.com_btn.setText(_translate("chart", "Comedy"))
        self.horror_btn.setText(_translate("chart", "Horror"))
        self.poetry_btn.setText(_translate("chart", "Poetry"))
        self.genre_label.setText(_translate("chart", "All Genre"))
        self.first_label.setText(_translate("chart", "WIN👑NER"))
        self.no1_rating.setText(_translate("chart", "⭐ 0"))
        self.second_label.setText(_translate("chart", "2nd place!"))
        self.no2_rating.setText(_translate("chart", "⭐ 0"))
        self.third_label.setText(_translate("chart", "3rd place!"))
        self.no3_rating.setText(_translate("chart", "⭐ 0"))

    def reset(self):
        self.updateGenre("All Genre")
        self.all_btn.setChecked(True)

    def updateGenre(self, genre):
        self.genre_label.setText(genre)
        if genre == "All Genre":
            self.no1 = db.database.books_ll.sort(2)[0]
            self.no2 = db.database.books_ll.sort(2)[1]
            self.no3 = db.database.books_ll.sort(2)[2]
        elif genre == "Fiction":
            self.no1 = db.database.fictions_ll.sort(2)[0]
            self.no2 = db.database.fictions_ll.sort(2)[1]
            self.no3 = db.database.fictions_ll.sort(2)[2]
        elif genre == "Thriller":
            self.no1 = db.database.thrillers_ll.sort(2)[0]
            self.no2 = db.database.thrillers_ll.sort(2)[1]
            self.no3 = db.database.thrillers_ll.sort(2)[2]
        elif genre == "Fantasy":
            self.no1 = db.database.fantasies_ll.sort(2)[0]
            self.no2 = db.database.fantasies_ll.sort(2)[1]
            self.no3 = db.database.fantasies_ll.sort(2)[2]
        elif genre == "Romance":
            self.no1 = db.database.romances_ll.sort(2)[0]
            self.no2 = db.database.romances_ll.sort(2)[1]
            self.no3 = db.database.romances_ll.sort(2)[2]
        elif genre == "Biography":
            self.no1 = db.database.biographies_ll.sort(2)[0]
            self.no2 = db.database.biographies_ll.sort(2)[1]
            self.no3 = db.database.biographies_ll.sort(2)[2]
        elif genre == "Comedy":
            self.no1 = db.database.comedies_ll.sort(2)[0]
            self.no2 = db.database.comedies_ll.sort(2)[1]
            self.no3 = db.database.comedies_ll.sort(2)[2]
        elif genre == "Horror":
            self.no1 = db.database.horrors_ll.sort(2)[0]
            self.no2 = db.database.horrors_ll.sort(2)[1]
            self.no3 = db.database.horrors_ll.sort(2)[2]
        elif genre == "Poetry":
            self.no1 = db.database.poetries_ll.sort(2)[0]
            self.no2 = db.database.poetries_ll.sort(2)[1]
            self.no3 = db.database.poetries_ll.sort(2)[2]
        self.no1_btn.setIcon(QtGui.QIcon(self.no1[2]))
        self.no2_btn.setIcon(QtGui.QIcon(self.no2[2]))
        self.no3_btn.setIcon(QtGui.QIcon(self.no3[2]))
        self.no1_rating.setText("⭐ {0:.2f}".format(float(self.no1[7])))
        self.no2_rating.setText("⭐ {0:.2f}".format(float(self.no2[7])))
        self.no3_rating.setText("⭐ {0:.2f}".format(float(self.no3[7])))

    def goToBook(self, book_id, book_title):
        authen.mainApp.setWindowTitle("Booque - " + book_title)
        authen.mainApp.app_panel.setCurrentIndex(5)
        bookApp.setId(int(book_id))


class Edit(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        global editApp
        editApp = self
        self.setupUi()
        self.setStyleSheet(editStyle.default)
        self.old_prof_pixmap = [i[6] for i in db.database.users_ll if i[0] == app.id][0]
        self.old_prof = [str(i[1]) for i in db.database.user_img if i[0] == app.id][0]
        self.prof_img.setPixmap(self.old_prof_pixmap)
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

    def setupUi(self):
        self.setObjectName("edit")
        self.resize(1200, 640)
        self.setMinimumSize(QtCore.QSize(1200, 640))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(100, 0, 100, 70)
        self.horizontalLayout.setSpacing(80)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.img = QtWidgets.QFrame(self)
        self.img.setMinimumSize(QtCore.QSize(420, 420))
        self.img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img.setObjectName("img")
        self.prof_img = QtWidgets.QLabel(self.img)
        self.prof_img.setGeometry(QtCore.QRect(0, 0, 420, 420))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prof_img.sizePolicy().hasHeightForWidth())
        self.prof_img.setSizePolicy(sizePolicy)
        self.prof_img.setMinimumSize(QtCore.QSize(420, 420))
        self.prof_img.setText("")
        self.prof_img.setObjectName("prof_img")
        self.img_frame = QtWidgets.QLabel(self.img)
        self.img_frame.setGeometry(QtCore.QRect(0, 0, 420, 420))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_frame.sizePolicy().hasHeightForWidth())
        self.img_frame.setSizePolicy(sizePolicy)
        self.img_frame.setMinimumSize(QtCore.QSize(420, 420))
        self.img_frame.setMaximumSize(QtCore.QSize(420, 420))
        self.img_frame.setText("")
        self.img_frame.setObjectName("img_frame")
        self.verticalLayout.addWidget(self.img)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.upload_btn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_btn.sizePolicy().hasHeightForWidth())
        self.upload_btn.setSizePolicy(sizePolicy)
        self.upload_btn.setMinimumSize(QtCore.QSize(25, 25))
        self.upload_btn.setMaximumSize(QtCore.QSize(25, 25))
        self.upload_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("rsrc/img/cam.png"), QtGui.QIcon.Normal, QtGui.QIcon.On
        )
        self.upload_btn.setIcon(icon)
        self.upload_btn.setIconSize(QtCore.QSize(25, 25))
        self.upload_btn.setObjectName("upload_btn")
        self.horizontalLayout_12.addWidget(self.upload_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.back_btn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back_btn.setFont(font)
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_13.addWidget(self.back_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.delete_account = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.delete_account.sizePolicy().hasHeightForWidth()
        )
        self.delete_account.setSizePolicy(sizePolicy)
        self.delete_account.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.delete_account.setFont(font)
        self.delete_account.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_account.setObjectName("delete_account")
        self.horizontalLayout_14.addWidget(self.delete_account)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.edit_frame = QtWidgets.QFrame(self)
        self.edit_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_frame.setObjectName("edit_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.edit_frame)
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.edit_label = QtWidgets.QLabel(self.edit_frame)
        self.edit_label.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        font.setPointSize(35)
        self.edit_label.setFont(font)
        self.edit_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.edit_label.setObjectName("edit_label")
        self.verticalLayout_2.addWidget(self.edit_label)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.edit_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(160, 0))
        self.label_5.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.username = QtWidgets.QLineEdit(self.edit_frame)
        self.username.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(11)
        self.username.setFont(font)
        self.username.setFrame(False)
        self.username.setClearButtonEnabled(True)
        self.username.setObjectName("username")
        self.horizontalLayout_9.addWidget(self.username)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.edit_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(160, 0))
        self.label_9.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.f_name = QtWidgets.QLineEdit(self.edit_frame)
        self.f_name.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(11)
        self.f_name.setFont(font)
        self.f_name.setFrame(False)
        self.f_name.setClearButtonEnabled(True)
        self.f_name.setObjectName("f_name")
        self.horizontalLayout_8.addWidget(self.f_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.edit_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(160, 0))
        self.label_2.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.l_name = QtWidgets.QLineEdit(self.edit_frame)
        self.l_name.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(11)
        self.l_name.setFont(font)
        self.l_name.setFrame(False)
        self.l_name.setClearButtonEnabled(True)
        self.l_name.setObjectName("l_name")
        self.horizontalLayout_2.addWidget(self.l_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.edit_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(160, 0))
        self.label_6.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.email = QtWidgets.QLineEdit(self.edit_frame)
        self.email.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(11)
        self.email.setFont(font)
        self.email.setFrame(False)
        self.email.setClearButtonEnabled(True)
        self.email.setObjectName("email")
        self.horizontalLayout_5.addWidget(self.email)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.edit_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(160, 0))
        self.label_3.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(self.edit_frame)
        self.password.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(11)
        self.password.setFont(font)
        self.password.setFrame(False)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(False)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.edit_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(160, 0))
        self.label_8.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.re_password = QtWidgets.QLineEdit(self.edit_frame)
        self.re_password.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        font.setPointSize(11)
        self.re_password.setFont(font)
        self.re_password.setFrame(False)
        self.re_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.re_password.setClearButtonEnabled(False)
        self.re_password.setObjectName("re_password")
        self.horizontalLayout_7.addWidget(self.re_password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.edit_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(160, 0))
        self.label_7.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.cur_read_box = QtWidgets.QComboBox(self.edit_frame)
        self.cur_read_box.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT")
        self.cur_read_box.setFont(font)
        self.cur_read_box.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cur_read_box.setCurrentText("")
        self.cur_read_box.setObjectName("cur_read_box")
        self.horizontalLayout_6.addWidget(self.cur_read_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem9)
        self.frame = QtWidgets.QFrame(self.edit_frame)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.save_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_4.addWidget(self.save_btn)
        self.restore_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restore_btn.sizePolicy().hasHeightForWidth())
        self.restore_btn.setSizePolicy(sizePolicy)
        self.restore_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.restore_btn.setFont(font)
        self.restore_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restore_btn.setObjectName("restore_btn")
        self.horizontalLayout_4.addWidget(self.restore_btn)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.edit_frame)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.upload_btn, self.username)
        self.setTabOrder(self.username, self.f_name)
        self.setTabOrder(self.f_name, self.l_name)
        self.setTabOrder(self.l_name, self.email)
        self.setTabOrder(self.email, self.password)
        self.setTabOrder(self.password, self.re_password)
        self.setTabOrder(self.re_password, self.cur_read_box)
        self.setTabOrder(self.cur_read_box, self.back_btn)
        self.setTabOrder(self.back_btn, self.save_btn)
        self.setTabOrder(self.save_btn, self.restore_btn)
        self.setTabOrder(self.restore_btn, self.delete_account)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.back_btn.setText(_translate("edit", "Back"))
        self.delete_account.setText(_translate("edit", "Delete Account"))
        self.edit_label.setText(_translate("edit", "Edit Profile"))
        self.label_5.setText(_translate("edit", "Username"))
        self.username.setPlaceholderText(_translate("edit", "Username"))
        self.label_9.setText(_translate("edit", "First name"))
        self.f_name.setPlaceholderText(_translate("edit", "First name"))
        self.label_2.setText(_translate("edit", "Last name"))
        self.l_name.setPlaceholderText(_translate("edit", "Last name"))
        self.label_6.setText(_translate("edit", "E-mail"))
        self.email.setPlaceholderText(_translate("edit", "E-mail"))
        self.label_3.setText(_translate("edit", "Password"))
        self.password.setPlaceholderText(
            _translate("edit", "Password must be 8 or more charactors")
        )
        self.label_8.setText(_translate("edit", "Confirm password"))
        self.re_password.setPlaceholderText(
            _translate("edit", "Password must be 8 or more charactors")
        )
        self.label_7.setText(_translate("edit", "Currently Reading"))
        self.save_btn.setText(_translate("edit", "Save Changes"))
        self.restore_btn.setText(_translate("edit", "Restore Profile Data"))

    def goToHome(self):
        self.prof_img.setPixmap(self.old_prof_pixmap)
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
            db.database.updateDatabase(True, True, False, False)
            ratings = {}
            for i in db.database.ratings_ll:
                try:
                    ratings[i[1]].append(i[3])
                except:
                    ratings[i[1]] = [i[3]]
            if ratings:
                ratings_avg = []
                for i, j in zip(ratings.keys(), ratings.values()):
                    j = float(sum(j) / len(j))
                    ratings_avg.append([i, j])
                    for i in ratings_avg:
                        db.database.curs.execute(
                            "UPDATE books SET rating="
                            + str(i[1])
                            + " WHERE book_id="
                            + str(i[0])
                        )
            else:
                for i in db.database.books_ll:
                    db.database.curs.execute(
                        "UPDATE books SET rating="
                        + str(0.0)
                        + " WHERE book_id="
                        + str(i[0])
                    )
            db.database.db.commit()
            db.database.updateDatabase(False, False, True, True)
            db.database.exit(1)

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
            self.prof_img.setPixmap(self.old_prof_pixmap)

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
                self.old_prof_pixmap = QtGui.QPixmap(self.new_prof)
                authen.mainApp.prof.setPixmap(self.old_prof_pixmap)
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
            db.database.updateRsrc()
            db.database.updateDatabase(False, True, False, False)
            homeApp.updateCurBook(self.cur_book_id)
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
        self.prof_img.setPixmap(self.old_prof_pixmap)
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


class Home(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        global homeApp
        homeApp = self
        self.setupUi()
        self.setStyleSheet(homeStyle.default)
        self.f_name = [str(i[1]) for i in db.database.users_ll if i[0] == app.id][0]
        self.cur_read = [i[7] for i in db.database.users_ll if i[0] == app.id][0]
        self.updateCurBook(self.cur_read)
        self.welcome_label.setText(
            "Welcome, " + self.f_name + "!\nto BOOQUE, your favorite book app."
        )
        self.quote_label.setText(
            '" The world breaks everyone, and afterward, many are strong at the broken places. "'
        )
        self.credit_label.setText("- Ernest Hemingway, A Farewell to Arms")
        self.welcome_label.resizeEvent = self.resizeWelcome
        self.quote_label.resizeEvent = self.resizeQuote
        self.credit_label.resizeEvent = self.resizeCredit

    def setupUi(self):
        self.setObjectName("home")
        self.resize(1200, 690)
        self.setMinimumSize(QtCore.QSize(1200, 690))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(40, 0, 30, 30)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.welcome_label = QtWidgets.QLabel(self)
        self.welcome_label.setMinimumSize(QtCore.QSize(350, 0))
        self.welcome_label.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Medium Ext")
        font.setPointSize(16)
        self.welcome_label.setFont(font)
        self.welcome_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.welcome_label.setWordWrap(True)
        self.welcome_label.setObjectName("welcome_label")
        self.verticalLayout_4.addWidget(self.welcome_label)
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_4.addItem(spacerItem)
        self.quote_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quote_label.sizePolicy().hasHeightForWidth())
        self.quote_label.setSizePolicy(sizePolicy)
        self.quote_label.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.quote_label.setFont(font)
        self.quote_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.quote_label.setWordWrap(True)
        self.quote_label.setObjectName("quote_label")
        self.verticalLayout_4.addWidget(self.quote_label)
        self.credit_label = QtWidgets.QLabel(self)
        self.credit_label.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Light Cond")
        font.setPointSize(16)
        self.credit_label.setFont(font)
        self.credit_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.credit_label.setWordWrap(True)
        self.credit_label.setObjectName("credit_label")
        self.verticalLayout_4.addWidget(self.credit_label)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.scrollArea = QtWidgets.QScrollArea(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(800, 16777215))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContents = QtWidgets.QWidget()
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 498, 660))
        self.scrollAreaContents.setMaximumSize(QtCore.QSize(800, 16777215))
        self.scrollAreaContents.setObjectName("scrollAreaContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cur_book = QtWidgets.QFrame(self.scrollAreaContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cur_book.sizePolicy().hasHeightForWidth())
        self.cur_book.setSizePolicy(sizePolicy)
        self.cur_book.setMinimumSize(QtCore.QSize(0, 660))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cur_book.setFont(font)
        self.cur_book.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cur_book.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cur_book.setObjectName("cur_book")
        self.gridLayout = QtWidgets.QGridLayout(self.cur_book)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.cur_btn = QtWidgets.QPushButton(self.cur_book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cur_btn.sizePolicy().hasHeightForWidth())
        self.cur_btn.setSizePolicy(sizePolicy)
        self.cur_btn.setMinimumSize(QtCore.QSize(360, 550))
        self.cur_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cur_btn.setText("")
        self.cur_btn.setFlat(True)
        self.cur_btn.setObjectName("cur_btn")
        self.gridLayout.addWidget(self.cur_btn, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.cur_label = QtWidgets.QLabel(self.cur_book)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        font.setPointSize(12)
        self.cur_label.setFont(font)
        self.cur_label.setText("")
        self.cur_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cur_label.setObjectName("cur_label")
        self.gridLayout.addWidget(self.cur_label, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.cur_book, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.welcome_label.setText(_translate("home", "Text"))
        self.quote_label.setText(_translate("home", '"Quote"'))
        self.credit_label.setText(_translate("home", "- Credit"))

    def resizeWelcome(self, event):
        if self.rect().width() // 75 > 16:
            font = QtGui.QFont(
                "Helvetica Neue LT Medium Ext", self.rect().width() // 75
            )
        else:
            font = QtGui.QFont("Helvetica Neue LT Medium Ext", 16)
        self.welcome_label.setFont(font)

    def resizeQuote(self, event):
        if self.rect().width() // 40 > 30:
            font = QtGui.QFont(
                "Helvetica Neue LT Black Ext", self.rect().width() // 40 - 8
            )
        else:
            font = QtGui.QFont("Helvetica Neue LT Black Ext", 30)
        self.quote_label.setFont(font)

    def resizeCredit(self, event):
        if self.rect().width() // 75 > 16:
            font = QtGui.QFont(
                "Helvetica Neue LT Light Cond", self.rect().width() // 75
            )
        else:
            font = QtGui.QFont("Helvetica Neue LT Light Cond", 16)
        self.credit_label.setFont(font)

    def goToBook(self, book_id, book_title):
        authen.mainApp.setWindowTitle("Booque - " + book_title)
        authen.mainApp.app_panel.setCurrentIndex(5)
        bookApp.setId(int(book_id))

    def updateCurBook(self, book_id):
        if book_id:
            self.cur_label.setText("You are currently reading")
            self.cur_btn.setIcon(
                QtGui.QIcon(
                    [i[2] for i in db.database.books_ll if int(i[0]) == int(book_id)][0]
                )
            )
            self.cur_btn.clicked.connect(
                lambda: self.goToBook(
                    int(book_id),
                    [i[1] for i in db.database.books_ll if int(i[0]) == int(book_id)][
                        0
                    ],
                )
            )
        else:
            self.cur_label.setText("Recommended for you")
            self.recommended_book = db.database.books_ll.recommended()
            self.cur_btn.setIcon(QtGui.QIcon(self.recommended_book[2]))
            self.cur_btn.clicked.connect(
                lambda: self.goToBook(
                    self.recommended_book[0], self.recommended_book[1]
                )
            )
        self.cur_btn.setIconSize(self.cur_btn.size())


class Library(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        global libApp
        libApp = self
        self.setupUi()
        self.setStyleSheet(libStyle.default)
        self.book_ids = []
        self.book_titles = []
        self.book_authors = []
        self.book_rating = []
        self.book_imgs = []
        self.column = 4
        self.sort = 0
        self.no_match.hide()
        self.search_btn.clicked.connect(self.search)
        self.sort_box.activated.connect(lambda x: self.setSort(x))
        self.genre_box.activated.connect(lambda x: self.setGenre(x))
        QtWidgets.QScroller.grabGesture(
            self.scrollArea, QtWidgets.QScroller.LeftMouseButtonGesture
        )
        self.reset()

    def setupUi(self):
        self.setObjectName("Library")
        self.resize(1200, 640)
        self.setMinimumSize(QtCore.QSize(1200, 640))
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(50, 0, 50, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContents = QtWidgets.QWidget()
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 1100, 520))
        self.scrollAreaContents.setObjectName("scrollAreaContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.book_shelf = QtWidgets.QGridLayout()
        self.book_shelf.setContentsMargins(-1, 20, -1, 50)
        self.book_shelf.setHorizontalSpacing(30)
        self.book_shelf.setVerticalSpacing(60)
        self.book_shelf.setObjectName("book_shelf")
        self.gridLayout_2.addLayout(self.book_shelf, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_2.addItem(spacerItem, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.no_match = QtWidgets.QLabel(self.scrollAreaContents)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT UltLight Ext")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.no_match.setFont(font)
        self.no_match.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.no_match.setObjectName("no_match")
        self.gridLayout_2.addWidget(self.no_match, 0, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.lib_label = QtWidgets.QLabel(self)
        self.lib_label.setMinimumSize(QtCore.QSize(420, 120))
        self.lib_label.setMaximumSize(QtCore.QSize(420, 120))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lib_label.setFont(font)
        self.lib_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.lib_label.setObjectName("lib_label")
        self.gridLayout.addWidget(self.lib_label, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.genre_box = QtWidgets.QComboBox(self)
        self.genre_box.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.genre_box.setFont(font)
        self.genre_box.setObjectName("genre_box")
        self.genre_box.addItem("")
        self.genre_box.addItem("")
        self.genre_box.addItem("")
        self.genre_box.addItem("")
        self.genre_box.addItem("")
        self.genre_box.addItem("")
        self.genre_box.addItem("")
        self.genre_box.addItem("")
        self.genre_box.addItem("")
        self.horizontalLayout_2.addWidget(self.genre_box)
        self.sort_box = QtWidgets.QComboBox(self)
        self.sort_box.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        self.sort_box.setFont(font)
        self.sort_box.setFrame(False)
        self.sort_box.setObjectName("sort_box")
        self.sort_box.addItem("")
        self.sort_box.addItem("")
        self.sort_box.addItem("")
        self.sort_box.addItem("")
        self.horizontalLayout_2.addWidget(self.sort_box)
        self.search_bar = QtWidgets.QLineEdit(self)
        self.search_bar.setMinimumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.search_bar.setFont(font)
        self.search_bar.setText("")
        self.search_bar.setFrame(False)
        self.search_bar.setClearButtonEnabled(True)
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout_2.addWidget(self.search_bar)
        self.search_btn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMinimumSize(QtCore.QSize(28, 28))
        self.search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("rsrc/img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.On
        )
        self.search_btn.setIcon(icon)
        self.search_btn.setIconSize(QtCore.QSize(28, 28))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_2.addWidget(self.search_btn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.genre_box, self.sort_box)
        self.setTabOrder(self.sort_box, self.search_bar)
        self.setTabOrder(self.search_bar, self.search_btn)
        self.setTabOrder(self.search_btn, self.scrollArea)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.no_match.setText(_translate("Library", "< No result matched >"))
        self.lib_label.setText(_translate("Library", "Library"))
        self.genre_box.setItemText(0, _translate("Library", "All"))
        self.genre_box.setItemText(1, _translate("Library", "Fiction"))
        self.genre_box.setItemText(2, _translate("Library", "Thriller"))
        self.genre_box.setItemText(3, _translate("Library", "Fantasy"))
        self.genre_box.setItemText(4, _translate("Library", "Romance"))
        self.genre_box.setItemText(5, _translate("Library", "Biography"))
        self.genre_box.setItemText(6, _translate("Library", "Comedy"))
        self.genre_box.setItemText(7, _translate("Library", "Horror"))
        self.genre_box.setItemText(8, _translate("Library", "Poetry"))
        self.sort_box.setItemText(0, _translate("Library", "a-z"))
        self.sort_box.setItemText(1, _translate("Library", "z-a"))
        self.sort_box.setItemText(2, _translate("Library", "Rating (most)"))
        self.sort_box.setItemText(3, _translate("Library", "Rating (least)"))
        self.search_bar.setPlaceholderText(_translate("Library", "Search"))

    def goToBook(self, book_id, book_title):
        authen.mainApp.setWindowTitle("Booque - " + book_title)
        authen.mainApp.app_panel.setCurrentIndex(5)
        bookApp.setId(int(book_id))

    def reset(self):
        self.cur_ll = db.database.books_ll
        self.updateCatalog(self.cur_ll.sort(self.sort))

    def clearLayout(self, layout):
        self.book_ids = []
        self.book_titles = []
        self.book_imgs = []
        self.book_authors = []
        self.book_ratings = []
        self.pos = []
        self.button = []
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clearLayout(child.layout())

    def updateCatalog(self, ll, type=None):
        self.scrollArea.verticalScrollBar().setValue(0)
        self.clearLayout(self.book_shelf)
        if not type:
            self.cur_ll = ll
        if ll:
            self.no_match.hide()
            for i in ll:
                self.book_ids.append(i[0])
                self.book_titles.append(i[1])
                self.book_imgs.append(i[2])
                self.book_authors.append(i[3])
                self.book_ratings.append(float(i[7]))
            self.pos = [
                [r, c]
                for r in range(int(len(ll) / self.column) + 1)
                for c in range(self.column)
            ]
            self.button = [
                [[] for c in range(self.column)]
                for r in range(int(len(ll) / self.column) + 1)
            ]
            for pos, id, title, img, author, rating in zip(
                self.pos,
                self.book_ids,
                self.book_titles,
                self.book_imgs,
                self.book_authors,
                self.book_ratings,
            ):
                title_label = QtWidgets.QLabel(self.scrollAreaContents)
                title_label.setText(title)
                title_label.setFont(QtGui.QFont("Product Sans", 12))
                title_label.setWordWrap(True)
                title_label.setAlignment(QtCore.Qt.AlignCenter)
                title_label.setMinimumWidth(250)
                title_label.setMaximumHeight(200)
                author_label = QtWidgets.QLabel(self.scrollAreaContents)
                author_label.setText(author)
                author_label.setFont(QtGui.QFont("Product Sans", 11))
                author_label.setWordWrap(True)
                author_label.setAlignment(QtCore.Qt.AlignCenter)
                author_label.setMinimumWidth(250)
                author_label.setMaximumHeight(30)
                rating_label = QtWidgets.QLabel(self.scrollAreaContents)
                rating_label.setText("⭐ {0:.2f}".format(rating))
                rating_label.setFont(QtGui.QFont("Product Sans", 10))
                rating_label.setWordWrap(True)
                rating_label.setAlignment(QtCore.Qt.AlignCenter)
                rating_label.setMinimumWidth(250)
                rating_label.setMaximumHeight(30)
                button = QtWidgets.QPushButton(self.scrollAreaContents)
                button.setIcon(QtGui.QIcon(img))
                button.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                )
                button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                button.setMinimumSize(250, 380)
                button.setIconSize(button.minimumSize())
                button.clicked.connect(
                    lambda x, id=id, title=title: self.goToBook(id, title)
                )
                book_container = QtWidgets.QVBoxLayout()
                book_container.setSpacing(5)
                book_container.addWidget(button, 0, alignment=QtCore.Qt.AlignCenter)
                book_container.addWidget(title_label, 1)
                book_container.addWidget(author_label, 2)
                book_container.addWidget(rating_label, 3)
                self.book_shelf.addLayout(book_container, *pos)
        else:
            self.no_match.show()

    def search(self):
        if self.search_bar.text():
            temp = self.cur_ll.search(self.search_bar.text())
            self.updateCatalog(temp, 1)
        else:
            self.updateCatalog(self.cur_ll)
        self.search_bar.setText("")

    def setSort(self, index):
        self.search_bar.setText("")
        self.sort = index
        self.updateCatalog(self.cur_ll.sort(self.sort))

    def setGenre(self, index):
        self.search_bar.setText("")
        if index == 0:
            self.updateCatalog(db.database.books_ll.sort(self.sort))
        elif index == 1:
            self.updateCatalog(db.database.fictions_ll.sort(self.sort))
        elif index == 2:
            self.updateCatalog(db.database.thrillers_ll.sort(self.sort))
        elif index == 3:
            self.updateCatalog(db.database.fantasies_ll.sort(self.sort))
        elif index == 4:
            self.updateCatalog(db.database.romances_ll.sort(self.sort))
        elif index == 5:
            self.updateCatalog(db.database.biographies_ll.sort(self.sort))
        elif index == 6:
            self.updateCatalog(db.database.comedies_ll.sort(self.sort))
        elif index == 7:
            self.updateCatalog(db.database.horrors_ll.sort(self.sort))
        elif index == 8:
            self.updateCatalog(db.database.poetries_ll.sort(self.sort))


class Request(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        global reqApp
        reqApp = self
        self.setupUi()
        self.setStyleSheet(reqStyle.default)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon("rsrc/img/logo.png"))
        self.submit_btn.clicked.connect(self.submitReq)

    def setupUi(self):
        self.setObjectName("Request")
        self.resize(1200, 690)
        self.setMinimumSize(QtCore.QSize(1200, 690))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(50, 0, 50, 50)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.submit_btn = QtWidgets.QPushButton(self)
        self.submit_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.submit_btn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.submit_btn.setFont(font)
        self.submit_btn.setFlat(False)
        self.submit_btn.setObjectName("submit_btn")
        self.gridLayout.addWidget(self.submit_btn, 11, 0, 1, 1)
        self.req_label = QtWidgets.QLabel(self)
        self.req_label.setMinimumSize(QtCore.QSize(1000, 150))
        self.req_label.setMaximumSize(QtCore.QSize(1000, 150))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.req_label.setFont(font)
        self.req_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.req_label.setObjectName("req_label")
        self.gridLayout.addWidget(self.req_label, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.req_title = QtWidgets.QLineEdit(self)
        self.req_title.setMinimumSize(QtCore.QSize(900, 50))
        self.req_title.setMaximumSize(QtCore.QSize(16777215, 1000))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Medium Ext")
        font.setPointSize(14)
        self.req_title.setFont(font)
        self.req_title.setInputMask("")
        self.req_title.setFrame(False)
        self.req_title.setClearButtonEnabled(True)
        self.req_title.setObjectName("req_title")
        self.gridLayout.addWidget(self.req_title, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem2, 10, 0, 1, 1)
        self.req_author = QtWidgets.QLineEdit(self)
        self.req_author.setMinimumSize(QtCore.QSize(900, 50))
        self.req_author.setMaximumSize(QtCore.QSize(16777215, 1000))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Medium Ext")
        font.setPointSize(14)
        self.req_author.setFont(font)
        self.req_author.setFrame(False)
        self.req_author.setClearButtonEnabled(True)
        self.req_author.setObjectName("req_author")
        self.gridLayout.addWidget(self.req_author, 8, 0, 1, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.req_title, self.req_author)
        self.setTabOrder(self.req_author, self.submit_btn)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.submit_btn.setText(_translate("Request", "Submit"))
        self.req_label.setText(_translate("Request", "Request"))
        self.req_title.setPlaceholderText(_translate("Request", "Book title"))
        self.req_author.setPlaceholderText(_translate("Request", "Author"))

    def submitReq(self):
        if not db.database.books_ll.existed(self.req_title.text(), self.req_author.text()):
            if self.req_title.text() and self.req_author.text():
                self.req_info = db.RequestNode(
                    self.req_title.text(), self.req_author.text()
                )
                db.database.req_q.enqueue(self.req_info)
                print(db.database.req_q)
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


class Setting(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setStyleSheet(settingStyle.default)
        self.dark_mode.setChecked(app.dark)
        self.dark_mode.clicked.connect(lambda x: self.setDarkMode(x))

    def setupUi(self):
        self.setObjectName("Request")
        self.resize(1200, 690)
        self.setMinimumSize(QtCore.QSize(1200, 690))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(50, 0, 50, 50)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.req_label = QtWidgets.QLabel(self)
        self.req_label.setMinimumSize(QtCore.QSize(1200, 150))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Black Ext")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.req_label.setFont(font)
        self.req_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.req_label.setObjectName("req_label")
        self.gridLayout.addWidget(self.req_label, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dark_mode = QtWidgets.QPushButton(self)
        self.dark_mode.setMinimumSize(QtCore.QSize(80, 30))
        self.dark_mode.setMaximumSize(QtCore.QSize(80, 30))
        self.dark_mode.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("rsrc/img/off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        icon.addPixmap(
            QtGui.QPixmap("rsrc/img/on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On
        )
        self.dark_mode.setIcon(icon)
        self.dark_mode.setIconSize(QtCore.QSize(80, 30))
        self.dark_mode.setCheckable(True)
        self.dark_mode.setObjectName("dark_mode")
        self.horizontalLayout_2.addWidget(self.dark_mode)
        self.dark_mode_label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue LT Medium Ext")
        font.setPointSize(14)
        self.dark_mode_label.setFont(font)
        self.dark_mode_label.setObjectName("dark_mode_label")
        self.horizontalLayout_2.addWidget(self.dark_mode_label)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.req_label.setText(_translate("Request", "Setting"))
        self.dark_mode_label.setText(_translate("Request", "Dark mode"))

    def setDarkMode(self, i):
        app.dark = i
        if app.dark:
            authen.mainApp.home_btn.setIcon(QtGui.QIcon("rsrc/img/logo_full_dark.png"))
            authen.mainApp.prof_btn.setIcon(QtGui.QIcon("rsrc/img/frame_dark.png"))
            authen.mainApp.setStyleSheet(appStyle.dark_mode)
            bookApp.user_frame.setPixmap(QtGui.QPixmap("rsrc/img/frame_dark.png"))
            bookApp.setStyleSheet(bookStyle.dark_mode)
            bookApp.frame = "rsrc/img/frame_dark.png"
            chartApp.setStyleSheet(chartStyle.dark_mode)
            editApp.img_frame.setPixmap(QtGui.QPixmap("rsrc/img/frame_dark_big.png"))
            editApp.setStyleSheet(editStyle.dark_mode)
            homeApp.setStyleSheet(homeStyle.dark_mode)
            libApp.setStyleSheet(libStyle.dark_mode)
            reqApp.setStyleSheet(reqStyle.dark_mode)
            self.setStyleSheet(settingStyle.dark_mode)
        else:
            authen.mainApp.home_btn.setIcon(QtGui.QIcon("rsrc/img/logo_full.png"))
            authen.mainApp.prof_btn.setIcon(QtGui.QIcon("rsrc/img/frame.png"))
            authen.mainApp.setStyleSheet(appStyle.default)
            bookApp.user_frame.setPixmap(QtGui.QPixmap("rsrc/img/frame.png"))
            bookApp.setStyleSheet(bookStyle.default)
            bookApp.frame = "rsrc/img/frame.png"
            chartApp.setStyleSheet(chartStyle.default)
            editApp.img_frame.setPixmap(QtGui.QPixmap("rsrc/img/frame_big.png"))
            editApp.setStyleSheet(editStyle.default)
            homeApp.setStyleSheet(homeStyle.default)
            libApp.setStyleSheet(libStyle.default)
            reqApp.setStyleSheet(reqStyle.default)
            self.setStyleSheet(settingStyle.default)
