# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_tests.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)
import res_rc

class Ui_NewTests(object):
    def setupUi(self, NewTests):
        if not NewTests.objectName():
            NewTests.setObjectName(u"NewTests")
        NewTests.resize(1440, 1024)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewTests.sizePolicy().hasHeightForWidth())
        NewTests.setSizePolicy(sizePolicy)
        NewTests.setMinimumSize(QSize(700, 700))
        NewTests.setStyleSheet(u"background-color: rgb(2, 49, 93);\n"
"color: #ffffff;\n"
"font: 10pt \"URW Gothic\";")
        self.centralwidget = QWidget(NewTests)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(360, 16777215))
        self.groupBox.setStyleSheet(u"border: 0px;\n"
"background-color: #00457E;\n"
"font: 10pt \"URW Gothic\";")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 70))
        self.frame.setMaximumSize(QSize(16777215, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, 10, 0, 10)
        self.menu_button = QPushButton(self.frame)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setMinimumSize(QSize(50, 50))
        self.menu_button.setMaximumSize(QSize(50, 50))
        self.menu_button.setStyleSheet(u"background-image: url(:/new_test_img/menu.png);\n"
"border: 0px;\n"
"border-radius: 25;")

        self.horizontalLayout_9.addWidget(self.menu_button)

        self.horizontalSpacer_8 = QSpacerItem(288, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addWidget(self.frame)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(227, 134, 100);")
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 47))
        self.frame_3.setMaximumSize(QSize(16777215, 47))
        self.frame_3.setStyleSheet(u"border: none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.lk = QFrame(self.groupBox)
        self.lk.setObjectName(u"lk")
        self.lk.setMinimumSize(QSize(0, 60))
        self.lk.setMaximumSize(QSize(16777215, 60))
        self.lk.setFrameShape(QFrame.StyledPanel)
        self.lk.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.lk)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lk_button = QPushButton(self.lk)
        self.lk_button.setObjectName(u"lk_button")
        sizePolicy.setHeightForWidth(self.lk_button.sizePolicy().hasHeightForWidth())
        self.lk_button.setSizePolicy(sizePolicy)
        self.lk_button.setMinimumSize(QSize(180, 60))
        self.lk_button.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setFamilies([u"URW Gothic"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.lk_button.setFont(font)
        self.lk_button.setStyleSheet(u"font-size: 14pt;\n"
"color: rgb(255, 255, 255);\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.lk_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.lk)

        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy1)
        self.line_4.setMinimumSize(QSize(0, 2))
        self.line_4.setMaximumSize(QSize(400, 2))
        self.line_4.setStyleSheet(u"background-color: #2F71AE;")
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.my_tests = QFrame(self.groupBox)
        self.my_tests.setObjectName(u"my_tests")
        self.my_tests.setMinimumSize(QSize(0, 60))
        self.my_tests.setMaximumSize(QSize(16777215, 60))
        self.my_tests.setFrameShape(QFrame.StyledPanel)
        self.my_tests.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.my_tests)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.my_tests_button = QPushButton(self.my_tests)
        self.my_tests_button.setObjectName(u"my_tests_button")
        sizePolicy.setHeightForWidth(self.my_tests_button.sizePolicy().hasHeightForWidth())
        self.my_tests_button.setSizePolicy(sizePolicy)
        self.my_tests_button.setMinimumSize(QSize(130, 60))
        self.my_tests_button.setMaximumSize(QSize(16777215, 70))
        self.my_tests_button.setStyleSheet(u"font-size: 14pt;\n"
"color: rgb(255, 255, 255);\n"
"border: none;")

        self.horizontalLayout.addWidget(self.my_tests_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.arrow_button = QPushButton(self.my_tests)
        self.arrow_button.setObjectName(u"arrow_button")
        sizePolicy.setHeightForWidth(self.arrow_button.sizePolicy().hasHeightForWidth())
        self.arrow_button.setSizePolicy(sizePolicy)
        self.arrow_button.setMinimumSize(QSize(60, 0))
        self.arrow_button.setMaximumSize(QSize(60, 16777215))
        icon = QIcon()
        icon.addFile(u":/new_test_img/arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arrow_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.arrow_button)


        self.verticalLayout.addWidget(self.my_tests)

        self.line_5 = QFrame(self.groupBox)
        self.line_5.setObjectName(u"line_5")
        sizePolicy1.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy1)
        self.line_5.setMinimumSize(QSize(0, 2))
        self.line_5.setMaximumSize(QSize(400, 2))
        self.line_5.setStyleSheet(u"background-color: #2F71AE;")
        self.line_5.setLineWidth(0)
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.new_2 = QFrame(self.groupBox)
        self.new_2.setObjectName(u"new_2")
        self.new_2.setMinimumSize(QSize(0, 60))
        self.new_2.setMaximumSize(QSize(16777215, 60))
        self.new_2.setStyleSheet(u"background-color: rgb(2, 49, 93);\n"
"border: 0px;")
        self.new_2.setFrameShape(QFrame.StyledPanel)
        self.new_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.new_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, 0, 0, 0)
        self.new_4 = QPushButton(self.new_2)
        self.new_4.setObjectName(u"new_4")
        sizePolicy.setHeightForWidth(self.new_4.sizePolicy().hasHeightForWidth())
        self.new_4.setSizePolicy(sizePolicy)
        self.new_4.setMinimumSize(QSize(20, 0))
        self.new_4.setMaximumSize(QSize(20, 16777215))
        self.new_4.setStyleSheet(u"background-color: rgb(2, 49, 93);\n"
"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/new_test_img/double_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_4.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.new_4)

        self.new_3 = QPushButton(self.new_2)
        self.new_3.setObjectName(u"new_3")
        sizePolicy.setHeightForWidth(self.new_3.sizePolicy().hasHeightForWidth())
        self.new_3.setSizePolicy(sizePolicy)
        self.new_3.setMinimumSize(QSize(60, 0))
        self.new_3.setMaximumSize(QSize(16777215, 70))
        self.new_3.setStyleSheet(u"background-color: #02315D;\n"
"font-size: 14pt;\n"
"color: rgb(255, 255, 255);\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.new_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.new_2)

        self.line_7 = QFrame(self.groupBox)
        self.line_7.setObjectName(u"line_7")
        sizePolicy1.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy1)
        self.line_7.setMinimumSize(QSize(0, 2))
        self.line_7.setMaximumSize(QSize(16777215, 2))
        self.line_7.setStyleSheet(u"background-color: #2F71AE;")
        self.line_7.setLineWidth(0)
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_7)

        self.complete = QFrame(self.groupBox)
        self.complete.setObjectName(u"complete")
        self.complete.setMinimumSize(QSize(0, 60))
        self.complete.setMaximumSize(QSize(16777215, 60))
        self.complete.setStyleSheet(u"background-color: rgb(2, 49, 93);\n"
"border: 0px;")
        self.complete.setFrameShape(QFrame.StyledPanel)
        self.complete.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.complete)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(30, 0, 0, 0)
        self.complete_3 = QPushButton(self.complete)
        self.complete_3.setObjectName(u"complete_3")
        sizePolicy.setHeightForWidth(self.complete_3.sizePolicy().hasHeightForWidth())
        self.complete_3.setSizePolicy(sizePolicy)
        self.complete_3.setMinimumSize(QSize(20, 0))
        self.complete_3.setMaximumSize(QSize(20, 16777215))
        self.complete_3.setStyleSheet(u"background-color: rgb(2, 49, 93);\n"
"border: none;")
        self.complete_3.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.complete_3)

        self.complete_2 = QPushButton(self.complete)
        self.complete_2.setObjectName(u"complete_2")
        self.complete_2.setMinimumSize(QSize(122, 0))
        self.complete_2.setMaximumSize(QSize(16777215, 70))
        self.complete_2.setStyleSheet(u"background-color: #02315D;\n"
"font-size: 14pt;\n"
"color: rgb(255, 255, 255);\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.complete_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addWidget(self.complete)

        self.line_6 = QFrame(self.groupBox)
        self.line_6.setObjectName(u"line_6")
        sizePolicy1.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy1)
        self.line_6.setMinimumSize(QSize(0, 2))
        self.line_6.setMaximumSize(QSize(16777215, 2))
        self.line_6.setStyleSheet(u"background-color: #2F71AE;")
        self.line_6.setLineWidth(0)
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 3, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border: 0px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 8, 20, 7)
        self.horizontalSpacer = QSpacerItem(1007, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.photo = QLabel(self.frame_4)
        self.photo.setObjectName(u"photo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.photo.sizePolicy().hasHeightForWidth())
        self.photo.setSizePolicy(sizePolicy2)
        self.photo.setMinimumSize(QSize(50, 55))
        self.photo.setMaximumSize(QSize(50, 55))
        self.photo.setStyleSheet(u"background-image: url(:/new_test_img/user.png);\n"
"background-repeat: none;")

        self.horizontalLayout_7.addWidget(self.photo)


        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(227, 134, 100);")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border: 0px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(40, 30, 40, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"URW Gothic"])
        font1.setPointSize(28)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #FFFFFF;\n"
"font-size: 28pt;")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(self.frame_5)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical{\n"
"width: 5px;\n"
"border: none;\n"
"background-color: #2F71AE;\n"
"border-radius: 0;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"width: 3px;\n"
"border: none;\n"
"background-color: #00457E;\n"
"border-radius: 2;\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"width: 0px;\n"
"height: 0px;\n"
"border: none;\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"width: 0px;\n"
"height: 0px;\n"
"border: none;\n"
"}\n"
"QScrollArea{font: 10pt \"URW Gothic\";}\n"
"QWidget{font: 10pt \"URW Gothic\";}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1000, 805))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.frame_5, 2, 1, 1, 1)

        NewTests.setCentralWidget(self.centralwidget)
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.groupBox.raise_()
        self.line.raise_()
        self.menubar = QMenuBar(NewTests)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1440, 22))
        NewTests.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(NewTests)
        self.statusbar.setObjectName(u"statusbar")
        NewTests.setStatusBar(self.statusbar)

        self.retranslateUi(NewTests)

        QMetaObject.connectSlotsByName(NewTests)
    # setupUi

    def retranslateUi(self, NewTests):
        NewTests.setWindowTitle(QCoreApplication.translate("NewTests", u"NewTests", None))
        self.groupBox.setTitle("")
        self.menu_button.setText("")
        self.lk_button.setText(QCoreApplication.translate("NewTests", u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.my_tests_button.setText(QCoreApplication.translate("NewTests", u"\u041c\u043e\u0438 \u0442\u0435\u0441\u0442\u044b", None))
        self.arrow_button.setText("")
        self.new_4.setText("")
        self.new_3.setText(QCoreApplication.translate("NewTests", u"\u041d\u043e\u0432\u044b\u0435", None))
        self.complete_3.setText("")
        self.complete_2.setText(QCoreApplication.translate("NewTests", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0435", None))
        self.photo.setText("")
        self.label.setText(QCoreApplication.translate("NewTests", u"\u041d\u043e\u0432\u044b\u0435 \u0442\u0435\u0441\u0442\u044b", None))
    # retranslateUi

