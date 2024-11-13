from app.controllers.customer_controller import CustomerController
from app.database import Accountant,db

class AccountantController:

    def get(self):
        return Accountant.query.all()
    
    def exists(self, cnpj):
        accountant = Accountant.query.filter_by(cnpj=cnpj).first()
        return accountant!=None

    def checkLogin(self, cnpj, password):
        accountant = Accountant.query.filter_by(cnpj=cnpj, password=password).first()
        return accountant!=None
    
    def getBy(self, cnpj):
        accountant = Accountant.query.filter_by(cnpj=cnpj).first()
        return accountant
    
    def getById(self, id):
        accountant = Accountant.query.filter_by(id=id).first()
        return accountant
        
    def delete(self, id):
        accountant = Accountant.query.filter_by(id=id).first()
        if accountant:
            db.session.delete(accountant)
            db.session.commit()
            
    def addAccountant(self, form):
        data = {**form}
        accountant = Accountant(**data)
        if('id' not in data):
            db.session.add(accountant)
        else:
            accountant = Accountant.query.filter_by(id=data['id']).update(data)
        db.session.commit()
        return accountant
