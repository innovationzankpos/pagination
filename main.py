import math

import PyQt5
import pyodbc
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QColor, QFont
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

rows_per_page = 300
current_page = 0
total_pages = 0
isUsed = False
search_result = []


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.searchTxt.setStyleSheet("""
            QLineEdit {
                border: 2px solid lightgray; 
                font-size: 18px; 
                padding: 5px
            }
            QLineEdit::focus {
                border: 3px solid black;
            }
            QLineEdit::hover {
                border: 3px solid black;
            }
        """)
        # Connect the returnPressed signal to the custom method
        self.searchTxt.returnPressed.connect(self.search)
        # Connect the textChanged signal to the custom method
        self.searchTxt.textChanged.connect(self.search_isEmpty)
        self.searchBtn.clicked.connect(self.search)
        self.searchBtn.setStyleSheet("""
            QPushButton {
                background-color: #880808;
                color: white;
            }
            QPushButton:hover {
                outline: 2px solid white;
                outline-offset: -2px;
            }
        """)
        self.itemBtn.clicked.connect(self.item)
        self.itemBtn.setStyleSheet("""
            QPushButton {
                background-color : black;
                color: white;
            }
            QPushButton:hover {
                outline: 2px solid white;
                outline-offset: -10px;
            }
        """)
        self.brandBtn.clicked.connect(self.brand)
        self.brandBtn.setStyleSheet("""
            QPushButton {
                background-color : black;
                color: white;
            }
            QPushButton:hover {
                outline: 2px solid white;
                outline-offset: -2px;
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
            QPushButton {
                background-color : green;
                color: white;
            }
            QPushButton:hover {
                outline: 2px solid white;
                outline-offset: -2px;
            }
        """)
        self.closeBtn.clicked.connect(self.closeUI)
        self.closeBtn.setStyleSheet("""
            QPushButton {
                background-color: #880808;
                color: white;
            }
            QPushButton:hover {
                outline: 2px solid white;
                outline-offset: -2px;
            }
        """)

        self.model = QStandardItemModel()

        # Set the font size
        self.font = QFont()
        # font.setBold(True)
        self.font.setPixelSize(14)  # Replace 12 with the desired font size

        # Create a QTableView and set its model
        self.tableView.setModel(self.model)

        # Hide the vertical header
        self.tableView.verticalHeader().setVisible(False)

        # Set the selection mode to select rows
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Set the table view as non-editable
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # # Hide the horizontal scroll bar
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Populate the table with data
        self.populate_tableview(current_page)

    def search(self):

        global search_result
        global isUsed

        isUsed = True

        # Retrieve the text from the QLineEdit
        input_text = self.searchTxt.text()
        print("Text entered:", input_text)

        # Execute a query to check if the text is a substring of the column in the database
        cursor.execute("SELECT itemcode as ITEMCODE, itemname as ITEMNAME, department as DEPARTMENT, uom as UOM, unitprice as PRICE, sellingprice as WHOLESALE, end_qty as BAL FROM items WHERE itemname LIKE ?", ('%' + input_text + '%',))
        search_result = cursor.fetchall()

        # if input_text == "":
        #     self.nextBtn.setDisabled(False)
        #     self.nextBtn.setStyleSheet("background-color: blue; color: white;")
        if input_text != "":
            if len(search_result) > 0:
                self.prevBtn.setDisabled(True)
                self.prevBtn.setStyleSheet("background-color: #5D8AA8; color: darkgray;")
                self.nextBtn.setDisabled(False)
                self.nextBtn.setStyleSheet("background-color: blue; color: white;")
                print("Text is a substring in the database")
                global current_page

                current_page = 0
                self.model.clear()
                self.populate_tableview(current_page)
            else:
                print("Text is not a substring in the database")

        # cursor.close()

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
        global isUsed

        isUsed = False

        if current_page > 0 and current_page != 1:
            self.prevBtn.setDisabled(False)
            self.prevBtn.setStyleSheet("background-color: blue; color: white;")
            self.nextBtn.setDisabled(False)
            self.nextBtn.setStyleSheet("background-color: blue; color: white;")
            current_page = current_page - 1
            self.populate_tableview(current_page);
        elif current_page == 1:
                self.prevBtn.setDisabled(True)
                self.prevBtn.setStyleSheet("background-color: #5D8AA8; color: darkgray;")
                self.nextBtn.setDisabled(False)
                self.nextBtn.setStyleSheet("background-color: blue; color: white;")
                current_page = current_page - 1
                self.populate_tableview(current_page);

    def next(self):
            print("Next!")
            self.model.clear()

            # cursor.execute("SELECT itemcode, itemname, department, uom, unitprice, sellingprice, end_qty FROM items")
            #
            # result = cursor.fetchall()

            global current_page
            global total_pages

            total_pages = math.ceil(len(self.search_isUsed())/rows_per_page)
            print("Total: ", total_pages)

            if current_page < total_pages - 1:
                current_page = current_page + 1
                self.populate_tableview(current_page)

                if current_page == total_pages - 1:
                        self.nextBtn.setDisabled(True)
                        self.nextBtn.setStyleSheet("background-color: #5D8AA8; color: darkgray;")

            self.prevBtn.setDisabled(False)
            self.prevBtn.setStyleSheet("background-color: blue; color: white;")

    def search_isUsed(self):

        if isUsed:
            return search_result
        else:
            return result

    def search_isEmpty(self):
        global isUsed
        global current_page

        if self.searchTxt.text() == "":
            isUsed = False
            current_page - 0
            self.model.clear()
            self.populate_tableview(current_page)

    def populate_tableview(self, page):

        print("Current Page: ", current_page+1)

        global total_pages

        total_pages = math.ceil(len(self.search_isUsed()) / rows_per_page)
        print("Total Length: ", len(self.search_isUsed()))

        # Set the column headers
        headers = [column[0] for column in cursor.description]
        self.model.setHorizontalHeaderLabels(headers)

        startIndex = page * rows_per_page
        endIndex = startIndex + rows_per_page

        # Populate the model with the selected rows
        for index, row in enumerate(self.search_isUsed()):
            item_row = []
            if startIndex <= index < endIndex:
                print("Index: ", index)
                for column in row:
                    item = QStandardItem(str(column))
                    item.setTextAlignment(Qt.AlignCenter)
                    item_row.append(item)

                self.model.appendRow(item_row)

            if index == len(self.search_isUsed())+1 and isUsed:
                print("Index: ", index)
                print("Length: ", len(self.search_isUsed()))
                self.nextBtn.setDisabled(True)
                self.nextBtn.setStyleSheet("background-color: #5D8AA8; color: darkgray;")
            elif current_page == total_pages - 1:
                print("Curpage: ", current_page)
                print("total: ", total_pages)
                self.nextBtn.setDisabled(True)
                self.nextBtn.setStyleSheet("background-color: #5D8AA8; color: darkgray;")
            # elif index == len(self.search_isUsed())-1 and isUsed:
            #     print("Index: ", index)
            #     print("Length: ", len(self.search_isUsed()))
            #     self.nextBtn.setDisabled(True)
            #     self.nextBtn.setStyleSheet("background-color: #5D8AA8; color: darkgray;")

        # Set fixed size for rows and columns
        for row in range(self.model.rowCount()):
            self.tableView.setRowHeight(row, 50)  # Set row height to 50 pixels
            # self.tableView.setStyleSheet("font-size: 18px; text-align: center:")

        # Set fixed size for specific headers
        header = self.tableView.horizontalHeader()
        header.resizeSection(0, 30)
        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setHighlightSections(False)
        header.setStyleSheet("""
            QHeaderView::section {
                font-size: 18px; 
                background-color: orange; 
                font-weight: bold; 
                text-align: center;
                border: 1px solid #6c6c6c;
                margin: 1px;
            }
        """)

        self.tableView.setShowGrid(False)
        self.tableView.setFont(self.font)
        self.tableView.setStyleSheet("""
            border: none;
        """)
        self.tableView.setColumnWidth(0, 130)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 140)
        self.tableView.setColumnWidth(3, 60)
        self.tableView.setColumnWidth(4, 100)
        self.tableView.setColumnWidth(5, 120)
        self.tableView.setColumnWidth(6, 100)


if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication([])
    window = MainWindow()
    window.setFixedSize(890, 600)  # Set the desired width and height
    # window.populate_tableview(current_page)
    window.show()
    app.exec_()

    # cursor.close()
    conn.close()
