import sys, os
from PyQt5 import QtWidgets, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, authen, book, chart, edit, home, library, request
import rsrc.rsrc
from rsrc.style import (
    setting as settingStyle,
    app as appStyle,
    book as bookStyle,
    chart as chartStyle,
    edit as editStyle,
    home as homeStyle,
    library as libStyle,
    request as reqStyle,
)


class Setting(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/setting.ui", self)
        self.setStyleSheet(settingStyle.default)
        self.dark_mode.setChecked(app.dark)
        self.dark_mode.clicked.connect(lambda x: self.setDarkMode(x))

    def setDarkMode(self, i):
        app.dark = i
        if app.dark:
            authen.mainApp.home_btn.setIcon(
                QtGui.QIcon("rsrc/img/logo_full_dark.png")
            )
            authen.mainApp.prof_btn.setIcon(QtGui.QIcon("rsrc/img/frame_dark.png"))
            authen.mainApp.setStyleSheet(appStyle.dark_mode)
            chart.chartApp.setStyleSheet(chartStyle.dark_mode)
            edit.editApp.img_frame.setPixmap(
                QtGui.QPixmap("rsrc/img/frame_dark_big.png")
            )
            edit.editApp.setStyleSheet(editStyle.dark_mode)
            home.homeApp.setStyleSheet(homeStyle.dark_mode)
            library.libApp.setStyleSheet(libStyle.dark_mode)
            request.reqApp.setStyleSheet(reqStyle.dark_mode)
            self.setStyleSheet(settingStyle.dark_mode)
        else:
            authen.mainApp.home_btn.setIcon(QtGui.QIcon("rsrc/img/logo_full.png"))
            authen.mainApp.prof_btn.setIcon(QtGui.QIcon("rsrc/img/frame.png"))
            authen.mainApp.setStyleSheet(appStyle.default)
            chart.chartApp.setStyleSheet(chartStyle.default)
            edit.editApp.img_frame.setPixmap(QtGui.QPixmap("rsrc/img/frame_big.png"))
            edit.editApp.setStyleSheet(editStyle.default)
            home.homeApp.setStyleSheet(homeStyle.default)
            library.libApp.setStyleSheet(libStyle.default)
            request.reqApp.setStyleSheet(reqStyle.default)
            self.setStyleSheet(settingStyle.default)
