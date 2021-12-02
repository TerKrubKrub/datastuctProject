import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle("test Lib")
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("1234")
        self.label.move(50, 50)

        self.btn0 = QtWidgets.QPushButton(self)
        self.btn0.setText("Click")
        self.btn0.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You Clicked 12344575678679")
        self.update()

    def update(self):
        self.label.adjustSize()

def main():
    app = QApplication(sys.argv)
    ex = window()
    print("Hello")
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()