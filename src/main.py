import sys, sqlite3
from PyQt5 import QtWidgets
from gui.authen import *
from gui.app import App


def run():
    app = QtWidgets.QApplication(sys.argv)
    db = sqlite3.connect("rsrc/db/data.db")
    curs = db.cursor()
    curs.execute("SELECT id, rmb FROM current_user")
    try:
        cur_user = curs.fetchone()
        if cur_user[1]:
            gui = App(cur_user[0])
        else:
            gui = LogIn()
    except:
        cur_user = None
        gui = LogIn()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
