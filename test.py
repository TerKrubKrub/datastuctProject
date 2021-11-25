import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class window(QWidget):
    def __init__(self):
        super(window, self).__init__()
        self.resize(200, 50)
        self.setWindowTitle("test Lib")
        self.label = QLabel(self)
        self.label.setText("1234")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50, 20)

def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()