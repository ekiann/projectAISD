# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authorization.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        if not Authorization.objectName():
            Authorization.setObjectName(u"Authorization")
        Authorization.resize(1440, 1071)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Authorization.sizePolicy().hasHeightForWidth())
        Authorization.setSizePolicy(sizePolicy)
        Authorization.setMinimumSize(QSize(600, 700))
        Authorization.setMaximumSize(QSize(1920, 1080))
        palette = QPalette()
        brush = QBrush(QColor(2, 49, 93, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        Authorization.setPalette(palette)
        Authorization.setLayoutDirection(Qt.LeftToRight)
        Authorization.setStyleSheet(u"background-color: rgb(2, 49, 93);")
        self.centralwidget = QWidget(Authorization)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(600, 653))
        self.centralwidget.setMaximumSize(QSize(1920, 1033))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(300, 430))
        self.frame.setMaximumSize(QSize(470, 600))
        self.frame.setStyleSheet(u"background-color: rgb(128, 101, 146);\n"
"color: rgb(145, 65, 172);\n"
"border-radius: 25;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(60, 60, 60, 60)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(40)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.headder = QLabel(self.frame_4)
        self.headder.setObjectName(u"headder")
        sizePolicy1.setHeightForWidth(self.headder.sizePolicy().hasHeightForWidth())
        self.headder.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"URW Gothic"])
        font.setPointSize(40)
        self.headder.setFont(font)
        self.headder.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.headder)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(210, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 9, 0, 9)
        self.user_2 = QLabel(self.frame_2)
        self.user_2.setObjectName(u"user_2")
        sizePolicy1.setHeightForWidth(self.user_2.sizePolicy().hasHeightForWidth())
        self.user_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"URW Gothic"])
        font1.setPointSize(14)
        self.user_2.setFont(font1)
        self.user_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.user_2)

        self.user_entry_2 = QLineEdit(self.frame_2)
        self.user_entry_2.setObjectName(u"user_entry_2")
        sizePolicy1.setHeightForWidth(self.user_entry_2.sizePolicy().hasHeightForWidth())
        self.user_entry_2.setSizePolicy(sizePolicy1)
        self.user_entry_2.setMinimumSize(QSize(210, 50))
        self.user_entry_2.setMaximumSize(QSize(380, 60))
        self.user_entry_2.setStyleSheet(u"border: 2px solid #FFA566;\n"
"border-radius: 20px;\n"
"color: #D1D1D1;\n"
"font: 12pt \"URW Gothic\";")

        self.verticalLayout_4.addWidget(self.user_entry_2)

        self.password_2 = QLabel(self.frame_2)
        self.password_2.setObjectName(u"password_2")
        sizePolicy.setHeightForWidth(self.password_2.sizePolicy().hasHeightForWidth())
        self.password_2.setSizePolicy(sizePolicy)
        self.password_2.setMinimumSize(QSize(210, 0))
        self.password_2.setMaximumSize(QSize(380, 16777215))
        self.password_2.setFont(font1)
        self.password_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.password_2)

        self.password_entry_2 = QLineEdit(self.frame_2)
        self.password_entry_2.setObjectName(u"password_entry_2")
        sizePolicy1.setHeightForWidth(self.password_entry_2.sizePolicy().hasHeightForWidth())
        self.password_entry_2.setSizePolicy(sizePolicy1)
        self.password_entry_2.setMinimumSize(QSize(210, 50))
        self.password_entry_2.setMaximumSize(QSize(380, 60))
        self.password_entry_2.setStyleSheet(u"border: 2px solid #FFA566;\n"
"border-radius: 20px;\n"
"color: #D1D1D1;\n"
"font: 12pt \"URW Gothic\";")
        self.password_entry_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.password_entry_2)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(210, 0))
        self.frame_3.setMaximumSize(QSize(380, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setMidLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.link_2 = QLabel(self.frame_3)
        self.link_2.setObjectName(u"link_2")
        sizePolicy1.setHeightForWidth(self.link_2.sizePolicy().hasHeightForWidth())
        self.link_2.setSizePolicy(sizePolicy1)
        self.link_2.setMaximumSize(QSize(16777215, 16777215))
        self.link_2.setFont(font1)
        self.link_2.setLayoutDirection(Qt.LeftToRight)
        self.link_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.link_2.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout.addWidget(self.link_2)

        self.horizontalSpacer_2 = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.button_2 = QPushButton(self.frame_3)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy1)
        self.button_2.setMinimumSize(QSize(0, 50))
        self.button_2.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"URW Gothic"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.button_2.setFont(font2)
        self.button_2.setLayoutDirection(Qt.LeftToRight)
        self.button_2.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 165, 102);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"background-color: #FF8936;\n"
"border-radius: 20px;\n"
"}")
        self.button_2.setAutoDefault(False)
        self.button_2.setFlat(False)

        self.verticalLayout.addWidget(self.button_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        Authorization.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Authorization)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1440, 24))
        Authorization.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Authorization)
        self.statusbar.setObjectName(u"statusbar")
        Authorization.setStatusBar(self.statusbar)

        self.retranslateUi(Authorization)

        self.button_2.setDefault(False)


        QMetaObject.connectSlotsByName(Authorization)
    # setupUi

    def retranslateUi(self, Authorization):
        Authorization.setWindowTitle(QCoreApplication.translate("Authorization", u"Authorization", None))
        self.headder.setText(QCoreApplication.translate("Authorization", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.user_2.setText(QCoreApplication.translate("Authorization", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.user_entry_2.setPlaceholderText(QCoreApplication.translate("Authorization", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.password_2.setText(QCoreApplication.translate("Authorization", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.password_entry_2.setInputMask("")
        self.password_entry_2.setPlaceholderText(QCoreApplication.translate("Authorization", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.link_2.setText(QCoreApplication.translate("Authorization", u"\u0417\u0430\u0431\u044b\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c?", None))
        self.button_2.setText(QCoreApplication.translate("Authorization", u"LOGIN", None))
    # retranslateUi

