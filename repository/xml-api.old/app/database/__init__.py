from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Xml(db.Model):
    __tablename__ = 'xmls'
    id = db.Column(db.Integer, primary_key=True)

    nf_code = db.Column(db.String)
    xml_type = db.Column(db.String)
    xml = db.Column(db.Text)
    md5 = db.Column(db.String)
    df_model = db.Column(db.String)
    nf_number = db.Column(db.String)
    status = db.Column(db.String)
    date = db.Column(db.Date)
    nf_key = db.Column(db.String)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())


class XmlEntrada(db.Model):
    __tablename__ = 'xmls_entradas'
    id = db.Column(db.Integer, primary_key=True)

    nf_code = db.Column(db.String)
    xml_type = db.Column(db.String)
    xml = db.Column(db.Text)
    md5 = db.Column(db.String)
    df_model = db.Column(db.String)
    nf_number = db.Column(db.String)
    status = db.Column(db.String)
    date = db.Column(db.Date)
    nf_key = db.Column(db.String)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())


class XmlInutilizada(db.Model):
    __tablename__ = 'xmls_inutilizadas'
    id = db.Column(db.Integer, primary_key=True)

    modelo_df = db.Column(db.String)
    numero_nf = db.Column(db.String)
    protocolo_inutilizacao = db.Column(db.String)
    data_inutilizacao = db.Column(db.Date)
    md5 = db.Column(db.String)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)

    active = db.Column(db.Boolean, default=True)
    name = db.Column(db.String)
    cnpj = db.Column(db.String)
    email = db.Column(db.Text)
    phone = db.Column(db.Text)
    password = db.Column(db.String)

    accountant_id = db.Column(db.Integer, db.ForeignKey('accountants.id'))
    xmls = db.relationship("Xml", backref="customers",
                           cascade="all, delete-orphan", uselist=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())


class Accountant(db.Model):
    __tablename__ = 'accountants'
    id = db.Column(db.Integer, primary_key=True)

    active = db.Column(db.Boolean, default=True)
    name = db.Column(db.String)
    cnpj = db.Column(db.String)
    email = db.Column(db.Text)
    phone = db.Column(db.Text)

    password = db.Column(db.String)
    customers = db.relationship(
        "Customer", backref="accountants", cascade="all, delete-orphan", uselist=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())
