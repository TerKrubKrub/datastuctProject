import sys, os, sqlite3
from PyQt5 import QtWidgets, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, authen
import rsrc.rsrc
import rsrc.style.home as style


class Home(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/home.ui", self)
        print("Home!\nuser id:", app.id)
        self.chart_btn.clicked.connect(self.goToChart)

    def goToChart(self):
        authen.mainApp.setWindowTitle("Booque - charts")
        authen.mainApp.app_panel.setCurrentIndex(7)
