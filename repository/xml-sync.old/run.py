import threading
from PySide6.QtWidgets import QApplication, QStyleFactory
from app.services.log import Log
from app.utils import runAsAdmin
from app.utils.constants import DEBUG_MODE
from app.views.home import HomeUI
from app.services import TaskService
from tendo import singleton
from tendo.singleton import SingleInstanceException
import sys
import ctypes

def run():

    log = Log()
    log.init()

    service = TaskService()
    service.startSchedule()
    t = threading.Thread(target=service.execute)
    t.start()

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))

    window = HomeUI()
    window.onExit.connect(service.stopSchedule)
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    if(DEBUG_MODE):
        run()
    else:
        try:
            single = singleton.SingleInstance()
            runAsAdmin(func=run)
        except SingleInstanceException as e:
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Já existe uma instância do programa em execução', 'Ops...',  0x0 | 0x10)