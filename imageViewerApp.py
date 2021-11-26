from PyQt5.QtCore import QFileDevice
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #Load the ui file
        uic.loadUi("image.ui", self)

        #Define widgets
        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")

        self.button.clicked.connect(self.clicker)

        self.show()

    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "c:\\images", "All Files (*);;PNG Files (*.png);;Jpeg Files (*.jpg)")

        #Open the images
        self.pixmap = QPixmap(fname[0])

        #Add Pic to label
        self.label.setPixmap(self.pixmap)

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()