import sqlite3

from PySide6.QtWidgets import QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QFrame, QSizePolicy, QLabel, QHBoxLayout, QWidget, QSpacerItem
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QRect, QSize, QPropertyAnimation, QTimer, Qt

from ui_authorization import Ui_Authorization
import router
import res_rc


class Authorization(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)
        self.setWindowTitle('authorization')
        self.router = router.Router()
        self.ui.button_2.clicked.connect(self.button_clicked)
        self.ui.link_2.mousePressEvent = self.link_activated

    def button_clicked(self):
        user = self.ui.user_entry_2.text()
        password = self.ui.password_entry_2.text()
#        print(user, password)
        # отправлять запрос на сервер в бд для поиска совпадения
        #да -> перекидывать на страницу тестов, нет -> invalid_data()
        connection = sqlite3.connect('/home/ramina/Документы/GitHub/aboba_2/authorization_py/database.db')
        cursor = connection.cursor()
        info = cursor.execute('SELECT * FROM users WHERE username=? and password=?', (user, password)).fetchall()
        connection.close()
#        print(info)
        if not info:
            self.invalid_data()
        else:
            self.window = self.router.go_to_new_tests(info[0])
            self.window.show()
            self.close()
#        if user == 'aboba' and password == '12345':
#            self.window = NewTests()
#            self.window.show()
#            self.close()
#        else:
#            self.invalid_data()
        self.ui.user_entry_2.clear()
        self.ui.password_entry_2.clear()

    def link_activated(self, event):
        popup = QMessageBox()
        popup.setStyleSheet('''QMessageBox{background-color: #00457E; font-family: URW Gothic, Book;}
        QLabel{color: #FFFFFF; font-size: 12pt;}
        QPushButton{border-radius: 10; background-color: #E38664; min-height: 30; min-width: 60; color: #FFFFFF;}''')
        popup.setWindowTitle('смена пароля')
        popup.setIconPixmap(QPixmap(':/authorization_img/information.png'))
        popup.addButton('OK', QMessageBox.AcceptRole)
        popup.setText('Для смены пароля обратитесь в отдел кадров')
        popup.setInformativeText('Тел: 88005553535')
        popup.exec()

    def invalid_data(self):
        popup = QMessageBox()
        popup.setStyleSheet('''QMessageBox{background-color: #00457E; font-family: URW Gothic, Book;}
        QLabel{color: #FFFFFF; font-size: 12pt;}
        QPushButton{border-radius: 10; background-color: #E38664; min-height: 30; min-width: 60; color: #FFFFFF;}''')
        popup.setWindowTitle('некорректные данные')
        popup.setIconPixmap(QPixmap(':/authorization_img/error.png'))
        popup.addButton('OK', QMessageBox.AcceptRole)
        popup.setText('Данные были введены неверно')
        popup.setInformativeText('Попробуйте еще раз')
        popup.exec()
