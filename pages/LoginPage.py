from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLabel

from Tables import Users, Roles


class LoginPage(object):
    def showPopUp(self, text):
        dialog = QDialog()
        dialog.setWindowTitle("Уведомление")

        dialog.setStyleSheet("background-color: rgb(77, 77, 77);")

        label = QLabel(text)
        label.setStyleSheet("color: rgb(255, 255, 255);")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("OK")
        button.setStyleSheet("QPushButton {\n"
                             "    background-color:rgb(52, 52, 52);\n"
                             "    border-color: rgb(66, 66, 66);\n"
                             "    color: rgb(255, 255, 255);\n"
                             "    border-radius: 8px;    \n"
                             "    height: 30px; margin-top: 10px;"
                             "}\n"
                             "QPushButton:hover {\n"
                             "    background-color: rgba(255, 255, 255, 0.3);\n"
                             "    color: rgb(52, 52, 52);\n"
                             "}")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        dialog.setLayout(layout)

        button.clicked.connect(dialog.accept)

        dialog.exec_()
    def __init__(self):
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.login_page_back = QtWidgets.QLabel(self.login_page)
        self.login_page_back.setGeometry(QtCore.QRect(30, 30, 86, 23))
        self.login_page_back.setText("")
        self.login_page_back.setPixmap(QtGui.QPixmap("assets/back.png"))
        self.login_page_back.setObjectName("register_page_2_back")
        self.login_page_frame = QtWidgets.QFrame(self.login_page)
        self.login_page_frame.setGeometry(QtCore.QRect(490, 290, 450, 359))
        self.login_page_frame.setMinimumSize(QtCore.QSize(450, 320))
        self.login_page_frame.setMaximumSize(QtCore.QSize(399, 16777215))
        self.login_page_frame.setStyleSheet("border: 1px solid rgb(91, 91, 91);\n"
                                            "border-radius: 30px;")
        self.login_page_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_page_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_page_frame.setObjectName("login_page_frame")
        self.login_page_login = QtWidgets.QWidget(self.login_page_frame)
        self.login_page_login.setGeometry(QtCore.QRect(30, 40, 399, 101))
        self.login_page_login.setMinimumSize(QtCore.QSize(0, 101))
        self.login_page_login.setStyleSheet("border: none")
        self.login_page_login.setObjectName("login_page_login")
        self.login_page_login_header = QtWidgets.QLabel(self.login_page_login)
        self.login_page_login_header.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.login_page_login_header.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_page_login_header.setFont(font)
        self.login_page_login_header.setStyleSheet("color: rgb(217, 217, 217);")
        self.login_page_login_header.setObjectName("login_page_login_header")
        self.login_page_login_lineedit = QtWidgets.QLineEdit(self.login_page_login)
        self.login_page_login_lineedit.setGeometry(QtCore.QRect(0, 60, 390, 35))
        self.login_page_login_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_page_login_lineedit.setFont(font)
        self.login_page_login_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                     "border-color: rgb(66, 66, 66);\n"
                                                     "background-color: rgb(91, 91, 91);\n"
                                                     "border-radius: 8px;\n"
                                                     "padding: 5px;")
        self.login_page_login_lineedit.setText("")
        self.login_page_login_lineedit.setObjectName("login_page_login_lineedit")
        self.login_page_pswrd = QtWidgets.QWidget(self.login_page_frame)
        self.login_page_pswrd.setGeometry(QtCore.QRect(30, 140, 399, 101))
        self.login_page_pswrd.setMinimumSize(QtCore.QSize(0, 101))
        self.login_page_pswrd.setStyleSheet("border: none")
        self.login_page_pswrd.setObjectName("login_page_pswrd")
        self.login_page_psswrd_label = QtWidgets.QLabel(self.login_page_pswrd)
        self.login_page_psswrd_label.setGeometry(QtCore.QRect(0, 30, 67, 17))
        self.login_page_psswrd_label.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_page_psswrd_label.setFont(font)
        self.login_page_psswrd_label.setStyleSheet("color: rgb(217, 217, 217);")
        self.login_page_psswrd_label.setObjectName("login_page_psswrd_label")
        self.login_page_pswrd_lineedit = QtWidgets.QLineEdit(self.login_page_pswrd)
        self.login_page_pswrd_lineedit.setGeometry(QtCore.QRect(0, 60, 390, 35))
        self.login_page_pswrd_lineedit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_page_pswrd_lineedit.setFont(font)
        self.login_page_pswrd_lineedit.setStyleSheet("color: rgb(217, 217, 217);\n"
                                                     "border-color: rgb(66, 66, 66);\n"
                                                     "background-color: rgb(91, 91, 91);\n"
                                                     "border-radius: 8px;\n"
                                                     "padding: 5px;")
        self.login_page_pswrd_lineedit.setText("")
        self.login_page_pswrd_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_page_pswrd_lineedit.setObjectName("login_page_pswrd_lineedit")
        self.login_page_btn = QtWidgets.QPushButton(self.login_page_frame)
        self.login_page_btn.setEnabled(True)
        self.login_page_btn.setGeometry(QtCore.QRect(30, 280, 390, 35))
        self.login_page_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.login_page_btn.setMaximumSize(QtCore.QSize(16777215, 10000))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_page_btn.setFont(font)
        self.login_page_btn.setStyleSheet("QPushButton {\n"
                                          "    background-color:rgb(52, 52, 52);\n"
                                          "    border-color: rgb(66, 66, 66);\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    border-radius: 8px;    \n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgba(255, 255, 255, 0.3);\n"
                                          "    color: rgb(52, 52, 52);\n"
                                          "}")
        self.login_page_btn.setIconSize(QtCore.QSize(16, 16))
        self.login_page_btn.setObjectName("login_page_btn")
        self.login_page_header = QtWidgets.QLabel(self.login_page)
        self.login_page_header.setGeometry(QtCore.QRect(660, 280, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_page_header.setFont(font)
        self.login_page_header.setStyleSheet("border: none;\n"
                                             "color: rgb(217, 217, 217)")
        self.login_page_header.setAlignment(QtCore.Qt.AlignCenter)
        self.login_page_header.setObjectName("login_page_header")

        self.login_page_btn.clicked.connect(self.setMainPage)

    def setMainPage(self, event):
        try:
            user = Users.get(Users.nickname == self.login_page_login_lineedit.text())
            if user.password != self.login_page_pswrd_lineedit.text():
                self.showPopUp('Неверный пароль')
                return
            else:
                self.currentUser = user.id
                self.userRole = Roles.get(Roles.id == user.role).name
                print(self.userRole)
                if self.userRole == "Администратор" or self.userRole == 'Директор':
                    self.addAdminTabs()
        except Users.DoesNotExist:
            self.showPopUp('Пользователь не найден')
            return
        self.stackedWidget.setCurrentIndex(1)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.login_page_login_header.setText(_translate("MainWindow", "Логин"))
        self.login_page_login_lineedit.setPlaceholderText(_translate("MainWindow", "Введите логин"))
        self.login_page_psswrd_label.setText(_translate("MainWindow", "Пароль"))
        self.login_page_pswrd_lineedit.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
        self.login_page_btn.setText(_translate("MainWindow", "Войти"))
        self.login_page_header.setText(_translate("MainWindow", "Вход"))