from gui.authen import *


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = LogIn()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
