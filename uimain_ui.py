# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uimain.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableView, QWidget)
import qrs_ico_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 533)
        icon = QIcon()
        icon.addFile(u":/iconcis/g_translate_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLineEdit{\n"
"    border: 1px solid rgba(255, 246, 246,80);\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    color: white;\n"
"    background-color: rgb(62, 75, 75)\n"
"}\n"
"\n"
"QLabel{\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    color:white;\n"
"    font-size: 16px;\n"
"    background-color: rgb(62, 75, 75);\n"
"    border:none;\n"
"} \n"
"\n"
"QWidget{\n"
"    background-color: rgb(22, 54, 56);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(116, 63, 240,50);\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    border: 1px solid rgba(247,247,247,90);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    opacity: 0.2;\n"
"    transition: all 0.5s;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(116, 63, 240,90);\n"
"	border: 1px solid rgba(247,247,247,80);\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgb(62, 75, 75);\n"
"    border-radius: 10"
                        "px;\n"
"    border: none;\n"
"} \n"
"\n"
"QComboBox{\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 16px;\n"
"    background-color:rgb(86, 83, 90);\n"
"    border-radius: 10px;\n"
"    border:1px solid rgb(113, 111, 117);\n"
"	color:white;\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	border: 1px solid rgba(247,247,247,80);\n"
"    border-radius: 10px;\n"
"    font-family: Comic Sans MS;\n"
"    font-size: 14px;\n"
"    color: white;\n"
"    background-color:rgb(86, 83, 90)\n"
"}\n"
"QTableView {\n"
"background-color: rgb(62, 75, 75);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255"
                        ", 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.WORK_FRAME = QFrame(self.centralwidget)
        self.WORK_FRAME.setObjectName(u"WORK_FRAME")
        self.WORK_FRAME.setGeometry(QRect(10, 10, 611, 511))
        self.WORK_FRAME.setFrameShape(QFrame.StyledPanel)
        self.WORK_FRAME.setFrameShadow(QFrame.Raised)
        self.POSTGRE_SQL = QTableView(self.WORK_FRAME)
        self.POSTGRE_SQL.setObjectName(u"POSTGRE_SQL")
        self.POSTGRE_SQL.setGeometry(QRect(10, 300, 591, 201))
        self.USER_TEXT = QPlainTextEdit(self.WORK_FRAME)
        self.USER_TEXT.setObjectName(u"USER_TEXT")
        self.USER_TEXT.setGeometry(QRect(20, 50, 251, 181))
        self.TRANSLATE_TEXT = QPlainTextEdit(self.WORK_FRAME)
        self.TRANSLATE_TEXT.setObjectName(u"TRANSLATE_TEXT")
        self.TRANSLATE_TEXT.setGeometry(QRect(340, 50, 251, 181))
        self.TRANSLATE_BUTTON = QPushButton(self.WORK_FRAME)
        self.TRANSLATE_BUTTON.setObjectName(u"REANSLATE_BUTTON")
        self.TRANSLATE_BUTTON.setGeometry(QRect(210, 250, 181, 41))
        icon1 = QIcon()
        icon1.addFile(u":/iconcis/check_small_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TRANSLATE_BUTTON.setIcon(icon1)
        self.TRANSLATE_BUTTON.setIconSize(QSize(32, 32))
        self.COPY_BUTTON1 = QPushButton(self.WORK_FRAME)
        self.COPY_BUTTON1.setObjectName(u"COPY_BUTTON1")
        self.COPY_BUTTON1.setGeometry(QRect(50, 250, 31, 31))
        icon2 = QIcon()
        icon2.addFile(u":/iconcis/file_copy_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.COPY_BUTTON1.setIcon(icon2)
        self.COPY_BUTTON1.setIconSize(QSize(22, 22))
        self.VOICE_BUTTON1 = QPushButton(self.WORK_FRAME)
        self.VOICE_BUTTON1.setObjectName(u"VOICE_BUTTON1")
        self.VOICE_BUTTON1.setGeometry(QRect(130, 250, 31, 31))
        icon3 = QIcon()
        icon3.addFile(u":/iconcis/record_voice_over_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.VOICE_BUTTON1.setIcon(icon3)
        self.VOICE_BUTTON1.setIconSize(QSize(22, 22))
        self.COPY_BUTTON2 = QPushButton(self.WORK_FRAME)
        self.COPY_BUTTON2.setObjectName(u"COPY_BUTTON2")
        self.COPY_BUTTON2.setGeometry(QRect(510, 250, 31, 31))
        self.COPY_BUTTON2.setIcon(icon2)
        self.COPY_BUTTON2.setIconSize(QSize(22, 22))
        self.VOICE_BUTTON2 = QPushButton(self.WORK_FRAME)
        self.VOICE_BUTTON2.setObjectName(u"VOICE_BUTTON2")
        self.VOICE_BUTTON2.setGeometry(QRect(450, 250, 31, 31))
        self.VOICE_BUTTON2.setIcon(icon3)
        self.VOICE_BUTTON2.setIconSize(QSize(22, 22))
        self.comboBox = QComboBox(self.WORK_FRAME)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 10, 251, 22))
        self.comboBox_2 = QComboBox(self.WORK_FRAME)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(340, 10, 251, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.languages = {'Russian': 'ru', 'English': 'en', 'Ukrainian': 'uk', 'Germany': 'de', 'France': 'fr', 'Spanish': 'es', 'Italian':'it', 'Polish': 'pl'} 
        self.comboBox.addItems(self.languages.keys())
        self.comboBox_2.addItems(self.languages.keys())
        self.TRANSLATE_TEXT.setReadOnly(True)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.TRANSLATE_BUTTON.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.COPY_BUTTON1.setText("")
        self.VOICE_BUTTON1.setText("")
        self.COPY_BUTTON2.setText("")
        self.VOICE_BUTTON2.setText("")
    # retranslateUi

