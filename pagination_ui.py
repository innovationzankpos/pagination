# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pagination.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 612)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../OneDrive/Pictures/SPARKY-RESTO-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(10, 20, 120, 50))
        self.searchBtn.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchBtn.setFont(font)
        self.searchBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchBtn.setMouseTracking(True)
        self.searchBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.searchBtn.setStyleSheet("")
        self.searchBtn.setDefault(True)
        self.searchBtn.setFlat(False)
        self.searchBtn.setObjectName("searchBtn")
        self.searchTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.searchTxt.setGeometry(QtCore.QRect(140, 20, 870, 50))
        self.searchTxt.setMinimumSize(QtCore.QSize(600, 50))
        self.searchTxt.setObjectName("searchTxt")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 90, 1020, 420))
        self.tableView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableView.setObjectName("tableView")
        self.brandBtn = QtWidgets.QPushButton(self.centralwidget)
        self.brandBtn.setGeometry(QtCore.QRect(140, 530, 120, 50))
        self.brandBtn.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.brandBtn.setFont(font)
        self.brandBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.brandBtn.setMouseTracking(True)
        self.brandBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.brandBtn.setObjectName("brandBtn")
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setGeometry(QtCore.QRect(910, 530, 120, 50))
        self.closeBtn.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.closeBtn.setFont(font)
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBtn.setMouseTracking(True)
        self.closeBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.closeBtn.setObjectName("closeBtn")
        self.enterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.enterBtn.setGeometry(QtCore.QRect(780, 530, 120, 50))
        self.enterBtn.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enterBtn.setFont(font)
        self.enterBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterBtn.setMouseTracking(True)
        self.enterBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.enterBtn.setObjectName("enterBtn")
        self.prevBtn = QtWidgets.QPushButton(self.centralwidget)
        self.prevBtn.setGeometry(QtCore.QRect(400, 530, 100, 50))
        self.prevBtn.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prevBtn.setFont(font)
        self.prevBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prevBtn.setMouseTracking(True)
        self.prevBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.prevBtn.setObjectName("prevBtn")
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextBtn.setGeometry(QtCore.QRect(510, 530, 100, 50))
        self.nextBtn.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextBtn.setFont(font)
        self.nextBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextBtn.setMouseTracking(True)
        self.nextBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.nextBtn.setObjectName("nextBtn")
        self.itemBtn = QtWidgets.QPushButton(self.centralwidget)
        self.itemBtn.setGeometry(QtCore.QRect(10, 530, 120, 50))
        self.itemBtn.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.itemBtn.setFont(font)
        self.itemBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.itemBtn.setMouseTracking(True)
        self.itemBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.itemBtn.setStyleSheet("")
        self.itemBtn.setDefault(True)
        self.itemBtn.setObjectName("itemBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1044, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zank POS"))
        self.searchBtn.setText(_translate("MainWindow", "SEARCH"))
        self.brandBtn.setText(_translate("MainWindow", "BRAND"))
        self.closeBtn.setText(_translate("MainWindow", "CLOSE"))
        self.enterBtn.setText(_translate("MainWindow", "ENTER"))
        self.prevBtn.setText(_translate("MainWindow", "PREV"))
        self.nextBtn.setText(_translate("MainWindow", "NEXT"))
        self.itemBtn.setText(_translate("MainWindow", "ITEM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
