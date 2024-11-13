# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Database(object):
    def setupUi(self, Database):
        if not Database.objectName():
            Database.setObjectName(u"Database")
        Database.setWindowModality(Qt.ApplicationModal)
        Database.resize(381, 705)
        Database.setMinimumSize(QSize(0, 0))
        Database.setMaximumSize(QSize(1111111, 1111111))
        icon = QIcon()
        icon.addFile(u"../../../assets/database.png", QSize(), QIcon.Normal, QIcon.Off)
        Database.setWindowIcon(icon)
        Database.setStyleSheet(u"QGroupBox{\n"
"	border: 1px solid #d9d9d9;\n"
"	padding-top: 20px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(Database)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gbICThUS = QGroupBox(Database)
        self.gbICThUS.setObjectName(u"gbICThUS")
        self.verticalLayout_2 = QVBoxLayout(self.gbICThUS)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbServer = QLabel(self.gbICThUS)
        self.lbServer.setObjectName(u"lbServer")

        self.verticalLayout_2.addWidget(self.lbServer)

        self.leServer = QLineEdit(self.gbICThUS)
        self.leServer.setObjectName(u"leServer")
        self.leServer.setMinimumSize(QSize(0, 34))
        self.leServer.setMaximumSize(QSize(16777215, 34))

        self.verticalLayout_2.addWidget(self.leServer)

        self.lbUser = QLabel(self.gbICThUS)
        self.lbUser.setObjectName(u"lbUser")

        self.verticalLayout_2.addWidget(self.lbUser)

        self.leUser = QLineEdit(self.gbICThUS)
        self.leUser.setObjectName(u"leUser")
        self.leUser.setMinimumSize(QSize(0, 34))
        self.leUser.setMaximumSize(QSize(16777215, 34))

        self.verticalLayout_2.addWidget(self.leUser)

        self.lbPassword = QLabel(self.gbICThUS)
        self.lbPassword.setObjectName(u"lbPassword")

        self.verticalLayout_2.addWidget(self.lbPassword)

        self.lePassword = QLineEdit(self.gbICThUS)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setMinimumSize(QSize(0, 34))
        self.lePassword.setMaximumSize(QSize(16777215, 34))
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.lePassword)

        self.lbDatabase = QLabel(self.gbICThUS)
        self.lbDatabase.setObjectName(u"lbDatabase")

        self.verticalLayout_2.addWidget(self.lbDatabase)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cbDatabase = QComboBox(self.gbICThUS)
        self.cbDatabase.setObjectName(u"cbDatabase")
        self.cbDatabase.setMinimumSize(QSize(0, 34))
        self.cbDatabase.setMaximumSize(QSize(16777215, 34))

        self.horizontalLayout_2.addWidget(self.cbDatabase)

        self.btnLoadDatabases = QPushButton(self.gbICThUS)
        self.btnLoadDatabases.setObjectName(u"btnLoadDatabases")
        self.btnLoadDatabases.setMinimumSize(QSize(34, 34))
        self.btnLoadDatabases.setMaximumSize(QSize(34, 34))
        self.btnLoadDatabases.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../../../assets/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLoadDatabases.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btnLoadDatabases)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label = QLabel(self.gbICThUS)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.cbXmlDatabase = QComboBox(self.gbICThUS)
        self.cbXmlDatabase.setObjectName(u"cbXmlDatabase")
        self.cbXmlDatabase.setMinimumSize(QSize(0, 34))
        self.cbXmlDatabase.setMaximumSize(QSize(16777215, 34))

        self.verticalLayout_2.addWidget(self.cbXmlDatabase)


        self.verticalLayout_3.addWidget(self.gbICThUS)

        self.gbXML = QGroupBox(Database)
        self.gbXML.setObjectName(u"gbXML")
        self.verticalLayout = QVBoxLayout(self.gbXML)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbServerXml = QLabel(self.gbXML)
        self.lbServerXml.setObjectName(u"lbServerXml")

        self.verticalLayout.addWidget(self.lbServerXml)

        self.leServerXml = QLineEdit(self.gbXML)
        self.leServerXml.setObjectName(u"leServerXml")
        self.leServerXml.setMinimumSize(QSize(0, 34))
        self.leServerXml.setMaximumSize(QSize(16777215, 34))
        self.leServerXml.setSizeIncrement(QSize(0, 34))

        self.verticalLayout.addWidget(self.leServerXml)

        self.lbCompany = QLabel(self.gbXML)
        self.lbCompany.setObjectName(u"lbCompany")

        self.verticalLayout.addWidget(self.lbCompany)

        self.hlCompany = QHBoxLayout()
        self.hlCompany.setObjectName(u"hlCompany")
        self.cbCompany = QComboBox(self.gbXML)
        self.cbCompany.setObjectName(u"cbCompany")
        self.cbCompany.setMinimumSize(QSize(0, 34))
        self.cbCompany.setMaximumSize(QSize(16777215, 34))

        self.hlCompany.addWidget(self.cbCompany)

        self.btnLoadCompanies = QPushButton(self.gbXML)
        self.btnLoadCompanies.setObjectName(u"btnLoadCompanies")
        self.btnLoadCompanies.setMaximumSize(QSize(34, 34))
        self.btnLoadCompanies.setSizeIncrement(QSize(34, 34))
        self.btnLoadCompanies.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLoadCompanies.setIcon(icon1)

        self.hlCompany.addWidget(self.btnLoadCompanies)


        self.verticalLayout.addLayout(self.hlCompany)

        self.lbServerPassword = QLabel(self.gbXML)
        self.lbServerPassword.setObjectName(u"lbServerPassword")

        self.verticalLayout.addWidget(self.lbServerPassword)

        self.hlServer = QHBoxLayout()
        self.hlServer.setObjectName(u"hlServer")
        self.leServerPassword = QLineEdit(self.gbXML)
        self.leServerPassword.setObjectName(u"leServerPassword")
        self.leServerPassword.setMinimumSize(QSize(0, 34))
        self.leServerPassword.setEchoMode(QLineEdit.Password)

        self.hlServer.addWidget(self.leServerPassword)

        self.btnCheckServer = QPushButton(self.gbXML)
        self.btnCheckServer.setObjectName(u"btnCheckServer")
        self.btnCheckServer.setMinimumSize(QSize(30, 34))
        self.btnCheckServer.setMaximumSize(QSize(30, 34))
        self.btnCheckServer.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../../../assets/link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCheckServer.setIcon(icon2)

        self.hlServer.addWidget(self.btnCheckServer)


        self.verticalLayout.addLayout(self.hlServer)

        self.lbNotification = QLabel(self.gbXML)
        self.lbNotification.setObjectName(u"lbNotification")

        self.verticalLayout.addWidget(self.lbNotification)

        self.sbTime = QSpinBox(self.gbXML)
        self.sbTime.setObjectName(u"sbTime")
        self.sbTime.setMinimumSize(QSize(0, 34))
        self.sbTime.setMaximumSize(QSize(16777215, 34))
        self.sbTime.setMinimum(1)
        self.sbTime.setValue(60)

        self.verticalLayout.addWidget(self.sbTime)


        self.verticalLayout_3.addWidget(self.gbXML)

        self.pbLoading = QProgressBar(Database)
        self.pbLoading.setObjectName(u"pbLoading")
        self.pbLoading.setMinimumSize(QSize(0, 10))
        self.pbLoading.setMaximumSize(QSize(16777215, 10))
        self.pbLoading.setMaximum(0)
        self.pbLoading.setValue(0)

        self.verticalLayout_3.addWidget(self.pbLoading)

        self.frActions = QFrame(Database)
        self.frActions.setObjectName(u"frActions")
        self.frActions.setMaximumSize(QSize(363, 56))
        self.frActions.setStyleSheet(u"QFrame{\n"
"	border: 1px solid #d9d9d9;\n"
"}")
        self.frActions.setFrameShape(QFrame.StyledPanel)
        self.frActions.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frActions)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(self.frActions)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 34))
        self.btnCancel.setMaximumSize(QSize(100, 34))
        self.btnCancel.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"../../../assets/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCancel.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.frActions)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 32))
        self.btnSave.setMaximumSize(QSize(100, 32))
        self.btnSave.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSave.setAutoFillBackground(False)
        self.btnSave.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"../../../assets/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSave.setIcon(icon4)

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout_3.addWidget(self.frActions)


        self.retranslateUi(Database)

        QMetaObject.connectSlotsByName(Database)
    # setupUi

    def retranslateUi(self, Database):
        Database.setWindowTitle(QCoreApplication.translate("Database", u"Configura\u00e7\u00e3o da Conex\u00e3o", None))
        self.gbICThUS.setTitle(QCoreApplication.translate("Database", u"Conex\u00e3o ICThUS", None))
        self.lbServer.setText(QCoreApplication.translate("Database", u"Servidor", None))
        self.lbUser.setText(QCoreApplication.translate("Database", u"Usu\u00e1rio", None))
        self.lbPassword.setText(QCoreApplication.translate("Database", u"Senha", None))
        self.lbDatabase.setText(QCoreApplication.translate("Database", u"Banco de dados", None))
