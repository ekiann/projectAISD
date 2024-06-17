import sqlite3

from PySide6.QtWidgets import QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QFrame, QSizePolicy, QLabel, QHBoxLayout, QWidget, QSpacerItem
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QRect, QSize, QPropertyAnimation, QTimer, Qt

from ui_lk import Ui_Lk
import router
import res_rc


class Lk(QMainWindow):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.ui = Ui_Lk()
        self.ui.setupUi(self)
        self.router = router.Router()
        self.user_info = info
#        print(self.user_info)
        self.ui.fio.setText(self.user_info[3] + ' ' + self.user_info[4] + ' ' + self.user_info[5])
        self.ui.position.setText(self.user_info[6])
        connection = sqlite3.connect('/home/ramina/Документы/GitHub/aboba_2/authorization_py/database.db')
        cursor = connection.cursor()
        company = cursor.execute('SELECT * FROM companies WHERE id=?', (self.user_info[1], )).fetchall()[0][1]
        connection.close()
        self.ui.company.setText(company)
        self.ui.mail.setText(self.user_info[7])
        self.ui.personal_num.setText(self.user_info[2])
        self.ui.lk_photo.setPixmap(QPixmap(self.user_info[10]))
        self.ui.lk_photo.setScaledContents(True)
        self.ui.photo.setPixmap(QPixmap(self.user_info[10]))
        self.ui.photo.setScaledContents(True)
        self.menu_button_clicked(0)
        self.ui.menu_button.clicked.connect(lambda checked: self.menu_button_clicked(150))
        self.ui.my_tests.mousePressEvent = self.tests(0, 150)
        self.ui.my_tests_button.clicked.connect(lambda checked: self.tests(0, 150))
        self.ui.arrow_button.clicked.connect(lambda checked: self.tests(0, 150))
        self.ui.new_2.mousePressEvent = self.show_new_window
        self.ui.new_3.clicked.connect(self.show_new_window)
        self.ui.new_4.clicked.connect(self.show_new_window)
        self.ui.complete.mousePressEvent = self.show_complete_window
        self.ui.complete_2.clicked.connect(self.show_complete_window)
        self.ui.complete_3.clicked.connect(self.show_complete_window)

    def show_new_window(self):
        self.window = self.router.go_to_new_tests(self.user_info)
        self.window.show()
        self.close()

    def show_complete_window(self):
        self.window = self.router.go_to_completed_tests(self.user_info)
        self.window.show()
        self.close()

    def tests(self, event, t):
        new = self.ui.new_2
        new_text = self.ui.new_3
        new_arrow = self.ui.new_4
        complete = self.ui.complete
        complete_text = self.ui.complete_2
        complete_arrow = self.ui.complete_3

        if not complete.isHidden():
            start_size_complete_text = complete_text.geometry()
            end_size_complete_text = QRect(start_size_complete_text.x(),
                                           start_size_complete_text.y(),
                                           start_size_complete_text.width(), 0)
            start_size_complete_arrow = complete_arrow.geometry()
            end_size_complete_arrow = QRect(start_size_complete_arrow.x(),
                                            start_size_complete_arrow.y(),
                                            start_size_complete_arrow.width(), 0)
            start_size_new_text = new_text.geometry()
            end_size_new_text = QRect(start_size_new_text.x(),
                                      start_size_new_text.y(),
                                      start_size_new_text.width(), 0)
            start_size_new_arrow = new_arrow.geometry()
            end_size_new_arrow = QRect(start_size_new_arrow.x(),
                                       start_size_new_arrow.y(),
                                       start_size_new_arrow.width(), 0)

            self.anim_new = QPropertyAnimation(new, b"minimumSize")
            self.anim_complete = QPropertyAnimation(complete, b"minimumSize")
            self.anim_new_arrow = QPropertyAnimation(new_arrow, b"geometry")
            self.anim_complete_arrow = QPropertyAnimation(
                                                   complete_arrow, b"geometry")
            self.anim_new_text = QPropertyAnimation(new_text, b"geometry")
            self.anim_complete_text = QPropertyAnimation(
                                                   complete_text, b"geometry")

            self.anim_new.setDuration(t)
            self.anim_complete.setDuration(t)
            self.anim_new_arrow.setDuration(t)
            self.anim_complete_arrow.setDuration(t)
            self.anim_new_text.setDuration(t)
            self.anim_complete_text.setDuration(t)

            self.anim_new.setStartValue(QSize(0, 60))
            self.anim_complete.setStartValue(QSize(0, 60))
            self.anim_new_arrow.setStartValue(start_size_new_arrow)
            self.anim_complete_arrow.setStartValue(start_size_complete_arrow)
            self.anim_new_text.setStartValue(start_size_new_text)
            self.anim_complete_text.setStartValue(start_size_complete_text)

            self.anim_new.setEndValue(QSize(0, 0))
            self.anim_complete.setEndValue(QSize(0, 0))
            self.anim_new_arrow.setEndValue(end_size_new_arrow)
            self.anim_complete_arrow.setEndValue(end_size_complete_arrow)
            self.anim_new_text.setEndValue(end_size_new_text)
            self.anim_complete_text.setEndValue(end_size_complete_text)
            self.anim_new.start()
            self.anim_complete.start()
            self.anim_new_arrow.start()
            self.anim_complete_arrow.start()
            self.anim_new_text.start()
            self.anim_complete_text.start()
            self.timer = QTimer(self)
            self.timer.setSingleShot(True)
            self.timer.timeout.connect(self.hide_tests)
            self.timer.start(t)
            self.ui.arrow_button.setIcon(QIcon(':/lk_img/arrow.png'))

        else:
            self.ui.new_2.show()
            self.ui.complete.show()
            self.ui.line_6.show()
            self.ui.line_7.show()
            new_text.setStyleSheet(
                '''QPushButton{ background-color: rgb(2, 49, 93);
                font-size: 14pt; border: none; }''')
            complete_text.setStyleSheet(
                '''QPushButton{ background-color: rgb(2, 49, 93);
                font-size: 14pt; border: none; }''')
            start_size_complete_text = complete_text.geometry()
            end_size_complete_text = QRect(start_size_complete_text.x(),
                                           start_size_complete_text.y(),
                                           start_size_complete_text.width(),
                                           60)
            start_size_complete_arrow = complete_arrow.geometry()
            end_size_complete_arrow = QRect(start_size_complete_arrow.x(),
                                            start_size_complete_arrow.y(),
                                            start_size_complete_arrow.width(),
                                            60)
            start_size_new_text = new_text.geometry()
            end_size_new_text = QRect(start_size_new_text.x(),
                                      start_size_new_text.y(),
                                      start_size_new_text.width(),
                                      60)
            start_size_new_arrow = new_arrow.geometry()
            end_size_new_arrow = QRect(start_size_new_arrow.x(),
                                       start_size_new_arrow.y(),
                                       start_size_new_arrow.width(),
                                       60)

            self.anim_new = QPropertyAnimation(new, b"minimumSize")
            self.anim_complete = QPropertyAnimation(complete, b"minimumSize")
            self.anim_new_arrow = QPropertyAnimation(new_arrow, b"geometry")
            self.anim_complete_arrow = QPropertyAnimation(complete_arrow,
                                                          b"geometry")
            self.anim_new_text = QPropertyAnimation(new_text, b"geometry")
            self.anim_complete_text = QPropertyAnimation(complete_text,
                                                         b"geometry")

            self.anim_new.setDuration(t)
            self.anim_complete.setDuration(t)
            self.anim_new_arrow.setDuration(t)
            self.anim_complete_arrow.setDuration(t)
            self.anim_new_text.setDuration(t)
            self.anim_complete_text.setDuration(t)

            self.anim_new.setStartValue(QSize(0, 0))
            self.anim_complete.setStartValue(QSize(0, 0))
            self.anim_new_arrow.setStartValue(start_size_new_arrow)
            self.anim_complete_arrow.setStartValue(start_size_complete_arrow)
            self.anim_new_text.setStartValue(start_size_new_text)
            self.anim_complete_text.setStartValue(start_size_complete_text)

            self.anim_new.setEndValue(QSize(0, 60))
            self.anim_complete.setEndValue(QSize(0, 60))
            self.anim_new_arrow.setEndValue(end_size_new_arrow)
            self.anim_complete_arrow.setEndValue(end_size_complete_arrow)
            self.anim_new_text.setEndValue(end_size_new_text)
            self.anim_complete_text.setEndValue(end_size_complete_text)
            self.anim_new.start()
            self.anim_complete.start()
            self.anim_new_arrow.start()
            self.anim_complete_arrow.start()
            self.anim_new_text.start()
            self.anim_complete_text.start()
            self.ui.arrow_button.setIcon(QIcon(':/lk_img/down_arrow.png'))

    def hide_tests(self):
        self.ui.new_2.hide()
        self.ui.complete.hide()
        self.ui.line_6.hide()
        self.ui.line_7.hide()

    def hide(self):
        self.ui.lk.hide()
        self.ui.my_tests.hide()
        self.ui.line_4.hide()
        self.ui.line_5.hide()
        self.ui.menu_button.setStyleSheet(
            '''QPushButton{ background-color: rgb(2, 49, 93); border-radius: 25;
            background-image: url(:/lk_img/menu.png); border: none;}''')
        self.ui.frame_3.setStyleSheet(
            "QFrame{ background-color: rgb(2, 49, 93); border: none; }")
        self.ui.frame.setStyleSheet(
            "QFrame{ background-color: rgb(2, 49, 93); border: none; }")
        self.ui.groupBox.setStyleSheet(
            "QGroupBox { background-color: rgb(2, 49, 93); border: none;}")

    def menu_button_clicked(self, t):
        group = self.ui.groupBox
        if not self.ui.lk.isHidden():
            if not self.ui.complete.isHidden():
                self.tests(0, t)
            self.anim = QPropertyAnimation(group, b"maximumWidth")
            self.anim.setDuration(t)
            self.anim.setStartValue(360)
            self.anim.setEndValue(70)
            self.anim.start()
            self.timer = QTimer(self)
            self.timer.setSingleShot(True)
            self.timer.timeout.connect(self.hide)
            self.timer.start(t)
        else:
            self.anim = QPropertyAnimation(group, b"maximumWidth")
            self.anim.setDuration(t)
            self.anim.setStartValue(70)
            self.anim.setEndValue(360)
            self.anim.start()
            self.ui.lk.show()
            self.ui.my_tests.show()
            self.ui.line_4.show()
            self.ui.line_5.show()
            self.ui.menu_button.setStyleSheet(
                '''QPushButton{ background-color: rgb(0, 69, 126);border-radius: 25;
                background-image: url(:/lk_img/menu.png); border: none;}''')
            self.ui.frame_3.setStyleSheet(
                "QFrame{ background-color: rgb(0, 69, 126); border: none; }")
            self.ui.frame.setStyleSheet(
                "QFrame{ background-color: rgb(0, 69, 126); border: none; }")
            self.ui.groupBox.setStyleSheet(
                '''QGroupBox { background-color: rgb(0, 69, 126);
                border: none; }''')
            self.ui.lk.setStyleSheet(
                "QFrame{ background-color: rgb(0, 69, 126); border: none; }")
            self.ui.my_tests.setStyleSheet(
                "QFrame{ background-color: rgb(0, 69, 126); border: none; }")
            self.ui.arrow_button.setStyleSheet(
                '''QPushButton{ background-color: rgb(0, 69, 126);
                border: none;}''')
            self.ui.lk_button.setStyleSheet(
                '''QPushButton{ background-color: rgb(0, 69, 126);
                font-size: 14pt; border: none;}''')
            self.ui.my_tests_button.setStyleSheet(
                '''QPushButton{ background-color: rgb(0, 69, 126);
                font-size: 14pt; border: none;}''')
