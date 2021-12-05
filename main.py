import sys, sqlite3
from PyQt5 import QtWidgets, QtGui
from gui.authen import *
from gui.app import App


def init_font():
    fontDB = QtGui.QFontDatabase()
    fontDB.addApplicationFont(":/Font/font/Better Grade/Better Grade.ttf")
    fontDB.addApplicationFont(":/Font/font/Product Sans/Product Sans Regular.ttf")
    fontDB.addApplicationFont(
        ":/Font/font/Helvetica Neue/Helvetica Neue LT 93 Black Extended Oblique.ttf"
    )
    fontDB.addApplicationFont(
        ":/Font/font/Helvetica Neue/Helvetica Neue LT 87 Heavy Condensed Oblique.ttf"
    )
    fontDB.addApplicationFont(
        ":/Font/font/Helvetica Neue/Helvetica Neue LT 63 Medium Extended Oblique.ttf"
    )
    fontDB.addApplicationFont(
        ":/Font/font/Helvetica Neue/Helvetica Neue LT 63 Medium Extended.ttf"
    )
    fontDB.addApplicationFont(
        ":/Font/font/Helvetica Neue/Helvetica Neue LT 53 Extended.ttf"
    )
    fontDB.addApplicationFont(
        ":/Font/font/Helvetica Neue/Helvetica Neue LT 55 Roman.ttf"
    )
    fontDB.addApplicationFont(
        ":/Font/font/Helvetica Neue/Helvetica Neue LT 47 Light Condensed.ttf"
    )


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = LogIn()
    init_font()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
