
from app.database import Customer, db

class CustomerController:
    
    error = ''

    def get(self):
        return Customer.query.all()
    
    def getFromAccountant(self, id):
        return Customer.query.filter_by(accountant_id=id).all()
    
    def getBy(self, id):
        return Customer.query.filter_by(id=id).first()
     
    def login(self, cnpj, password):  
        customer = Customer.query.filter_by(cnpj=cnpj, password=password).first()
        if customer:
            return customer 
        else:
            return None
        
    def exists(self, cnpj):
        customer = Customer.query.filter_by(cnpj=cnpj).first()
        return customer!=None
        
    def delete(self, id):
        customer = Customer.query.filter_by(id=id).first()
        if customer:
            db.session.delete(customer)
            db.session.commit()
            
    def addCustomer(self, form):
        data = {**form}
        customer = Customer(**data)
        if('id' not in data):
            db.session.add(customer)
        else:
            customer = Customer.query.filter_by(id=data['id']).update(data)
        db.session.commit()
        return customer