# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'First7.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
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
        self.label.setGeometry(QRect(480, 160, 591, 151))
        font = QFont()
        font.setFamilies([u"Javanese Text"])
        font.setPointSize(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(430, 330, 691, 61))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;     \n"
"padding: 5px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 400, 741, 141))
        font2 = QFont()
        font2.setFamilies([u"Javanese Text"])
        font2.setPointSize(25)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 540, 751, 181))
        self.label_3.setFont(font2)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 710, 1011, 141))
        self.label_4.setFont(font2)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 1060, 1491, 90))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setBold(True)
        font3.setUnderline(False)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_5)

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

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1280, 880, 171, 161))
        icon1 = QIcon()
        icon1.addFile(u"home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(150, 150))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(1010, 870, 61, 61))
        self.pushButton_9.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"\ud654\uc0b4\ud45c.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QSize(45, 45))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(480, 870, 591, 61))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setPointSize(15)
        self.textEdit.setFont(font5)
        self.textEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 10px;     \n"
"padding: 5px;")
        self.textEdit.setFrameShape(QFrame.WinPanel)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(2)
        self.textEdit.setLineWrapMode(QTextEdit.WidgetWidth)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.plainTextEdit.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.verticalLayoutWidget.raise_()
        self.pushButton_6.raise_()
        self.textEdit.raise_()
        self.pushButton_9.raise_()
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"USER", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NONE!!!", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\uc785\ub825\ubc1b\uc740 URL \ud45c\uc2dc", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc785\ub825\ubc1b\uc740 URL \ud45c\uc2dc", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DB\uc5d0 \uc5c6\ub294 \uc0c8\ub85c\uc6b4 URL \uc785\ub2c8\ub2e4.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825\ud558\uc2e0 URL\uc740 \n"
"\uc790\ub3d9\uc801\uc73c\ub85c \uc811\uc218\uc644\ub8cc \ub418\uc5c8\uc2b5\ub2c8\ub2e4.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc774\uba54\uc77c \uc785\ub825\ud558\uc2dc\uba74 \uacb0\uacfc \ubc1b\uc744 \uc218 \uc788\uc2b5\ub2c8\ub2e4.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\ub300\ud55c\ubbfc\uad6d", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\uad11\uace0\ubb38\uc758", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\ube44\uc988\ub2c8\uc2a4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\uc57d\uad00", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub77c\uc774\uc5b8\ud2b8 \uba85\uc138\uc11c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"AI \uae30\uc220 \ubc0f \ubaa8\ub378", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uc545\uc131URL \ubaa8\uc74c\uc9d1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ucee4\ubba4\ub2c8\ud2f0", None))
        self.pushButton_6.setText("")
        self.pushButton_9.setText("")
#if QT_CONFIG(tooltip)
        self.textEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
#endif // QT_CONFIG(tooltip)
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim';\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc774\uba54\uc77c\uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
    # retranslateUi

