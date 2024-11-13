import datetime
from app.controllers.accountant_controller import AccountantController
from app.controllers.customer_controller import CustomerController
from app.controllers.xml_controller import XmlController
from app.utils import createZip, get_path, toMMYY
import subprocess
from flask_mail import Message
import re
from jinja2 import Template
import html

class XMLReport:
  sender = ("WM Sistemas de Gestão", 'nao-responda@wmsistemas.inf.br')

  def __init__(self):
    self.customerCtr = CustomerController()
    self.accountCtr = AccountantController()
    self.xmlCtr = XmlController()

  def render_template(self, accountant, customer, url, parsedDate):
      template_string = ''
      with open(get_path('../templates/emails/report.html'), "r", encoding='utf-8') as file:
        template_string = html.unescape(file.read())

      template = Template(template_string)
      return template.render(accountant=accountant, customer=customer, url=url, startDate=parsedDate)    
    
  def generateFile(self, customer):
    try:
      filter = self.getFilter(customer)
      xmls = self.xmlCtr.getByFilter(filter)
      return createZip(xmls, name=self.getFilename(customer), clean=False)
    except Exception as e:
      print(f'Falha ao gerar arquivo zip do cliente {customer.name}. {str(e)}')
      return None
    
  def generateLink(self, file):
    try:
      content = subprocess.getoutput(f'curl -T {file} temp.sh')
      return re.search("(?P<url>https?://[^\s]+)", content).group("url")
    except Exception as e:
      print(f'Falha ao gerar link para o arquivo {str(file)}. {str(e)}')
      return None
    
  def getFilename(self, customer):
    startDate = self.getLastPeriod()[0]
    return customer.name.replace(' ','_')+"_"+toMMYY(startDate)
  
  def sendToAll(self, mail):
    customers = self.customerCtr.get()
    for customer in customers:
        try:
          accountant = self.accountCtr.getById(customer.accountant_id)
          file = self.generateFile(customer)
          if(file != None):
              url = self.generateLink(file)
              if(url!=None):
                  startDate = self.getLastPeriod()[0]
                  parsedDate = toMMYY(startDate).replace('_','/')
                  subject = f'XMLs do Cliente {customer.name} do mês {parsedDate}'
                  recipient = accountant.email
                              
                  msg = Message(subject, sender=self.sender, recipients = [recipient])
                  msg.html = self.render_template(accountant, customer, url, parsedDate)
                  mail.send(msg) 
                  print(f'E-mail enviado para {accountant.name}')
        except Exception as e:
          print(f'Falha ao enviar e-mail para {accountant.name}. {str(e)}')
    
  def getFilter(self, customer)->dict:
    startDate, endDate = self.getLastPeriod()
    return {
            'start_date': startDate,
            'end_date': endDate,
            'customer_id': customer.id,
            'xml_status': []
    }
    
  def getLastPeriod(self):
    today = datetime.date.today()
    firstDayThisMonth = today.replace(day=1)
    lastDay = firstDayThisMonth - datetime.timedelta(days=1)
    firstDay = lastDay.replace(day=1)
    return firstDay.strftime("%Y-%m-%d"), lastDay.strftime("%Y-%m-%d")