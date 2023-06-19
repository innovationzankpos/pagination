import math

import PyQt5
import pyodbc
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QColor
from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHeaderView, QStyledItemDelegate, \
    QAbstractItemView
from pagination_ui import Ui_MainWindow


# Establish a connection
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server={localhost\sqlexpress2014};"
    "Database={POWERPOS};"
)

cursor = conn.cursor()

cursor.execute("SELECT itemcode as ITEMCODE, itemname as ITEMNAME, department as DEPARTMENT, uom as UOM, unitprice as PRICE, sellingprice as WHOLESALE, end_qty as BAL FROM items")

result = cursor.fetchall()

current_page = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.searchBtn.clicked.connect(self.search)
        self.searchBtn.setStyleSheet("""
            QPushButton{
                background-color: #880808;
                color: white;
            }
            QPushButton::hover{
                background-color: #D22B2B;
            }
        """)
        # self.searchTxt.clicked.connect(self.search)
        self.searchTxt.setStyleSheet("border: 1px solid black; font-size: 18px; padding: 5px")
        self.itemBtn.clicked.connect(self.item)
        self.itemBtn.setStyleSheet("""
            QPushButton{
                background-color : black;
                color: white;
            }
            QPushButton::hover{
                background-color: #2E2E2E;
            }
        """)
        self.brandBtn.clicked.connect(self.brand)
        self.brandBtn.setStyleSheet("""
            QPushButton{
                background-color: black;
                color: white;
            }
            QPushButton::hover{
                background-color: #2E2E2E;
            }
        """)
        self.prevBtn.clicked.connect(self.prev)
        self.prevBtn.setStyleSheet("""
            QPushButton{
                background-color: #5D8AA8;
                color: darkgray;
            }
            QPushButton::hover{
                background-color: #4169E1;
            }
        """)
        self.prevBtn.setDisabled(True)
        self.nextBtn.clicked.connect(self.next)
        self.nextBtn.setStyleSheet("""
            QPushButton{
                background-color: blue;
                color: white;
            }
            QPushButton::hover{
                background-color: #4169E1;
            }
        """)
        self.enterBtn.clicked.connect(self.enter)
        self.enterBtn.setStyleSheet("""
            QPushButton{
                background-color: green;
                color: white;
            }
            QPushButton::hover{
                background-color: #00A36C;
            }
        """)
        self.closeBtn.clicked.connect(self.closeUI)
        self.closeBtn.setStyleSheet("""
            QPushButton{
                background-color: #880808;
                color: white;
            }
            QPushButton::hover{
                background-color: #D22B2B;
            }
        """)

        self.model = QStandardItemModel()
        # # self.model.setHorizontalHeaderLabels(
        # #     ["ITEMCODE", "ITEMNAME", "DEPARTMENT", "UOM", "PRICE", "WHOLESALE", "BAL"])  # Set the column headers
        #
        # Create a QTableView and set its model
        self.tableView.setModel(self.model)

        # Hide the vertical header
        self.tableView.verticalHeader().setVisible(False)

        # Set the selection mode to select rows
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Set the table view as non-editable
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Hide the vertical scroll bar
        # self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # # Hide the horizontal scroll bar
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Populate the table with data
        self.populate_tableview(current_page)

        # Set fixed size for rows and columns
        for row in range(self.model.rowCount()):
            self.tableView.setRowHeight(row, 50)  # Set row height to 50 pixels
            self.tableView.setStyleSheet("font-size: 15px; text-align: center")

        # Set fixed size for specific headers
        header = self.tableView.horizontalHeader()
        header.resizeSection(0, 30)  # Set width of header for column 0 to 100 pixels
        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setHighlightSections(False)
        header.setStyleSheet(
            'QHeaderView::section { background-color: orange; font-weight: bold; text-align: center; }')

        self.tableView.setColumnWidth(0, 130)  # Set width of column 0 to 100 pixels
        self.tableView.setColumnWidth(1, 200)  # Set width of column 2 to 150 pixels
        self.tableView.setColumnWidth(2, 130)  # Set width of column 0 to 100 pixels
        self.tableView.setColumnWidth(3, 50)  # Set width of column 2 to 150 pixels
        self.tableView.setColumnWidth(4, 100)  # Set width of column 0 to 100 pixels
        self.tableView.setColumnWidth(5, 100)  # Set width of column 2 to 150 pixels
        self.tableView.setColumnWidth(6, 100)  # Set width of column 2 to 150 pixels

    def search(self):
        print("Searched!")

    def item(self):
        print("Item!")

    def brand(self):
        print("Brand!")

    def enter(self):
        print("Entered!")

    def closeUI(self):
        print("Closed!")
        self.close()

    def prev(self):
        print("Previous!")
        self.model.clear()
        global current_page

        if current_page > 0 and current_page != 1:
            self.prevBtn.setDisabled(False)
            self.prevBtn.setStyleSheet("background-color: blue; color: white;")
            self.nextBtn.setDisabled(False)
            self.nextBtn.setStyleSheet("background-color: blue; color: white;")
            current_page = current_page - 1
            self.populate_tableview(current_page);

            # Set fixed size for rows and columns
            for row in range(self.model.rowCount()):
                self.tableView.setRowHeight(row, 50)  # Set row height to 50 pixels
                self.tableView.setStyleSheet("font-size: 15px; text-align: center")

            # Set fixed size for specific headers
            header = self.tableView.horizontalHeader()
            header.resizeSection(0, 30)  # Set width of header for column 0 to 100 pixels
            header.setSectionResizeMode(QHeaderView.Fixed)
            header.setHighlightSections(False)
            header.setStyleSheet(
                'QHeaderView::section { background-color: orange; font-weight: bold; text-align: center; }')

            self.tableView.setColumnWidth(0, 130)  # Set width of column 0 to 100 pixels
            self.tableView.setColumnWidth(1, 200)  # Set width of column 2 to 150 pixels
            self.tableView.setColumnWidth(2, 130)  # Set width of column 0 to 100 pixels
            self.tableView.setColumnWidth(3, 50)  # Set width of column 2 to 150 pixels
            self.tableView.setColumnWidth(4, 100)  # Set width of column 0 to 100 pixels
            self.tableView.setColumnWidth(5, 100)  # Set width of column 2 to 150 pixels
            self.tableView.setColumnWidth(6, 100)  # Set width of column 2 to 150 pixels
        elif current_page == 1:
            self.prevBtn.setDisabled(True)
            self.prevBtn.setStyleSheet("background-color: #5D8AA8; color: darkgray;")
            self.nextBtn.setDisabled(False)
            self.nextBtn.setStyleSheet("background-color: blue; color: white;")
            current_page = current_page - 1
            self.populate_tableview(current_page);

            # Set fixed size for rows and columns
            for row in range(self.model.rowCount()):
                self.tableView.setRowHeight(row, 50)  # Set row height to 50 pixels
                self.tableView.setStyleSheet("font-size: 15px; text-align: center")

            # Set fixed size for specific headers
            header = self.tableView.horizontalHeader()
            header.resizeSection(0, 30)  # Set width of header for column 0 to 100 pixels
            header.setSectionResizeMode(QHeaderView.Fixed)
            header.setHighlightSections(False)
            header.setStyleSheet(
                'QHeaderView::section { background-color: orange; font-weight: bold; text-align: center; }')

            self.tableView.setColumnWidth(0, 130)  # Set width of column 0 to 100 pixels
            self.tableView.setColumnWidth(1, 200)  # Set width of column 2 to 150 pixels
            self.tableView.setColumnWidth(2, 130)  # Set width of column 0 to 100 pixels
            self.tableView.setColumnWidth(3, 50)  # Set width of column 2 to 150 pixels
            self.tableView.setColumnWidth(4, 100)  # Set width of column 0 to 100 pixels
            self.tableView.setColumnWidth(5, 100)  # Set width of column 2 to 150 pixels
            self.tableView.setColumnWidth(6, 100)  # Set width of column 2 to 150 pixels

    def next(self):
        print("Next!")
        self.model.clear()

        # cursor.execute("SELECT itemcode, itemname, department, uom, unitprice, sellingprice, end_qty FROM items")
        #
        # result = cursor.fetchall()

        rows_per_page = 300
        global current_page

        total_pages = math.ceil(len(result)/rows_per_page)

        if current_page < total_pages - 1:
            current_page = current_page + 1
            self.populate_tableview(current_page)

            # Set fixed size for rows and columns
            for row in range(self.model.rowCount()):
                self.tableView.setRowHeight(row, 50)  # Set row height to 50 pixels
                self.tableView.setStyleSheet("font-size: 15px; text-align: center")

            # Set fixed size for specific headers
            header = self.tableView.horizontalHeader()
            header.resizeSection(0, 30)  # Set width of header for column 0 to 100 pixels
            header.setSectionResizeMode(QHeaderView.Fixed)
            header.setHighlightSections(False)
            header.setStyleSheet(
                'QHeaderView::section { background-color: orange; font-weight: bold; text-align: center; }')

            self.tableView.setColumnWidth(0, 140)  # Set width of column 0 to 100 pixels
            self.tableView.setColumnWidth(1, 230)  # Set width of column 2 to 150 pixels
            self.tableView.setColumnWidth(2, 130)  # Set width of column 0 to 100 pixels
            self.tableView.setColumnWidth(3, 50)  # Set width of column 2 to 150 pixels
            self.tableView.setColumnWidth(4, 100)  # Set width of column 0 to 100 pixels
            self.tableView.setColumnWidth(5, 100)  # Set width of column 2 to 150 pixels
            self.tableView.setColumnWidth(6, 100)  # Set width of column 2 to 150 pixels
            if current_page == total_pages - 1:
                self.nextBtn.setDisabled(True)
                self.nextBtn.setStyleSheet("background-color: #5D8AA8; color: darkgray;")

        self.prevBtn.setDisabled(False)
        self.prevBtn.setStyleSheet("background-color: blue; color: white;")

    def populate_tableview(self, page):

        print("Current Page: ", current_page+1)

        # cursor.execute("SELECT itemcode, itemname, department, uom, unitprice, sellingprice, end_qty FROM items")
        #
        # result = cursor.fetchall()

        # Set the column headers
        headers = [column[0] for column in cursor.description]
        self.model.setHorizontalHeaderLabels(headers)

        rows_per_page = 300

        startIndex = page * rows_per_page
        endIndex = startIndex + rows_per_page
        # row_count = startIndex

        # print("Page: ", page)

        # Populate the model with the selected rows
        for index, row in enumerate(result):
            item_row = []
            if startIndex <= index < endIndex:
                for column in row:
                    item = QStandardItem(str(column))
                    item.setTextAlignment(Qt.AlignCenter)
                    item_row.append(item)
                    # row_count+=1

                self.model.appendRow(item_row)

            # print("Index: ", index)
            # print("Data length: ", len(result)+1)
            # if index == len(result):
            #     print("Final Count: ", index)
            #     self.nextBtn.setDisabled(True)
            #     self.nextBtn.setStyleSheet("background-color: black")



if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication([])
    window = MainWindow()
    window.setFixedSize(870, 600)  # Set the desired width and height
    # window.populate_tableview(current_page)
    window.show()
    app.exec_()

    # cursor.close()
    conn.close()
