
import glob
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMessageBox
from decimal import Decimal
from decimal import Decimal
import schedule
import time
import threading
import os
import ctypes
import json
import platform
import sys
import time

def get_path(context, filename) -> str:
    path = os.path.dirname(os.path.abspath(context))
    return os.path.join(path, filename)


def getPixmap(name):
    return QPixmap(from_asset(__file__, name))

def ask(parent=None, title: str = 'Atenção', message: str = None) -> bool:
    box = QMessageBox(parent=parent)
    box.setIcon(QMessageBox.Question)
    box.setWindowTitle(title)
    box.setText(message)
    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    box.setDefaultButton(QMessageBox.Yes)

    yesButton = box.button(QMessageBox.Yes)
    yesButton.setText("Sim")
    noButton = box.button(QMessageBox.No)
    noButton.setText("Não")

    return box.exec_() == QMessageBox.Yes



def getIcon(name):
    return QIcon(from_asset(__file__, name))


def getAsset(name):
    return from_asset(__file__, name)


def from_asset(context, filename) -> str:
    return get_path(context, '../../assets/' + filename)


def get_asset_path() -> str:
    return get_path(__file__, '../../assets/')


def exists(path) -> bool:
    return os.path.exists(path)


def createDirs(path):
    os.makedirs(path)

def restartApp():
    os.execl(sys.executable, sys.executable, *sys.argv)


def run_continuously(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

def is_admin() -> bool:
    if (any(platform.win32_ver())):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        return True


def fill(txt, times=1):
    s = ''
    for i in range(times):
        s += txt
    return s


def runAsAdmin(func):
    if (not is_admin()):
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        func()


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
