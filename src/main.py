from authen import *


def run():
    app = QApplication(sys.argv)
    ui = LogIn()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
