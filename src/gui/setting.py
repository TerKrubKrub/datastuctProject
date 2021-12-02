import sys, os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import rsrc.rsrc
import rsrc.style.setting as style


class Setting(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/setting.ui", self)