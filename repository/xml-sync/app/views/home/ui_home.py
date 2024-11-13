# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(752, 472)
        icon = QIcon()
        icon.addFile(u"../../../assets/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u"../../../assets/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon()
        icon2.addFile(u"../../../assets/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionDatabase = QAction(MainWindow)
        self.actionDatabase.setObjectName(u"actionDatabase")
        icon3 = QIcon()
        icon3.addFile(u"../../../assets/database.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDatabase.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(113, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 43, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(441, 280))
        self.label.setMaximumSize(QSize(441, 280))
        self.label.setTextFormat(Qt.AutoText)
        self.label.setPixmap(QPixmap(u"../../../assets/logo.png"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.lbVersion = QLabel(self.frame)
        self.lbVersion.setObjectName(u"lbVersion")
        font = QFont()
        font.setBold(True)
        self.lbVersion.setFont(font)
        self.lbVersion.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbVersion)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer = QSpacerItem(112, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 752, 21))
        self.menubar.setStyleSheet(u"QMenuBar{\n"
"	background-color: #de052e;\n"
"	color: white;\n"
"}")
        self.menubar.setNativeMenuBar(True)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionDatabase)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Portal XML - Sync", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.actionDatabase.setText(QCoreApplication.translate("MainWindow", u"Banco de dados", None))
        self.label.setText("")
        self.lbVersion.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o: 2022.01.01.11.11", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
    # retranslateUi

