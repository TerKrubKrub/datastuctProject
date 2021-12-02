import sys, os, sqlite3
from PyQt5 import QtWidgets, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, authen
import rsrc.rsrc
import rsrc.style.chart as style


class Chart(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/chart.ui", self)
