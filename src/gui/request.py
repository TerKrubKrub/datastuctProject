import sys, os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import rsrc.rsrc
import rsrc.style.request as style


class Request(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/request.ui", self)