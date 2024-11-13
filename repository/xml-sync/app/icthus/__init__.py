import logging
import pyodbc
from app.settings import Preferences


class ICThUSSdk:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.prefs = Preferences()

        self.server = self.prefs.get('db_server')
        self.name = self.prefs.get('db_name')
        self.user = self.prefs.get('db_user')
        self.password = self.prefs.get('db_password')

        if (self.server != '' and self.user != '' and self.password != ''):
            self.__connectDb()

    def __connectDb(self):
        try:
            self.db = pyodbc.connect((
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "Server={"+self.server+"};"
                f"Database={self.name};"
                f"UID={self.user};"
                f"PWD={self.password};"
            ))
        except Exception as e:
            self.log.error(e)

    def __getCursor(self):
        try:
            if not hasattr(self, 'db'):
                self.__connectDb()
            return self.db.cursor()
        except Exception as e:
            self.log.error(e)
            self.__connectDb()
            try:
                return self.db.cursor()
            except Exception as es:
                self.log.error("Falha ao obter cursor")
                self.log.error(es)

    def getXmls(self) -> list:
        cursor = self.__getCursor()
        sql = f""" 
            SELECT  [NF XML].[Código NF],
                    [NF XML].[Tipo XML],
                    [NF XML].[XML NFe],
                    [NF XML].[MD5],
                    [NF].[Modelo DF],
                    [NF].[Número NF],
                    [NF].[Status NFe],
                    [NF].[Data Emissão],
                    [NF].[Chave NFe]
            FROM [NF XML] 
            INNER JOIN [NF] 
            ON [NF XML].[Código NF] = [NF].[Código NF]
            
             WHERE [NF].[Status NFe] in (\'2 - Autorizada\', \'3 - Cancelada\', \'4 - Denegada\');
        """
        cursor.execute(sql)
        r = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]

        data = (r[0] if r else None) if None else r
        return data
    
    def getXmlsEntradas(self) -> list:
        cursor = self.__getCursor()
        sql = f""" 
            SELECT  [Entradas XML].[Código Entrada NF],
                    [Entradas XML].[Tipo XML],
                    [Entradas XML].[XML NFe],
                    [Entradas XML].[MD5],
                    [NF].[Modelo DF],
                    [NF].[Número NF],
                    [NF].[Status NFe],
                    [NF].[Data Emissão],
                    [NF].[Chave NFe]
            FROM [Entradas XML] 
            INNER JOIN [NF] 
            ON [Entradas XML].[Código Entrada NF] = [NF].[Código NF];
        """
        cursor.execute(sql)
        r = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]

        data = (r[0] if r else None) if None else r
        return data
    
    def getNfInutilizadas(self) -> list:
        cursor = self.__getCursor()
        sql = f""" 
            SELECT [NF Inutilizadas].[Modelo DF]
                ,[NF Inutilizadas].[Número NF]
                ,[Protocolo Inutilização]
                ,[Data Inutilização]
                ,[Hora Inutilização]
                ,[NF Inutilizadas].[MD5]
            FROM [WM_Tijolar].[dbo].[NF Inutilizadas];
            /****** INNER JOIN [NF] ON [NF Inutilizadas].[Número NF] = [NF].[Código NF] ******/
        """
        cursor.execute(sql)
        r = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]

        data = (r[0] if r else None) if None else r
        return data

    def get_databases(self):
        cursor = self.__getCursor()
        sql = 'SELECT name FROM sys.databases'
        cursor.execute(sql)
        databases = []
        for row in cursor.fetchall():
            databases.append(row[0])
        return databases

    def get_companies(self, database = ''):
        if (database!=''):
            self.name = database
        cursor = self.__getCursor()
        sql = f""" 
            SELECT *
            FROM [{self.name}].[dbo].[Empresas];
        """
        print(sql)
        cursor.execute(sql)
        r = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]

        data = (r[0] if r else None) if None else r
        return data

    def __get(self, table, fields='*', where=''):
        cursor = self.__getCursor()
        sql = f""" 
            SELECT {fields}
            FROM [{self.name}].[dbo].[{table}]
            {where};
        """
        cursor.execute(sql)
        r = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]

        data = (r[0] if r else None) if None else r
        return data