import sys, sqlite3
from PyQt5 import QtWidgets
from gui.authen import *
from gui.app import App


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = LogIn()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
