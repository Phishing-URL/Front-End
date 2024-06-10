# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'First4.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 1200)
        icon = QIcon()
        icon.addFile(u"\ud574\uace8.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(72, 72, 72);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(520, 300, 491, 151))
        font = QFont()
        font.setFamilies([u"Javanese Text"])
        font.setPointSize(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(470, 500, 591, 61))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(15)
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;     \n"
"padding: 5px;")
        self.textEdit.setFrameShape(QFrame.WinPanel)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(2)
        self.textEdit.setLineWrapMode(QTextEdit.WidgetWidth)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1000, 500, 61, 61))
        self.pushButton_6.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"\ub3cb\ubcf4\uae30.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(45, 45))
        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(510, 570, 141, 41))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(7)
        self.commandLinkButton.setFont(font2)
        self.commandLinkButton_2 = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        self.commandLinkButton_2.setGeometry(QRect(870, 570, 141, 41))
        self.commandLinkButton_2.setFont(font2)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 1070, 1491, 90))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setBold(True)
        font3.setUnderline(False)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_8 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        font4 = QFont()
        font4.setBold(True)
        self.pushButton_8.setFont(font4)
        self.pushButton_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font4)
        self.pushButton_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(1270, 870, 171, 161))
        icon2 = QIcon()
        icon2.addFile(u"home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QSize(150, 150))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1500, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"URL-SCAN", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"URL-SCAN", None))
#if QT_CONFIG(tooltip)
        self.textEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
#endif // QT_CONFIG(tooltip)
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim';\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URL \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_6.setText("")
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\ud53c\uc2f1 URL \uac80\uc0c9", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"OWASP TOP 10", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ub300\ud55c\ubbfc\uad6d", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\uad11\uace0\ubb38\uc758", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\ube44\uc988\ub2c8\uc2a4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\uc57d\uad00", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub77c\uc774\uc5b8\ud2b8 \uba85\uc138\uc11c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"AI \uae30\uc220 \ubc0f \ubaa8\ub378", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uc545\uc131URL \ubaa8\uc74c\uc9d1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ucee4\ubba4\ub2c8\ud2f0", None))
        self.pushButton_9.setText("")
    # retranslateUi

