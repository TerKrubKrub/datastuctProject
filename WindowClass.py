from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window")
        #self.setWindowIcon(QIcon(".png"))
        self.setGeometry(500, 300, 1000, 800)

        stylesheet = (
            'background-color:white'
        )
        self.setStyleSheet(stylesheet)

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())