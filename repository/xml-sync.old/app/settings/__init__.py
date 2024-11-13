import logging
from app.utils import from_asset, exists
import json

defaultPrefs = {
    "db_password": "",
    "db_user": "",
    "db_server": "",
    "db_name": "",
    "company": "",
    "cnpj":"",
    "sync_password":"",
    "sync_server":"https://xml.wmsistemas.inf.br",
    "sync_time": 60,
    "last_update": "",
}

class Preferences:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.filename = from_asset(__file__, 'preferences.json')
        self.load()

    def get(self, key):
        try:
            return self.data[key]
        except Exception as e:
            return ''

    def set(self, key, value):
        self.data[key] = value

    def load(self):
        if exists(self.filename):
            with open(self.filename) as json_file:
                self.data = json.load(json_file)

        else:
            self.log.info(f'Preferences file not found, creating new one')
            self.data = defaultPrefs
            self.save(self.data)

    def save(self, prefs):
        with open(self.filename, 'w') as outfile:
            self.log.info(f'Saved preferences')
            json.dump(prefs, outfile,indent=4)
