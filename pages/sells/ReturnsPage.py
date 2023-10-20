from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QWidget

from utils import *

class ReturnsPage(object):
    def showListOfReturns(self, Return):
        data = getItemsByOrderId(Return['orderId'])

        self.returns_create_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1286, len(data)*40))
        self.returns_create_scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, len(data)*40))

        if len(data) > 0:
            self.returns_create_item.setText("Товар")
            self.returns_create_manufac.setText("Производитель")
            self.returns_create_inorder.setText("В заказе")
            self.returns_create_return.setText("Возврат")
        else:
            self.returns_create_item = QtWidgets.QLabel(self.returns_create)
            self.returns_create_item.setGeometry(QtCore.QRect(60, 230, 670, 17))
            self.returns_create_item.setObjectName("returns_create_item")
            self.returns_create_item.setText("Нет ни одного товара в заказе")
            self.returns_create_manufac.setText("")
            self.returns_create_inorder.setText("")
            self.returns_create_return.setText("")

        for i, item in enumerate(data):
            self.returns_create_item1 = QtWidgets.QWidget(self.returns_create_scrollAreaWidgetContents)
            self.returns_create_item1.setGeometry(QtCore.QRect(0, i*40, 1300, 35))
            self.returns_create_item1.setMinimumSize(QtCore.QSize(0, 0))
            self.returns_create_item1.setObjectName("returns_create_item1")

            self.returns_create_item1_name = QtWidgets.QLineEdit(self.returns_create_item1)
            self.returns_create_item1_name.setEnabled(False)
            self.returns_create_item1_name.setGeometry(QtCore.QRect(0, 0, 630, 35))
            self.returns_create_item1_name.setMinimumSize(QtCore.QSize(0, 35))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.returns_create_item1_name.setFont(font)
            self.returns_create_item1_name.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                         "border-color: rgb(66, 66, 66);\n"
                                                         "background-color:rgb(71, 71, 71);\n"
                                                         "border-radius: 8px;\n"
                                                         "padding: 5px;")
            self.returns_create_item1_name.setText("")
            self.returns_create_item1_name.setObjectName("returns_create_item1_name")
            self.returns_create_item1_manufac = QtWidgets.QLineEdit(self.returns_create_item1)
            self.returns_create_item1_manufac.setEnabled(False)
            self.returns_create_item1_manufac.setGeometry(QtCore.QRect(640, 0, 401, 35))
            self.returns_create_item1_manufac.setMinimumSize(QtCore.QSize(0, 35))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.returns_create_item1_manufac.setFont(font)
            self.returns_create_item1_manufac.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                            "border-color: rgb(66, 66, 66);\n"
                                                            "background-color: rgb(71, 71, 71);\n"
                                                            "border-radius: 8px;\n"
                                                            "padding: 5px;")
            self.returns_create_item1_manufac.setText("")
            self.returns_create_item1_manufac.setObjectName("returns_create_item1_manufac")
            self.returns_create_item1_amount = QtWidgets.QSpinBox(self.returns_create_item1)
            self.returns_create_item1_amount.setGeometry(QtCore.QRect(1170, 0, 110, 35))
            self.returns_create_item1_amount.setStyleSheet("\n"
                                                           "background-color:rgb(91, 91, 91);\n"
                                                           "color: rgb(217, 217, 217);\n"
                                                           "border-color: rgb(66, 66, 66);")
            self.returns_create_item1_amount.setAlignment(QtCore.Qt.AlignCenter)
            self.returns_create_item1_amount.setObjectName("returns_create_item1_amount")
            self.returns_create_item1_inorder = QtWidgets.QLineEdit(self.returns_create_item1)
            self.returns_create_item1_inorder.setEnabled(False)
            self.returns_create_item1_inorder.setGeometry(QtCore.QRect(1050, 0, 110, 35))
            self.returns_create_item1_inorder.setMinimumSize(QtCore.QSize(0, 35))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.returns_create_item1_inorder.setFont(font)
            self.returns_create_item1_inorder.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                            "border-color: rgb(66, 66, 66);\n"
                                                            "background-color: rgb(71, 71, 71);\n"
                                                            "border-radius: 8px;\n"
                                                            "padding: 5px;")
            self.returns_create_item1_inorder.setText("")
            self.returns_create_item1_inorder.setAlignment(QtCore.Qt.AlignCenter)
            self.returns_create_item1_inorder.setObjectName("returns_create_item1_inorder")

            self.returns_create_item1_name.setText(item['name'])
            self.returns_create_item1_manufac.setText(item['manufacturer'])
            self.returns_create_item1_inorder.setText(str(item['amount']) + ' ' + item['unit'])
            self.returns_create_cause_comboBox.setCurrentText(Return['cause'])
            self.returns_create_order_lineEdit.setText(str(Return['orderId']))
            self.returns_create_header.setText('Возврат: ' + str(Return['id']))

    def clearReturnsCreatePage(self):
        for child in self.returns_create_scrollAreaWidgetContents.findChildren(QWidget):
            child.deleteLater()
    def __init__(self):
        self.returns = QtWidgets.QWidget()
        self.returns.setObjectName("returns")
        self.returns_stackedWidget = QtWidgets.QStackedWidget(self.returns)
        self.returns_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 891))
        self.returns_stackedWidget.setObjectName("returns_stackedWidget")
        self.returns_main = QtWidgets.QWidget()
        self.returns_main.setObjectName("returns_main")

        # Start of Returns Table

        self.returnsData = fetchReturns()

        self.returns_main_table = QtWidgets.QTableWidget(self.returns_main)
        self.returns_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.returns_main_table.setObjectName("returns_main_table")
        self.returns_main_table.setColumnCount(4)
        self.returns_main_table.setRowCount(0)

        self.returns_main_table.setColumnWidth(0, 325)
        self.returns_main_table.setColumnWidth(1, 325)
        self.returns_main_table.setColumnWidth(2, 324)
        self.returns_main_table.setColumnWidth(3, 324)

        item = QtWidgets.QTableWidgetItem()
        self.returns_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.returns_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.returns_main_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.returns_main_table.setHorizontalHeaderItem(3, item)

        self.returns_main_table.setRowCount(len(self.returnsData))

        # Заполнение таблицы данными
        for row, item in enumerate(self.returnsData):
            cell = QTableWidgetItem(str(item['id']))
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.returns_main_table.setItem(row, 0, cell)

            cell = QTableWidgetItem(str(item['orderId']))
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.returns_main_table.setItem(row, 1, cell)

            cell = QTableWidgetItem(item['cause'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.returns_main_table.setItem(row, 2, cell)

            cell = QTableWidgetItem(item['date'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.returns_main_table.setItem(row, 3, cell)

        self.returnsCurrentRow = None
        # Выделение всей строки при клике
        def on_item_click(item):
            row = item.row()
            self.returnsCurrentRow = row

            for col in range(self.returns_main_table.columnCount()):
                self.returns_main_table.item(row, col).setSelected(True)

        self.returns_main_table.itemClicked.connect(on_item_click)

        #
        self.returns_main_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # End of Returns Table

        self.returns_main_search_img = QtWidgets.QLabel(self.returns_main)
        self.returns_main_search_img.setGeometry(QtCore.QRect(430, 50, 18, 18))
        self.returns_main_search_img.setStyleSheet("background: none")
        self.returns_main_search_img.setText("")
        self.returns_main_search_img.setPixmap(QtGui.QPixmap("assets/search.png"))
        self.returns_main_search_img.setObjectName("returns_main_search_img")
        self.returns_main_createBtn = QtWidgets.QLabel(self.returns_main)
        self.returns_main_createBtn.setGeometry(QtCore.QRect(1210, 50, 151, 20))
        self.returns_main_createBtn.setText("")
        self.returns_main_createBtn.setPixmap(QtGui.QPixmap("assets/new_return.png"))
        self.returns_main_createBtn.setObjectName("returns_main_createBtn")
        self.returns_main_search_lineEdit = QtWidgets.QLineEdit(self.returns_main)
        self.returns_main_search_lineEdit.setGeometry(QtCore.QRect(60, 40, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.returns_main_search_lineEdit.setFont(font)
        self.returns_main_search_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                        "font: 25 10pt \"Ubuntu\";\n"
                                                        "padding: 5px;\n"
                                                        "padding-right: 35px;\n"
                                                        "border-radius: 8px;\n"
                                                        "border-color: rgb(66, 66, 66);\n"
                                                        "background-color: rgb(52, 52, 52);")
        self.returns_main_search_lineEdit.setText("")
        self.returns_main_search_lineEdit.setObjectName("returns_main_search_lineEdit")
        self.returns_main_search_lineEdit.raise_()
        self.returns_main_table.raise_()
        self.returns_main_search_img.raise_()
        self.returns_main_createBtn.raise_()
        self.returns_stackedWidget.addWidget(self.returns_main)
        self.returns_create = QtWidgets.QWidget()
        self.returns_create.setObjectName("returns_create")
        self.returns_create_backBtn = QtWidgets.QLabel(self.returns_create)
        self.returns_create_backBtn.setGeometry(QtCore.QRect(60, 50, 91, 22))
        self.returns_create_backBtn.setText("")
        self.returns_create_backBtn.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.returns_create_backBtn.setObjectName("returns_create_backBtn")
        self.returns_create_header = QtWidgets.QLabel(self.returns_create)
        self.returns_create_header.setGeometry(QtCore.QRect(170, 50, 251, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.returns_create_header.setFont(font)
        self.returns_create_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.returns_create_header.setObjectName("returns_create_header")
        self.returns_create_cause = QtWidgets.QWidget(self.returns_create)
        self.returns_create_cause.setGeometry(QtCore.QRect(560, 120, 801, 80))
        self.returns_create_cause.setObjectName("returns_create_cause")
        self.returns_create_cause_header = QtWidgets.QLabel(self.returns_create_cause)
        self.returns_create_cause_header.setGeometry(QtCore.QRect(0, 10, 121, 17))
        self.returns_create_cause_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.returns_create_cause_header.setFont(font)
        self.returns_create_cause_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.returns_create_cause_header.setObjectName("returns_create_cause_header")
        self.returns_create_cause_comboBox = QtWidgets.QComboBox(self.returns_create_cause)
        self.returns_create_cause_comboBox.setGeometry(QtCore.QRect(0, 40, 801, 35))
        self.returns_create_cause_comboBox.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                                         "border-color: rgb(66, 66, 66);\n"
                                                         "border-radius: 8px;")
        self.returns_create_cause_comboBox.setObjectName("returns_create_cause_comboBox")
        self.returns_create_cause_comboBox.addItem("Не выбрано")
        self.returns_create_cause_comboBox.addItems(fetchCauses())
        self.returns_create_order_widget = QtWidgets.QWidget(self.returns_create)
        self.returns_create_order_widget.setGeometry(QtCore.QRect(60, 100, 501, 101))
        self.returns_create_order_widget.setMinimumSize(QtCore.QSize(0, 101))
        self.returns_create_order_widget.setStyleSheet("border: none")
        self.returns_create_order_widget.setObjectName("returns_create_order_widget")
        self.returns_create_order_header = QtWidgets.QLabel(self.returns_create_order_widget)
        self.returns_create_order_header.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.returns_create_order_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.returns_create_order_header.setFont(font)
        self.returns_create_order_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.returns_create_order_header.setObjectName("returns_create_order_header")
        self.returns_create_order_lineEdit = QtWidgets.QLineEdit(self.returns_create_order_widget)
        self.returns_create_order_lineEdit.setGeometry(QtCore.QRect(0, 60, 491, 35))
        self.returns_create_order_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.returns_create_order_lineEdit.setFont(font)
        self.returns_create_order_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                         "border-color: rgb(66, 66, 66);\n"
                                                         "background-color: rgb(91, 91, 91);\n"
                                                         "border-radius: 8px;\n"
                                                         "padding: 5px;")
        self.returns_create_order_lineEdit.setText("")
        self.returns_create_order_lineEdit.setObjectName("returns_create_order_lineEdit")
        self.returns_create_scrollArea = QtWidgets.QScrollArea(self.returns_create)
        self.returns_create_scrollArea.setGeometry(QtCore.QRect(60, 260, 1300, 611))
        self.returns_create_scrollArea.setStyleSheet("QScrollArea {\n"
                                                     "    border: none;\n"
                                                     "}")
        self.returns_create_scrollArea.setWidgetResizable(True)
        self.returns_create_scrollArea.setObjectName("returns_create_scrollArea")
        self.returns_create_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.returns_create_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1286, 100))
        self.returns_create_scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 100))
        self.returns_create_scrollAreaWidgetContents.setObjectName("returns_create_scrollAreaWidgetContents")

        # Здесь был список

        self.returns_create_scrollArea.setWidget(self.returns_create_scrollAreaWidgetContents)

        self.returns_create_item = QtWidgets.QLabel(self.returns_create)
        self.returns_create_item.setGeometry(QtCore.QRect(60, 230, 670, 17))
        self.returns_create_item.setObjectName("returns_create_item")
        self.returns_create_manufac = QtWidgets.QLabel(self.returns_create)
        self.returns_create_manufac.setGeometry(QtCore.QRect(700, 230, 141, 17))
        self.returns_create_manufac.setObjectName("returns_create_manufac")
        self.returns_create_inorder = QtWidgets.QLabel(self.returns_create)
        self.returns_create_inorder.setGeometry(QtCore.QRect(1110, 230, 111, 17))
        self.returns_create_inorder.setAlignment(QtCore.Qt.AlignCenter)
        self.returns_create_inorder.setObjectName("returns_create_inorder")
        self.returns_create_return = QtWidgets.QLabel(self.returns_create)
        self.returns_create_return.setGeometry(QtCore.QRect(1230, 230, 111, 17))
        self.returns_create_return.setAlignment(QtCore.Qt.AlignCenter)
        self.returns_create_return.setObjectName("returns_create_return")

        self.returns_create_saveBtn = QtWidgets.QPushButton(self.returns_create)
        self.returns_create_saveBtn.setGeometry(QtCore.QRect(1000, 40, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.returns_create_saveBtn.setFont(font)
        self.returns_create_saveBtn.setStyleSheet("QPushButton {\n"
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
        self.returns_create_saveBtn.setObjectName("returns_create_saveBtn")
        self.returns_create_delete_img = QtWidgets.QLabel(self.returns_create)
        self.returns_create_delete_img.setGeometry(QtCore.QRect(1320, 40, 35, 35))
        self.returns_create_delete_img.setStyleSheet("QLabel:hover {\n"
                                                     "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                     "    color: rgb(52, 52, 52);\n"
                                                     "}")
        self.returns_create_delete_img.setText("")
        self.returns_create_delete_img.setPixmap(QtGui.QPixmap("assets/delete_button.png"))
        self.returns_create_delete_img.setObjectName("returns_create_delete_img")
        self.returns_create_closeBtn = QtWidgets.QPushButton(self.returns_create)
        self.returns_create_closeBtn.setGeometry(QtCore.QRect(1160, 40, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.returns_create_closeBtn.setFont(font)
        self.returns_create_closeBtn.setStyleSheet("QPushButton {\n"
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
        self.returns_create_closeBtn.setObjectName("returns_create_closeBtn")
        self.returns_stackedWidget.addWidget(self.returns_create)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        item = self.returns_main_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код возврата"))
        item = self.returns_main_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Код заказа"))
        item = self.returns_main_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Причина"))
        item = self.returns_main_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата и время"))
        self.returns_main_search_lineEdit.setPlaceholderText(_translate("MainWindow", "Найти..."))
        self.returns_create_header.setText(_translate("MainWindow", "Возрват 123123"))
        self.returns_create_cause_header.setText(_translate("MainWindow", "Причина"))
        self.returns_create_cause_comboBox.setPlaceholderText(_translate("MainWindow", "Выберите"))
        self.returns_create_cause_comboBox.setItemText(0, _translate("MainWindow", "Нарушена упаковка"))
        self.returns_create_cause_comboBox.setItemText(1, _translate("MainWindow", "Неполный комплект"))
        self.returns_create_cause_comboBox.setItemText(2, _translate("MainWindow", "Не тот товар"))
        self.returns_create_cause_comboBox.setItemText(3, _translate("MainWindow", "Товар поврежден"))
        self.returns_create_cause_comboBox.setItemText(4, _translate("MainWindow", "Бракованный товар"))
        self.returns_create_order_header.setText(_translate("MainWindow", "Заказ"))
        self.returns_create_order_lineEdit.setPlaceholderText(_translate("MainWindow", "Введите номер заказа"))
        self.returns_create_saveBtn.setText(_translate("MainWindow", "СОХРАНИТЬ"))
        self.returns_create_closeBtn.setText(_translate("MainWindow", "ЗАКРЫТЬ"))