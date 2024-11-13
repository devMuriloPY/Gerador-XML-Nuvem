from app.icthus import ICThUSSdk
from app.services.log import Log
from app.services.sync_server import SyncServer
from app.settings import Preferences
from app.utils import  run_continuously
from datetime import datetime
import logging
import schedule

class TaskService:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.prefs = Preferences()
        self.executing = False

    def startSchedule(self):
        time = int(self.prefs.get('sync_time'))
        schedule.every(time).minutes.do(self.execute)
        schedule.every(1).minutes.do(self.deleteOldLogs)
        schedule.every(1).minutes.do(self.test)
        self.service_thread = run_continuously()

    def deleteOldLogs(self):
        self.log.info('Deletando logs antigos')
        log = Log()
        log.delete_old_logs()

    def test(self):
        self.log.info('Executing...')
        
    def stopSchedule(self):
        self.service_thread.set()

    def restartSchedule(self):
        self.stopSchedule()
        self.startSchedule()
        
    def hasConnection(self)->bool:
        try:
            self.prefs = Preferences()
            if (self.prefs.get('db_server') == ''):
                return False 
            if (self.prefs.get('db_user') == ''):
                return False 
            if (self.prefs.get('db_name') == ''):
                return False 
            if (self.prefs.get('db_password') == ''):
                return False 
            if (self.prefs.get('cnpj') == ''):
                return False 
            if (self.prefs.get('sync_password') == ''):
                return False 
            if (self.prefs.get('sync_server') == ''):
                return False 
            
            ok = SyncServer().checkServer(self.prefs.get('sync_server'), self.prefs.get('cnpj'), self.prefs.get('sync_password'))
            if(not ok):
                return False
            
            return True
        except Exception as e:
            return False
        
    def getListToSync(self)->list:
        listToSync = []
        if self.hasConnection():
            xmls = ICThUSSdk().getXmls()
            self.log.info(f'{len(xmls)} encontrados')
            sync = SyncServer()
            for xml in xmls:
                local = sync.existsLocal(xml['Código NF'], xml['Status NFe'], xml['MD5'])
                if local is None:
                    listToSync.append(xml)      
        else:
            self.log.info('sem conexão') 
        return listToSync
                

    def execute(self):
        if(not self.executing):
            self.log.info('Iniciando sincronizacao...')
            self.executing = True
            try:
                xmls = self.getListToSync()
                self.log.info(f'{len(xmls)} para sincronizar')
                sync = SyncServer()
                for xml in xmls:
                    self.log.info(f'Sincronizando XML Código {xml["Código NF"]}...')
                    try:
                        data = {
                            'nf_code': xml['Código NF'],
                            'xml_type': xml['Tipo XML'],
                            'xml': xml['XML NFe'],
                            'md5': xml['MD5'],
                            'df_model': xml['Modelo DF'],
                            'nf_number': xml['Número NF'],
                            'status': xml['Status NFe'],
                            'date': xml['Data Emissão'].strftime('%Y-%m-%d'),
                            'nf_key': xml['Chave NFe']
                        }
                        ok = sync.sendXml(data)
                        if(ok):
                            self.log.info(f'XML {xml["Código NF"]} sincronizado!')
                            sync.saveLocal(code=xml['Código NF'], md5=xml['MD5'], status=xml['Status NFe'])
                        else:
                            self.log.error(f'Falha ao sincronizar XML: {xml}.\n{sync.error}')
                    except Exception as ex:
                        self.log.error(ex)
                        self.log.error(f'Falha ao sincronizar {xml}')
            except Exception as e:
                self.log.error(e)
                self.log.error(f'Falha ao buscar xmls.')
            finally:
                self.log.info('Sincronizacao finalizada...')
                self.prefs.set('last_update', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                self.prefs.save(self.prefs.data)
                self.executing = False
        else:
            self.log.info('Sincronizacao em andamento...')
