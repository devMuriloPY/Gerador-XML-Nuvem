from PySide6.QtWidgets import QWidget
from app.utils import getIcon, getPixmap
from app.utils.constants import APP_VERSION

from app.views.about.ui_about import Ui_About
import re


class AboutUI(QWidget, Ui_About):

    def __init__(self):
        super(AboutUI, self).__init__()
        self.setupUi(self)

        self.loadComponents()

    def loadComponents(self):
        self.loadAssets()
        
        text = self.lbSite.text()

        # Substituindo a data antiga pela data atual
        content = re.sub(r"\d{4}\.\d{2}\.\d{2}\.\d{2}\.\d{2}", APP_VERSION, text)
        self.lbSite.setText(content)


    def loadAssets(self):
        self.lbLogo.setPixmap(getPixmap('logo.png'))
        self.setWindowIcon(getIcon('info.png'))
        