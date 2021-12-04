import sys, os, sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtCore import Qt

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import authen,library
import rsrc.rsrc
import rsrc.style.app as style


class App(QtWidgets.QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        global id
        id = self.user_id
        global dark
        dark = False
        uic.loadUi("rsrc/ui/app.ui", self)
        self.setWindowTitle("Booque - Home")
        self.setStyleSheet(style.default)
        self.app_panel.setCurrentIndex(0)
        self.db = sqlite3.connect("rsrc/db/data.db")
        self.curs = self.db.cursor()
        self.curs.execute('SELECT user_img FROM users WHERE user_id="' + str(id) + '"')
        self.home_btn.clicked.connect(self.goToHome)
        self.prof_img = self.curs.fetchone()[0]
        self.prof.setPixmap(QtGui.QPixmap(self.prof_img))
        self.prof.setScaledContents(True)
        self.prof_btn.setIcon(QtGui.QIcon(":/Image/img/frame.png"))
        self.menu = QtWidgets.QMenu("menu_list", self)
        self.menu.setFont(QtGui.QFont("Product Sans", 10))
        self.menu.triggered.connect(lambda x: self.handleMenu(x.text()))
        self.menu.addAction("Library").setIcon(QtGui.QIcon("rsrc/img/library.ico"))
        self.menu.addAction("Chart").setIcon(QtGui.QIcon("rsrc/img/trophy.png"))
        self.menu.addAction("Request").setIcon(QtGui.QIcon("rsrc/img/request.png"))
        self.menu.addAction("Profile").setIcon(QtGui.QIcon("rsrc/img/prof.png"))
        self.menu.addAction("Setting").setIcon(QtGui.QIcon("rsrc/img/gear.png"))
        self.menu.addAction("Log out").setIcon(QtGui.QIcon("rsrc/img/logout.png"))
        self.menu.setProperty("hide", True)
        self.prof_btn.setMenu(self.menu)

    def goToHome(self):
        self.setWindowTitle("Booque - Home")
        self.app_panel.setCurrentIndex(0)

    def handleMenu(self, action):
        if action == "Profile":
            self.setWindowTitle("Booque - Profile")
            self.app_panel.setCurrentIndex(1)
        elif action == "Library":
            self.setWindowTitle("Booque - Library")
            self.app_panel.setCurrentIndex(3)
        elif action == "Request":
            self.setWindowTitle("Booque - Request")
            self.app_panel.setCurrentIndex(4)
        elif action == "Setting":
            self.setWindowTitle("Booque - Setting")
            self.app_panel.setCurrentIndex(5)
        if action == "Chart":
            self.setWindowTitle("Booque - Charts")
            self.app_panel.setCurrentIndex(7)
        elif action == "Log out":
            self.curs.execute("DELETE FROM current_user")
            self.db.commit()
            self.db.close()

            self.log_in = authen.LogIn()
            self.log_in.show()
            self.close()
