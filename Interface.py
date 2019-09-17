from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QTableWidget, QTableWidgetItem, QComboBox, QMainWindow
from PyQt5.QtCore import Qt

"""
Класс, отрисовывающий интерфейс приложения.
"""
class Ui_MainWindow(object):
    """
    Инициализация интерфейса.
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 620)

        self.back = QLabel(MainWindow)
        self.back.setPixmap(QPixmap('images/back.jpg'))
        self.back.setGeometry(0, 0, 1500, 1500)

        self.label = QLabel(MainWindow)
        self.label.setPixmap(QPixmap('images/firefox.jpg'))
        self.label.setGeometry(50, 20, 120, 120)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 70, 230, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(QtGui.QFont("Gugi", 20))

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(600, 120, 180, 50))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setFont(QtGui.QFont("Gugi", 20))

        self.direct_label = QLabel(MainWindow)
        self.direct_label.setText('Directory:')
        self.direct_label.setGeometry(205, 30, 150, 25)
        self.direct_label.setFont(QtGui.QFont("Gugi", 14))

        self.folder_path = QtWidgets.QTextEdit(MainWindow)
        self.folder_path.setGeometry(280, 30, 510, 25)
        self.folder_path.setFont(QtGui.QFont("Gugi", 12))
        self.folder_path.setReadOnly(True)

        self.label1 = QLabel(MainWindow)
        self.label1.setText("ANALISYS RESULTS")
        self.label1.setGeometry(90, 185, 250, 50)
        self.label1.setFont(QtGui.QFont("Gugi", 24))
        self.label1.adjustSize()

        self.tableWidget1 = QTableWidget(MainWindow)
        self.tableWidget1.setGeometry(60, 220, 730, 300)
        self.tableWidget1.setRowCount(1)
        self.tableWidget1.setColumnCount(2)
        self.tableWidget1.setColumnWidth(0, 615)
        self.tableWidget1.setColumnWidth(1, 100)
        self.tableWidget1.setHorizontalHeaderLabels(["Image", "Result"])
        self.tableWidget1.horizontalHeaderItem(0).setFont(QtGui.QFont("Gugi", 14))
        self.tableWidget1.horizontalHeaderItem(1).setFont(QtGui.QFont("Gugi", 14))
        self.tableWidget1.setItem(0, 0, QTableWidgetItem("No Images"))
        self.tableWidget1.setItem(0, 1, QTableWidgetItem("----"))
        self.tableWidget1.item(0, 0).setFont(QtGui.QFont("Gugi", 12))
        self.tableWidget1.item(0, 1).setFont(QtGui.QFont("Gugi", 12))
        self.tableWidget1.item(0, 1).setTextAlignment(Qt.AlignCenter)


        self.fireImg = QComboBox(MainWindow)
        self.fireImg.setGeometry(70, 540, 565, 30)

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(645, 535, 140, 40))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setFont(QtGui.QFont("Gugi", 20))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 312, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FireFreeClient"))
        self.pushButton.setText(_translate("MainWindow", "select directory"))
        self.pushButton1.setText(_translate('MainWindow', 'SHOW'))
        self.pushButton2.setText(_translate('MainWindow', 'analyze'))
    """
    Функция обновления таблицы. Данная функция вносит в указанную строку таблицы данные, состоящие из наименования 
    изображения и результата аналитической обработки.
    """
    def update_table(self, num_of_row, filename, verdict):
        ver = 'No'
        if verdict:
            ver = 'Yes'
        self.tableWidget1.insertRow(num_of_row)
        self.tableWidget1.setItem(num_of_row, 0, QTableWidgetItem(filename))
        self.tableWidget1.item(num_of_row, 0).setFont(QtGui.QFont("Gugi", 12))
        self.tableWidget1.setItem(num_of_row, 1, QTableWidgetItem(ver))
        self.tableWidget1.item(num_of_row, 1).setFont(QtGui.QFont("Gugi", 12))
        self.tableWidget1.item(num_of_row, 1).setTextAlignment(Qt.AlignCenter)


