from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

class WriteOffsPage(object):
    def fetchWriteOffs(self):
        return [
            {'id': 1, 'date': '23.06.2023', 'itemName': 'Молоко', 'amount': '2 Шт', 'cause': 'Нарушена упаковки'},
            {'id': 2, 'date': '23.06.2023', 'itemName': 'Кефир', 'amount': '2 Шт', 'cause': 'Срок годности'},
            {'id': 3, 'date': '24.06.2023', 'itemName': 'Сгущенка', 'amount': '2 Шт', 'cause': 'Срок годности'},
            {'id': 4, 'date': '25.06.2023', 'itemName': 'Сыр', 'amount': '2 Шт', 'cause': 'Нарушена упаковки'},
            {'id': 5, 'date': '25.06.2023', 'itemName': 'Торт', 'amount': '2 Шт', 'cause': 'Срок годности'},
        ]
    def __init__(self):
        self.writeOffs = QtWidgets.QWidget()
        self.writeOffs.setObjectName("writeOffs")
        self.writeOffs_stackedWidget = QtWidgets.QStackedWidget(self.writeOffs)
        self.writeOffs_stackedWidget.setGeometry(QtCore.QRect(10, 0, 1421, 891))
        self.writeOffs_stackedWidget.setObjectName("writeOffs_stackedWidget")
        self.writeOffs_main = QtWidgets.QWidget()
        self.writeOffs_main.setObjectName("writeOffs_main")

        # Start of WriteOffs Table

        data = self.fetchWriteOffs()

        self.writeOffs_main_table = QtWidgets.QTableWidget(self.writeOffs_main)
        self.writeOffs_main_table.setGeometry(QtCore.QRect(60, 120, 1300, 700))
        self.writeOffs_main_table.setObjectName("writeOffs_main_table")
        self.writeOffs_main_table.setColumnCount(5)
        self.writeOffs_main_table.setRowCount(0)

        self.writeOffs_main_table.setColumnWidth(0, 260)
        self.writeOffs_main_table.setColumnWidth(1, 260)
        self.writeOffs_main_table.setColumnWidth(2, 260)
        self.writeOffs_main_table.setColumnWidth(3, 259)
        self.writeOffs_main_table.setColumnWidth(4, 259)

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

        self.writeOffs_main_table.setRowCount(len(data))

        # Заполнение таблицы данными
        for row, item in enumerate(data):
            cell = QTableWidgetItem(str(item['id']))
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.writeOffs_main_table.setItem(row, 0, cell)

            cell = QTableWidgetItem(item['date'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.writeOffs_main_table.setItem(row, 1, cell)

            cell = QTableWidgetItem(item['itemName'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.writeOffs_main_table.setItem(row, 2, cell)

            cell = QTableWidgetItem(item['amount'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.writeOffs_main_table.setItem(row, 3, cell)

            cell = QTableWidgetItem(item['cause'])
            cell.setFlags(cell.flags() & ~Qt.ItemIsEditable)  # Отключение редактирования
            self.writeOffs_main_table.setItem(row, 4, cell)

        # Выделение всей строки при клике
        def on_item_click(item):
            row = item.row()
            for col in range(self.writeOffs_main_table.columnCount()):
                self.writeOffs_main_table.item(row, col).setSelected(True)

        self.writeOffs_main_table.itemClicked.connect(on_item_click)

        #
        self.writeOffs_main_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # End of WriteOffs Table

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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

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