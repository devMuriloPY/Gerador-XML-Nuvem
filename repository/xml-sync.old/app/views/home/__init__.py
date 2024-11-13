from PySide6.QtWidgets import QMainWindow, QMenu, QSystemTrayIcon
from PySide6.QtCore import Signal
from app.utils import getIcon, getPixmap
from app.utils.constants import APP_NAME, APP_VERSION
from app.views.about import AboutUI
from app.views.database import DatabaseUI
from app.views.home.ui_home import Ui_MainWindow
import sys

class HomeUI(QMainWindow, Ui_MainWindow):

    onExit = Signal()

    def __init__(self):
        super(HomeUI, self).__init__()
        self.setupUi(self)
        self.loadComponents()

    def loadComponents(self):
        self.loadAssets()
        self.actionExit.triggered.connect(self.exitApplication)
        self.actionAbout.triggered.connect(self.openAbout)
        self.actionDatabase.triggered.connect(self.openDatabase)

        self.lbVersion.setText(f'Versão: {APP_VERSION}')

        self.initInTray()

    def loadAssets(self):
        self.setWindowIcon(getIcon('logo.png'))

        self.label.setPixmap(getPixmap('logo.png'))
        self.actionDatabase.setIcon(getIcon('database.png'))
        self.actionAbout.setIcon(getIcon('info.png'))
        self.actionExit.setIcon(getIcon('logout.png'))
        

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def initInTray(self):
        menu = QMenu()
        openAction = menu.addAction("Abrir aplicação")
        openAction.triggered.connect(self.show)

        menu.addSeparator()

        exitAction = menu.addAction("Sair")
        exitAction.triggered.connect(self.exitApplication)

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(getIcon('logo.png'))
        self.tray.setContextMenu(menu)
        self.tray.show()
        self.tray.setToolTip(APP_NAME)

    def exitApplication(self):
        self.close()
        self.onExit.emit()
        sys.exit(0)

    def openAbout(self):
        self.w = AboutUI()
        self.w.show()
        
    def openDatabase(self):
        self.w = DatabaseUI()
        self.w.show()