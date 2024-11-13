import os
import re
import shutil
from time import sleep
import datetime

APP_NAME = "Portal XML"
CONSTANTS_PATH = "../app/utils/constants.py"
CLOUD_BASE_PATH = r'G:/Meu Drive/Clientes/WM Sistemas de Gestão/Portal XML/Builds/'
OLD_FILES = [
    "dist/",
    "build/",
    "Portal XML - Setup.exe",
]
DEV_FILES = [
    {'file': 'dist/run/assets/preferences.json'},
    {'file': 'dist/run/assets/database.db'},
    {'file': 'dist/run/assets/logs/', 'exception': 'xml.log'},
]

def removeContentDir(dir, exception=''):
    for f in os.listdir(dir):
        if f != exception:
            remove(filename=os.path.join(dir, f))
            
def isDirectory(filename):
    return str(filename).endswith("/")

def remove(filename):
    try:
        isFile = not isDirectory(filename=filename)
        if isFile:
            os.remove(filename)
        else:
            shutil.rmtree(filename)
    except Exception as e:
        print(e)


def removePreviusFiles():
    print("********************************")
    print("***Removendo arquivos antigos***")
    print("********************************")
    for file in OLD_FILES:
        print(f'Removendo {file}...')
        remove(file)


def generateInstaller():
    print("********************************")
    print("******Gerando Instalador********")
    print("********************************")
    os.system("pyinstaller run.spec")
    
def generateRequirements():
    print("********************************")
    print("*****Gerando Requirements*******")
    print("********************************")
    os.system("pip freeze > requirements.txt")


def removeProdFiles():
    print("********************************")
    print("***Removendo arquivos de teste**")
    print("********************************")
    for file in DEV_FILES:
        if not isDirectory(file['file']):
            print(f"Removendo arquivo {file['file']}...")
            remove(file['file'])
        else:
            exception = ''
            if 'exception' in file:
                exception = file['exception']
            print(f"Removendo diretório {file['file']}...")
            removeContentDir(dir=file['file'], exception=exception)
            
def replaceVersion(version, filename):
    with open(filename, "r") as file:
        content = file.read()
        content = re.sub(
            r"\d{4}\.\d{2}\.\d{2}\.\d{2}\.\d{2}", version, content)
        
    print(f'Alterando versão no arquivo {filename}')
    with open(filename, "w") as file:
        file.write(content)


def defineVersion(version):
    print("********************************")
    print("*******Definindo Versão*********")
    print("********************************")
    replaceVersion(version, CONSTANTS_PATH)
    replaceVersion(version, 'installer.iss')

def compile():
    print("********************************")
    print("*****Compilando Instalador******")
    print("********************************")
    os.system('iscc /q ./installer.iss')


def sendToCloud() -> str:
    print("********************************")
    print("*****Enviando para a Nuvem******")
    print("********************************")
    current_date = datetime.datetime.now()
    name = current_date.strftime("%Y-%m-%d")
    path = CLOUD_BASE_PATH
    path = f'{path}/{name}'
    os.makedirs(path, exist_ok=True)
    filename = f'{APP_NAME} - Setup.exe'
    shutil.copyfile(filename, f'{path}/{filename}')
    return f'{path}/{filename}'


if __name__ == "__main__":
    current_date = datetime.datetime.now()
    version = current_date.strftime("%Y.%m.%d.%H.%M")
    os.system('cls')
    ok = input(
        f'Tem certeza que deseja gerar a versão {version} do {APP_NAME}? ')
    os.system('cls')
    if (ok.lower() == 's' or ok.lower() == 'y'):
        defineVersion(version=version)
        removePreviusFiles()
        sleep(1)
        generateInstaller()
        generateRequirements()
        os.system('cls')
        sleep(1)
        removeProdFiles()
        compile()
        p = sendToCloud()
        print("********************************")
        print(f"*Build {version} Gerado!*")
        print("********************************")
        print(f'Caminho: {p}')
