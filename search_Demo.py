import sys
from PyQt5.QtWidgets import QApplication, QHeaderView, QVBoxLayout, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import uic

class SearchDemo(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("search.ui", self)

        self.setWindowTitle("Search")

        companies = ('Apple', 'Facebook', 'Google', 'Amazon', 'Walmart', 'Dropbox', 'Starbucks', 'eBay', 'Canon')
        model = QStandardItemModel(len(companies), 1)
        model.setHorizontalHeaderLabels(['Company'])

        for row, company in enumerate(companies):
            item = QStandardItem(company)
            model.setItem(row, 0, item)
        
        self.button = self.findChild(QPushButton,"pushButton")
        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
        self.button.clicked.connect(self.clickerForSearch)

        self.show()

    def clickerForSearch(self):
        pass


app = QApplication(sys.argv)
Searchdemo = SearchDemo()
Searchdemo.show()
sys.exit(app.exec_())