from datetime import date
from sqlalchemy import and_, func
from app.database import Xml, XmlEntrada, XmlInutilizada, db
from app.utils import fromEnv


class XmlController:
    error =''
    def getById(self, id):
        return Xml.query.filter_by(id=id).first()

    def getXmlStatus(self):
        return Xml.query.distinct(Xml.status)
    
    def getByCustomer(self, customer_id):
        return Xml.query.filter_by(customer_id=customer_id).all()
    
    def getByCustomerWithLimit(self, customer_id, limit = 5000):
        limit = fromEnv('LIMIT') or limit
        return Xml.query.filter_by(customer_id=customer_id).order_by(Xml.updated_at.desc()).limit(limit)
    

    def getEntradaByCustomerWithLimit(self, customer_id, limit = 5000):
        limit = fromEnv('LIMIT') or limit
        return XmlEntrada.query.filter_by(customer_id=customer_id).order_by(XmlEntrada.updated_at.desc()).limit(limit)
    
    def getInutilizadasByCustomerWithLimit(self, customer_id, limit = 5000):
        limit = fromEnv('LIMIT') or limit
        return XmlInutilizada.query.filter_by(customer_id=customer_id).order_by(XmlInutilizada.updated_at.desc()).limit(limit)
    
    def getXMLCount(self, customer_id):
        return Xml.query.filter_by(customer_id=customer_id).count()
    
    def getByFilter(self, form):
        startDate = form['start_date']
        endDate = form['end_date']
        customerId = form['customer_id']
        
        if(startDate==''):
            startDate='1970-01-01'
        if (endDate ==''):
            endDate = str(date.today())
        
        if(type(form) is dict):
            xml_status = form['xml_status']
        else:
            xml_status = form.getlist('xml_status')
        if(len(xml_status)>0):
            return Xml.query.filter(and_(func.date(Xml.date) >= startDate),\
                                                func.date(Xml.date) <= endDate)\
                                                .filter(Xml.status.in_(xml_status))\
                                                .filter(Xml.customer_id == customerId).all()
        else:
            return Xml.query.filter(and_(func.date(Xml.date) >= startDate),\
                                                func.date(Xml.date) <= endDate)\
                                                    .filter(Xml.customer_id == customerId).all()
    def exists(self, code, status, md5)->int:
        try:
            xml = Xml.query.filter_by(nf_code=code, status=status,  md5=md5).first()
            if xml:
                return xml.id
            else:
                return 0
        except Exception as e:
            return 0
        
    def existsEntrada(self, code, status, md5)->int:
        try:
            xml = XmlEntrada.query.filter_by(nf_code=code, status=status,  md5=md5).first()
            if xml:
                return xml.id
            else:
                return 0
        except Exception as e:
            return 0
        
    def add(self, form, customer):
        try:
            self.error = ''
            if(form['type'] == 'entrada'):
                id = self.existsEntrada(form['nf_code'], status=form['status'], md5=form['md5'])
            else:
                id = self.exists(form['nf_code'], status=form['status'], md5=form['md5'])
            x = Xml(
                nf_code=form['nf_code'],
                xml_type=form['xml_type'],
                xml=form['xml'],
                md5=form['md5'],
                df_model=form['df_model'],
                nf_number=form['nf_number'],
                status=form['status'],
                date=form['date'],
                nf_key =form['nf_key']
            )
            if (id==0):
                customer.xmls.append(x)
                db.session.add(customer)
            else:
                x.id = id
            db.session.commit()
        except Exception as e:
            self.error = str(e)