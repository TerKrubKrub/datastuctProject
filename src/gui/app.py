import sys, os, sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import rsrc.rsrc
import rsrc.style.app as style
import gui.authen as authen


class App(QtWidgets.QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        global id
        id = self.user_id
        uic.loadUi("rsrc/ui/app.ui", self)
        self.app_panel.setCurrentIndex(0)
        self.db = sqlite3.connect("rsrc/db/data.db")
        self.curs = self.db.cursor()
        self.curs.execute('SELECT user_img FROM users WHERE user_id="' + str(id) + '"')
        self.home_btn.clicked.connect(lambda: self.app_panel.setCurrentIndex(0))
        self.prof_img = self.curs.fetchone()[0]
        self.prof.setPixmap(QtGui.QPixmap(self.prof_img))
        self.prof.setScaledContents(True)
        self.prof_btn.setIcon(QtGui.QIcon(":/Image/img/frame.png"))
        self.prof_btn.clicked.connect(lambda: self.app_panel.setCurrentIndex(1))
        self.menu = QtWidgets.QMenu("menu_list", self)
        self.menu.triggered.connect(lambda x: self.menuHandler(x.text()))
        self.menu.addAction("Library").setIcon(QtGui.QIcon("rsrc/img/library.ico"))
        self.menu.addAction("Chart").setIcon(QtGui.QIcon("rsrc/img/trophy.png"))
        self.menu.addAction("Request").setIcon(QtGui.QIcon("rsrc/img/request.png"))
        self.menu.addAction("Setting").setIcon(QtGui.QIcon("rsrc/img/gear.png"))
        self.menu.addAction("Log out").setIcon(QtGui.QIcon("rsrc/img/logout.png"))
        self.menu.setProperty("hide", True)
        self.menu_btn.setMenu(self.menu)

    def menuHandler(self, action):
        if action == "Library":
            self.app_panel.setCurrentIndex(5)
        elif action == "Chart":
            self.app_panel.setCurrentIndex(7)
        elif action == "Request":
            self.app_panel.setCurrentIndex(4)
        elif action == "Setting":
            self.app_panel.setCurrentIndex(3)
        elif action == "Log out":
            self.curs.execute("DELETE FROM current_user")
            self.db.commit()
            self.db.close()

            self.log_in = authen.LogIn()
            self.log_in.show()
            self.close()
