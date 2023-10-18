# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignerFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from pages.HelloPage import HelloPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.RegisterPage import RegisterPage


class Ui_MainWindow(MainPage, HelloPage, RegisterPage, LoginPage):
    def setupUi(self, MainWindow):
        MainPage.__init__(self)
        HelloPage.__init__(self)
        RegisterPage.__init__(self)
        LoginPage.__init__(self)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1430, 964)
        MainWindow.setStyleSheet("background-color: rgb(77, 77, 77);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1421, 971))
        self.stackedWidget.setObjectName("stackedWidget")

        self.stackedWidget.addWidget(self.hello_page)
        self.stackedWidget.addWidget(self.main_page)
        self.stackedWidget.addWidget(self.register_page_2)
        self.stackedWidget.addWidget(self.register_page_1)
        self.stackedWidget.addWidget(self.login_page)

        MainWindow.setCentralWidget(self.centralwidget)

        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        # stackedWidget:
        # 0 - hello page
        # 1 - main page
        #       main_tab:
        #       0 - items
        #               items_stackedWidget:
        #               0 - main
        #               1 - create
        #       1 - sells
        #       2 - watch
        #       3 - employees
        # 2 - register_page 2
        # 3 - register_page 1
        # 4 - login_page

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.main_tab.setCurrentIndex(0)
        self.items_stackedWidget.setCurrentIndex(0)
        self.sells_tab.setCurrentIndex(0)
        self.stock_stackedWidget.setCurrentIndex(0)
        self.orders_stackedWidget.setCurrentIndex(0)
        self.returns_stackedWidget.setCurrentIndex(0)
        self.getStocks_stackedWidget.setCurrentIndex(0)
        self.writeOffs_stackedWidget.setCurrentIndex(0)
        self.employees_stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Event listeners
        self.hello_page_login_label.clicked.connect(self.setLoginPage)          # Кнопка войти на HelloPage
        self.hello_page_register_label.clicked.connect(self.setRegisterPage1)   # Кнопка ргеистрация на HelloPage
        self.register_page_1_back.mousePressEvent = self.setHelloPage           # Кнопка назад на RegisterPage1
        self.register_page_2_back.mousePressEvent = self.setRegisterPage1       # Кнопка назад на RegisterPage2
        self.login_page_back.mousePressEvent = self.setHelloPage                # Кнопка назад на LoginPage
        self.register_page_1_btn_btn.clicked.connect(self.setRegisterPage2)     # Кнопка далее на RegisterPage1
        self.register_page_2_btn.clicked.connect(self.setMainPage)              # Кнопка далее на RegisterPage1
        self.login_page_btn.clicked.connect(self.setMainPage)                   # Кнопка войт на LoginPage

    def setLoginPage(self, event):
        self.stackedWidget.setCurrentIndex(4)

    def setRegisterPage1(self, event):
        self.stackedWidget.setCurrentIndex(3)

    def setRegisterPage2(self, event):
        self.stackedWidget.setCurrentIndex(2)

    def setHelloPage(self, event):
        self.stackedWidget.setCurrentIndex(0)

    def setMainPage(self, event):
        self.stackedWidget.setCurrentIndex(1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        RegisterPage.retranslateUi(self)
        HelloPage.retranslateUi(self)
        MainPage.retranslateUi(self)
        LoginPage.retranslateUi(self)

        MainWindow.setWindowTitle(_translate("MainWindow", "Умная система складского учета"))

        self.action.setText(_translate("MainWindow", "Продажи"))
        self.action_2.setText(_translate("MainWindow", "Отслеживание"))
        self.action_3.setText(_translate("MainWindow", "Сотрудники"))
