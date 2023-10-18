from PyQt5 import QtCore, QtGui, QtWidgets


class HelloPage(object):
    def __init__(self):
        self.hello_page = QtWidgets.QWidget()
        self.hello_page.setObjectName("hello_page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.hello_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 270, 891, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.hello_page_container = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.hello_page_container.setContentsMargins(0, 0, 0, 0)
        self.hello_page_container.setObjectName("hello_page_container")
        self.hello_page_logo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hello_page_logo.setText("")
        self.hello_page_logo.setPixmap(QtGui.QPixmap("assets/logo.png"))
        self.hello_page_logo.setObjectName("hello_page_logo")
        self.hello_page_container.addWidget(self.hello_page_logo, 0, QtCore.Qt.AlignHCenter)
        self.hello_page_welcomeMessage = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.hello_page_welcomeMessage.setFont(font)
        self.hello_page_welcomeMessage.setStyleSheet("color: rgb(217, 217, 217);")
        self.hello_page_welcomeMessage.setObjectName("hello_page_welcomeMessage")
        self.hello_page_container.addWidget(self.hello_page_welcomeMessage, 0, QtCore.Qt.AlignHCenter)
        self.hello_page_tip = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hello_page_tip.setFont(font)
        self.hello_page_tip.setStyleSheet("color: rgb(217, 217, 217);\n"
                                          "line-height: 22px;")
        self.hello_page_tip.setAlignment(QtCore.Qt.AlignCenter)
        self.hello_page_tip.setObjectName("hello_page_tip")
        self.hello_page_container.addWidget(self.hello_page_tip, 0, QtCore.Qt.AlignHCenter)
        self.hello_page_space = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.hello_page_space.setObjectName("hello_page_space")
        self.hello_page_container.addWidget(self.hello_page_space)
        self.hello_page_login_widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.hello_page_login_widget.setObjectName("hello_page_login_widget")
        self.hello_page_login_label = QtWidgets.QPushButton(self.hello_page_login_widget)
        self.hello_page_login_label.setEnabled(True)
        self.hello_page_login_label.setGeometry(QtCore.QRect(250, 10, 400, 35))
        self.hello_page_login_label.setMaximumSize(QtCore.QSize(16777215, 10000))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hello_page_login_label.setFont(font)
        self.hello_page_login_label.setStyleSheet("QPushButton {\n"
                                                  "    background-color:rgb(52, 52, 52);\n"
                                                  "    border-color: rgb(66, 66, 66);\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    border-radius: 8px;    \n"
                                                  "}\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                  "    color: rgb(52, 52, 52);\n"
                                                  "}")
        self.hello_page_login_label.setIconSize(QtCore.QSize(16, 16))
        self.hello_page_login_label.setObjectName("hello_page_login_label")
        self.hello_page_container.addWidget(self.hello_page_login_widget)
        self.hello_page_line_widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.hello_page_line_widget.setObjectName("hello_page_line_widget")
        self.hello_page_line_line = QtWidgets.QFrame(self.hello_page_line_widget)
        self.hello_page_line_line.setGeometry(QtCore.QRect(250, 30, 400, 1))
        self.hello_page_line_line.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.hello_page_line_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.hello_page_line_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hello_page_line_line.setObjectName("hello_page_line_line")
        self.hello_page_line_label = QtWidgets.QLabel(self.hello_page_line_widget)
        self.hello_page_line_label.setGeometry(QtCore.QRect(420, 20, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.hello_page_line_label.setFont(font)
        self.hello_page_line_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.hello_page_line_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hello_page_line_label.setObjectName("hello_page_line_label")
        self.hello_page_container.addWidget(self.hello_page_line_widget)
        self.hello_page_register_widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.hello_page_register_widget.setObjectName("hello_page_register_widget")
        self.hello_page_register_label = QtWidgets.QPushButton(self.hello_page_register_widget)
        self.hello_page_register_label.setGeometry(QtCore.QRect(250, 10, 400, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hello_page_register_label.setFont(font)
        self.hello_page_register_label.setStyleSheet("QPushButton {\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "    background-color: rgb(66, 66, 66);\n"
                                                     "    border-color: rgb(66, 66, 66);\n"
                                                     "    border-radius: 8px;\n"
                                                     "}\n"
                                                     "QPushButton:hover {\n"
                                                     "    background-color: rgba(255, 255, 255, 0.5);\n"
                                                     "    \n"
                                                     "    color: rgb(52, 52, 52);\n"
                                                     "}")
        self.hello_page_register_label.setObjectName("hello_page_register_label")
        self.hello_page_container.addWidget(self.hello_page_register_widget)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.hello_page_welcomeMessage.setText(
            _translate("MainWindow", "Добро пожаловать в приложение Умный Складской Учет!"))
        self.hello_page_tip.setText(_translate("MainWindow",
                                               "Если вы являетесь сотрудником -  нажмите “Вход” и введите данные, которые вам передал администратор системы.\n"
                                               "Если вы являетесь управляющим складом, вам необходимо зарегистрировать аккаунт.\n"
                                               "Зарегистрированный аккаунт автоматически станет администратором созданной системы."))
        self.hello_page_login_label.setText(_translate("MainWindow", "Вход"))
        self.hello_page_line_label.setText(_translate("MainWindow", "ИЛИ"))
        self.hello_page_register_label.setText(_translate("MainWindow", "Регистрация"))
        self.hello_page_welcomeMessage.setText(_translate("MainWindow", "Добро пожаловать в приложение Умный Складской Учет!"))
        self.hello_page_tip.setText(_translate("MainWindow", "Если вы являетесь сотрудником -  нажмите “Вход” и введите данные, которые вам передал администратор системы.\n"
"Если вы являетесь управляющим складом, вам необходимо зарегистрировать аккаунт.\n"
"Зарегистрированный аккаунт автоматически станет администратором созданной системы."))
        self.hello_page_login_label.setText(_translate("MainWindow", "Вход"))
        self.hello_page_line_label.setText(_translate("MainWindow", "ИЛИ"))
        self.hello_page_register_label.setText(_translate("MainWindow", "Регистрация"))

