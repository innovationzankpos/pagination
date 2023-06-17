#
# import PyQt5
# from PyQt5 import QtWidgets
# from PyQt5.QtGui import QStandardItem
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QStandardItemModel
# from pagination.ui import MainWindow
# # from PyQt5.uic import loadUi
#
#
# # app = QApplication([])
# #
# # ui_file_path = "pagination.ui"  # Replace with the actual path to your .ui file
# #
# # ui = loadUi(ui_file_path)
#
# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
#
# def close():
#     print("Closed!")
#     window.close()
#
#
# button = window.findChild(QtWidgets.QPushButton, "closeBtn")  # Replace "buttonObjectName" with the actual name you assigned to the button
# button.clicked.connect(close)
#
#
# def populate_tableview():
#     model = QStandardItemModel()
#     model.setHorizontalHeaderLabels(["ITEMCODE", "ITEMNAME", "DEPARTMENT", "UOM", "PRICE", "WHOLESALE", "BAL"])  # Set the column headers
#
#     # Add data to the model
#     for row in range(5):
#         item1 = QStandardItem(f"Item {row+1}-1")
#         item2 = QStandardItem(f"Item {row+1}-2")
#         model.appendRow([item1, item2])
#
#     tableview.setModel(model)
#
#
# # Create a main window and set the loaded UI as the central widget
# window = QMainWindow()
# window.setFixedSize(800, 600)  # Set the desired width and height
# window.setCentralWidget(ui)
#
# # Show the main window
# window.show()
#
# # Start the event loop
# app.exec_()
import PyQt5
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QColor
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHeaderView, QStyledItemDelegate
from pagination_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # button = self.findChild(PyQt5.QtWidgets.QPushButton, "closeBtn")  # Replace "buttonObjectName" with the actual name you assigned to the button
        # button.clicked.connect(self.close)
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

    #     self.searchBtn.setMouseTracking(True)
    #     self.searchBtn.enterEvent = lambda event: self.on_button_hover(self.searchBtn, True)
    #     self.searchBtn.leaveEvent = lambda event: self.on_button_hover(self.searchBtn, False)
    #
    #     self.closeBtn.setMouseTracking(True)
    #     self.closeBtn.enterEvent = lambda event: self.on_button_hover(self.closeBtn, True)
    #     self.closeBtn.leaveEvent = lambda event: self.on_button_hover(self.closeBtn, False)
    #
    # def on_button_hover(self, button, hover):
    #     if hover:
    #         button.setWindowOpacity(0.5)
    #     else:
    #         button.setWindowOpacity(1.0)

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

    def populate_tableview(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["ITEMCODE", "ITEMNAME", "DEPARTMENT", "UOM", "PRICE", "WHOLESALE", "BAL"])  # Set the column headers
        model.set

        for row in range(5):
            item1 = QStandardItem(f"Item {row+1}-1")
            item2 = QStandardItem(f"Item {row+1}-2")
            model.appendRow([item1, item2])

        self.tableView.setModel(model)

        # Set fixed size for rows and columns
        for row in range(model.rowCount()):
            self.tableView.setRowHeight(row, 50)  # Set row height to 50 pixels

        # Set fixed size for specific headers
        header = self.tableView.horizontalHeader()
        header.resizeSection(0, 30)  # Set width of header for column 0 to 100 pixels
        header.setSectionResizeMode(QHeaderView.Fixed)

        self.tableView.setColumnWidth(0, 100)  # Set width of column 0 to 100 pixels
        self.tableView.setColumnWidth(1, 200)  # Set width of column 2 to 150 pixels
        self.tableView.setColumnWidth(2, 100)  # Set width of column 0 to 100 pixels
        self.tableView.setColumnWidth(3, 50)  # Set width of column 2 to 150 pixels
        self.tableView.setColumnWidth(4, 100)  # Set width of column 0 to 100 pixels
        self.tableView.setColumnWidth(5, 100)  # Set width of column 2 to 150 pixels
        self.tableView.setColumnWidth(6, 100)  # Set width of column 2 to 150 pixels

        # Set the resizing mode for the header sections
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # # Create a layout and set the table view as its widget
        # layout = QVBoxLayout()
        # layout.addWidget(self.tableView)
        #
        # # Create a central widget and set the layout on it
        # central_widget = QWidget()
        # central_widget.setLayout(layout)
        # self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication([])
    window = MainWindow()
    window.populate_tableview()
    window.setFixedSize(800, 600)  # Set the desired width and height
    # window.setCentralWidget()
    window.show()
    app.exec_()
