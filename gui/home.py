import sys, os, sqlite3
from PyQt5 import QtWidgets, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app
import rsrc.rsrc
import rsrc.style.home as style


class Home(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/home.ui", self)
        global homeApp
        homeApp = self
        self.setStyleSheet(style.default)
        self.db = sqlite3.connect("rsrc/db/data.db")
        self.curs = self.db.cursor()
        self.curs.execute(
            'SELECT f_name FROM users WHERE user_id="' + str(app.id) + '"'
        )
        self.f_name = self.curs.fetchone()[0]
        self.welcome_label.setText(
            "Welcome, " + self.f_name + "!\nto BOOQUE, your favorite book app."
        )
        self.quote_label.setText(
            '" The world breaks everyone, and afterward, many are strong at the broken places. "'
        )
        self.credit_label.setText("- Ernest Hemingway, A Farewell to Arms")
