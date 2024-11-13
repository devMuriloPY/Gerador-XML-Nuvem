# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.setWindowModality(Qt.ApplicationModal)
        About.resize(366, 320)
        About.setMinimumSize(QSize(366, 320))
        About.setMaximumSize(QSize(366, 320))
        self.verticalLayout_2 = QVBoxLayout(About)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(About)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbLogo = QLabel(self.frame)
        self.lbLogo.setObjectName(u"lbLogo")
        self.lbLogo.setMaximumSize(QSize(181, 120))
        self.lbLogo.setPixmap(QPixmap(u"../../../assets/logo.png"))
        self.lbLogo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.lbLogo)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.lbSite = QLabel(About)
        self.lbSite.setObjectName(u"lbSite")
        self.lbSite.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.lbSite)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"Sobre", None))
        self.lbLogo.setText("")
        self.lbSite.setText(QCoreApplication.translate("About", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#888a85;\">Vers\u00e3o:</span><span style=\" font-size:10pt; color:#888a85;\"> 2023.01.16.16.35</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#888a85;\">Denvolvedor: </span><span style=\" font-size:10pt; color:#888a85;\">Awake Tecnologia</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#888a85;\">Distribui\u00e7\u00e3o:</span><span style=\" font-size:10pt; color:#888a85;\"> WM Sistemas de Gest\u00e3o</span></p><p align=\"center\"><a href=\"http://awaketecnologia.com.br\"><span style=\" text-decoration: underline; color:#1b6acb;\">www.awaketecnologia.com.br</span></a></p></body></html>", None))
    # retranslateUi

