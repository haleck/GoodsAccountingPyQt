from PyQt5 import QtCore, QtGui, QtWidgets


class StockPage(object):
    def __init__(self):
        self.stock = QtWidgets.QWidget()
        self.stock.setObjectName("stock")
        self.stock_stackedWidget = QtWidgets.QStackedWidget(self.stock)
        self.stock_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 891))
        self.stock_stackedWidget.setObjectName("stock_stackedWidget")
        self.stock_main = QtWidgets.QWidget()
        self.stock_main.setObjectName("stock_main")

        # Start of Stock Table

        self.stock_main_table = QtWidgets.QTableWidget(self.stock_main)
        self.stock_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.stock_main_table.setRowCount(0)
        self.stock_main_table.setObjectName("stock_main_table")
        self.stock_main_table.setColumnCount(7)

        self.stock_main_table.setColumnWidth(0, 150)
        self.stock_main_table.setColumnWidth(1, 250)
        self.stock_main_table.setColumnWidth(2, 250)
        self.stock_main_table.setColumnWidth(3, 175)
        self.stock_main_table.setColumnWidth(4, 158)
        self.stock_main_table.setColumnWidth(5, 158)
        self.stock_main_table.setColumnWidth(6, 157)

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

        # End of Stock Table

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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
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
