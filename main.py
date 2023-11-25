import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffeeInfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_coffee_info()

    def load_coffee_info(self):
        conn = sqlite3.connect('coffee.sqlite')
        cur = conn.cursor()

        cur.execute("SELECT * FROM coffe")
        coffee_data = cur.fetchall()

        self.tableWidget.setRowCount(len(coffee_data))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Название сорта", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки"]
        )

        for row, coffee in enumerate(coffee_data):
            for col, value in enumerate(coffee):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

        conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeInfoWindow()
    window.show()
    sys.exit(app.exec_())
