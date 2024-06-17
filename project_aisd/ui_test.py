# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_Test(object):
    def setupUi(self, Test):
        if not Test.objectName():
            Test.setObjectName(u"Test")
        Test.resize(1440, 951)
        Test.setMinimumSize(QSize(700, 700))
        Test.setStyleSheet(u"background-color: rgb(2, 49, 93);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"URW Gothic\";")
        self.centralwidget = QWidget(Test)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 70))
        self.frame_2.setMaximumSize(QSize(16777215, 70))
        self.frame_2.setStyleSheet(u"border: 0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 8, 20, 7)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(210, 35))
        self.pushButton.setMaximumSize(QSize(16777215, 40))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"background-color: rgb(91, 160, 191);\n"
"border-radius: 10;\n"
"font-size: 12pt;\n"
"}\n"
"QPushButton:pressed{\n"
"color: #FFFFFF; \n"
"background-color: #2A97C8;\n"
" border-radius: 10;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(1137, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.photo = QLabel(self.frame_2)
        self.photo.setObjectName(u"photo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.photo.sizePolicy().hasHeightForWidth())
        self.photo.setSizePolicy(sizePolicy2)
        self.photo.setMinimumSize(QSize(50, 55))
        self.photo.setMaximumSize(QSize(50, 55))
        self.photo.setStyleSheet(u"background-image: url(:/test_img/user.png);\n"
"background-repeat: none;")

        self.horizontalLayout.addWidget(self.photo)


        self.verticalLayout.addWidget(self.frame_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 3))
        self.line.setMaximumSize(QSize(16777215, 3))
        self.line.setStyleSheet(u"background-color: rgb(227, 134, 100);")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setMinimumSize(QSize(700, 500))
        self.frame_5.setMaximumSize(QSize(900, 500))
        self.frame_5.setBaseSize(QSize(0, 0))
        self.frame_5.setStyleSheet(u"border: 3px solid #E38664;\n"
"border-radius: 40;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.questions = QScrollArea(self.frame_5)
        self.questions.setObjectName(u"questions")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.questions.sizePolicy().hasHeightForWidth())
        self.questions.setSizePolicy(sizePolicy4)
        self.questions.setMinimumSize(QSize(50, 400))
        self.questions.setMaximumSize(QSize(50, 16777215))
        self.questions.setStyleSheet(u"QScrollBar{width: 0px; height: 0px;}\n"
"QScrollArea{border: 0px;}\n"
"QWidget{border: 0px;}")
        self.questions.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 50, 454))
        self.questions.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget(self.questions)

        self.scroll_area = QScrollArea(self.frame_5)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"QScrollBar{width: 0px; height: 0px;}\n"
