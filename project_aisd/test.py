import sqlite3

from PySide6.QtWidgets import QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QFrame, QSizePolicy, QLabel, QHBoxLayout, QWidget, QSpacerItem
from PySide6.QtGui import QPixmap, QIcon, QPalette
from PySide6.QtCore import QRect, QSize, QPropertyAnimation, QTimer, Qt

from ui_test import Ui_Test
import res_rc


class Test(QMainWindow):
    def __init__(self, info, t_info, parent=None):
        super().__init__(parent)
        self.ui = Ui_Test()
        self.ui.setupUi(self)
        self.user_info = info
        self.test_info = t_info
        self.ui.photo.setPixmap(QPixmap(self.user_info[10]))
        self.ui.photo.setScaledContents(True)
        self.grid = QVBoxLayout()
        self.grid.setContentsMargins(5, 5, 5, 5)
        self.grid.setSpacing(10)
        for i in range(self.test_info[3]):
            question = QPushButton(str(i + 1))
            question.setStyleSheet('''
            QPushButton{
            background-color: #5BA0BF;
            color: #FFFFFF;
            font-size: 17pt;
            font-weight: bold;
            border: 0px;
            border-radius: 5;
            }
            ''')
            question.setMaximumHeight(40)
            question.setMinimumHeight(40)
            question.setMaximumWidth(40)
            question.setMinimumWidth(40)
            self.grid.addWidget(question, i)
            question.clicked.connect(lambda checked, i=i: self.change_question(i))
        w = QWidget()
        w.setLayout(self.grid)
        self.ui.questions.setWidget(w)
        self.cur_question = 0
        self.change_question(self.cur_question)

    def change_question(self, next_question):
        button = self.grid.itemAt(self.cur_question).widget()
#        print(button.palette().color(button.backgroundRole()).name())
        if self.ui.answer_1.isChecked() or self.ui.answer_2.isChecked() or self.ui.answer_3.isChecked() or self.ui.answer_4.isChecked():
            button.setStyleSheet('''
            QPushButton{
            background-color: #806592;
            color: #FFFFFF;
            font-size: 17pt;
            font-weight: bold;
            border: 0px;
            border-radius: 5;
            }''')
        elif button.palette().color(button.backgroundRole()).name() == '#806592':
            button.setStyleSheet('''
            QPushButton{
            background-color: #806592;
            color: #FFFFFF;
            font-size: 17pt;
            font-weight: bold;
            border: 0px;
            border-radius: 5;
            }''')
        else:
            button.setStyleSheet('''
            QPushButton{
            background-color: #5BA0BF;
            color: #FFFFFF;
            font-size: 17pt;
            font-weight: bold;
            border: 0px;
            border-radius: 5;
            }''')

        self.ui.question.setText(self.test_info[next_question + 5])
        connection = sqlite3.connect('/home/ramina/Документы/GitHub/aboba_2/authorization_py/database.db')
        cursor = connection.cursor()
        self.answers = cursor.execute('SELECT * FROM answers WHERE test_id=?', (self.test_info[0], )).fetchall()[0]
        connection.close()
        self.ui.answer_1.setAutoExclusive(False)
        self.ui.answer_2.setAutoExclusive(False)
        self.ui.answer_3.setAutoExclusive(False)
        self.ui.answer_4.setAutoExclusive(False)
        self.ui.answer_1.setChecked(False)
        self.ui.answer_2.setChecked(False)
        self.ui.answer_3.setChecked(False)
        self.ui.answer_4.setChecked(False)
        self.ui.answer_1.repaint()
        self.ui.answer_2.repaint()
        self.ui.answer_3.repaint()
        self.ui.answer_4.repaint()
        self.ui.answer_1.setAutoExclusive(True)
        self.ui.answer_2.setAutoExclusive(True)
        self.ui.answer_3.setAutoExclusive(True)
        self.ui.answer_4.setAutoExclusive(True)
        self.ui.answer_1.setText(self.answers[next_question + 2].split('\n')[0])
        self.ui.answer_2.setText(self.answers[next_question + 2].split('\n')[1])
        self.ui.answer_3.setText(self.answers[next_question + 2].split('\n')[2])
        self.ui.answer_4.setText(self.answers[next_question + 2].split('\n')[3])
        if next_question == self.test_info[3] - 1:
            self.ui.end.show()
        else:
            self.ui.end.hide()
        self.cur_question = next_question
        button = self.grid.itemAt(self.cur_question).widget()
        if button.palette().color(button.backgroundRole()).name() == '#806592':
            button.setStyleSheet('''
            QPushButton{
            background-color: #806592;
            color: #FFFFFF;
            font-size: 17pt;
            font-weight: bold;
            border: 2px solid #FFFFFF;
            border-radius: 5;
            }''')
        else:
            button.setStyleSheet('''
            QPushButton{
            background-color: #5BA0BF;
            color: #FFFFFF;
            font-size: 17pt;
            font-weight: bold;
            border: 2px solid #FFFFFF;
            border-radius: 5;
            }''')
