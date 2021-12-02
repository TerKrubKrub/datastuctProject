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
        print("user id:", app.id)
        self.db = sqlite3.connect("rsrc/db/data.db")
        self.curs = self.db.cursor()
        self.curs.execute(
            'SELECT f_name FROM users WHERE user_id="' + str(app.id) + '"'
        )
        self.f_name = self.curs.fetchone()[0]
        self.welcome_label.setText(
            "Welcome " + self.f_name + "\nto BOOQUE,\nthe best book review app!"
        )
        self.quote_label.setText(
            "“With great degree,\ncomes (a lot of)\ngreat projects”\n- a suffering student"
        )
        self.chart_btn.clicked.connect(self.goToChart)

    def goToChart(self):
        authen.mainApp.setWindowTitle("Booque - Charts")
        authen.mainApp.app_panel.setCurrentIndex(7)
