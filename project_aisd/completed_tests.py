import sqlite3

from PySide6.QtWidgets import QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QFrame, QSizePolicy, QLabel, QHBoxLayout, QWidget, QSpacerItem
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QRect, QSize, QPropertyAnimation, QTimer, Qt

from ui_completed_tests import Ui_CompletedTests
import router
import res_rc


class CompletedTests(QMainWindow):
    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.ui = Ui_CompletedTests()
        self.ui.setupUi(self)
        self.router = router.Router()
        self.user_info = info
        self.menu_button_clicked(0)
        self.ui.photo.setPixmap(QPixmap(self.user_info[10]))
        self.ui.photo.setScaledContents(True)
        grid = QVBoxLayout()
        grid.setContentsMargins(40, 10, 40, 10)
        grid.setSpacing(30)
        for i in range(8):
            frame = QFrame()
            button = QPushButton()
            button.setText('Подробнее')
            button.setStyleSheet('QPushButton{background-color: #FFA566; border-radius: 20; color: #FFFFFF; font-size: 17pt; font-weight: bold;}')
            button.setMaximumHeight(50)
            button.setMinimumHeight(40)
            button.setMaximumWidth(400)
            button.setMinimumWidth(200)
            button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            grid_button = QVBoxLayout()
            grid_button.addWidget(button)
            label_title = QLabel()
            label_title.setText('Тест №' + str(i))
            label_title.setStyleSheet('QLabel{color: #FFFFFF; font-size: 18pt; font-weight: bold;}')
            label_res = QLabel()
            label_res.setText('Результат: <b>n%</b>')
            label_res.setStyleSheet('QLabel{color: #FFFFFF; font-size: 13pt;}')
            label_status = QLabel()
            label_status.setText('Статус: <b>xxx</b>')
            label_status.setStyleSheet('QLabel{color: #FFFFFF; font-size: 13pt;}')
            grid_labels = QVBoxLayout()
            grid_labels.addWidget(label_title)
            grid_labels.addWidget(label_res)
            grid_labels.addWidget(label_status)
            grid_labels.setContentsMargins(0, 0, 0, 0)
            grid_labels.setSpacing(10)
            grid_frame = QHBoxLayout()
            grid_frame.addLayout(grid_labels)
            grid_frame.addLayout(grid_button)
            grid_frame.setContentsMargins(50, 20, 50, 20)
            frame.setMinimumHeight(135)
            frame.setMinimumWidth(450)
            frame.setMaximumHeight(200)
            frame.setMaximumWidth(1500)
            frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            frame.setStyleSheet('QFrame {background-color: #806592; border-radius: 25;}')
            frame.setLayout(grid_frame)
            grid.addWidget(frame, i)
        w = QWidget()
        w.setLayout(grid)
        self.ui.scrollArea.setWidget(w)
        self.ui.menu_button.clicked.connect(lambda checked: self.menu_button_clicked(150))
        self.ui.my_tests.mousePressEvent = self.tests(0, 150)
        self.ui.my_tests_button.clicked.connect(lambda checked: self.tests(0, 150))
        self.ui.arrow_button.clicked.connect(lambda checked: self.tests(0, 150))
        self.ui.new_2.mousePressEvent = self.show_new_window
        self.ui.new_3.clicked.connect(self.show_new_window)
        self.ui.new_4.clicked.connect(self.show_new_window)
        self.ui.lk.mousePressEvent = self.show_lk_window
        self.ui.lk_button.clicked.connect(self.show_lk_window)

    def show_new_window(self):
        self.window = self.router.go_to_new_tests(self.user_info)
        self.window.show()
        self.close()

    def show_lk_window(self):
        self.window = self.router.go_to_lk(self.user_info)
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
            self.ui.arrow_button.setIcon(QIcon(':/completed_test_img/arrow.png'))

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
            self.ui.arrow_button.setIcon(QIcon(':/completed_test_img/down_arrow.png'))

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
            background-image: url(:/completed_test_img/menu.png); border: none;}''')
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
                background-image: url(:/completed_test_img/menu.png); border: none;}''')
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
