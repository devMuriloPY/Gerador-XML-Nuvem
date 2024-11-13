from functools import wraps
from dotenv import load_dotenv, dotenv_values
from flask import session, redirect, url_for
import os
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime

load_dotenv(override=True)

def fromEnv(key):
    return dotenv_values()[key] or ''

def getDotEnvValues():
    return dotenv_values()

def get_path(filename) -> str:
    path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(path, filename)

def getZipFile(filename):
    return get_path(f"../../zip/{filename}")

def getZipFolder(filename):
    xml_folder = get_path(f"../../zip/{filename}")
    if not os.path.exists(xml_folder):
        try:
            os.makedirs(xml_folder)
        except Exception as e:
            print(f'Problema ao criar pasta {str(e)}')
    
    return xml_folder

def createFile(xml, name='xml'):
    xml_folder = getZipFolder(f'xml/')
    clear_directory(xml_folder)
    root = ET.fromstring(xml.xml) # Converte a string XML em objeto ElementTree
    tree = ET.ElementTree(root)
    file_name = f'{name}.xml'
    tree.write(f'{xml_folder}/{file_name}')
    return getZipFolder(f'xml/')+file_name

def clear_directory(path):
    try:
        files = os.listdir(path)
        for file in files:
            os.remove(os.path.join(path, file))
    except Exception as e:
        print(f"Falha ao limpar diretorio {path}.\n{str(e)}")

def createZip(xmls, name='xml', clean =True):
    xml_folder = getZipFolder(f'{name}/xml_files')
    if(clean):
        clear_directory(xml_folder)
    
    for i, d in enumerate(xmls):
        root = ET.fromstring(d.xml) # Converte a string XML em objeto ElementTree
        tree = ET.ElementTree(root)
        file_name = f'{d.nf_number}.xml'
        tree.write(f'{xml_folder}/{file_name}') # Salva o arquivo XML na pasta criada
    zip_name = f'{name}.zip'
    with zipfile.ZipFile(getZipFile(zip_name), 'w') as myzip:
        for file in os.listdir(xml_folder):
            myzip.write(f'{xml_folder}/{file}', arcname=file) # Adiciona todos os arquivos XML à pasta ZIP
            
    if(clean):
        clear_directory(xml_folder)
    return getZipFile(zip_name)
    
def checkLogin(user, password)->bool:
    adminUsername = os.getenv('USERNAME')
    adminPassword = os.getenv('PASSWORD')
    return user == adminUsername and password == adminPassword

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

def is_logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged' in session:
            return redirect(url_for('home'))
        return func(*args, **kwargs)
    return wrapper

def is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'admin' not in session or (not session.get('admin')):
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper

def toMMYY(date):
    return datetime.strptime(date, "%Y-%m-%d").strftime("%m_%y")

def toDDMMYY(date):
    return datetime.strptime(date, "%Y-%m-%d").strftime("%d_%m_%y")

def secretKey():
    return os.getenv('SECRET_KEY')

def getFromEnv(key):
    return os.getenv(key)