from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QTableWidgetItem, QWidget

from pages.sells.StockPage import StockPage
from pages.sells.OrdersPage import OrdersPage
from pages.sells.ReturnsPage import ReturnsPage
from pages.sells.GetStocksPage import GetStocksPage
from pages.sells.WriteOffsPage import WriteOffsPage

from utils import *

class MainPage(StockPage, OrdersPage, ReturnsPage, GetStocksPage, WriteOffsPage):
    def __init__(self):
        StockPage.__init__(self)
        OrdersPage.__init__(self)
        ReturnsPage.__init__(self)
        GetStocksPage.__init__(self)
        WriteOffsPage.__init__(self)



        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.main_tab = QtWidgets.QTabWidget(self.main_page)
        self.main_tab.setGeometry(QtCore.QRect(0, 0, 1431, 1031))
        self.main_tab.setMaximumSize(QtCore.QSize(1511, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.main_tab.setFont(font)
        self.main_tab.setStyleSheet("color: rgb(217, 217, 217);")
        self.main_tab.setObjectName("main_tab")

        # Start of items

        self.items = QtWidgets.QWidget()
        self.items.setObjectName("items")
        self.items_stackedWidget = QtWidgets.QStackedWidget(self.items)
        self.items_stackedWidget.setGeometry(QtCore.QRect(-10, 0, 1431, 941))
        self.items_stackedWidget.setObjectName("items_stackedWidget")
        self.items_main = QtWidgets.QWidget()
        self.items_main.setObjectName("items_main")
        self.items_main_search_img = QtWidgets.QLabel(self.items_main)
        self.items_main_search_img.setGeometry(QtCore.QRect(440, 80, 18, 18))
        self.items_main_search_img.setStyleSheet("background: none")
        self.items_main_search_img.setText("")
        self.items_main_search_img.setPixmap(QtGui.QPixmap("assets/search.png"))
        self.items_main_search_img.setObjectName("items_main_search_img")
        self.items_main_search_lineEdit = QtWidgets.QLineEdit(self.items_main)
        self.items_main_search_lineEdit.setGeometry(QtCore.QRect(70, 70, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.items_main_search_lineEdit.setFont(font)
        self.items_main_search_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                      "font: 25 10pt \"Ubuntu\";\n"
                                                      "padding: 5px;\n"
                                                      "padding-right: 35px;\n"
                                                      "border-radius: 8px;\n"
                                                      "border-color: rgb(66, 66, 66);\n"
                                                      "background-color: rgb(52, 52, 52);")
        self.items_main_search_lineEdit.setText("")
        self.items_main_search_lineEdit.setObjectName("items_main_search_lineEdit")

        # Start of Items Table

        self.itemsData = fetchItems()

        self.items_main_table = QtWidgets.QTableWidget(self.items_main)
        self.items_main_table.setGeometry(QtCore.QRect(70, 150, 1300, 700))
        self.items_main_table.setAlternatingRowColors(False)
        self.items_main_table.setColumnCount(7)
        self.items_main_table.setObjectName("items_main_table")
        self.items_main_table.setRowCount(0)

        self.items_main_table.setColumnWidth(0, 150)
        self.items_main_table.setColumnWidth(1, 300)
        self.items_main_table.setColumnWidth(2, 150)
        self.items_main_table.setColumnWidth(3, 150)
        self.items_main_table.setColumnWidth(4, 250)
        self.items_main_table.setColumnWidth(5, 149)
        self.items_main_table.setColumnWidth(6, 149)

        # Создание заголовков столбцов
        for j in range(7):
            item = QtWidgets.QTableWidgetItem()
            self.items_main_table.setHorizontalHeaderItem(j, item)

        self.items_main_table.setRowCount(len(self.itemsData))

        # Заполнение таблицы данными
        for row, item in enumerate(self.itemsData):
            cell = QTableWidgetItem(str(item['id']))
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.items_main_table.setItem(row, 0, cell)

            cell = QTableWidgetItem(item['name'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.items_main_table.setItem(row, 1, cell)

            cell = QTableWidgetItem(item['manufacturer'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.items_main_table.setItem(row, 2, cell)

            cell = QTableWidgetItem(item['category'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.items_main_table.setItem(row, 3, cell)

            cell = QTableWidgetItem(item['description'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.items_main_table.setItem(row, 4, cell)

            cell = QTableWidgetItem(item['unit'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.items_main_table.setItem(row, 5, cell)

            cell = QTableWidgetItem(str(item['price']))
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.items_main_table.setItem(row, 6, cell)

        self.itemsCurrentRow = None
        # Выделение всей строки при клике
        def on_item_click(item):
            row = item.row()
            self.itemsCurrentRow = row

            for col in range(self.items_main_table.columnCount()):
                self.items_main_table.item(row, col).setSelected(True)

        self.items_main_table.itemClicked.connect(on_item_click)

        #
        self.items_main_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # End of Items Table

        self.items_main_add_image = QtWidgets.QLabel(self.items_main)
        self.items_main_add_image.setGeometry(QtCore.QRect(1210, 80, 158, 20))
        self.items_main_add_image.setText("")
        self.items_main_add_image.setPixmap(QtGui.QPixmap("assets/add_item.png"))
        self.items_main_add_image.setObjectName("items_main_add_image")
        self.items_main_search_lineEdit.raise_()
        self.items_main_search_img.raise_()
        self.items_main_table.raise_()
        self.items_main_add_image.raise_()
        self.items_stackedWidget.addWidget(self.items_main)
        self.items_create = QtWidgets.QWidget()
        self.items_create.setObjectName("items_create")
        self.items_create_back_image = QtWidgets.QLabel(self.items_create)
        self.items_create_back_image.setGeometry(QtCore.QRect(70, 100, 91, 22))
        self.items_create_back_image.setText("")
        self.items_create_back_image.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.items_create_back_image.setObjectName("items_create_back_image")
        self.items_create_header = QtWidgets.QLabel(self.items_create)
        self.items_create_header.setGeometry(QtCore.QRect(180, 100, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.items_create_header.setFont(font)
        self.items_create_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.items_create_header.setObjectName("items_create_header")
        self.items_create_delete_image = QtWidgets.QLabel(self.items_create)
        self.items_create_delete_image.setGeometry(QtCore.QRect(1340, 90, 35, 35))
        self.items_create_delete_image.setStyleSheet("QLabel:hover {\n"
                                                     "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                     "    color: rgb(52, 52, 52);\n"
                                                     "}")
        self.items_create_delete_image.setText("")
        self.items_create_delete_image.setPixmap(QtGui.QPixmap("assets/delete_button.png"))
        self.items_create_delete_image.setObjectName("items_create_delete_image")
        self.items_create_fieldItem_widget = QtWidgets.QWidget(self.items_create)
        self.items_create_fieldItem_widget.setGeometry(QtCore.QRect(60, 220, 1321, 101))
        self.items_create_fieldItem_widget.setMinimumSize(QtCore.QSize(0, 101))
        self.items_create_fieldItem_widget.setStyleSheet("border: none")
        self.items_create_fieldItem_widget.setObjectName("items_create_fieldItem_widget")
        self.items_create_fieldItemHeader = QtWidgets.QLabel(self.items_create_fieldItem_widget)
        self.items_create_fieldItemHeader.setGeometry(QtCore.QRect(10, 30, 361, 17))
        self.items_create_fieldItemHeader.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_create_fieldItemHeader.setFont(font)
        self.items_create_fieldItemHeader.setStyleSheet("color: rgb(217, 217, 217);")
        self.items_create_fieldItemHeader.setObjectName("items_create_fieldItemHeader")
        self.items_create_fieldItem_lineEdit = QtWidgets.QLineEdit(self.items_create_fieldItem_widget)
        self.items_create_fieldItem_lineEdit.setGeometry(QtCore.QRect(9, 60, 1300, 35))
        self.items_create_fieldItem_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_create_fieldItem_lineEdit.setFont(font)
        self.items_create_fieldItem_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                           "border-color: rgb(66, 66, 66);\n"
                                                           "background-color: rgb(91, 91, 91);\n"
                                                           "border-radius: 8px;\n"
                                                           "padding: 5px;")
        self.items_create_fieldItem_lineEdit.setText("")
        self.items_create_fieldItem_lineEdit.setObjectName("items_create_fieldItem_lineEdit")
        self.items_create_descr_widget = QtWidgets.QWidget(self.items_create)
        self.items_create_descr_widget.setGeometry(QtCore.QRect(60, 330, 1321, 300))
        self.items_create_descr_widget.setObjectName("items_create_descr_widget")
        self.items_create_descr_textEdit = QtWidgets.QTextEdit(self.items_create_descr_widget)
        self.items_create_descr_textEdit.setGeometry(QtCore.QRect(9, 40, 1300, 250))
        self.items_create_descr_textEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                       "background-color: rgb(91, 91, 91);\n"
                                                       "border-color: rgb(66, 66, 66);\n"
                                                       "border-radius: 8px;")
        self.items_create_descr_textEdit.setObjectName("items_create_descr_textEdit")
        self.items_create_descr_header = QtWidgets.QLabel(self.items_create_descr_widget)
        self.items_create_descr_header.setGeometry(QtCore.QRect(10, 10, 331, 17))
        self.items_create_descr_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_create_descr_header.setFont(font)
        self.items_create_descr_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.items_create_descr_header.setObjectName("items_create_descr_header")
        self.items_create_saveBtn = QtWidgets.QPushButton(self.items_create)
        self.items_create_saveBtn.setGeometry(QtCore.QRect(1020, 90, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_create_saveBtn.setFont(font)
        self.items_create_saveBtn.setStyleSheet("QPushButton {\n"
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
        self.items_create_saveBtn.setObjectName("items_create_saveBtn")
        self.items_create_closeBtn = QtWidgets.QPushButton(self.items_create)
        self.items_create_closeBtn.setGeometry(QtCore.QRect(1180, 90, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_create_closeBtn.setFont(font)
        self.items_create_closeBtn.setStyleSheet("QPushButton {\n"
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
        self.items_create_closeBtn.setObjectName("items_create_closeBtn")
        self.items_create_category_widget = QtWidgets.QWidget(self.items_create)
        self.items_create_category_widget.setGeometry(QtCore.QRect(70, 650, 431, 80))
        self.items_create_category_widget.setObjectName("items_create_category_widget")
        self.items_create_categoty_hedaer = QtWidgets.QLabel(self.items_create_category_widget)
        self.items_create_categoty_hedaer.setGeometry(QtCore.QRect(0, 10, 121, 17))
        self.items_create_categoty_hedaer.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_create_categoty_hedaer.setFont(font)
        self.items_create_categoty_hedaer.setStyleSheet("color: rgb(217, 217, 217);")
        self.items_create_categoty_hedaer.setObjectName("items_create_categoty_hedaer")
        self.items_create_category_comboBox = QtWidgets.QComboBox(self.items_create_category_widget)
        self.items_create_category_comboBox.setGeometry(QtCore.QRect(0, 40, 425, 35))
        self.items_create_category_comboBox.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "border-radius: 8px;")
        self.items_create_category_comboBox.setObjectName("items_create_category_comboBox")
        self.items_create_category_comboBox.addItems(fetchCategories())
        self.items_create_manufact_widget = QtWidgets.QWidget(self.items_create)
        self.items_create_manufact_widget.setGeometry(QtCore.QRect(530, 650, 431, 80))
        self.items_create_manufact_widget.setObjectName("items_create_manufact_widget")
        self.items_create_manufact_header = QtWidgets.QLabel(self.items_create_manufact_widget)
        self.items_create_manufact_header.setGeometry(QtCore.QRect(0, 10, 121, 17))
        self.items_create_manufact_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_create_manufact_header.setFont(font)
        self.items_create_manufact_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.items_create_manufact_header.setObjectName("items_create_manufact_header")
        self.items_create_manufact_comboBox = QtWidgets.QComboBox(self.items_create_manufact_widget)
        self.items_create_manufact_comboBox.setGeometry(QtCore.QRect(0, 40, 425, 35))
        self.items_create_manufact_comboBox.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "border-radius: 8px;")
        self.items_create_manufact_comboBox.setObjectName("items_create_manufact_comboBox")
        self.items_create_manufact_comboBox.addItems(fetchManufacturers())
        self.items_create_edIzm_widget = QtWidgets.QWidget(self.items_create)
        self.items_create_edIzm_widget.setGeometry(QtCore.QRect(990, 650, 161, 80))
        self.items_create_edIzm_widget.setObjectName("items_create_edIzm_widget")
        self.items_create_edizm_header = QtWidgets.QLabel(self.items_create_edIzm_widget)
        self.items_create_edizm_header.setGeometry(QtCore.QRect(0, 10, 121, 17))
        self.items_create_edizm_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_create_edizm_header.setFont(font)
        self.items_create_edizm_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.items_create_edizm_header.setObjectName("items_create_edizm_header")
        self.items_create_edizm_ComboBox = QtWidgets.QComboBox(self.items_create_edIzm_widget)
        self.items_create_edizm_ComboBox.setGeometry(QtCore.QRect(0, 40, 150, 35))
        self.items_create_edizm_ComboBox.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                                       "border-color: rgb(66, 66, 66);\n"
                                                       "border-radius: 8px;")
        self.items_create_edizm_ComboBox.setObjectName("items_create_edizm_ComboBox")
        self.items_create_edizm_ComboBox.addItem("")
        self.items_create_edizm_ComboBox.addItems(fetchUnits())
        self.items_create_price_widget = QtWidgets.QWidget(self.items_create)
        self.items_create_price_widget.setGeometry(QtCore.QRect(1170, 630, 201, 101))
        self.items_create_price_widget.setMinimumSize(QtCore.QSize(0, 101))
        self.items_create_price_widget.setStyleSheet("border: none")
        self.items_create_price_widget.setObjectName("items_create_price_widget")
        self.items_create_price_header = QtWidgets.QLabel(self.items_create_price_widget)
        self.items_create_price_header.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.items_create_price_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_create_price_header.setFont(font)
        self.items_create_price_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.items_create_price_header.setObjectName("items_create_price_header")
        self.items_create_price_lineEdit = QtWidgets.QLineEdit(self.items_create_price_widget)
        self.items_create_price_lineEdit.setGeometry(QtCore.QRect(0, 60, 200, 35))
        self.items_create_price_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.items_create_price_lineEdit.setFont(font)
        self.items_create_price_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                       "border-color: rgb(66, 66, 66);\n"
                                                       "background-color: rgb(91, 91, 91);\n"
                                                       "border-radius: 8px;\n"
                                                       "padding: 5px;")
        self.items_create_price_lineEdit.setText("")
        self.items_create_price_lineEdit.setObjectName("items_create_price_lineEdit")
        self.items_stackedWidget.addWidget(self.items_create)

        # End of items

        self.main_tab.addTab(self.items, "")

        # Start of sells

        self.sells = QtWidgets.QWidget()
        self.sells.setObjectName("sells")
        self.sells_tab = QtWidgets.QTabWidget(self.sells)
        self.sells_tab.setGeometry(QtCore.QRect(-10, 0, 1441, 981))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sells_tab.setFont(font)
        self.sells_tab.setFocusPolicy(QtCore.Qt.TabFocus)
        self.sells_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sells_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.sells_tab.setObjectName("sells_tab")

        # End of sells

        self.sells_tab.addTab(self.stock, "")
        self.sells_tab.addTab(self.orders, "")
        self.sells_tab.addTab(self.returns, "")
        self.sells_tab.addTab(self.getStocks, "")
        self.sells_tab.addTab(self.writeOffs, "")

        # End of sells

        self.main_tab.addTab(self.sells, "")

        # Start of watch

        self.watch = QtWidgets.QWidget()
        self.watch.setObjectName("watch")
        self.watch_search_lineEdit = QtWidgets.QLineEdit(self.watch)
        self.watch_search_lineEdit.setGeometry(QtCore.QRect(60, 70, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.watch_search_lineEdit.setFont(font)
        self.watch_search_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                 "font: 25 10pt \"Ubuntu\";\n"
                                                 "padding: 5px;\n"
                                                 "padding-right: 35px;\n"
                                                 "border-radius: 8px;\n"
                                                 "border-color: rgb(66, 66, 66);\n"
                                                 "background-color: rgb(52, 52, 52);")
        self.watch_search_lineEdit.setText("")
        self.watch_search_lineEdit.setObjectName("watch_search_lineEdit")
        self.watch_search_img = QtWidgets.QLabel(self.watch)
        self.watch_search_img.setGeometry(QtCore.QRect(430, 80, 18, 18))
        self.watch_search_img.setStyleSheet("background: none")
        self.watch_search_img.setText("")
        self.watch_search_img.setPixmap(QtGui.QPixmap("assets/search.png"))
        self.watch_search_img.setObjectName("watch_search_img")

        # Start of watch table

        self.watchData = fetchActions()

        self.watch_table = QtWidgets.QTableWidget(self.watch)
        self.watch_table.setGeometry(QtCore.QRect(60, 150, 1300, 700))
        self.watch_table.setObjectName("watch_table")
        self.watch_table.setColumnCount(4)
        self.watch_table.setRowCount(0)

        self.watch_table.setColumnWidth(0, 325)
        self.watch_table.setColumnWidth(1, 325)
        self.watch_table.setColumnWidth(2, 324)
        self.watch_table.setColumnWidth(3, 324)

        item = QtWidgets.QTableWidgetItem()
        self.watch_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.watch_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.watch_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.watch_table.setHorizontalHeaderItem(3, item)

        self.watch_table.setRowCount(len(self.watchData))

        # Заполнение таблицы данными
        for row, item in enumerate(self.watchData):
            cell = QTableWidgetItem(str(item['id']))
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.watch_table.setItem(row, 0, cell)

            cell = QTableWidgetItem(item['action'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.watch_table.setItem(row, 1, cell)

            cell = QTableWidgetItem(item['employee'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.watch_table.setItem(row, 2, cell)

            cell = QTableWidgetItem(item['date'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.watch_table.setItem(row, 3, cell)

        self.watchCurrentRow = None
        # Выделение всей строки при клике
        def on_item_click(item):
            row = item.row()
            self.watchCurrentRow = row

            for col in range(self.watch_table.columnCount()):
                self.watch_table.item(row, col).setSelected(True)

        self.watch_table.itemClicked.connect(on_item_click)

        #
        self.watch_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # End of watch table
        # End of watch

        self.main_tab.addTab(self.watch, "")

        # Start of employees

        self.employees = QtWidgets.QWidget()
        self.employees.setObjectName("employees")
        self.employees_stackedWidget = QtWidgets.QStackedWidget(self.employees)
        self.employees_stackedWidget.setGeometry(QtCore.QRect(0, 0, 1421, 931))
        self.employees_stackedWidget.setObjectName("employees_stackedWidget")
        self.employees_main = QtWidgets.QWidget()
        self.employees_main.setObjectName("employees_main")

        # Start of Employees Table
        self.employeesData = fetchEmployees()

        self.employees_main_table = QtWidgets.QTableWidget(self.employees_main)
        self.employees_main_table.setGeometry(QtCore.QRect(60, 150, 1300, 700))
        self.employees_main_table.setObjectName("employees_main_table")
        self.employees_main_table.setColumnCount(6)
        self.employees_main_table.setRowCount(0)

        self.employees_main_table.setColumnWidth(0, 216)
        self.employees_main_table.setColumnWidth(1, 217)
        self.employees_main_table.setColumnWidth(2, 216)
        self.employees_main_table.setColumnWidth(3, 217)
        self.employees_main_table.setColumnWidth(4, 216)
        self.employees_main_table.setColumnWidth(5, 216)

        item = QtWidgets.QTableWidgetItem()
        self.employees_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.employees_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.employees_main_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.employees_main_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.employees_main_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.employees_main_table.setHorizontalHeaderItem(5, item)

        self.employees_main_table.setRowCount(len(self.employeesData))

        # Заполнение таблицы данными
        for row, item in enumerate(self.employeesData):
            cell = QTableWidgetItem(str(item['id']))
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.employees_main_table.setItem(row, 0, cell)

            cell = QTableWidgetItem(item['surname'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.employees_main_table.setItem(row, 1, cell)

            cell = QTableWidgetItem(item['name'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.employees_main_table.setItem(row, 2, cell)

            cell = QTableWidgetItem(item['patronymic'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.employees_main_table.setItem(row, 3, cell)

            cell = QTableWidgetItem(item['role'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.employees_main_table.setItem(row, 4, cell)

            cell = QTableWidgetItem(item['number'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.employees_main_table.setItem(row, 5, cell)

        self.employeesCurrentRow = None
        # Выделение всей строки при клике
        def on_item_click(item):
            row = item.row()
            self.employeesCurrentRow = row

            for col in range(self.employees_main_table.columnCount()):
                self.employees_main_table.item(row, col).setSelected(True)

        self.employees_main_table.itemClicked.connect(on_item_click)

        #
        self.employees_main_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # End of Employees Table

        self.employees_main_search_lineEdit = QtWidgets.QLineEdit(self.employees_main)
        self.employees_main_search_lineEdit.setGeometry(QtCore.QRect(60, 70, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.employees_main_search_lineEdit.setFont(font)
        self.employees_main_search_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                          "font: 25 10pt \"Ubuntu\";\n"
                                                          "padding: 5px;\n"
                                                          "padding-right: 35px;\n"
                                                          "border-radius: 8px;\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "background-color: rgb(52, 52, 52);")
        self.employees_main_search_lineEdit.setText("")
        self.employees_main_search_lineEdit.setObjectName("employees_main_search_lineEdit")
        self.employees_main_search_img = QtWidgets.QLabel(self.employees_main)
        self.employees_main_search_img.setGeometry(QtCore.QRect(430, 80, 18, 18))
        self.employees_main_search_img.setStyleSheet("background: none")
        self.employees_main_search_img.setText("")
        self.employees_main_search_img.setPixmap(QtGui.QPixmap("assets/search.png"))
        self.employees_main_search_img.setObjectName("employees_main_search_img")
        self.employees_main_create = QtWidgets.QLabel(self.employees_main)
        self.employees_main_create.setGeometry(QtCore.QRect(1160, 80, 203, 20))
        self.employees_main_create.setText("")
        self.employees_main_create.setPixmap(QtGui.QPixmap("assets/new_employee.png"))
        self.employees_main_create.setObjectName("employees_main_create")
        self.employees_stackedWidget.addWidget(self.employees_main)
        self.employees_create = QtWidgets.QWidget()
        self.employees_create.setObjectName("employees_create")
        self.employees_create_header = QtWidgets.QLabel(self.employees_create)
        self.employees_create_header.setGeometry(QtCore.QRect(170, 100, 251, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.employees_create_header.setFont(font)
        self.employees_create_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.employees_create_header.setObjectName("employees_create_header")
        self.employees_create_back = QtWidgets.QLabel(self.employees_create)
        self.employees_create_back.setGeometry(QtCore.QRect(60, 100, 91, 22))
        self.employees_create_back.setText("")
        self.employees_create_back.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.employees_create_back.setObjectName("employees_create_back")
        self.employees_create_delete = QtWidgets.QLabel(self.employees_create)
        self.employees_create_delete.setGeometry(QtCore.QRect(1330, 90, 35, 35))
        self.employees_create_delete.setStyleSheet("QLabel:hover {\n"
                                                   "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                   "    color: rgb(52, 52, 52);\n"
                                                   "}")
        self.employees_create_delete.setText("")
        self.employees_create_delete.setPixmap(QtGui.QPixmap("assets/delete_button.png"))
        self.employees_create_delete.setObjectName("employees_create_delete")
        self.employees_create_save = QtWidgets.QPushButton(self.employees_create)
        self.employees_create_save.setGeometry(QtCore.QRect(1010, 90, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_save.setFont(font)
        self.employees_create_save.setStyleSheet("QPushButton {\n"
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
        self.employees_create_save.setObjectName("employees_create_save")
        self.employees_create_close = QtWidgets.QPushButton(self.employees_create)
        self.employees_create_close.setGeometry(QtCore.QRect(1170, 90, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_close.setFont(font)
        self.employees_create_close.setStyleSheet("QPushButton {\n"
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
        self.employees_create_close.setObjectName("employees_create_close")
        self.employees_create_surname = QtWidgets.QWidget(self.employees_create)
        self.employees_create_surname.setGeometry(QtCore.QRect(50, 200, 655, 101))
        self.employees_create_surname.setMinimumSize(QtCore.QSize(0, 101))
        self.employees_create_surname.setStyleSheet("border: none")
        self.employees_create_surname.setObjectName("employees_create_surname")
        self.employees_create_surname_header = QtWidgets.QLabel(self.employees_create_surname)
        self.employees_create_surname_header.setGeometry(QtCore.QRect(0, 30, 91, 17))
        self.employees_create_surname_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_surname_header.setFont(font)
        self.employees_create_surname_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.employees_create_surname_header.setObjectName("employees_create_surname_header")
        self.employees_create_surname_lineEdit = QtWidgets.QLineEdit(self.employees_create_surname)
        self.employees_create_surname_lineEdit.setGeometry(QtCore.QRect(0, 60, 641, 35))
        self.employees_create_surname_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_surname_lineEdit.setFont(font)
        self.employees_create_surname_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                             "border-color: rgb(66, 66, 66);\n"
                                                             "background-color: rgb(91, 91, 91);\n"
                                                             "border-radius: 8px;\n"
                                                             "padding: 5px;")
        self.employees_create_surname_lineEdit.setText("")
        self.employees_create_surname_lineEdit.setObjectName("employees_create_surname_lineEdit")
        self.employees_create_name = QtWidgets.QWidget(self.employees_create)
        self.employees_create_name.setGeometry(QtCore.QRect(710, 200, 655, 101))
        self.employees_create_name.setMinimumSize(QtCore.QSize(0, 101))
        self.employees_create_name.setStyleSheet("border: none")
        self.employees_create_name.setObjectName("employees_create_name")
        self.employees_create_name_header = QtWidgets.QLabel(self.employees_create_name)
        self.employees_create_name_header.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.employees_create_name_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_name_header.setFont(font)
        self.employees_create_name_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.employees_create_name_header.setObjectName("employees_create_name_header")
        self.employees_create_name_lineEdit = QtWidgets.QLineEdit(self.employees_create_name)
        self.employees_create_name_lineEdit.setGeometry(QtCore.QRect(10, 60, 641, 35))
        self.employees_create_name_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_name_lineEdit.setFont(font)
        self.employees_create_name_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "background-color: rgb(91, 91, 91);\n"
                                                          "border-radius: 8px;\n"
                                                          "padding: 5px;")
        self.employees_create_name_lineEdit.setText("")
        self.employees_create_name_lineEdit.setObjectName("employees_create_name_lineEdit")
        self.employees_create_patronymic_widget = QtWidgets.QWidget(self.employees_create)
        self.employees_create_patronymic_widget.setGeometry(QtCore.QRect(50, 310, 655, 81))
        self.employees_create_patronymic_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.employees_create_patronymic_widget.setStyleSheet("border: none")
        self.employees_create_patronymic_widget.setObjectName("employees_create_patronymic_widget")
        self.employees_create_patronymic_label = QtWidgets.QLabel(self.employees_create_patronymic_widget)
        self.employees_create_patronymic_label.setGeometry(QtCore.QRect(0, 10, 81, 17))
        self.employees_create_patronymic_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_patronymic_label.setFont(font)
        self.employees_create_patronymic_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.employees_create_patronymic_label.setObjectName("employees_create_patronymic_label")
        self.employees_create_patronymic_lineedit = QtWidgets.QLineEdit(self.employees_create_patronymic_widget)
        self.employees_create_patronymic_lineedit.setGeometry(QtCore.QRect(0, 40, 641, 35))
        self.employees_create_patronymic_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_patronymic_lineedit.setFont(font)
        self.employees_create_patronymic_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                                "border-color: rgb(66, 66, 66);\n"
                                                                "background-color: rgb(91, 91, 91);\n"
                                                                "border-radius: 8px;\n"
                                                                "padding: 5px;")
        self.employees_create_patronymic_lineedit.setText("")
        self.employees_create_patronymic_lineedit.setObjectName("employees_create_patronymic_lineedit")
        self.employees_create_role = QtWidgets.QWidget(self.employees_create)
        self.employees_create_role.setGeometry(QtCore.QRect(50, 400, 655, 81))
        self.employees_create_role.setMinimumSize(QtCore.QSize(0, 0))
        self.employees_create_role.setStyleSheet("border: none")
        self.employees_create_role.setObjectName("employees_create_role")
        self.employees_create_role_label = QtWidgets.QLabel(self.employees_create_role)
        self.employees_create_role_label.setGeometry(QtCore.QRect(0, 10, 67, 17))
        self.employees_create_role_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_role_label.setFont(font)
        self.employees_create_role_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.employees_create_role_label.setObjectName("employees_create_role_label")
        self.employees_create_role_combobox = QtWidgets.QComboBox(self.employees_create_role)
        self.employees_create_role_combobox.setGeometry(QtCore.QRect(0, 40, 641, 35))
        self.employees_create_role_combobox.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "border-radius: 8px;")
        self.employees_create_role_combobox.setObjectName("employees_create_role_combobox")
        self.employees_create_role_combobox.addItem("")
        self.employees_create_role_combobox.addItems(fetchRoles())
        self.employees_create_number = QtWidgets.QWidget(self.employees_create)
        self.employees_create_number.setGeometry(QtCore.QRect(710, 400, 655, 81))
        self.employees_create_number.setMinimumSize(QtCore.QSize(0, 0))
        self.employees_create_number.setStyleSheet("border: none")
        self.employees_create_number.setObjectName("employees_create_number")
        self.employees_create_number_label = QtWidgets.QLabel(self.employees_create_number)
        self.employees_create_number_label.setGeometry(QtCore.QRect(10, 10, 141, 17))
        self.employees_create_number_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_number_label.setFont(font)
        self.employees_create_number_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.employees_create_number_label.setObjectName("employees_create_number_label")
        self.employees_create_number_lineedit = QtWidgets.QLineEdit(self.employees_create_number)
        self.employees_create_number_lineedit.setGeometry(QtCore.QRect(10, 40, 641, 35))
        self.employees_create_number_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_number_lineedit.setFont(font)
        self.employees_create_number_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                            "border-color: rgb(66, 66, 66);\n"
                                                            "background-color: rgb(91, 91, 91);\n"
                                                            "border-radius: 8px;\n"
                                                            "padding: 5px;")
        self.employees_create_number_lineedit.setText("")
        self.employees_create_number_lineedit.setObjectName("employees_create_number_lineedit")
        self.employees_create_user = QtWidgets.QWidget(self.employees_create)
        self.employees_create_user.setGeometry(QtCore.QRect(50, 490, 655, 81))
        self.employees_create_user.setMinimumSize(QtCore.QSize(0, 0))
        self.employees_create_user.setStyleSheet("border: none")
        self.employees_create_user.setObjectName("employees_create_user")
        self.employees_create_user_header = QtWidgets.QLabel(self.employees_create_user)
        self.employees_create_user_header.setGeometry(QtCore.QRect(0, 10, 161, 17))
        self.employees_create_user_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_user_header.setFont(font)
        self.employees_create_user_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.employees_create_user_header.setObjectName("employees_create_user_header")
        self.employees_create_user_lineedit = QtWidgets.QLineEdit(self.employees_create_user)
        self.employees_create_user_lineedit.setGeometry(QtCore.QRect(0, 40, 641, 35))
        self.employees_create_user_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_user_lineedit.setFont(font)
        self.employees_create_user_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "background-color: rgb(91, 91, 91);\n"
                                                          "border-radius: 8px;\n"
                                                          "padding: 5px;")
        self.employees_create_user_lineedit.setText("")
        self.employees_create_user_lineedit.setObjectName("employees_create_user_lineedit")
        self.employees_create_password = QtWidgets.QWidget(self.employees_create)
        self.employees_create_password.setGeometry(QtCore.QRect(710, 480, 655, 91))
        self.employees_create_password.setMinimumSize(QtCore.QSize(0, 0))
        self.employees_create_password.setStyleSheet("border: none")
        self.employees_create_password.setObjectName("employees_create_password")
        self.employees_create_password_header = QtWidgets.QLabel(self.employees_create_password)
        self.employees_create_password_header.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.employees_create_password_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_password_header.setFont(font)
        self.employees_create_password_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.employees_create_password_header.setObjectName("employees_create_password_header")
        self.employees_create_password_lineedit = QtWidgets.QLineEdit(self.employees_create_password)
        self.employees_create_password_lineedit.setGeometry(QtCore.QRect(10, 50, 641, 35))
        self.employees_create_password_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_password_lineedit.setFont(font)
        self.employees_create_password_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                              "border-color: rgb(66, 66, 66);\n"
                                                              "background-color: rgb(91, 91, 91);\n"
                                                              "border-radius: 8px;\n"
                                                              "padding: 5px;")
        self.employees_create_password_lineedit.setText("")
        self.employees_create_password_lineedit.setObjectName("employees_create_password_lineedit")
        self.employees_create_sex_male = QtWidgets.QRadioButton(self.employees_create)
        self.employees_create_sex_male.setGeometry(QtCore.QRect(720, 350, 151, 41))
        self.employees_create_sex_male.setStyleSheet("QRadioButton::indicator {\n"
                                                     "    width: 35px; /* Устанавливает ширину элемента indicator */\n"
                                                     "    height: 35px; /* Устанавливает высоту элемента indicator */\n"
                                                     "}")
        self.employees_create_sex_male.setObjectName("employees_create_sex_male")
        self.employees_create_sex = QtWidgets.QLabel(self.employees_create)
        self.employees_create_sex.setGeometry(QtCore.QRect(720, 330, 81, 17))
        self.employees_create_sex.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employees_create_sex.setFont(font)
        self.employees_create_sex.setStyleSheet("color: rgb(217, 217, 217);")
        self.employees_create_sex.setObjectName("employees_create_sex")
        self.employees_create_sex_female = QtWidgets.QRadioButton(self.employees_create)
        self.employees_create_sex_female.setGeometry(QtCore.QRect(880, 350, 151, 41))
        self.employees_create_sex_female.setStyleSheet("QRadioButton::indicator {\n"
                                                       "    width: 35px; /* Устанавливает ширину элемента indicator */\n"
                                                       "    height: 35px; /* Устанавливает высоту элемента indicator */\n"
                                                       "}")
        self.employees_create_sex_female.setObjectName("employees_create_sex_female")
        self.employees_stackedWidget.addWidget(self.employees_create)

        # End of employees

        self.main_tab.addTab(self.employees, "")

        # Event listeners

        # Items
        self.items_main_add_image.mousePressEvent = self.setItemsCreatePage
        self.items_create_back_image.mousePressEvent = self.setItemsMainPage
        self.items_create_saveBtn.clicked.connect(self.itemsCreateSave)
        self.items_create_closeBtn.clicked.connect(self.itemsCreateClose)
        self.items_create_delete_image.mousePressEvent = self.itemsCreateDelete
        self.items_main_table.itemDoubleClicked.connect(self.setUpItemsCreatePage)
        # Sells
        #   Stock
        self.stock_main_createBtn.mousePressEvent = self.setStockCreatePage
        self.stock_create_backBtn.mousePressEvent = self.setStockMainPage
        self.stock_create_saveBtn.clicked.connect(self.stockCreateSave)
        self.stock_create_closeBtn.clicked.connect(self.stockCreateClose)
        self.stock_create_deleteImg.mousePressEvent = self.stockCreateDelete
        #   Orders
        self.orders_main_createBtn.mousePressEvent = self.setOrdersCreatePage
        self.orders_create_back_btn.mousePressEvent = self.setOrdersMainPage
        self.orders_create_closeBtn.clicked.connect(self.ordersCreateClose)
        self.orders_create_saveBtn.clicked.connect(self.ordersCreateSave)
        self.orders_create_deleteImg.mousePressEvent = self.ordersCreateDelete
        self.orders_main_table.itemDoubleClicked.connect(self.setUpOrdersCreatePage)
        #   Returns
        self.returns_main_createBtn.mousePressEvent = self.setReturnsCreatePage
        self.returns_create_backBtn.mousePressEvent = self.setReturnsMainPage
        self.returns_create_delete_img.mousePressEvent = self.returnsCreateDelete
        self.returns_create_saveBtn.clicked.connect(self.returnsCreateSave)
        self.returns_create_closeBtn.clicked.connect(self.returnsCreateClose)
        self.returns_main_table.itemDoubleClicked.connect(self.setUpReturnsPage)
        #   GetStocks
        self.getStocks_main_createBtn.mousePressEvent = self.setGetStocksCreatePage
        self.getStocks_create_backBtn.mousePressEvent = self.setGetStocksMainPage
        self.getStocks_create_delete.mousePressEvent = self.setGetStocksMainPage
        self.getStocks_create_close.clicked.connect(self.getStocksCreateClose)
        self.getStocks_create_save.clicked.connect(self.getStocksCreateSave)
        self.getStocks_main_table.itemDoubleClicked.connect(self.setUpGetStocksCreatePage)
        #   WriteOffs
        self.writeOffs_main_create.mousePressEvent = self.setWriteOffsCreatePage
        self.writeOff_create_back.mousePressEvent = self.setWriteOffsMainPage
        self.writeOff_create_delete.mousePressEvent = self.writeOffsCreateDelete
        self.pushButton_15.clicked.connect(self.writeOffsCreateSave)
        self.pushButton_16.clicked.connect(self.writeOffsCreateClose)
        self.writeOffs_main_table.itemDoubleClicked.connect(self.setUpWrireOffsCreatePage)
        # Employees
        self.employees_main_create.mousePressEvent = self.setEmployeesCreatePage
        self.employees_create_back.mousePressEvent = self.setEmployeesMainPage
        self.employees_create_delete.mousePressEvent = self.employeesCreateDelete
        self.employees_create_close.clicked.connect(self.employeesCreateClose)
        self.employees_create_save.clicked.connect(self.employeesCreateSave)
        self.employees_main_table.itemDoubleClicked.connect(self.setUpEmployeesCreatePage)
    # Items
    def setItemsMainPage(self, event):
        self.items_stackedWidget.setCurrentIndex(0)
    def setItemsCreatePage(self, event):
        self.items_stackedWidget.setCurrentIndex(1)
    def itemsCreateClose(self):
        self.items_stackedWidget.setCurrentIndex(0)
    def itemsCreateSave(self):
        self.items_stackedWidget.setCurrentIndex(0)
    def itemsCreateDelete(self, event):
        self.items_stackedWidget.setCurrentIndex(0)
    def setUpItemsCreatePage(self):
        row = self.itemsData[self.itemsCurrentRow]
        self.items_create_fieldItem_lineEdit.setText(row['name'])
        self.items_create_descr_textEdit.setText(row['description'])
        self.items_create_category_comboBox.setCurrentText(row['category'])
        self.items_create_manufact_comboBox.setCurrentText(row['manufacturer'])
        self.items_create_edizm_ComboBox.setCurrentText(row['unit'])
        self.items_create_price_lineEdit.setText(str(row['price']))
        self.items_stackedWidget.setCurrentIndex(1)

    # Sells
    def setStockMainPage(self, event):
        self.stock_stackedWidget.setCurrentIndex(0)
    def setStockCreatePage(self, event):
        self.stock_stackedWidget.setCurrentIndex(1)
    def stockCreateClose(self):
        self.stock_stackedWidget.setCurrentIndex(0)
    def stockCreateSave(self):
        self.stock_stackedWidget.setCurrentIndex(0)
    def stockCreateDelete(self, event):
        self.stock_stackedWidget.setCurrentIndex(0)

    def setOrdersMainPage(self, event):
        self.orders_stackedWidget.setCurrentIndex(0)
    def setOrdersCreatePage(self, event):
        self.ordersCurrentRow = None
        self.orders_create_header.setText('Создание заказа')
        self.orders_create_login_lineEdit.setText('')
        self.orders_create_status_combobox.setCurrentText('Создан')
        self.clearOrdersInCreationPage()
        self.showOrdersList([])
        self.showNewItemCreationInOrderPage()
        self.orders_create_table_manufac.setText('')
        self.orders_create_table_insys.setText('')
        self.orders_create_inorder.setText('')
        self.orders_stackedWidget.setCurrentIndex(1)
    def ordersCreateClose(self, event):
        self.orders_stackedWidget.setCurrentIndex(0)
    def ordersCreateDelete(self, event):
        self.orders_stackedWidget.setCurrentIndex(0)
    def ordersCreateSave(self, event):
        self.orders_stackedWidget.setCurrentIndex(0)
    def setUpOrdersCreatePage(self):
        self.clearOrdersInCreationPage()
        row = self.ordersData[self.ordersCurrentRow]
        self.orders_create_header.setText('Заказ ' + str(row['id']))
        self.orders_create_login_lineEdit.setText(row['address'])
        self.orders_create_status_combobox.setCurrentText(row['status'])
        self.showOrdersList(row['items'])
        self.showNewItemCreationInOrderPage()
        self.orders_stackedWidget.setCurrentIndex(1)

    def setReturnsMainPage(self, event):
        self.returns_stackedWidget.setCurrentIndex(0)
    def setReturnsCreatePage(self, event):
        self.returns_create_order_lineEdit.setEnabled(True)
        self.returnsCurrentRow = None
        self.clearReturnsCreatePage()
        self.returns_create_item = QtWidgets.QLabel(self.returns_create)
        self.returns_create_item.setGeometry(QtCore.QRect(60, 230, 670, 17))

        self.returns_create_order_lineEdit.setText('')
        self.returns_create_cause_comboBox.setCurrentText('Не выбрано')
        self.returns_create_header.setText('Создание возврата')
        self.returns_create_item.setObjectName("returns_create_item")
        self.returns_create_item.setText("Для оформления возврата сперва найдите нужный заказ")
        self.returns_create_manufac.setText("")
        self.returns_create_inorder.setText("")
        self.returns_create_return.setText("")
        self.returns_stackedWidget.setCurrentIndex(1)
    def returnsCreateClose(self):
        self.returns_stackedWidget.setCurrentIndex(0)
    def returnsCreateDelete(self, event):
        self.returns_stackedWidget.setCurrentIndex(0)
    def returnsCreateSave(self):
        self.returns_stackedWidget.setCurrentIndex(0)
    def setUpReturnsPage(self):
        self.returns_create_order_lineEdit.setEnabled(False)
        self.clearReturnsCreatePage()
        self.showListOfReturns(self.returnsData[self.returnsCurrentRow])
        self.returns_stackedWidget.setCurrentIndex(1)

    def setGetStocksMainPage(self, event):
        self.getStocks_stackedWidget.setCurrentIndex(0)
    def setGetStocksCreatePage(self, event):
        self.getStocksCurrentRow = None
        self.clearGetStocksInCreationPage()
        self.showListOfGetStocks([])
        self.showItemCreationInGetStocksPage()
        self.getStocks_create_header.setText('Новое оприходвание')
        self.getStocks_stackedWidget.setCurrentIndex(1)
    def getStocksCreateClose(self):
        self.getStocks_stackedWidget.setCurrentIndex(0)
    def getStocksCreateDelete(self):
        self.getStocks_stackedWidget.setCurrentIndex(0)
    def getStocksCreateSave(self):
        self.getStocks_stackedWidget.setCurrentIndex(0)
    def setUpGetStocksCreatePage(self):
        self.clearGetStocksInCreationPage()
        self.showListOfGetStocks(self.getStocksData[self.getStocksCurrentRow]['items'])
        self.showItemCreationInGetStocksPage()
        self.getStocks_create_header.setText('Оприходование ' + str(self.getStocksData[self.getStocksCurrentRow]['id']))
        self.getStocks_stackedWidget.setCurrentIndex(1)

    def setWriteOffsMainPage(self, event):
        self.writeOffs_stackedWidget.setCurrentIndex(0)
    def setWriteOffsCreatePage(self, event):
        self.writeOffsCurrentRow = None
        self.page_header_6.setText('Новое списание')
        self.writeOff_create_cause_lineEdit.setText('')
        self.writeOff_create_item_lineEdit.setText('')
        self.writeOff_create_manufac_lineEdit.setText('')
        self.writeOff_create_amount_spinbox.setValue(0)
        self.writeOffs_stackedWidget.setCurrentIndex(1)
    def writeOffsCreateClose(self, event):
        self.writeOffs_stackedWidget.setCurrentIndex(0)
    def writeOffsCreateDelete(self, event):
        self.writeOffs_stackedWidget.setCurrentIndex(0)
    def writeOffsCreateSave(self, event):
        self.writeOffs_stackedWidget.setCurrentIndex(0)
    def setUpWrireOffsCreatePage(self):
        currentElement = self.writeOffsData[self.writeOffsCurrentRow]
        self.page_header_6.setText('Списание ' + str(currentElement['id']))
        self.writeOff_create_cause_lineEdit.setText(currentElement['cause'])
        self.writeOff_create_item_lineEdit.setText(currentElement['itemName'])
        self.writeOff_create_manufac_lineEdit.setText(currentElement['manufacturer'])
        self.writeOff_create_amount_spinbox.setValue(currentElement['amount'])
        self.writeOffs_stackedWidget.setCurrentIndex(1)

    def setEmployeesMainPage(self, event):
        self.employees_stackedWidget.setCurrentIndex(0)
    def setEmployeesCreatePage(self, event):
        self.itemsCurrentRow = None
        self.employeesCurrentRow = None
        self.employees_create_surname_lineEdit.setText('')
        self.employees_create_name_lineEdit.setText('')
        self.employees_create_patronymic_lineedit.setText('')
        self.employees_create_role_combobox.setCurrentText('')
        self.employees_create_number_lineedit.setText('')
        self.employees_create_user_lineedit.setText('')
        self.employees_create_password_lineedit.setText('')
        self.employees_create_sex_male.setChecked(False)
        self.employees_create_sex_female.setChecked(False)
        self.employees_create_header.setText("Добавление сотрудника")
        self.employees_stackedWidget.setCurrentIndex(1)
    def employeesCreateClose(self, event):
        self.employees_stackedWidget.setCurrentIndex(0)
    def employeesCreateDelete(self, event):
        self.employees_stackedWidget.setCurrentIndex(0)
    def employeesCreateSave(self, event):
        self.employees_stackedWidget.setCurrentIndex(0)
    def setUpEmployeesCreatePage(self):
        row = self.employeesData[self.employeesCurrentRow]
        self.employees_create_surname_lineEdit.setText(row['surname'])
        self.employees_create_name_lineEdit.setText(row['name'])
        self.employees_create_patronymic_lineedit.setText(row['patronymic'])
        self.employees_create_role_combobox.setCurrentText(row['role'])
        self.employees_create_number_lineedit.setText(row['number'])
        self.employees_create_user_lineedit.setText(row['username'])
        self.employees_create_password_lineedit.setText(row['password'])
        self.employees_create_sex_male.setChecked(row['sex'] == 'male')
        self.employees_create_sex_female.setChecked(row['sex'] == 'female')
        self.employees_create_header.setText('Сотрудник ' + str(row['id']))
        self.employees_stackedWidget.setCurrentIndex(1)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        StockPage.retranslateUi(self)
        OrdersPage.retranslateUi(self)
        ReturnsPage.retranslateUi(self)
        GetStocksPage.retranslateUi(self)
        WriteOffsPage.retranslateUi(self)

        self.items_main_search_lineEdit.setPlaceholderText(_translate("MainWindow", "Найти..."))
        item = self.items_main_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код товара"))
        item = self.items_main_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.items_main_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Производитель"))
        item = self.items_main_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Категория"))
        item = self.items_main_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.items_main_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Ед. изм."))
        item = self.items_main_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Цена"))
        self.items_create_header.setText(_translate("MainWindow", "Код товара: 12312"))
        self.items_create_fieldItemHeader.setText(_translate("MainWindow", "Наименование товара"))
        self.items_create_fieldItem_lineEdit.setPlaceholderText(_translate("MainWindow", "Введите наименование товара"))
        self.items_create_descr_textEdit.setPlaceholderText(_translate("MainWindow", "Введите описание"))
        self.items_create_descr_header.setText(_translate("MainWindow", "Описание товара"))
        self.items_create_saveBtn.setText(_translate("MainWindow", "СОХРАНИТЬ"))
        self.items_create_closeBtn.setText(_translate("MainWindow", "ЗАКРЫТЬ"))
        self.items_create_categoty_hedaer.setText(_translate("MainWindow", "Категория"))
        self.items_create_category_comboBox.setPlaceholderText(_translate("MainWindow", "Выберите"))
        self.items_create_manufact_header.setText(_translate("MainWindow", "Производитель"))
        self.items_create_manufact_comboBox.setPlaceholderText(_translate("MainWindow", "Выберите"))
        self.items_create_edizm_header.setText(_translate("MainWindow", "Ед. измерения"))
        self.items_create_edizm_ComboBox.setPlaceholderText(_translate("MainWindow", "Выберите"))
        self.items_create_edizm_ComboBox.setItemText(0, _translate("MainWindow", "Шт"))
        self.items_create_price_header.setText(_translate("MainWindow", "Цена"))
        self.items_create_price_lineEdit.setPlaceholderText(_translate("MainWindow", "Введите цену"))

        self.main_tab.setTabText(self.main_tab.indexOf(self.items), _translate("MainWindow", "Товары"))

        self.sells_tab.setTabText(self.sells_tab.indexOf(self.stock), _translate("MainWindow", "Товары на реализации"))
        self.sells_tab.setTabText(self.sells_tab.indexOf(self.orders), _translate("MainWindow", "Заказы"))
        self.sells_tab.setTabText(self.sells_tab.indexOf(self.returns), _translate("MainWindow", "Возвраты"))
        self.sells_tab.setTabText(self.sells_tab.indexOf(self.getStocks), _translate("MainWindow", "Оприходования"))
        self.sells_tab.setTabText(self.sells_tab.indexOf(self.writeOffs), _translate("MainWindow", "Списания"))

        self.main_tab.setTabText(self.main_tab.indexOf(self.sells), _translate("MainWindow", "Продажи"))

        self.watch_search_lineEdit.setPlaceholderText(_translate("MainWindow", "Найти..."))
        item = self.watch_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код изменения"))
        item = self.watch_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Действие"))
        item = self.watch_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Сотрудник"))
        item = self.watch_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата и время"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.watch), _translate("MainWindow", "Отслеживание"))
        item = self.employees_main_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код сотрудника"))
        item = self.employees_main_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.employees_main_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.employees_main_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Отчество"))
        item = self.employees_main_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Роль"))
        item = self.employees_main_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Номер"))
        self.employees_main_search_lineEdit.setPlaceholderText(_translate("MainWindow", "Найти..."))
        self.employees_create_header.setText(_translate("MainWindow", "Добавление сотрудника"))
        self.employees_create_save.setText(_translate("MainWindow", "СОХРАНИТЬ"))
        self.employees_create_close.setText(_translate("MainWindow", "ЗАКРЫТЬ"))
        self.employees_create_surname_header.setText(_translate("MainWindow", "Фамилия"))
        self.employees_create_surname_lineEdit.setPlaceholderText(_translate("MainWindow", "Введите фамилию"))
        self.employees_create_name_header.setText(_translate("MainWindow", "Имя"))
        self.employees_create_name_lineEdit.setPlaceholderText(_translate("MainWindow", "Введите имя"))
        self.employees_create_patronymic_label.setText(_translate("MainWindow", "Отчество"))
        self.employees_create_patronymic_lineedit.setPlaceholderText(_translate("MainWindow", "Введите отчество"))
        self.employees_create_role_label.setText(_translate("MainWindow", "Роль"))
        self.employees_create_role_combobox.setPlaceholderText(_translate("MainWindow", "Выберите"))
        self.employees_create_role_combobox.setItemText(0, _translate("MainWindow", "Сотрудник"))
        self.employees_create_role_combobox.setItemText(1, _translate("MainWindow", "Администратор"))
        self.employees_create_number_label.setText(_translate("MainWindow", "Номер телефона"))
        self.employees_create_number_lineedit.setPlaceholderText(_translate("MainWindow", "Введите номер телефона"))
        self.employees_create_user_header.setText(_translate("MainWindow", "Имя пользователя"))
        self.employees_create_user_lineedit.setPlaceholderText(_translate("MainWindow", "Введите имя пользователя"))
        self.employees_create_password_header.setText(_translate("MainWindow", "Пароль"))
        self.employees_create_password_lineedit.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
        self.employees_create_sex_male.setText(_translate("MainWindow", "(Мужчина)"))
        self.employees_create_sex.setText(_translate("MainWindow", "Пол"))
        self.employees_create_sex_female.setText(_translate("MainWindow", "(Женщина)"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.employees), _translate("MainWindow", "Сотрудники"))