#if QT_CONFIG(tooltip)
        self.btnLoadDatabases.setToolTip(QCoreApplication.translate("Database", u"Atualizar Banco de Dados", None))
#endif // QT_CONFIG(tooltip)
        self.btnLoadDatabases.setText("")
        self.label.setText(QCoreApplication.translate("Database", u"Banco de Dados XML", None))
        self.gbXML.setTitle(QCoreApplication.translate("Database", u"Op\u00e7\u00f5es XML", None))
        self.lbServerXml.setText(QCoreApplication.translate("Database", u"Servidor XML", None))
        self.lbCompany.setText(QCoreApplication.translate("Database", u"Empresa", None))
        self.btnLoadCompanies.setText("")
        self.lbServerPassword.setText(QCoreApplication.translate("Database", u"Senha", None))
#if QT_CONFIG(tooltip)
        self.btnCheckServer.setToolTip(QCoreApplication.translate("Database", u"Checar conex\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.btnCheckServer.setText("")
        self.lbNotification.setText(QCoreApplication.translate("Database", u"Tempo para sincroniza\u00e7\u00e3o (minutos)", None))
#if QT_CONFIG(tooltip)
        self.btnCancel.setToolTip(QCoreApplication.translate("Database", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
        self.btnCancel.setText(QCoreApplication.translate("Database", u"Cancelar", None))
#if QT_CONFIG(tooltip)
        self.btnSave.setToolTip(QCoreApplication.translate("Database", u"Salvar", None))
#endif // QT_CONFIG(tooltip)
        self.btnSave.setText(QCoreApplication.translate("Database", u"Salvar", None))
    # retranslateUi

