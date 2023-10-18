from PyQt5 import QtCore, QtGui, QtWidgets


class MainPage(object):
    def __init__(self):
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
        self.items_main_table = QtWidgets.QTableWidget(self.items_main)
        self.items_main_table.setGeometry(QtCore.QRect(70, 150, 1300, 700))
        self.items_main_table.setAlternatingRowColors(False)
        self.items_main_table.setColumnCount(7)
        self.items_main_table.setObjectName("items_main_table")
        self.items_main_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.items_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_main_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_main_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_main_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_main_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_main_table.setHorizontalHeaderItem(6, item)
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

        # Start of stock

        self.stock = QtWidgets.QWidget()
        self.stock.setObjectName("stock")
        self.stock_stackedWidget = QtWidgets.QStackedWidget(self.stock)
        self.stock_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 891))
        self.stock_stackedWidget.setObjectName("stock_stackedWidget")
        self.stock_main = QtWidgets.QWidget()
        self.stock_main.setObjectName("stock_main")
        self.stock_main_table = QtWidgets.QTableWidget(self.stock_main)
        self.stock_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.stock_main_table.setRowCount(0)
        self.stock_main_table.setObjectName("stock_main_table")
        self.stock_main_table.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.stock_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stock_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stock_main_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.stock_main_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.stock_main_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.stock_main_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.stock_main_table.setHorizontalHeaderItem(6, item)
        self.stock_main_createBtn = QtWidgets.QLabel(self.stock_main)
        self.stock_main_createBtn.setGeometry(QtCore.QRect(1100, 50, 262, 20))
        self.stock_main_createBtn.setText("")
        self.stock_main_createBtn.setPixmap(QtGui.QPixmap("assets/new_invvent.png"))
        self.stock_main_createBtn.setObjectName("stock_main_createBtn")
        self.stock_main_lineEdit = QtWidgets.QLineEdit(self.stock_main)
        self.stock_main_lineEdit.setGeometry(QtCore.QRect(60, 40, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.stock_main_lineEdit.setFont(font)
        self.stock_main_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                               "font: 25 10pt \"Ubuntu\";\n"
                                               "padding: 5px;\n"
                                               "padding-right: 35px;\n"
                                               "border-radius: 8px;\n"
                                               "border-color: rgb(66, 66, 66);\n"
                                               "background-color: rgb(52, 52, 52);")
        self.stock_main_lineEdit.setText("")
        self.stock_main_lineEdit.setObjectName("stock_main_lineEdit")
        self.stock_main_searchImg = QtWidgets.QLabel(self.stock_main)
        self.stock_main_searchImg.setGeometry(QtCore.QRect(430, 50, 18, 18))
        self.stock_main_searchImg.setStyleSheet("background: none")
        self.stock_main_searchImg.setText("")
        self.stock_main_searchImg.setPixmap(QtGui.QPixmap("assets/search.png"))
        self.stock_main_searchImg.setObjectName("stock_main_searchImg")
        self.stock_main_lineEdit.raise_()
        self.stock_main_table.raise_()
        self.stock_main_createBtn.raise_()
        self.stock_main_searchImg.raise_()
        self.stock_stackedWidget.addWidget(self.stock_main)
        self.stock_create = QtWidgets.QWidget()
        self.stock_create.setObjectName("stock_create")
        self.stock_create_backBtn = QtWidgets.QLabel(self.stock_create)
        self.stock_create_backBtn.setGeometry(QtCore.QRect(60, 50, 91, 22))
        self.stock_create_backBtn.setText("")
        self.stock_create_backBtn.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.stock_create_backBtn.setObjectName("stock_create_backBtn")
        self.stock_create_header = QtWidgets.QLabel(self.stock_create)
        self.stock_create_header.setGeometry(QtCore.QRect(170, 50, 251, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stock_create_header.setFont(font)
        self.stock_create_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.stock_create_header.setObjectName("stock_create_header")
        self.stock_create_scrollArea = QtWidgets.QScrollArea(self.stock_create)
        self.stock_create_scrollArea.setGeometry(QtCore.QRect(60, 270, 1291, 551))
        self.stock_create_scrollArea.setStyleSheet("QScrollArea {\n"
                                                   "    border: none;\n"
                                                   "}")
        self.stock_create_scrollArea.setWidgetResizable(True)
        self.stock_create_scrollArea.setObjectName("stock_create_scrollArea")
        self.stock_create_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.stock_create_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1277, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_create_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.stock_create_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.stock_create_scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 800))
        self.stock_create_scrollAreaWidgetContents.setObjectName("stock_create_scrollAreaWidgetContents")
        self.stock_create_table_item1 = QtWidgets.QWidget(self.stock_create_scrollAreaWidgetContents)
        self.stock_create_table_item1.setGeometry(QtCore.QRect(0, 0, 1300, 35))
        self.stock_create_table_item1.setMinimumSize(QtCore.QSize(0, 0))
        self.stock_create_table_item1.setObjectName("stock_create_table_item1")
        self.stock_create_table_checkbox = QtWidgets.QCheckBox(self.stock_create_table_item1)
        self.stock_create_table_checkbox.setGeometry(QtCore.QRect(0, 0, 35, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_create_table_checkbox.sizePolicy().hasHeightForWidth())
        self.stock_create_table_checkbox.setSizePolicy(sizePolicy)
        self.stock_create_table_checkbox.setMinimumSize(QtCore.QSize(0, 0))
        self.stock_create_table_checkbox.setStyleSheet("QCheckBox::indicator { \n"
                                                       "    width: 35px; \n"
                                                       "    height: 35px;\n"
                                                       "}\n"
                                                       "QCheckBox {\n"
                                                       "    background-color: rgb(91, 91, 91);\n"
                                                       "    border-color: rgb(66, 66, 66);\n"
                                                       "    border-radius: 6px;\n"
                                                       "}")
        self.stock_create_table_checkbox.setText("")
        self.stock_create_table_checkbox.setIconSize(QtCore.QSize(40, 40))
        self.stock_create_table_checkbox.setChecked(False)
        self.stock_create_table_checkbox.setObjectName("stock_create_table_checkbox")
        self.stock_create_table_name_lineEdit = QtWidgets.QLineEdit(self.stock_create_table_item1)
        self.stock_create_table_name_lineEdit.setEnabled(False)
        self.stock_create_table_name_lineEdit.setGeometry(QtCore.QRect(40, 0, 580, 35))
        self.stock_create_table_name_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stock_create_table_name_lineEdit.setFont(font)
        self.stock_create_table_name_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                            "border-color: rgb(66, 66, 66);\n"
                                                            "background-color:rgb(71, 71, 71);\n"
                                                            "border-radius: 8px;\n"
                                                            "padding: 5px;")
        self.stock_create_table_name_lineEdit.setText("")
        self.stock_create_table_name_lineEdit.setObjectName("stock_create_table_name_lineEdit")
        self.stock_create_table_manufac_lineEdit = QtWidgets.QLineEdit(self.stock_create_table_item1)
        self.stock_create_table_manufac_lineEdit.setEnabled(False)
        self.stock_create_table_manufac_lineEdit.setGeometry(QtCore.QRect(630, 0, 275, 35))
        self.stock_create_table_manufac_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stock_create_table_manufac_lineEdit.setFont(font)
        self.stock_create_table_manufac_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                               "border-color: rgb(66, 66, 66);\n"
                                                               "background-color: rgb(71, 71, 71);\n"
                                                               "border-radius: 8px;\n"
                                                               "padding: 5px;")
        self.stock_create_table_manufac_lineEdit.setText("")
        self.stock_create_table_manufac_lineEdit.setObjectName("stock_create_table_manufac_lineEdit")
        self.stock_create_table_item1_insys = QtWidgets.QLineEdit(self.stock_create_table_item1)
        self.stock_create_table_item1_insys.setEnabled(False)
        self.stock_create_table_item1_insys.setGeometry(QtCore.QRect(920, 0, 110, 35))
        self.stock_create_table_item1_insys.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stock_create_table_item1_insys.setFont(font)
        self.stock_create_table_item1_insys.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "background-color: rgb(71, 71, 71);\n"
                                                          "border-radius: 8px;\n"
                                                          "padding: 5px;")
        self.stock_create_table_item1_insys.setText("")
        self.stock_create_table_item1_insys.setAlignment(QtCore.Qt.AlignCenter)
        self.stock_create_table_item1_insys.setObjectName("stock_create_table_item1_insys")
        self.stock_create_fact = QtWidgets.QSpinBox(self.stock_create_table_item1)
        self.stock_create_fact.setGeometry(QtCore.QRect(1040, 0, 110, 35))
        self.stock_create_fact.setStyleSheet("\n"
                                             "background-color:rgb(91, 91, 91);\n"
                                             "color: rgb(217, 217, 217);\n"
                                             "border-color: rgb(66, 66, 66);")
        self.stock_create_fact.setAlignment(QtCore.Qt.AlignCenter)
        self.stock_create_fact.setObjectName("stock_create_fact")
        self.stock_create_writeOff_2 = QtWidgets.QSpinBox(self.stock_create_table_item1)
        self.stock_create_writeOff_2.setGeometry(QtCore.QRect(1160, 0, 110, 35))
        self.stock_create_writeOff_2.setStyleSheet("\n"
                                                   "background-color:rgb(91, 91, 91);\n"
                                                   "color: rgb(217, 217, 217);")
        self.stock_create_writeOff_2.setAlignment(QtCore.Qt.AlignCenter)
        self.stock_create_writeOff_2.setObjectName("stock_create_writeOff_2")
        self.stock_create_scrollArea.setWidget(self.stock_create_scrollAreaWidgetContents)
        self.stock_create_search_lineEdit = QtWidgets.QLineEdit(self.stock_create)
        self.stock_create_search_lineEdit.setGeometry(QtCore.QRect(60, 120, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.stock_create_search_lineEdit.setFont(font)
        self.stock_create_search_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                        "font: 25 10pt \"Ubuntu\";\n"
                                                        "padding: 5px;\n"
                                                        "padding-right: 35px;\n"
                                                        "border-radius: 8px;\n"
                                                        "border-color: rgb(66, 66, 66);\n"
                                                        "background-color: rgb(52, 52, 52);")
        self.stock_create_search_lineEdit.setText("")
        self.stock_create_search_lineEdit.setObjectName("stock_create_search_lineEdit")
        self.stock_create_searchImg = QtWidgets.QLabel(self.stock_create)
        self.stock_create_searchImg.setGeometry(QtCore.QRect(430, 130, 18, 18))
        self.stock_create_searchImg.setStyleSheet("background: none")
        self.stock_create_searchImg.setText("")
        self.stock_create_searchImg.setPixmap(QtGui.QPixmap("assets/search.png"))
        self.stock_create_searchImg.setObjectName("stock_create_searchImg")
        self.stock_create_actions = QtWidgets.QWidget(self.stock_create)
        self.stock_create_actions.setGeometry(QtCore.QRect(800, 80, 191, 80))
        self.stock_create_actions.setObjectName("stock_create_actions")
        self.stock_create_actions_combobox = QtWidgets.QComboBox(self.stock_create_actions)
        self.stock_create_actions_combobox.setGeometry(QtCore.QRect(0, 40, 191, 35))
        self.stock_create_actions_combobox.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                                         "border-color: rgb(66, 66, 66);\n"
                                                         "border-radius: 8px;")
        self.stock_create_actions_combobox.setObjectName("stock_create_actions_combobox")
        self.stock_create_actions_combobox.addItem("")
        self.stock_create_actions_combobox.addItem("")
        self.stock_create_actions_combobox.addItem("")
        self.stock_create_actions_combobox.addItem("")
        self.stock_create_saveBtn = QtWidgets.QPushButton(self.stock_create)
        self.stock_create_saveBtn.setGeometry(QtCore.QRect(1000, 120, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stock_create_saveBtn.setFont(font)
        self.stock_create_saveBtn.setStyleSheet("QPushButton {\n"
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
        self.stock_create_saveBtn.setObjectName("stock_create_saveBtn")
        self.stock_create_deleteImg = QtWidgets.QLabel(self.stock_create)
        self.stock_create_deleteImg.setGeometry(QtCore.QRect(1320, 120, 35, 35))
        self.stock_create_deleteImg.setStyleSheet("QLabel:hover {\n"
                                                  "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                  "    color: rgb(52, 52, 52);\n"
                                                  "}")
        self.stock_create_deleteImg.setText("")
        self.stock_create_deleteImg.setPixmap(QtGui.QPixmap("assets/delete_button.png"))
        self.stock_create_deleteImg.setObjectName("stock_create_deleteImg")
        self.stock_create_closeBtn = QtWidgets.QPushButton(self.stock_create)
        self.stock_create_closeBtn.setGeometry(QtCore.QRect(1160, 120, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stock_create_closeBtn.setFont(font)
        self.stock_create_closeBtn.setStyleSheet("QPushButton {\n"
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
        self.stock_create_closeBtn.setObjectName("stock_create_closeBtn")
        self.stock_create_table_item = QtWidgets.QLabel(self.stock_create)
        self.stock_create_table_item.setGeometry(QtCore.QRect(100, 240, 67, 17))
        self.stock_create_table_item.setObjectName("stock_create_table_item")
        self.stock_create_table_manufact = QtWidgets.QLabel(self.stock_create)
        self.stock_create_table_manufact.setGeometry(QtCore.QRect(690, 240, 121, 17))
        self.stock_create_table_manufact.setObjectName("stock_create_table_manufact")
        self.stock_create_table_insys = QtWidgets.QLabel(self.stock_create)
        self.stock_create_table_insys.setGeometry(QtCore.QRect(980, 240, 111, 17))
        self.stock_create_table_insys.setAlignment(QtCore.Qt.AlignCenter)
        self.stock_create_table_insys.setObjectName("stock_create_table_insys")
        self.stock_create_table_fact = QtWidgets.QLabel(self.stock_create)
        self.stock_create_table_fact.setGeometry(QtCore.QRect(1100, 240, 101, 17))
        self.stock_create_table_fact.setAlignment(QtCore.Qt.AlignCenter)
        self.stock_create_table_fact.setObjectName("stock_create_table_fact")
        self.stock_create_writeOff = QtWidgets.QLabel(self.stock_create)
        self.stock_create_writeOff.setGeometry(QtCore.QRect(1220, 240, 101, 17))
        self.stock_create_writeOff.setAlignment(QtCore.Qt.AlignCenter)
        self.stock_create_writeOff.setObjectName("stock_create_writeOff")
        self.stock_create_tip = QtWidgets.QLabel(self.stock_create)
        self.stock_create_tip.setGeometry(QtCore.QRect(60, 190, 491, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stock_create_tip.setFont(font)
        self.stock_create_tip.setStyleSheet("color: rgba(217, 217, 217, 0.5);")
        self.stock_create_tip.setObjectName("stock_create_tip")
        self.stock_stackedWidget.addWidget(self.stock_create)

        # End of stock

        self.sells_tab.addTab(self.stock, "")

        # Start of orders

        self.orders = QtWidgets.QWidget()
        self.orders.setObjectName("orders")
        self.orders_stackedWidget = QtWidgets.QStackedWidget(self.orders)
        self.orders_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 911))
        self.orders_stackedWidget.setObjectName("orders_stackedWidget")
        self.orders_main = QtWidgets.QWidget()
        self.orders_main.setObjectName("orders_main")
        self.orders_main_table = QtWidgets.QTableWidget(self.orders_main)
        self.orders_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.orders_main_table.setObjectName("orders_main_table")
        self.orders_main_table.setColumnCount(4)
        self.orders_main_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.orders_main_table.setHorizontalHeaderItem(3, item)
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
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_status_combobox.addItem("")
        self.orders_create_scrollArea = QtWidgets.QScrollArea(self.orders_create)
        self.orders_create_scrollArea.setGeometry(QtCore.QRect(60, 260, 1300, 611))
        self.orders_create_scrollArea.setStyleSheet("QScrollArea {\n"
                                                    "    border: none;\n"
                                                    "}")
        self.orders_create_scrollArea.setWidgetResizable(True)
        self.orders_create_scrollArea.setObjectName("orders_create_scrollArea")
        self.orders_create_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.orders_create_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1286, 800))
        self.orders_create_scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 800))
        self.orders_create_scrollAreaWidgetContents.setObjectName("orders_create_scrollAreaWidgetContents")
        self.orders_create_item1 = QtWidgets.QWidget(self.orders_create_scrollAreaWidgetContents)
        self.orders_create_item1.setGeometry(QtCore.QRect(0, 10, 1300, 35))
        self.orders_create_item1.setMinimumSize(QtCore.QSize(0, 0))
        self.orders_create_item1.setObjectName("orders_create_item1")
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
        self.orders_create_item1_name.setObjectName("orders_create_item1_name")
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
        self.orders_create_item1_manufac.setObjectName("orders_create_item1_manufac")
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
        self.orders_create_item1_insys.setObjectName("orders_create_item1_insys")
        self.orders_create_item1_inorder = QtWidgets.QSpinBox(self.orders_create_item1)
        self.orders_create_item1_inorder.setGeometry(QtCore.QRect(1120, 0, 110, 35))
        self.orders_create_item1_inorder.setStyleSheet("\n"
                                                       "background-color:rgb(91, 91, 91);\n"
                                                       "color: rgb(217, 217, 217);\n"
                                                       "border-color: rgb(66, 66, 66);")
        self.orders_create_item1_inorder.setAlignment(QtCore.Qt.AlignCenter)
        self.orders_create_item1_inorder.setObjectName("orders_create_item1_inorder")
        self.orders_create_item1_close = QtWidgets.QLabel(self.orders_create_item1)
        self.orders_create_item1_close.setGeometry(QtCore.QRect(1240, 0, 35, 35))
        self.orders_create_item1_close.setStyleSheet("QLabel:hover {\n"
                                                     "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                     "    color: rgb(52, 52, 52);\n"
                                                     "}")
        self.orders_create_item1_close.setText("")
        self.orders_create_item1_close.setPixmap(QtGui.QPixmap("assets/X.png"))
        self.orders_create_item1_close.setObjectName("orders_create_item1_close")
        self.orders_create_newItem = QtWidgets.QWidget(self.orders_create_scrollAreaWidgetContents)
        self.orders_create_newItem.setGeometry(QtCore.QRect(0, 60, 1281, 35))
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
        self.orders_create_newItem_amount = QtWidgets.QSpinBox(self.orders_create_newItem)
        self.orders_create_newItem_amount.setGeometry(QtCore.QRect(1050, 0, 110, 35))
        self.orders_create_newItem_amount.setStyleSheet("\n"
                                                        "background-color:rgb(91, 91, 91);\n"
                                                        "color: rgb(217, 217, 217);\n"
                                                        "border-color: rgb(66, 66, 66);")
        self.orders_create_newItem_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.orders_create_newItem_amount.setObjectName("orders_create_newItem_amount")
        self.orders_create_scrollArea.setWidget(self.orders_create_scrollAreaWidgetContents)
        self.orders_create_table_name = QtWidgets.QLabel(self.orders_create)
        self.orders_create_table_name.setGeometry(QtCore.QRect(60, 240, 67, 17))
        self.orders_create_table_name.setObjectName("orders_create_table_name")
        self.orders_create_table_manufac = QtWidgets.QLabel(self.orders_create)
        self.orders_create_table_manufac.setGeometry(QtCore.QRect(700, 240, 141, 17))
        self.orders_create_table_manufac.setObjectName("orders_create_table_manufac")
        self.orders_create_table_insys = QtWidgets.QLabel(self.orders_create)
        self.orders_create_table_insys.setGeometry(QtCore.QRect(1060, 240, 111, 17))
        self.orders_create_table_insys.setAlignment(QtCore.Qt.AlignCenter)
        self.orders_create_table_insys.setObjectName("orders_create_table_insys")
        self.orders_create_inorder = QtWidgets.QLabel(self.orders_create)
        self.orders_create_inorder.setGeometry(QtCore.QRect(1180, 240, 111, 17))
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

        # End of orders

        self.sells_tab.addTab(self.orders, "")

        # Start of returns

        self.returns = QtWidgets.QWidget()
        self.returns.setObjectName("returns")
        self.returns_stackedWidget = QtWidgets.QStackedWidget(self.returns)
        self.returns_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 891))
        self.returns_stackedWidget.setObjectName("returns_stackedWidget")
        self.returns_main = QtWidgets.QWidget()
        self.returns_main.setObjectName("returns_main")
        self.returns_main_table = QtWidgets.QTableWidget(self.returns_main)
        self.returns_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.returns_main_table.setObjectName("returns_main_table")
        self.returns_main_table.setColumnCount(4)
        self.returns_main_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.returns_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.returns_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.returns_main_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.returns_main_table.setHorizontalHeaderItem(3, item)
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
        self.returns_create_cause_comboBox.addItem("")
        self.returns_create_cause_comboBox.addItem("")
        self.returns_create_cause_comboBox.addItem("")
        self.returns_create_cause_comboBox.addItem("")
        self.returns_create_cause_comboBox.addItem("")
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
        self.returns_create_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1286, 800))
        self.returns_create_scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 800))
        self.returns_create_scrollAreaWidgetContents.setObjectName("returns_create_scrollAreaWidgetContents")
        self.returns_create_item1 = QtWidgets.QWidget(self.returns_create_scrollAreaWidgetContents)
        self.returns_create_item1.setGeometry(QtCore.QRect(0, 0, 1300, 35))
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
        self.returns_create_scrollArea.setWidget(self.returns_create_scrollAreaWidgetContents)
        self.returns_create_item = QtWidgets.QLabel(self.returns_create)
        self.returns_create_item.setGeometry(QtCore.QRect(60, 230, 67, 17))
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

        # End of returns

        self.sells_tab.addTab(self.returns, "")

        # Start of getStocks

        self.getStocks = QtWidgets.QWidget()
        self.getStocks.setObjectName("getStocks")
        self.getStocks_stackedWidget = QtWidgets.QStackedWidget(self.getStocks)
        self.getStocks_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 891))
        self.getStocks_stackedWidget.setObjectName("getStocks_stackedWidget")
        self.getStocks_main = QtWidgets.QWidget()
        self.getStocks_main.setObjectName("getStocks_main")
        self.getStocks_main_table = QtWidgets.QTableWidget(self.getStocks_main)
        self.getStocks_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.getStocks_main_table.setObjectName("getStocks_main_table")
        self.getStocks_main_table.setColumnCount(3)
        self.getStocks_main_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.getStocks_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.getStocks_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.getStocks_main_table.setHorizontalHeaderItem(2, item)
        self.getStocks_main_createBtn = QtWidgets.QLabel(self.getStocks_main)
        self.getStocks_main_createBtn.setGeometry(QtCore.QRect(1150, 50, 208, 20))
        self.getStocks_main_createBtn.setText("")
        self.getStocks_main_createBtn.setPixmap(QtGui.QPixmap("assets/new_posting.png"))
        self.getStocks_main_createBtn.setObjectName("getStocks_main_createBtn")
        self.getStocks_main_search_lineEdit = QtWidgets.QLineEdit(self.getStocks_main)
        self.getStocks_main_search_lineEdit.setGeometry(QtCore.QRect(60, 40, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.getStocks_main_search_lineEdit.setFont(font)
        self.getStocks_main_search_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                          "font: 25 10pt \"Ubuntu\";\n"
                                                          "padding: 5px;\n"
                                                          "padding-right: 35px;\n"
                                                          "border-radius: 8px;\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "background-color: rgb(52, 52, 52);")
        self.getStocks_main_search_lineEdit.setText("")
        self.getStocks_main_search_lineEdit.setObjectName("getStocks_main_search_lineEdit")
        self.getStocks_main_searchImg = QtWidgets.QLabel(self.getStocks_main)
        self.getStocks_main_searchImg.setGeometry(QtCore.QRect(430, 50, 18, 18))
        self.getStocks_main_searchImg.setStyleSheet("background: none")
        self.getStocks_main_searchImg.setText("")
        self.getStocks_main_searchImg.setPixmap(QtGui.QPixmap("assets/search.png"))
        self.getStocks_main_searchImg.setObjectName("getStocks_main_searchImg")
        self.getStocks_stackedWidget.addWidget(self.getStocks_main)
        self.getStocks_create = QtWidgets.QWidget()
        self.getStocks_create.setObjectName("getStocks_create")
        self.getStocks_create_header = QtWidgets.QLabel(self.getStocks_create)
        self.getStocks_create_header.setGeometry(QtCore.QRect(170, 50, 251, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.getStocks_create_header.setFont(font)
        self.getStocks_create_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.getStocks_create_header.setObjectName("getStocks_create_header")
        self.getStocks_create_backBtn = QtWidgets.QLabel(self.getStocks_create)
        self.getStocks_create_backBtn.setGeometry(QtCore.QRect(60, 50, 91, 22))
        self.getStocks_create_backBtn.setText("")
        self.getStocks_create_backBtn.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.getStocks_create_backBtn.setObjectName("getStocks_create_backBtn")
        self.getStocks_create_scrollArea = QtWidgets.QScrollArea(self.getStocks_create)
        self.getStocks_create_scrollArea.setGeometry(QtCore.QRect(60, 160, 1300, 611))
        self.getStocks_create_scrollArea.setStyleSheet("")
        self.getStocks_create_scrollArea.setWidgetResizable(True)
        self.getStocks_create_scrollArea.setObjectName("getStocks_create_scrollArea")
        self.getStocks_create_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.getStocks_create_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1284, 800))
        self.getStocks_create_scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 800))
        self.getStocks_create_scrollAreaWidgetContents.setObjectName("getStocks_create_scrollAreaWidgetContents")
        self.getStocks_create_item1 = QtWidgets.QWidget(self.getStocks_create_scrollAreaWidgetContents)
        self.getStocks_create_item1.setGeometry(QtCore.QRect(0, 0, 1300, 35))
        self.getStocks_create_item1.setMinimumSize(QtCore.QSize(0, 0))
        self.getStocks_create_item1.setObjectName("getStocks_create_item1")
        self.getStocks_create_item1_name = QtWidgets.QLineEdit(self.getStocks_create_item1)
        self.getStocks_create_item1_name.setEnabled(False)
        self.getStocks_create_item1_name.setGeometry(QtCore.QRect(0, 0, 630, 35))
        self.getStocks_create_item1_name.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getStocks_create_item1_name.setFont(font)
        self.getStocks_create_item1_name.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                       "border-color: rgb(66, 66, 66);\n"
                                                       "background-color:rgb(71, 71, 71);\n"
                                                       "border-radius: 6px;\n"
                                                       "padding: 5px;")
        self.getStocks_create_item1_name.setText("")
        self.getStocks_create_item1_name.setObjectName("getStocks_create_item1_name")
        self.getStocks_create_item1manufac = QtWidgets.QLineEdit(self.getStocks_create_item1)
        self.getStocks_create_item1manufac.setEnabled(False)
        self.getStocks_create_item1manufac.setGeometry(QtCore.QRect(640, 0, 351, 35))
        self.getStocks_create_item1manufac.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getStocks_create_item1manufac.setFont(font)
        self.getStocks_create_item1manufac.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                         "border-color: rgb(66, 66, 66);\n"
                                                         "background-color: rgb(71, 71, 71);\n"
                                                         "border-radius: 6px;\n"
                                                         "padding: 5px;")
        self.getStocks_create_item1manufac.setText("")
        self.getStocks_create_item1manufac.setObjectName("getStocks_create_item1manufac")
        self.getStocks_create_item1_nadlejc = QtWidgets.QSpinBox(self.getStocks_create_item1)
        self.getStocks_create_item1_nadlejc.setGeometry(QtCore.QRect(1120, 0, 110, 35))
        self.getStocks_create_item1_nadlejc.setStyleSheet("\n"
                                                          "background-color:rgb(91, 91, 91);\n"
                                                          "color: rgb(217, 217, 217);\n"
                                                          "border-color: rgb(66, 66, 66);")
        self.getStocks_create_item1_nadlejc.setAlignment(QtCore.Qt.AlignCenter)
        self.getStocks_create_item1_nadlejc.setObjectName("getStocks_create_item1_nadlejc")
        self.getStocks_create_item1_amount = QtWidgets.QSpinBox(self.getStocks_create_item1)
        self.getStocks_create_item1_amount.setGeometry(QtCore.QRect(1000, 0, 110, 35))
        self.getStocks_create_item1_amount.setStyleSheet("\n"
                                                         "background-color:rgb(91, 91, 91);\n"
                                                         "color: rgb(217, 217, 217);\n"
                                                         "border-color: rgb(66, 66, 66);")
        self.getStocks_create_item1_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.getStocks_create_item1_amount.setObjectName("getStocks_create_item1_amount")
        self.getStocks_create_item1_delete = QtWidgets.QLabel(self.getStocks_create_item1)
        self.getStocks_create_item1_delete.setGeometry(QtCore.QRect(1240, 0, 35, 35))
        self.getStocks_create_item1_delete.setStyleSheet("QLabel:hover {\n"
                                                         "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                         "    color: rgb(52, 52, 52);\n"
                                                         "}")
        self.getStocks_create_item1_delete.setText("")
        self.getStocks_create_item1_delete.setPixmap(QtGui.QPixmap("assets/X.png"))
        self.getStocks_create_item1_delete.setObjectName("getStocks_create_item1_delete")
        self.getStocks_create_new = QtWidgets.QWidget(self.getStocks_create_scrollAreaWidgetContents)
        self.getStocks_create_new.setGeometry(QtCore.QRect(0, 50, 1300, 35))
        self.getStocks_create_new.setMinimumSize(QtCore.QSize(0, 0))
        self.getStocks_create_new.setObjectName("getStocks_create_new")
        self.getStocks_create_new_name = QtWidgets.QLineEdit(self.getStocks_create_new)
        self.getStocks_create_new_name.setEnabled(True)
        self.getStocks_create_new_name.setGeometry(QtCore.QRect(0, 0, 991, 35))
        self.getStocks_create_new_name.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getStocks_create_new_name.setFont(font)
        self.getStocks_create_new_name.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                     "border-color: rgb(66, 66, 66);\n"
                                                     "background-color: rgb(91, 91, 91);\n"
                                                     "border-radius: 8px;\n"
                                                     "padding: 5px;")
        self.getStocks_create_new_name.setText("")
        self.getStocks_create_new_name.setObjectName("getStocks_create_new_name")
        self.getStocks_create_new_nadlejc = QtWidgets.QSpinBox(self.getStocks_create_new)
        self.getStocks_create_new_nadlejc.setGeometry(QtCore.QRect(1120, 0, 110, 35))
        self.getStocks_create_new_nadlejc.setStyleSheet("\n"
                                                        "background-color:rgb(91, 91, 91);\n"
                                                        "color: rgb(217, 217, 217);\n"
                                                        "border-color: rgb(66, 66, 66);")
        self.getStocks_create_new_nadlejc.setAlignment(QtCore.Qt.AlignCenter)
        self.getStocks_create_new_nadlejc.setObjectName("getStocks_create_new_nadlejc")
        self.getStocks_create_new_in = QtWidgets.QSpinBox(self.getStocks_create_new)
        self.getStocks_create_new_in.setGeometry(QtCore.QRect(1000, 0, 110, 35))
        self.getStocks_create_new_in.setStyleSheet("\n"
                                                   "background-color:rgb(91, 91, 91);\n"
                                                   "color: rgb(217, 217, 217);\n"
                                                   "border-color: rgb(66, 66, 66);")
        self.getStocks_create_new_in.setAlignment(QtCore.Qt.AlignCenter)
        self.getStocks_create_new_in.setObjectName("getStocks_create_new_in")
        self.getStocks_create_new_ok = QtWidgets.QPushButton(self.getStocks_create_new)
        self.getStocks_create_new_ok.setGeometry(QtCore.QRect(1240, 0, 35, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getStocks_create_new_ok.setFont(font)
        self.getStocks_create_new_ok.setStyleSheet("QPushButton {\n"
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
        self.getStocks_create_new_ok.setObjectName("getStocks_create_new_ok")
        self.getStocks_create_scrollArea.setWidget(self.getStocks_create_scrollAreaWidgetContents)
        self.getStocks_create_save = QtWidgets.QPushButton(self.getStocks_create)
        self.getStocks_create_save.setGeometry(QtCore.QRect(1000, 40, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getStocks_create_save.setFont(font)
        self.getStocks_create_save.setStyleSheet("QPushButton {\n"
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
        self.getStocks_create_save.setObjectName("getStocks_create_save")
        self.getStocks_create_delete = QtWidgets.QLabel(self.getStocks_create)
        self.getStocks_create_delete.setGeometry(QtCore.QRect(1320, 40, 35, 35))
        self.getStocks_create_delete.setStyleSheet("QLabel:hover {\n"
                                                   "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                   "    color: rgb(52, 52, 52);\n"
                                                   "}")
        self.getStocks_create_delete.setText("")
        self.getStocks_create_delete.setPixmap(QtGui.QPixmap("assets/delete_button.png"))
        self.getStocks_create_delete.setObjectName("getStocks_create_delete")
        self.getStocks_create_close = QtWidgets.QPushButton(self.getStocks_create)
        self.getStocks_create_close.setGeometry(QtCore.QRect(1160, 40, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getStocks_create_close.setFont(font)
        self.getStocks_create_close.setStyleSheet("QPushButton {\n"
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
        self.getStocks_create_close.setObjectName("getStocks_create_close")
        self.getStocks_create_nadlejc = QtWidgets.QLabel(self.getStocks_create)
        self.getStocks_create_nadlejc.setGeometry(QtCore.QRect(1180, 130, 111, 17))
        self.getStocks_create_nadlejc.setAlignment(QtCore.Qt.AlignCenter)
        self.getStocks_create_nadlejc.setObjectName("getStocks_create_nadlejc")
        self.getStocks_create_pribilo = QtWidgets.QLabel(self.getStocks_create)
        self.getStocks_create_pribilo.setGeometry(QtCore.QRect(1050, 130, 111, 17))
        self.getStocks_create_pribilo.setAlignment(QtCore.Qt.AlignCenter)
        self.getStocks_create_pribilo.setObjectName("getStocks_create_pribilo")
        self.getStocks_create_item = QtWidgets.QLabel(self.getStocks_create)
        self.getStocks_create_item.setGeometry(QtCore.QRect(60, 130, 67, 17))
        self.getStocks_create_item.setObjectName("getStocks_create_item")
        self.getStocks_create_manufac = QtWidgets.QLabel(self.getStocks_create)
        self.getStocks_create_manufac.setGeometry(QtCore.QRect(700, 130, 141, 17))
        self.getStocks_create_manufac.setObjectName("getStocks_create_manufac")
        self.getStocks_stackedWidget.addWidget(self.getStocks_create)

        # End of getstocks

        self.sells_tab.addTab(self.getStocks, "")

        # Start of writeOffs

        self.writeOffs = QtWidgets.QWidget()
        self.writeOffs.setObjectName("writeOffs")
        self.writeOffs_stackedWidget = QtWidgets.QStackedWidget(self.writeOffs)
        self.writeOffs_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 891))
        self.writeOffs_stackedWidget.setObjectName("writeOffs_stackedWidget")
        self.writeOffs_main = QtWidgets.QWidget()
        self.writeOffs_main.setObjectName("writeOffs_main")
        self.writeOffs_main_table = QtWidgets.QTableWidget(self.writeOffs_main)
        self.writeOffs_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.writeOffs_main_table.setObjectName("writeOffs_main_table")
        self.writeOffs_main_table.setColumnCount(5)
        self.writeOffs_main_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.writeOffs_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.writeOffs_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.writeOffs_main_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.writeOffs_main_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.writeOffs_main_table.setHorizontalHeaderItem(4, item)
        self.writeOffs_main_search = QtWidgets.QLineEdit(self.writeOffs_main)
        self.writeOffs_main_search.setGeometry(QtCore.QRect(60, 40, 401, 35))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.writeOffs_main_search.setFont(font)
        self.writeOffs_main_search.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                 "font: 25 10pt \"Ubuntu\";\n"
                                                 "padding: 5px;\n"
                                                 "padding-right: 35px;\n"
                                                 "border-radius: 8px;\n"
                                                 "border-color: rgb(66, 66, 66);\n"
                                                 "background-color: rgb(52, 52, 52);")
        self.writeOffs_main_search.setText("")
        self.writeOffs_main_search.setObjectName("writeOffs_main_search")
        self.writeOffs_main_searchImg = QtWidgets.QLabel(self.writeOffs_main)
        self.writeOffs_main_searchImg.setGeometry(QtCore.QRect(430, 50, 18, 18))
        self.writeOffs_main_searchImg.setStyleSheet("background: none")
        self.writeOffs_main_searchImg.setText("")
        self.writeOffs_main_searchImg.setPixmap(QtGui.QPixmap("assets/search.png"))
        self.writeOffs_main_searchImg.setObjectName("writeOffs_main_searchImg")
        self.writeOffs_main_create = QtWidgets.QLabel(self.writeOffs_main)
        self.writeOffs_main_create.setGeometry(QtCore.QRect(1200, 50, 160, 20))
        self.writeOffs_main_create.setText("")
        self.writeOffs_main_create.setPixmap(QtGui.QPixmap("assets/new_write-off.png"))
        self.writeOffs_main_create.setObjectName("writeOffs_main_create")
        self.writeOffs_stackedWidget.addWidget(self.writeOffs_main)
        self.writeOff_create = QtWidgets.QWidget()
        self.writeOff_create.setObjectName("writeOff_create")
        self.page_header_6 = QtWidgets.QLabel(self.writeOff_create)
        self.page_header_6.setGeometry(QtCore.QRect(170, 50, 251, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.page_header_6.setFont(font)
        self.page_header_6.setStyleSheet("color: rgb(217, 217, 217);")
        self.page_header_6.setObjectName("page_header_6")
        self.writeOff_create_back = QtWidgets.QLabel(self.writeOff_create)
        self.writeOff_create_back.setGeometry(QtCore.QRect(60, 50, 91, 22))
        self.writeOff_create_back.setText("")
        self.writeOff_create_back.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.writeOff_create_back.setObjectName("writeOff_create_back")
        self.writeOff_create_cause_widget = QtWidgets.QWidget(self.writeOff_create)
        self.writeOff_create_cause_widget.setGeometry(QtCore.QRect(60, 130, 1300, 101))
        self.writeOff_create_cause_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.writeOff_create_cause_widget.setStyleSheet("border: none")
        self.writeOff_create_cause_widget.setObjectName("writeOff_create_cause_widget")
        self.writeOff_create_cause_header = QtWidgets.QLabel(self.writeOff_create_cause_widget)
        self.writeOff_create_cause_header.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.writeOff_create_cause_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.writeOff_create_cause_header.setFont(font)
        self.writeOff_create_cause_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.writeOff_create_cause_header.setObjectName("writeOff_create_cause_header")
        self.writeOff_create_cause_lineEdit = QtWidgets.QLineEdit(self.writeOff_create_cause_widget)
        self.writeOff_create_cause_lineEdit.setGeometry(QtCore.QRect(0, 60, 1301, 35))
        self.writeOff_create_cause_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.writeOff_create_cause_lineEdit.setFont(font)
        self.writeOff_create_cause_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                          "border-color: rgb(66, 66, 66);\n"
                                                          "background-color: rgb(91, 91, 91);\n"
                                                          "border-radius: 8px;\n"
                                                          "padding: 5px;")
        self.writeOff_create_cause_lineEdit.setText("")
        self.writeOff_create_cause_lineEdit.setObjectName("writeOff_create_cause_lineEdit")
        self.writeOff_create_item_widget = QtWidgets.QWidget(self.writeOff_create)
        self.writeOff_create_item_widget.setGeometry(QtCore.QRect(60, 270, 661, 101))
        self.writeOff_create_item_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.writeOff_create_item_widget.setStyleSheet("border: none")
        self.writeOff_create_item_widget.setObjectName("writeOff_create_item_widget")
        self.writeOff_create_item_header = QtWidgets.QLabel(self.writeOff_create_item_widget)
        self.writeOff_create_item_header.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.writeOff_create_item_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.writeOff_create_item_header.setFont(font)
        self.writeOff_create_item_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.writeOff_create_item_header.setObjectName("writeOff_create_item_header")
        self.writeOff_create_item_lineEdit = QtWidgets.QLineEdit(self.writeOff_create_item_widget)
        self.writeOff_create_item_lineEdit.setGeometry(QtCore.QRect(0, 60, 651, 35))
        self.writeOff_create_item_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.writeOff_create_item_lineEdit.setFont(font)
        self.writeOff_create_item_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                         "border-color: rgb(66, 66, 66);\n"
                                                         "background-color: rgb(91, 91, 91);\n"
                                                         "border-radius: 8px;\n"
                                                         "padding: 5px;")
        self.writeOff_create_item_lineEdit.setText("")
        self.writeOff_create_item_lineEdit.setObjectName("writeOff_create_item_lineEdit")
        self.writeOff_create_manufac_widget = QtWidgets.QWidget(self.writeOff_create)
        self.writeOff_create_manufac_widget.setGeometry(QtCore.QRect(730, 270, 451, 101))
        self.writeOff_create_manufac_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.writeOff_create_manufac_widget.setStyleSheet("border: none")
        self.writeOff_create_manufac_widget.setObjectName("writeOff_create_manufac_widget")
        self.writeOff_create_manufac_header = QtWidgets.QLabel(self.writeOff_create_manufac_widget)
        self.writeOff_create_manufac_header.setGeometry(QtCore.QRect(0, 30, 141, 17))
        self.writeOff_create_manufac_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.writeOff_create_manufac_header.setFont(font)
        self.writeOff_create_manufac_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.writeOff_create_manufac_header.setObjectName("writeOff_create_manufac_header")
        self.writeOff_create_manufac_lineEdit = QtWidgets.QLineEdit(self.writeOff_create_manufac_widget)
        self.writeOff_create_manufac_lineEdit.setEnabled(False)
        self.writeOff_create_manufac_lineEdit.setGeometry(QtCore.QRect(0, 60, 451, 35))
        self.writeOff_create_manufac_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.writeOff_create_manufac_lineEdit.setFont(font)
        self.writeOff_create_manufac_lineEdit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                            "border-color: rgb(66, 66, 66);\n"
                                                            "background-color: rgb(66, 66, 66);\n"
                                                            "border-radius: 8px;\n"
                                                            "padding: 5px;")
        self.writeOff_create_manufac_lineEdit.setText("")
        self.writeOff_create_manufac_lineEdit.setObjectName("writeOff_create_manufac_lineEdit")
        self.writeOff_create_amount_widget = QtWidgets.QWidget(self.writeOff_create)
        self.writeOff_create_amount_widget.setGeometry(QtCore.QRect(1190, 270, 171, 101))
        self.writeOff_create_amount_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.writeOff_create_amount_widget.setStyleSheet("")
        self.writeOff_create_amount_widget.setObjectName("writeOff_create_amount_widget")
        self.writeOff_create_amount_header = QtWidgets.QLabel(self.writeOff_create_amount_widget)
        self.writeOff_create_amount_header.setGeometry(QtCore.QRect(0, 30, 151, 17))
        self.writeOff_create_amount_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.writeOff_create_amount_header.setFont(font)
        self.writeOff_create_amount_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.writeOff_create_amount_header.setAlignment(QtCore.Qt.AlignCenter)
        self.writeOff_create_amount_header.setObjectName("writeOff_create_amount_header")
        self.writeOff_create_amount_spinbox = QtWidgets.QSpinBox(self.writeOff_create_amount_widget)
        self.writeOff_create_amount_spinbox.setGeometry(QtCore.QRect(0, 60, 161, 35))
        self.writeOff_create_amount_spinbox.setStyleSheet("\n"
                                                          "background-color:rgb(91, 91, 91);\n"
                                                          "color: rgb(217, 217, 217);\n"
                                                          "border-color: rgb(66, 66, 66);")
        self.writeOff_create_amount_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.writeOff_create_amount_spinbox.setObjectName("writeOff_create_amount_spinbox")
        self.pushButton_15 = QtWidgets.QPushButton(self.writeOff_create)
        self.pushButton_15.setGeometry(QtCore.QRect(1000, 50, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton {\n"
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
        self.pushButton_15.setObjectName("pushButton_15")
        self.writeOff_create_delete = QtWidgets.QLabel(self.writeOff_create)
        self.writeOff_create_delete.setGeometry(QtCore.QRect(1320, 50, 35, 35))
        self.writeOff_create_delete.setStyleSheet("QLabel:hover {\n"
                                                  "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                  "    color: rgb(52, 52, 52);\n"
                                                  "}")
        self.writeOff_create_delete.setText("")
        self.writeOff_create_delete.setPixmap(QtGui.QPixmap("assets/delete_button.png"))
        self.writeOff_create_delete.setObjectName("writeOff_create_delete")
        self.pushButton_16 = QtWidgets.QPushButton(self.writeOff_create)
        self.pushButton_16.setGeometry(QtCore.QRect(1160, 50, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton {\n"
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
        self.pushButton_16.setObjectName("pushButton_16")
        self.writeOffs_stackedWidget.addWidget(self.writeOff_create)

        # End of writeOffs

        self.sells_tab.addTab(self.writeOffs, "")
        self.main_tab.addTab(self.sells, "")

        # End of sells

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
        self.watch_table = QtWidgets.QTableWidget(self.watch)
        self.watch_table.setGeometry(QtCore.QRect(60, 150, 1300, 700))
        self.watch_table.setObjectName("watch_table")
        self.watch_table.setColumnCount(4)
        self.watch_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.watch_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.watch_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.watch_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.watch_table.setHorizontalHeaderItem(3, item)

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
        self.employees_main_table = QtWidgets.QTableWidget(self.employees_main)
        self.employees_main_table.setGeometry(QtCore.QRect(60, 150, 1300, 700))
        self.employees_main_table.setObjectName("employees_main_table")
        self.employees_main_table.setColumnCount(6)
        self.employees_main_table.setRowCount(0)
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
        self.employees_create_role_combobox.addItem("")
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
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_tab.addTab(self.employees, "")

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
        item.setText(_translate("MainWindow", "Новый столбец"))
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
        item = self.stock_main_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код товара"))
        item = self.stock_main_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.stock_main_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Произоводитель"))
        item = self.stock_main_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Категория"))
        item = self.stock_main_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.stock_main_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Количество"))
        item = self.stock_main_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Зарезервировано"))
        self.stock_main_lineEdit.setPlaceholderText(_translate("MainWindow", "Найти..."))
        self.stock_create_header.setText(_translate("MainWindow", "Инвентаризация 12312"))
        self.stock_create_table_name_lineEdit.setPlaceholderText(
            _translate("MainWindow", "Молоко ультра пастеризованное 900 мл"))
        self.stock_create_table_manufac_lineEdit.setPlaceholderText(_translate("MainWindow", "ООО Простоквашено"))
        self.stock_create_table_item1_insys.setPlaceholderText(_translate("MainWindow", "0"))
        self.stock_create_search_lineEdit.setPlaceholderText(_translate("MainWindow", "Найти..."))
        self.stock_create_actions_combobox.setPlaceholderText(_translate("MainWindow", "Действия"))
        self.stock_create_actions_combobox.setItemText(0, _translate("MainWindow", "Выделить все"))
        self.stock_create_actions_combobox.setItemText(1, _translate("MainWindow", "Снять все"))
        self.stock_create_actions_combobox.setItemText(2, _translate("MainWindow", "Показать выделенные"))
        self.stock_create_actions_combobox.setItemText(3, _translate("MainWindow", "Показать все"))
        self.stock_create_saveBtn.setText(_translate("MainWindow", "СОХРАНИТЬ"))
        self.stock_create_closeBtn.setText(_translate("MainWindow", "ЗАКРЫТЬ"))
        self.stock_create_table_item.setText(_translate("MainWindow", "Товар"))
        self.stock_create_table_manufact.setText(_translate("MainWindow", "Производитель"))
        self.stock_create_table_insys.setText(_translate("MainWindow", "В системе"))
        self.stock_create_table_fact.setText(_translate("MainWindow", "Факт"))
        self.stock_create_writeOff.setText(_translate("MainWindow", "Списать"))
        self.stock_create_tip.setText(_translate("MainWindow", "Выбранные товары будут добавлены в PDF файл"))
        self.sells_tab.setTabText(self.sells_tab.indexOf(self.stock), _translate("MainWindow", "Товары на реализации"))
        item = self.orders_main_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код заказа"))
        item = self.orders_main_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.orders_main_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Адрес"))
        item = self.orders_main_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата и время"))
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
        self.orders_create_item1_name.setPlaceholderText(
            _translate("MainWindow", "Молоко ультра пастеризованное 900 мл"))
        self.orders_create_item1_manufac.setPlaceholderText(_translate("MainWindow", "ООО Простоквашено"))
        self.orders_create_item1_insys.setPlaceholderText(_translate("MainWindow", "0"))
        self.orders_create_newItem_ok.setText(_translate("MainWindow", "OK"))
        self.orders_create_newItem_name.setPlaceholderText(_translate("MainWindow", "Введите название..."))
        self.orders_create_table_name.setText(_translate("MainWindow", "Товар"))
        self.orders_create_table_manufac.setText(_translate("MainWindow", "Производитель"))
        self.orders_create_table_insys.setText(_translate("MainWindow", "В системе"))
        self.orders_create_inorder.setText(_translate("MainWindow", "В заказе"))
        self.orders_create_saveBtn.setText(_translate("MainWindow", "СОХРАНИТЬ"))
        self.orders_create_closeBtn.setText(_translate("MainWindow", "ЗАКРЫТЬ"))
        self.sells_tab.setTabText(self.sells_tab.indexOf(self.orders), _translate("MainWindow", "Заказы"))
        item = self.returns_main_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код возврата"))
        item = self.returns_main_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Новый столбец"))
        item = self.returns_main_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Код заказа"))
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
        self.returns_create_item1_name.setPlaceholderText(
            _translate("MainWindow", "Молоко ультра пастеризованное 900 мл"))
        self.returns_create_item1_manufac.setPlaceholderText(_translate("MainWindow", "ООО Простоквашено"))
        self.returns_create_item1_inorder.setPlaceholderText(_translate("MainWindow", "0"))
        self.returns_create_item.setText(_translate("MainWindow", "Товар"))
        self.returns_create_manufac.setText(_translate("MainWindow", "Производитель"))
        self.returns_create_inorder.setText(_translate("MainWindow", "В заказе"))
        self.returns_create_return.setText(_translate("MainWindow", "Возврат"))
        self.returns_create_saveBtn.setText(_translate("MainWindow", "СОХРАНИТЬ"))
        self.returns_create_closeBtn.setText(_translate("MainWindow", "ЗАКРЫТЬ"))
        self.sells_tab.setTabText(self.sells_tab.indexOf(self.returns), _translate("MainWindow", "Возвраты"))
        item = self.getStocks_main_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код оприходования"))
        item = self.getStocks_main_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.getStocks_main_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Время"))
        self.getStocks_main_search_lineEdit.setPlaceholderText(_translate("MainWindow", "Найти..."))
        self.getStocks_create_header.setText(_translate("MainWindow", "Оприходование 123123"))
        self.getStocks_create_item1_name.setPlaceholderText(
            _translate("MainWindow", "Молоко ультра пастеризованное 900 мл"))
        self.getStocks_create_item1manufac.setPlaceholderText(_translate("MainWindow", "ООО Простоквашено"))
        self.getStocks_create_new_name.setPlaceholderText(_translate("MainWindow", "Введите название товара..."))
        self.getStocks_create_new_ok.setText(_translate("MainWindow", "OK"))
        self.getStocks_create_save.setText(_translate("MainWindow", "СОХРАНИТЬ"))
        self.getStocks_create_close.setText(_translate("MainWindow", "ЗАКРЫТЬ"))
        self.getStocks_create_nadlejc.setText(_translate("MainWindow", "Надлеж. кач."))
        self.getStocks_create_pribilo.setText(_translate("MainWindow", "Прибыло"))
        self.getStocks_create_item.setText(_translate("MainWindow", "Товар"))
        self.getStocks_create_manufac.setText(_translate("MainWindow", "Производитель"))
        self.sells_tab.setTabText(self.sells_tab.indexOf(self.getStocks), _translate("MainWindow", "Оприходования"))
        item = self.writeOffs_main_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код списания"))
        item = self.writeOffs_main_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.writeOffs_main_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Название товара"))
        item = self.writeOffs_main_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Количество"))
        item = self.writeOffs_main_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Причина"))
        self.writeOffs_main_search.setPlaceholderText(_translate("MainWindow", "Найти..."))
        self.page_header_6.setText(_translate("MainWindow", "Списание 1234123"))
        self.writeOff_create_cause_header.setText(_translate("MainWindow", "Причина"))
        self.writeOff_create_cause_lineEdit.setPlaceholderText(_translate("MainWindow", "Введите причину"))
        self.writeOff_create_item_header.setText(_translate("MainWindow", "Товар"))
        self.writeOff_create_item_lineEdit.setPlaceholderText(_translate("MainWindow", "Выберите товар"))
        self.writeOff_create_manufac_header.setText(_translate("MainWindow", "Производитель"))
        self.writeOff_create_manufac_lineEdit.setPlaceholderText(_translate("MainWindow", "Производитель"))
        self.writeOff_create_amount_header.setText(_translate("MainWindow", "Количество"))
        self.pushButton_15.setText(_translate("MainWindow", "СОХРАНИТЬ"))
        self.pushButton_16.setText(_translate("MainWindow", "ЗАКРЫТЬ"))
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
        self.employees_create_header.setText(_translate("MainWindow", "Сотрудник 123123"))
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