"QScrollArea{border: 0px;}\n"
"QWidget{border: 0px;}")
        self.scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 804, 454))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(60, 20, 40, 20)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(40)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.question = QLabel(self.scrollAreaWidgetContents_3)
        self.question.setObjectName(u"question")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy5)
        self.question.setStyleSheet(u"font-size: 20pt;\n"
"background-color: rgb(255, 165, 102);\n"
"border-radius: 15;\n"
"padding: 5px 10px 5px 10px;")
        self.question.setAlignment(Qt.AlignCenter)
        self.question.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.question)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.answer_1 = QRadioButton(self.scrollAreaWidgetContents_3)
        self.answer_1.setObjectName(u"answer_1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.answer_1.sizePolicy().hasHeightForWidth())
        self.answer_1.setSizePolicy(sizePolicy6)
        self.answer_1.setMinimumSize(QSize(0, 0))
        self.answer_1.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(2, 49, 93, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.answer_1.setPalette(palette)
        font = QFont()
        font.setFamilies([u"URW Gothic"])
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.answer_1.setFont(font)
        self.answer_1.setStyleSheet(u"QRadioButton{\n"
"font-size: 13pt;\n"
"}\n"
"QRadioButton::indicator:unchecked{\n"
"	background-image: url(:/test_img/unchecked.png);\n"
"}\n"
"QRadioButton::indicator:checked{\n"
"	background-image: url(:/test_img/checked.png);\n"
"}")

        self.verticalLayout_2.addWidget(self.answer_1)

        self.answer_2 = QRadioButton(self.scrollAreaWidgetContents_3)
        self.answer_2.setObjectName(u"answer_2")
        sizePolicy6.setHeightForWidth(self.answer_2.sizePolicy().hasHeightForWidth())
        self.answer_2.setSizePolicy(sizePolicy6)
        self.answer_2.setMinimumSize(QSize(0, 0))
        self.answer_2.setMaximumSize(QSize(16777215, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.answer_2.setPalette(palette1)
        self.answer_2.setFont(font)
        self.answer_2.setStyleSheet(u"QRadioButton{\n"
"font-size: 13pt;\n"
"}\n"
"QRadioButton::indicator:unchecked{\n"
"	background-image: url(:/test_img/unchecked.png);\n"
"}\n"
"QRadioButton::indicator:checked{\n"
"	background-image: url(:/test_img/checked.png);\n"
"}")

        self.verticalLayout_2.addWidget(self.answer_2)

        self.answer_3 = QRadioButton(self.scrollAreaWidgetContents_3)
        self.answer_3.setObjectName(u"answer_3")
        sizePolicy6.setHeightForWidth(self.answer_3.sizePolicy().hasHeightForWidth())
        self.answer_3.setSizePolicy(sizePolicy6)
        self.answer_3.setMinimumSize(QSize(0, 0))
        self.answer_3.setMaximumSize(QSize(16777215, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.answer_3.setPalette(palette2)
        self.answer_3.setFont(font)
        self.answer_3.setStyleSheet(u"QRadioButton{\n"
"font-size: 13pt;\n"
"}\n"
"QRadioButton::indicator:unchecked{\n"
"	background-image: url(:/test_img/unchecked.png);\n"
"}\n"
"QRadioButton::indicator:checked{\n"
"	background-image: url(:/test_img/checked.png);\n"
"}")

        self.verticalLayout_2.addWidget(self.answer_3)

        self.answer_4 = QRadioButton(self.scrollAreaWidgetContents_3)
        self.answer_4.setObjectName(u"answer_4")
        sizePolicy6.setHeightForWidth(self.answer_4.sizePolicy().hasHeightForWidth())
        self.answer_4.setSizePolicy(sizePolicy6)
        self.answer_4.setMinimumSize(QSize(0, 0))
        self.answer_4.setMaximumSize(QSize(16777215, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.answer_4.setPalette(palette3)
        self.answer_4.setFont(font)
        self.answer_4.setStyleSheet(u"QRadioButton{\n"
"font-size: 13pt;\n"
"}\n"
"QRadioButton::indicator:unchecked{\n"
"	background-image: url(:/test_img/unchecked.png);\n"
"}\n"
"QRadioButton::indicator:checked{\n"
"	background-image: url(:/test_img/checked.png);\n"
"}")

        self.verticalLayout_2.addWidget(self.answer_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.end = QPushButton(self.scrollAreaWidgetContents_3)
        self.end.setObjectName(u"end")
        sizePolicy2.setHeightForWidth(self.end.sizePolicy().hasHeightForWidth())
        self.end.setSizePolicy(sizePolicy2)
        self.end.setMinimumSize(QSize(200, 40))
        self.end.setMaximumSize(QSize(200, 40))
        self.end.setStyleSheet(u"QPushButton{\n"
"font-size: 15pt;\n"
"background-color: rgb(255, 165, 102);\n"
"border-radius: 10;\n"
"}\n"
"QPushButton:pressed{\n"
"color: #FFFFFF; \n"
"background-color: #FF8936;\n"
" border-radius: 10;\n"
"}")

        self.verticalLayout_5.addWidget(self.end, 0, Qt.AlignHCenter)

        self.scroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_2.addWidget(self.scroll_area)


        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame)

        Test.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Test)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1440, 22))
        Test.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Test)
        self.statusbar.setObjectName(u"statusbar")
        Test.setStatusBar(self.statusbar)

        self.retranslateUi(Test)

        QMetaObject.connectSlotsByName(Test)
    # setupUi

    def retranslateUi(self, Test):
        Test.setWindowTitle(QCoreApplication.translate("Test", u"Test", None))
        self.pushButton.setText(QCoreApplication.translate("Test", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0442\u0435\u0441\u0442 \u0434\u043e\u0441\u0440\u043e\u0447\u043d\u043e", None))
        self.photo.setText("")
        self.question.setText(QCoreApplication.translate("Test", u"\u0427\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u0430\u043b\u0444\u0430\u0432\u0438\u0442?", None))
        self.answer_1.setText(QCoreApplication.translate("Test", u"\u0430\u0430\u0430\u0430\u0430\u0430\u0430\u0430", None))
        self.answer_2.setText(QCoreApplication.translate("Test", u"\u0431\u0431\u0431\u0431\u0431\u0431\u0431\u0431", None))
        self.answer_3.setText(QCoreApplication.translate("Test", u"\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432", None))
        self.answer_4.setText(QCoreApplication.translate("Test", u"\u0433\u0433\u0433\u0433\u0433\u0433\u0433\u0433", None))
        self.end.setText(QCoreApplication.translate("Test", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0442\u0435\u0441\u0442", None))
    # retranslateUi

