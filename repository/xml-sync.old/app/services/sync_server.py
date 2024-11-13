import logging
from app.settings import Preferences
from app.database import session, Sync
import requests

class SyncServer:
    error = ''
    
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.prefs  = Preferences()
        self.url = self.prefs.get('sync_server')+'/api'
        
    def existsLocal(self, code, status, md5):
        return session.query(Sync)\
            .filter(Sync.md5 == md5)\
            .filter(Sync.code == code)\
            .filter(Sync.status == status)\
            .first()
        
    def saveLocal(self, code, md5, status):
        sync = Sync(
            code=code,
            md5=md5,
            status = status
        )
        local = self.existsLocal(code, status, md5)
        if (local is None):
            session.add(sync)
        else:
            sync.id = local.id
            sync.code = code
            sync.md5 = md5
            sync.status = status
        session.commit()
            
    def sendXml(self, data)->bool:
        try:
            res = requests.post(self.url+'/send-xml', json={
                'cnpj': self.prefs.get('cnpj'),
                'password': self.prefs.get('sync_password'),
                **data
            })
            self.error = ''
            return res.ok
        except Exception as e:
            self.log.error(e)
            self.error = str(e) 
            return False
        
    def checkServer(self, server, cnpj, password)->bool:
        try:
            self.url = server+'/api'
            res = requests.post(self.url+'/check', json={
                'cnpj':cnpj,
                'password': password,
            })
            print(res.text)
            if res.ok:
                return True 
            else:
                self.error = res.json['msg']
                return False
        except Exception as e:
            self.error = f'Falha ao verificar servidor. {str(e)}'
            return False
        