from PyQt5 import QtCore, QtGui, QtWidgets


class GetStocksPage(object):
    def __init__(self):
        self.getStocks = QtWidgets.QWidget()
        self.getStocks.setObjectName("getStocks")
        self.getStocks_stackedWidget = QtWidgets.QStackedWidget(self.getStocks)
        self.getStocks_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 891))
        self.getStocks_stackedWidget.setObjectName("getStocks_stackedWidget")
        self.getStocks_main = QtWidgets.QWidget()
        self.getStocks_main.setObjectName("getStocks_main")

        # Start of GetStocks Table

        self.getStocks_main_table = QtWidgets.QTableWidget(self.getStocks_main)
        self.getStocks_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.getStocks_main_table.setObjectName("getStocks_main_table")
        self.getStocks_main_table.setColumnCount(3)
        self.getStocks_main_table.setRowCount(0)

        self.getStocks_main_table.setColumnWidth(0, 433)
        self.getStocks_main_table.setColumnWidth(1, 432)
        self.getStocks_main_table.setColumnWidth(2, 433)

        item = QtWidgets.QTableWidgetItem()
        self.getStocks_main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.getStocks_main_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.getStocks_main_table.setHorizontalHeaderItem(2, item)

        # End of GetStocks Table

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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

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