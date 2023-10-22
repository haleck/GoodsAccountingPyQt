import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QCompleter

from utils import *


class OrdersPage(object):
    def showOrdersList(self, data):
        for i, item in enumerate(data):
            self.orders_create_header.setText('Новый заказ')
            self.orders_create_item1 = QtWidgets.QWidget(self.orders_create_scrollAreaWidgetContents)
            self.orders_create_item1.setGeometry(QtCore.QRect(0, 40 * i, 1300, 35))
            self.orders_create_item1.setMinimumSize(QtCore.QSize(0, 0))
            self.orders_create_item1.setObjectName("orders_create_table_item" + str(i))
            self.orders_create_table_checkbox = QtWidgets.QCheckBox(self.orders_create_item1)

            self.orders_create_table_checkbox.setGeometry(QtCore.QRect(0, 0, 35, 35))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.orders_create_table_checkbox.sizePolicy().hasHeightForWidth())
            self.orders_create_table_checkbox.setSizePolicy(sizePolicy)
            self.orders_create_table_checkbox.setMinimumSize(QtCore.QSize(0, 0))
            self.orders_create_table_checkbox.setStyleSheet("QCheckBox::indicator { \n"
                                                           "    width: 35px; \n"
                                                           "    height: 35px;\n"
                                                           "}\n"
                                                           "QCheckBox {\n"
                                                           "    background-color: rgb(91, 91, 91);\n"
                                                           "    border-color: rgb(66, 66, 66);\n"
                                                           "    border-radius: 6px;\n"
                                                           "}")
            self.orders_create_table_checkbox.setText("")
            self.orders_create_table_checkbox.setIconSize(QtCore.QSize(40, 40))
            self.orders_create_table_checkbox.setChecked(False)
            self.orders_create_table_checkbox.setObjectName("orders_create_table_checkbox" + str(i))

            self.orders_create_table_name_lineEdit = QtWidgets.QLineEdit(self.orders_create_item1)
            self.orders_create_table_name_lineEdit.setEnabled(False)
            self.orders_create_table_name_lineEdit.setGeometry(QtCore.QRect(40, 0, 580, 35))
            self.orders_create_table_name_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.orders_create_table_name_lineEdit.setFont(font)
            self.orders_create_table_name_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                                "border-color: rgb(66, 66, 66);\n"
                                                                "background-color:rgb(71, 71, 71);\n"
                                                                "border-radius: 8px;\n"
                                                                "padding: 5px;")
            self.orders_create_table_name_lineEdit.setText("")
            self.orders_create_table_name_lineEdit.setObjectName("orders_create_table_name_lineEdit" + str(i))

            self.orders_create_table_manufac_lineEdit = QtWidgets.QLineEdit(self.orders_create_item1)
            self.orders_create_table_manufac_lineEdit.setEnabled(False)
            self.orders_create_table_manufac_lineEdit.setGeometry(QtCore.QRect(630, 0, 521, 35))
            self.orders_create_table_manufac_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.orders_create_table_manufac_lineEdit.setFont(font)
            self.orders_create_table_manufac_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                                   "border-color: rgb(66, 66, 66);\n"
                                                                   "background-color: rgb(71, 71, 71);\n"
                                                                   "border-radius: 8px;\n"
                                                                   "padding: 5px;")
            self.orders_create_table_manufac_lineEdit.setText("")
            self.orders_create_table_manufac_lineEdit.setObjectName("orders_create_table_manufac_lineEdit" + str(i))



            self.orders_create_writeOff_2 = QtWidgets.QSpinBox(self.orders_create_item1)
            self.orders_create_writeOff_2.setGeometry(QtCore.QRect(1160, 0, 110, 35))
            self.orders_create_writeOff_2.setStyleSheet("\n"
                                                       "background-color:rgb(91, 91, 91);\n"
                                                       "color: rgb(217, 217, 217);")
            self.orders_create_writeOff_2.setAlignment(QtCore.Qt.AlignCenter)
            self.orders_create_writeOff_2.setObjectName("orders_create_writeOff" + str(i))

            self.orders_create_table_name_lineEdit.setText(item['name'])
            self.orders_create_table_manufac_lineEdit.setText(item['manufacturer'])

    def showOrdersList1(self, data):
        self.orders_create_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1286, len(data) * 42 + 5))
        self.orders_create_scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, len(data) * 42 + 5))
        for i, item in enumerate(data):
            print(i, item)
            self.orders_create_item1 = QtWidgets.QWidget(self.orders_create_scrollAreaWidgetContents)
            self.orders_create_item1.setGeometry(QtCore.QRect(0, i * 40, 1300, 35))
            self.orders_create_item1.setMinimumSize(QtCore.QSize(0, 0))
            self.orders_create_item1.setObjectName("orders_create_item" + str(i) + str(random.randint(0,50)))
            self.orders_create_item1_name = QtWidgets.QLineEdit(self.orders_create_item1)
            self.orders_create_item1_name.setEnabled(False)
            self.orders_create_item1_name.setGeometry(QtCore.QRect(0, 0, 630, 35))
            self.orders_create_item1_name.setMinimumSize(QtCore.QSize(0, 35))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.orders_create_item1_name.setFont(font)
            self.orders_create_item1_name.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                        "border-color: rgb(66, 66, 66);\n"
                                                        "background-color:rgb(71, 71, 71);\n"
                                                        "border-radius: 8px;\n"
                                                        "padding: 5px;")
            self.orders_create_item1_name.setText("")
            self.orders_create_item1_name.setObjectName("orders_create_item1_name" + str(i)+ str(random.randint(0,50)))
            self.orders_create_item1_manufac = QtWidgets.QLineEdit(self.orders_create_item1)
            self.orders_create_item1_manufac.setEnabled(False)
            self.orders_create_item1_manufac.setGeometry(QtCore.QRect(640, 0, 351, 35))
            self.orders_create_item1_manufac.setMinimumSize(QtCore.QSize(0, 35))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.orders_create_item1_manufac.setFont(font)
            self.orders_create_item1_manufac.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                           "border-color: rgb(66, 66, 66);\n"
                                                           "background-color: rgb(71, 71, 71);\n"
                                                           "border-radius: 8px;\n"
                                                           "padding: 5px;")
            self.orders_create_item1_manufac.setText("")
            self.orders_create_item1_manufac.setObjectName("orders_create_item1_manufac" + str(i)+ str(random.randint(0,50)))
            self.orders_create_item1_insys = QtWidgets.QLineEdit(self.orders_create_item1)
            self.orders_create_item1_insys.setEnabled(False)
            self.orders_create_item1_insys.setGeometry(QtCore.QRect(1000, 0, 110, 35))
            self.orders_create_item1_insys.setMinimumSize(QtCore.QSize(0, 35))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.orders_create_item1_insys.setFont(font)
            self.orders_create_item1_insys.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                         "border-color: rgb(66, 66, 66);\n"
                                                         "background-color: rgb(71, 71, 71);\n"
                                                         "border-radius: 8px;\n"
                                                         "padding: 5px;")
            self.orders_create_item1_insys.setText("")
            self.orders_create_item1_insys.setAlignment(QtCore.Qt.AlignCenter)
            self.orders_create_item1_insys.setObjectName("orders_create_item1_insys" + str(i)+ str(random.randint(0,50)))
            self.orders_create_item1_inorder = QtWidgets.QSpinBox(self.orders_create_item1)
            self.orders_create_item1_inorder.setGeometry(QtCore.QRect(1120, 0, 110, 35))
            self.orders_create_item1_inorder.setStyleSheet("\n"
                                                           "background-color:rgb(91, 91, 91);\n"
                                                           "color: rgb(217, 217, 217);\n"
                                                           "border-color: rgb(66, 66, 66);")
            self.orders_create_item1_inorder.setAlignment(QtCore.Qt.AlignCenter)
            self.orders_create_item1_inorder.setObjectName("orders_create_item1_inorder" + str(i)+ str(random.randint(0,50)))
            self.orders_create_item1_close = QtWidgets.QLabel(self.orders_create_item1)
            self.orders_create_item1_close.setGeometry(QtCore.QRect(1240, 0, 35, 35))
            self.orders_create_item1_close.setStyleSheet("QLabel:hover {\n"
                                                         "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                         "    color: rgb(52, 52, 52);\n"
                                                         "}")
            self.orders_create_item1_close.setText("")
            self.orders_create_item1_close.setPixmap(QtGui.QPixmap("assets/X.png"))
            self.orders_create_item1_close.setObjectName("orders_create_item1_close" + str(i)+ str(random.randint(0,50)))

            self.orders_create_item1_name.setText(item['name'])
            self.orders_create_item1_manufac.setText(item['manufacturer'])
            self.orders_create_item1_insys.setText(str(item['amount']))

    def showNewItemCreationInOrderPage(self):
        self.orders_create_newItem = QtWidgets.QWidget(self.orders_create_scrollAreaWidgetContents)
        if self.ordersCurrentRow is not None:
            self.orders_create_newItem.setGeometry(
                QtCore.QRect(0, 10 + len(self.ordersData[self.ordersCurrentRow]['items']) * 40, 1281, 35))
        else:
            self.orders_create_newItem.setGeometry(QtCore.QRect(0, 10, 1281, 35))
        self.orders_create_newItem.setObjectName("orders_create_newItem")
        self.orders_create_newItem_ok = QtWidgets.QPushButton(self.orders_create_newItem)
        self.orders_create_newItem_ok.setGeometry(QtCore.QRect(1170, 0, 101, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_newItem_ok.setFont(font)
        self.orders_create_newItem_ok.setStyleSheet("QPushButton {\n"
                                                    "    background-color: rgb(91, 91, 91);\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    border-radius: 6px;\n"
                                                    "    border: 1px solid rgb(66, 66, 66);\n"
                                                    "}\n"
                                                    "QPushButton:hover {\n"
                                                    "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                    "    color: rgb(52, 52, 52);\n"
                                                    "}\n"
                                                    "")
        self.orders_create_newItem_ok.setObjectName("orders_create_newItem_ok")

        self.orders_create_newItem_name = QtWidgets.QLineEdit(self.orders_create_newItem)
        self.orders_create_newItem_name.setGeometry(QtCore.QRect(0, 0, 1041, 35))
        self.orders_create_newItem_name.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_newItem_name.setFont(font)
        self.orders_create_newItem_name.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                      "border-color: rgb(66, 66, 66);\n"
                                                      "background-color: rgb(91, 91, 91);\n"
                                                      "border-radius: 6px;\n"
                                                      "padding: 5px;")
        self.orders_create_newItem_name.setText("")
        self.orders_create_newItem_name.setObjectName("orders_create_newItem_name")

        self.orders_create_newItem_ok.setText("OK")
        self.orders_create_newItem_name.setPlaceholderText("Введите название...")

        addItemCompleters(self.orders_create_newItem_name)

    def clearOrdersInCreationPage(self):
        for child in self.orders_create_scrollAreaWidgetContents.findChildren(QWidget):
            child.deleteLater()

    def deleteNewItemCreationInOrdersPage(self):
        widget = self.orders_create_scrollAreaWidgetContents.findChild(QWidget, "orders_create_newItem")
        widget.deleteLater()

    def drawOrdersTable(self):
        self.ordersData = fetchOrders()

        self.orders_main_table = QtWidgets.QTableWidget(self.orders_main)
        self.orders_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.orders_main_table.setObjectName("orders_main_table")
        self.orders_main_table.setColumnCount(4)
        self.orders_main_table.setRowCount(0)

        self.orders_main_table.setColumnWidth(0, 325)
        self.orders_main_table.setColumnWidth(1, 325)
        self.orders_main_table.setColumnWidth(2, 324)
        self.orders_main_table.setColumnWidth(3, 324)

        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(3, item)

        self.orders_main_table.setRowCount(len(self.ordersData))

        # Заполнение таблицы данными
        for row, item in enumerate(self.ordersData):
            cell = QTableWidgetItem(str(item['id']))
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.orders_main_table.setItem(row, 0, cell)

            cell = QTableWidgetItem(item['status'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.orders_main_table.setItem(row, 1, cell)

            cell = QTableWidgetItem(item['address'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.orders_main_table.setItem(row, 2, cell)

            cell = QTableWidgetItem(item['date'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.orders_main_table.setItem(row, 3, cell)

        self.ordersCurrentRow = None

        # Выделение всей строки при клике
        def on_item_click(item):
            row = item.row()
            self.ordersCurrentRow = row
            for col in range(self.orders_main_table.columnCount()):
                self.orders_main_table.item(row, col).setSelected(True)

        self.orders_main_table.itemClicked.connect(on_item_click)

        #
        self.orders_main_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        item = self.orders_main_table.horizontalHeaderItem(0)
        item.setText("Код заказа")
        item = self.orders_main_table.horizontalHeaderItem(1)
        item.setText("Статус")
        item = self.orders_main_table.horizontalHeaderItem(2)
        item.setText("Адрес")
        item = self.orders_main_table.horizontalHeaderItem(3)
        item.setText("Дата и время")
    def __init__(self):
        self.ordersCurrentItems = []
        self.orders = QtWidgets.QWidget()
        self.orders.setObjectName("orders")
        self.orders_stackedWidget = QtWidgets.QStackedWidget(self.orders)
        self.orders_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 911))
        self.orders_stackedWidget.setObjectName("orders_stackedWidget")
        self.orders_main = QtWidgets.QWidget()
        self.orders_main.setObjectName("orders_main")

        # Start of Orders Table

        self.drawOrdersTable()

        # End of Orders Table

        self.orders_main_createBtn = QtWidgets.QLabel(self.orders_main)
        self.orders_main_createBtn.setGeometry(QtCore.QRect(1230, 50, 131, 20))
        self.orders_main_createBtn.setText("")
        self.orders_main_createBtn.setPixmap(QtGui.QPixmap("assets/new_order.png"))
        self.orders_main_createBtn.setObjectName("orders_main_createBtn")
        self.orders_main_search_lineEdit = QtWidgets.QLineEdit(self.orders_main)
        self.orders_main_search_lineEdit.setGeometry(QtCore.QRect(60, 40, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.orders_main_search_lineEdit.setFont(font)
        self.orders_main_search_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                       "font: 25 10pt \"Ubuntu\";\n"
                                                       "padding: 5px;\n"
                                                       "padding-right: 35px;\n"
                                                       "border-radius: 8px;\n"
                                                       "border-color: rgb(66, 66, 66);\n"
                                                       "background-color: rgb(52, 52, 52);")
        self.orders_main_search_lineEdit.setText("")
        self.orders_main_search_lineEdit.setObjectName("orders_main_search_lineEdit")
        self.orders_main_search_img = QtWidgets.QLabel(self.orders_main)
        self.orders_main_search_img.setGeometry(QtCore.QRect(430, 50, 18, 18))
        self.orders_main_search_img.setStyleSheet("background: none")
        self.orders_main_search_img.setText("")
        self.orders_main_search_img.setPixmap(QtGui.QPixmap("assets/search.png"))
        self.orders_main_search_img.setObjectName("orders_main_search_img")
        self.orders_stackedWidget.addWidget(self.orders_main)
        self.orders_create = QtWidgets.QWidget()
        self.orders_create.setObjectName("orders_create")
        self.orders_create_header = QtWidgets.QLabel(self.orders_create)
        self.orders_create_header.setGeometry(QtCore.QRect(170, 50, 251, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.orders_create_header.setFont(font)
        self.orders_create_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.orders_create_header.setObjectName("orders_create_header")
        self.orders_create_back_btn = QtWidgets.QLabel(self.orders_create)
        self.orders_create_back_btn.setGeometry(QtCore.QRect(60, 50, 91, 22))
        self.orders_create_back_btn.setText("")
        self.orders_create_back_btn.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.orders_create_back_btn.setObjectName("orders_create_back_btn")
        self.orders_create_login_widget = QtWidgets.QWidget(self.orders_create)
        self.orders_create_login_widget.setGeometry(QtCore.QRect(60, 100, 800, 101))
        self.orders_create_login_widget.setMinimumSize(QtCore.QSize(0, 101))
        self.orders_create_login_widget.setStyleSheet("border: none")
        self.orders_create_login_widget.setObjectName("orders_create_login_widget")
        self.orders_create_login_label = QtWidgets.QLabel(self.orders_create_login_widget)
        self.orders_create_login_label.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.orders_create_login_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_login_label.setFont(font)
        self.orders_create_login_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.orders_create_login_label.setObjectName("orders_create_login_label")
        self.orders_create_login_lineEdit = QtWidgets.QLineEdit(self.orders_create_login_widget)
        self.orders_create_login_lineEdit.setGeometry(QtCore.QRect(0, 60, 791, 35))
        self.orders_create_login_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_login_lineEdit.setFont(font)
        self.orders_create_login_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                        "border-color: rgb(66, 66, 66);\n"
                                                        "background-color: rgb(91, 91, 91);\n"
                                                        "border-radius: 8px;\n"
                                                        "padding: 5px;")
        self.orders_create_login_lineEdit.setText("")
        self.orders_create_login_lineEdit.setObjectName("orders_create_login_lineEdit")
        self.orders_create_status_widget = QtWidgets.QWidget(self.orders_create)
        self.orders_create_status_widget.setGeometry(QtCore.QRect(870, 120, 491, 80))
        self.orders_create_status_widget.setObjectName("orders_create_status_widget")
        self.orders_create_status_header = QtWidgets.QLabel(self.orders_create_status_widget)
        self.orders_create_status_header.setGeometry(QtCore.QRect(0, 10, 121, 17))
        self.orders_create_status_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_status_header.setFont(font)
        self.orders_create_status_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.orders_create_status_header.setObjectName("orders_create_status_header")
        self.orders_create_status_combobox = QtWidgets.QComboBox(self.orders_create_status_widget)
        self.orders_create_status_combobox.setGeometry(QtCore.QRect(0, 40, 491, 35))
        self.orders_create_status_combobox.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                                         "border-color: rgb(66, 66, 66);\n"
                                                         "border-radius: 8px;")
        self.orders_create_status_combobox.setObjectName("orders_create_status_combobox")
        self.orders_create_status_combobox.addItems(fetchStatuses())
        self.orders_create_scrollArea = QtWidgets.QScrollArea(self.orders_create)
        self.orders_create_scrollArea.setGeometry(QtCore.QRect(60, 260, 1300, 611))
        self.orders_create_scrollArea.setStyleSheet("QScrollArea {\n"
                                                    "    border: none;\n"
                                                    "}")
        self.orders_create_scrollArea.setWidgetResizable(True)
        self.orders_create_scrollArea.setObjectName("orders_create_scrollArea")
        self.orders_create_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.orders_create_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1286, 100))
        self.orders_create_scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 100))
        self.orders_create_scrollAreaWidgetContents.setObjectName("orders_create_scrollAreaWidgetContents")

        # Здесь был список
        # self.showNewItemCreationInOrderPage()
        # self.showOrdersList(fetchItems())

        self.orders_create_scrollArea.setWidget(self.orders_create_scrollAreaWidgetContents)
        self.orders_create_table_name = QtWidgets.QLabel(self.orders_create)
        self.orders_create_table_name.setGeometry(QtCore.QRect(100, 240, 67, 17))
        self.orders_create_table_name.setObjectName("orders_create_table_name")
        self.orders_create_inorder = QtWidgets.QLabel(self.orders_create)
        self.orders_create_inorder.setGeometry(QtCore.QRect(1213, 240, 111, 17))
        self.orders_create_inorder.setAlignment(QtCore.Qt.AlignCenter)
        self.orders_create_inorder.setObjectName("orders_create_inorder")
        self.orders_create_saveBtn = QtWidgets.QPushButton(self.orders_create)
        self.orders_create_saveBtn.setGeometry(QtCore.QRect(1000, 40, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_saveBtn.setFont(font)
        self.orders_create_saveBtn.setStyleSheet("QPushButton {\n"
                                                 "    background-color: rgb(91, 91, 91);\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    border-radius: 8px;\n"
                                                 "    border: 1px solid rgb(66, 66, 66);\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                 "    color: rgb(52, 52, 52);\n"
                                                 "}\n"
                                                 "")
        self.orders_create_saveBtn.setObjectName("orders_create_saveBtn")
        self.orders_create_deleteImg = QtWidgets.QLabel(self.orders_create)
        self.orders_create_deleteImg.setGeometry(QtCore.QRect(1320, 40, 35, 35))
        self.orders_create_deleteImg.setStyleSheet("QLabel:hover {\n"
                                                   "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                   "    color: rgb(52, 52, 52);\n"
                                                   "}")
        self.orders_create_deleteImg.setText("")
        self.orders_create_deleteImg.setPixmap(QtGui.QPixmap("assets/delete_button.png"))
        self.orders_create_deleteImg.setObjectName("orders_create_deleteImg")
        self.orders_create_closeBtn = QtWidgets.QPushButton(self.orders_create)
        self.orders_create_closeBtn.setGeometry(QtCore.QRect(1160, 40, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orders_create_closeBtn.setFont(font)
        self.orders_create_closeBtn.setStyleSheet("QPushButton {\n"
                                                  "    background-color: rgb(66, 66, 66);\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    border-radius: 8px;\n"
                                                  "    border: 1px solid rgb(52, 52, 52);\n"
                                                  "}\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                  "    color: rgb(52, 52, 52);\n"
                                                  "}\n"
                                                  "")
        self.orders_create_closeBtn.setObjectName("orders_create_closeBtn")
        self.orders_stackedWidget.addWidget(self.orders_create)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.orders_main_search_lineEdit.setPlaceholderText(_translate("MainWindow", "Найти..."))
        self.orders_create_header.setText(_translate("MainWindow", "Заказ 123123"))
        self.orders_create_login_label.setText(_translate("MainWindow", "Адрес"))
        self.orders_create_login_lineEdit.setPlaceholderText(_translate("MainWindow", "Введите адрес"))
        self.orders_create_status_header.setText(_translate("MainWindow", "Статус"))
        self.orders_create_status_combobox.setPlaceholderText(_translate("MainWindow", "Выберите"))
        self.orders_create_status_combobox.setItemText(0, _translate("MainWindow", "Создан"))
        self.orders_create_status_combobox.setItemText(1, _translate("MainWindow", "Принят"))
        self.orders_create_status_combobox.setItemText(2, _translate("MainWindow", "Собирается"))
        self.orders_create_status_combobox.setItemText(3, _translate("MainWindow", "Отправлен"))
        self.orders_create_status_combobox.setItemText(4, _translate("MainWindow", "Принят на складе"))
        self.orders_create_status_combobox.setItemText(5, _translate("MainWindow", "Передан курьеру"))
        self.orders_create_status_combobox.setItemText(6, _translate("MainWindow", "Завершен"))
        self.orders_create_table_name.setText(_translate("MainWindow", "Товар"))
        self.orders_create_inorder.setText(_translate("MainWindow", "В заказе"))
        self.orders_create_saveBtn.setText(_translate("MainWindow", "СОХРАНИТЬ"))
        self.orders_create_closeBtn.setText(_translate("MainWindow", "ЗАКРЫТЬ"))
