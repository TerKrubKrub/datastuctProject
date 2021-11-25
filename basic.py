from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300) # xpos, ypos, width, height
        self.setWindowTitle("Book Review")
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self) # ใส่ win เพื่อให้ label อยู่ใน win
        self.label.setText("my first label")
        self.label.move(50, 50) # set label's position

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed button")
        self.update()

    def update(self): # call ทุกครั้งที่มีการเเก้ไขอะไรก็ตามใน window
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()