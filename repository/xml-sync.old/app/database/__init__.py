from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.settings import Preferences


prefs = Preferences()

# Obtendo as informações de conexão do banco de dados
db_host = prefs.get('db_server')
db_name = prefs.get('xml_db_name')
db_user = prefs.get('db_user')
db_password = prefs.get('db_password')

# Criando a string de conexão
connection_string = f"mssql+pyodbc://{db_user}:{db_password}@{db_host}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server"

# Criando o mecanismo de conexão
engine = create_engine(connection_string)

# Criando sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criando tabela
Base = declarative_base()

class Sync(Base):
    __tablename__ = 'syncs'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    md5 = Column(String)
    status = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

class SyncEntrada(Base):
    __tablename__ = 'syncs_entradas'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    md5 = Column(String)
    status = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

class SyncNfInutilizada(Base):
    __tablename__ = 'syncs_nf_inutilizadas'
    id = Column(Integer, primary_key=True)
    
    modelo_df = Column(String)
    numero_nf = Column(String)
    protocolo_inutilizacao = Column(String)
    data_inutilizacao=Column(String)
    md5 = Column(String)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

Base.metadata.create_all(engine)
