import sys, os
from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import db, authen


def run():
    app = QApplication(sys.argv)
    db.database.updateRsrc(1)
    gui = authen.LogIn()
    gui.show()
    app.aboutToQuit.connect(db.database.exit)
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
