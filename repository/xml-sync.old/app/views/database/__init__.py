from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QThread, Signal
from PySide6.QtCore import Signal
from app.icthus import ICThUSSdk
from app.services.sync_server import SyncServer
from app.settings import Preferences
from app.utils import getIcon, getPixmap, restartApp

from app.views.database.ui_database import Ui_Database

import logging


class DatabaseUI(QDialog, Ui_Database):

    onChange = Signal()
    
    cnpj = ''
    company = ''

    def __init__(self):
        super(DatabaseUI, self).__init__()
        self.setupUi(self)
        self.log = logging.getLogger(__name__)
        self.loadComponents()

    def loadComponents(self):
        self.loadAssets()
        self.btnCancel.clicked.connect(self.close)
        self.btnSave.clicked.connect(self.save)
        self.btnLoadDatabases.clicked.connect(self.loadDatabases)
        self.btnLoadCompanies.clicked.connect(self.loadCompanies)
        self.btnCheckServer.clicked.connect(self.checkServer)
        self.cbCompany.currentTextChanged.connect(self.onCompanyChange)
        self.pbLoading.setVisible(False)

        self.loadFields()

    def loadAssets(self):
        self.btnLoadDatabases.setIcon(getPixmap('refresh.png'))
        self.btnLoadCompanies.setIcon(getPixmap('refresh.png'))
        self.btnCheckServer.setIcon(getPixmap('link.png'))
        self.btnCancel.setIcon(getPixmap('back.png'))
        self.btnSave.setIcon(getPixmap('check.png'))
        self.setWindowIcon(getIcon('database.png'))
        
    def loadCompanies(self):
        try:

            self.save(silent=True)

            self.thread = QThread(self)
            self.worker = WorkerCompany(self.cbDatabase.currentText())
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.loading.connect(self.onLoading)
            self.worker.result.connect(self.onResultCompany)
            self.worker.error.connect(self.onError)
            self.worker.finished.connect(self.thread.quit)
            self.thread.finished.connect(self.thread.deleteLater)

            self.thread.start()

        except Exception as e:
            self.log.error(e)
            QMessageBox.critical(
                self, 'Ops...', str(e))
        
    def onCompanyChange(self, value):
        self.company = value
        if hasattr(self, 'companies'):
            for company in self.companies:
                if(company['Razão Social'] == self.company):
                    self.cnpj = company['CNPJ']


    def loadFields(self):
        self.prefs = Preferences()
        
        self.company = self.prefs.get('company')
        self.cnpj = self.prefs.get('cnpj')
        
        self.cbCompany.addItem(self.company)
        self.cbCompany.setItemText(0, self.company)
        self.leServerPassword.setText(self.prefs.get('sync_password'))
        self.leServerXml.setText(self.prefs.get('sync_server'))
        self.sbTime.setValue(self.prefs.get('sync_time'))

        self.leServer.setText(self.prefs.get('db_server'))
        self.leUser.setText(self.prefs.get('db_user'))
        self.lePassword.setText(self.prefs.get('db_password'))

        self.cbDatabase.addItem(self.prefs.get('db_name'))
        self.cbDatabase.setItemText(0, self.prefs.get('db_name'))

        self.cbXmlDatabase.addItem(self.prefs.get('xml_db_name'))
        self.cbXmlDatabase.setItemText(0, self.prefs.get('xml_db_name'))


    def checkServer(self):
        if (self.leServerXml.text() == ''):
            QMessageBox.warning(self, 'Ops...', 'Informe o servidor XML')
        elif (self.cnpj == ''):
            QMessageBox.warning(self, 'Ops...', 'Informe a empresa')
        elif (self.leServerPassword.text() == ''):
            QMessageBox.warning(self, 'Ops...', 'Informe a senha')
        else:
            server = SyncServer()
            if server.checkServer(self.leServerXml.text(), self.cnpj, self.leServerPassword.text()):
                QMessageBox.information(self, 'Sucesso!', 'A sincronização pode ser realizada')
            else:
                
                QMessageBox.warning(self, 'Ops...', f'Ocorreu um erro ao validar informações do sincronizador.\n{server.error}')

    def save(self, silent=False):
        try:
            self.prefs.set('sync_server', self.leServerXml.text())
            self.prefs.set('company', self.company)
            self.prefs.set('cnpj', self.cnpj)
            self.prefs.set('sync_password', self.leServerPassword.text())
            self.prefs.set('sync_time', self.sbTime.value())
            self.prefs.set('db_server', self.leServer.text())
            self.prefs.set('db_user', self.leUser.text())
            self.prefs.set('db_password', self.lePassword.text())
            self.prefs.set('db_name', self.cbDatabase.currentText())
            self.prefs.set('xml_db_name', self.cbXmlDatabase.currentText())

            self.prefs.save(self.prefs.data)
            self.onChange.emit()

            if(not silent):
                self.close()
                QMessageBox.information(
                    self, 'Sucesso', 'As configurações foram salvas')
                restartApp()

        except Exception as e:
            self.log.error(e)
            QMessageBox.critical(
                self, 'Ops...', str(e))

    def onError(self, error):
        self.cbDatabase.clear()
        self.cbCompany.clear()
        QMessageBox.critical(
            self, 'Ops...', str(error))

    def onResult(self, result):
        self.cbDatabase.clear()
        self.cbDatabase.addItems(result)
        self.cbXmlDatabase.clear()
        self.cbXmlDatabase.addItems(result)
    
        
    def onResultCompany(self, companies):
        self.companies = companies
        
        self.cbCompany.clear()
        listCompanies = []
        for company in companies:
            listCompanies.append(company['Razão Social'])
            
        self.cbCompany.addItems(listCompanies)

    def onLoading(self, loading):
        if(loading):
            self.pbLoading.setVisible(True)
            self.btnLoadDatabases.setEnabled(False)
            self.btnSave.setEnabled(False)
        else:
            self.pbLoading.setVisible(False)
            self.btnLoadDatabases.setEnabled(True)
            self.btnSave.setEnabled(True)

    def loadDatabases(self):
        try:

            self.save(silent=True)

            self.thread = QThread(self)
            self.worker = Worker()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.loading.connect(self.onLoading)
            self.worker.result.connect(self.onResult)
            self.worker.error.connect(self.onError)
            self.worker.finished.connect(self.thread.quit)
            self.thread.finished.connect(self.thread.deleteLater)

            self.thread.start()

        except Exception as e:
            self.log.error(e)
            QMessageBox.critical(
                self, 'Ops...', str(e))


class Worker(QThread):

    finished = Signal()
    loading = Signal(bool)
    result = Signal(list)
    error = Signal(str)

    def __init__(self):
        QThread.__init__(self)
        self.log = logging.getLogger(__name__)

    def run(self):
        self.loading.emit(True)
        try:
            self.db = ICThUSSdk()
            databases = self.db.get_databases()
            self.result.emit(databases)
        except Exception as e:
            self.log.error(e)
            self.error.emit(str(e))
        finally:
            self.loading.emit(False)
            self.finished.emit()


class WorkerCompany(QThread):

    finished = Signal()
    loading = Signal(bool)
    result = Signal(list)
    error = Signal(str)

    def __init__(self, database):
        QThread.__init__(self)
        self.database = database
        self.log = logging.getLogger(__name__)

    def run(self):
        self.loading.emit(True)
        try:
            self.db = ICThUSSdk()
            databases = self.db.get_companies(self.database)
            self.result.emit(databases)
        except Exception as e:
            self.log.error(e)
            self.error.emit(str(e))
        finally:
            self.loading.emit(False)
            self.finished.emit()