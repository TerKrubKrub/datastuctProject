import sys
from PyQt5 import QtWidgets
from gui import db, authen


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = authen.LogIn()
    db.database.initFont()
    gui.show()
    app.aboutToQuit.connect(db.database.exit)
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
