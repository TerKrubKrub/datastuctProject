import sys, os
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui.authen import LogIn
import rsrc.rsrc
import rsrc.style.profile as style


class Profile(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/profile.ui", self)