from datetime import date
from flask import Flask, flash, make_response, redirect, request, jsonify, render_template, send_file, session
from flask_mail import Mail, Message
from flask_apscheduler import APScheduler
from flask_apscheduler.utils import job_to_dict
from app.database import db
from app.controllers.accountant_controller import AccountantController
from app.controllers.customer_controller import CustomerController
from app.controllers.xml_controller import XmlController
from app.services import XMLReport
from app.utils import checkLogin, createFile, createZip, fromEnv, getDotEnvValues, is_admin, is_logged, login_required, toDDMMYY, toMMYY

app = Flask(__name__)
app.config.from_mapping(getDotEnvValues())
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False

scheduler = APScheduler()
scheduler.init_app(app)

mail = Mail(app)
db.init_app(app)
    
accountCtr = AccountantController()
customerCtr = CustomerController()
xmlCtr = XmlController()

def isAdmin()->bool:
    isAdmin = False
    if 'admin' in session:
        isAdmin = session.get('admin')
        
    return isAdmin

@scheduler.task('cron', id='1', year='*', month='*', day='1', misfire_grace_time=900)
def sendReport():
    with app.app_context():
        XMLReport().sendToAll(mail)

scheduler.start()
for job in scheduler.get_jobs():
    print(job_to_dict(job))
    
@app.route('/send-test-email')
def sendTestEmail():
    msg = Message('E-mail de Teste', sender=("WM Sistemas de Gestão", 'nao-responda@wmsistemas.inf.br'), recipients = ['felipe.samuel.ti@gmail.com', 'samukajobs@gmail.com'])
    msg.body = 'Essa é uma mensagem de teste'
    mail.send(msg)
    return jsonify({'msg': 'ok!'})

@app.route('/logout')
@login_required
def logout():
    session.pop('logged')
    try:
        session.pop('admin')
        session.pop('accountant_id')
    except Exception as e:
        ...
    return redirect('/')

@app.before_first_request
def create_table():
    db.create_all()
    
@app.context_processor
def inject_product_count():
    username = 'Admin'
    if not isAdmin() and 'accountant_id' in session:
        username = accountCtr.getById(session['accountant_id']).name
    return dict(
        isAdmin=isAdmin(),
        username = username,
        today = date.today(),
    )
    
@app.route("/login", methods=['GET', 'POST'])
@is_logged
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        if (checkLogin(username, password)):
            session['logged'] = True
            session['admin'] = True
            session['accountant_id'] = 0
            return redirect('/accountants')
        elif accountCtr.checkLogin(username, password):
            session['logged'] = True
            session['admin'] = False
            session['accountant_id'] = accountCtr.getBy(username).id
            return redirect('/customers')
        else:
            flash('CNPJ ou senha incorretos', 'error')
            return redirect('/login')
        
@app.route('/customer/delete/<int:id>', methods=['POST', 'GET'])
@login_required
def delete(id):
    customerCtr.delete(id)
    return redirect('/customers')

@app.route('/customer/zip/<int:id>', methods=['GET'])
@login_required
def createZipFromCustomer(id):
    customer = customerCtr.getBy(id)
    filename = customer.name.replace(' ','_')
    zip_name = createZip(xmlCtr.getByCustomer(id), name=filename)
    response = make_response(send_file(zip_name, as_attachment=True)) # Cria a resposta com o arquivo ZIP
    response.headers['Content-Disposition'] = f'attachment; filename={filename}.zip'
    return response

@app.route('/customer/zip/filter', methods=['POST'])
@login_required
def createZipFromFilter():
    startDate = request.form['start_date']
    endDate = request.form['end_date']
    if(startDate==''):
        startDate='1970-01-01'
    if (endDate ==''):
        endDate = str(date.today())
    
    customer = customerCtr.getBy(request.form['customer_id'])
    filename = customer.name.replace(' ','_')+"_"+toDDMMYY(startDate)+"_a_"+toDDMMYY(endDate)
    zip_name = createZip(xmlCtr.getByFilter(request.form), name=filename)
    response = make_response(send_file(zip_name, as_attachment=True)) # Cria a resposta com o arquivo ZIP
    response.headers['Content-Disposition'] = f'attachment; filename={filename}.zip'
    return response

@app.route('/xml/download/<int:id>', methods=['GET'])
@login_required
def downloadXml(id):
    xml = xmlCtr.getById(id)
    customer = customerCtr.getBy(id=xml.customer_id)
    filename = customer.name.replace(' ','_')+'_'+xml.nf_number
    zip_name = createFile(xml, name=filename)
    response = make_response(send_file(zip_name, as_attachment=True)) # Cria a resposta com o arquivo ZIP
    response.headers['Content-Disposition'] = f'attachment; filename={filename}.xml'
    return response

@app.route('/customer/details/<int:id>', methods=['GET'])
@login_required
def details(id):
    customer = customerCtr.getBy(id)
    customer.accountant = accountCtr.getById(customer.accountant_id)
    customer.prev_xmls = xmlCtr.getByCustomerWithLimit(customer_id=customer.id)
    customer.entrada_xmls = xmlCtr.getEntradaByCustomerWithLimit(customer_id=customer.id)
    customer.xml_inutilizados = xmlCtr.getInutilizadasByCustomerWithLimit(customer_id=customer.id)
    xml_status = xmlCtr.getXmlStatus()
    filesSize = xmlCtr.getXMLCount(customer_id=customer.id)
    if customer:
        return render_template('profile.html', customer=customer, xml_status=xml_status, filesSize=filesSize)
    else:
        return redirect('/')
    
@app.route('/accountant/details/<int:id>', methods=['GET'])
@login_required
def accountantDetails(id):
    accountant = accountCtr.getById(id)
    customersSize = len(accountant.customers)
    if accountant:
        return render_template('profile_accountant.html', accountant=accountant, customersSize=customersSize)
    else:
        return redirect('/')
    
@app.route('/accountant/delete/<int:id>', methods=['POST', 'GET'])
@login_required
def deleteAccountant(id):
    customers = customerCtr.getFromAccountant(id=id)
    if(len(customers)>0):
        message = "<ul>"
        for customer in customers:
            message+=f'<li>{customer.name}</li>'
        message += "</ul>"
        flash(f'Este contador possui os seguintes clientes vinculados: {message}Antes de excluir, vincule os clientes a outros contadores.', 'error')
    else:
        accountCtr.delete(id)
    return redirect('/accountants')

@app.route('/customers')
def customers():
    if isAdmin():
        customers = customerCtr.get()
    else:
        customers = customerCtr.getFromAccountant(session['accountant_id'])
    return render_template('customers.html', customers = customers)

@app.route('/accountants')
@login_required
@is_admin
def accountants():
    accountantsList = accountCtr.get()
    return render_template('accountants.html', accountants = accountantsList)

@app.route('/accountant/<id>')
def editAccountant(id):
    accountant = accountCtr.getById(id)
    return render_template('accountant.html', accountant=accountant)

@app.route('/accountant', methods=['GET', 'POST'])
@login_required
def createAccountant():
    if request.method == 'GET':
        return render_template('accountant.html')

    elif request.method == 'POST':
        edit = True
        if 'id' not in request.form:
            edit = False
            cnpj = request.form['cnpj']
            if(accountCtr.exists(cnpj)):
                flash('Este CNPJ já está sendo usado.', 'error')
                return redirect('accountant')
        
        accountCtr.addAccountant(request.form)
        flash(f'{request.form["name"]} {"atualizado" if edit else "adicionado"} com sucesso!', 'success')
        return redirect('/')
    return jsonify({'msg':'Método não permitido'})

@app.route('/customer/<id>')
def editCustomer(id):
    customer = customerCtr.getBy(id)
    accountants = accountCtr.get()
    return render_template('customer.html', customer=customer,  accountants = accountants)

@app.route('/customer', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        accountants = accountCtr.get()
        return render_template('customer.html', accountants=accountants)

    elif request.method == 'POST':
        edit = True
        if 'id' not in request.form:
            cnpj = request.form['cnpj']
            if(customerCtr.exists(cnpj)):
                flash('Este CNPJ já está sendo usado.', 'error')
                return redirect('customer')

        customerCtr.addCustomer(request.form)
        flash(f'{request.form["name"]} {"atualizado" if edit else "adicionado"} com sucesso!', 'success')
        return redirect('/customers')
    
    return jsonify({'msg':'Método não permitido'})

@app.route('/api/check', methods=['POST'])
def check():
    try:
        cnpj = request.json['cnpj']
        password = request.json['password']
        customer = customerCtr.login(cnpj, password)
        if(customer):
            return jsonify({'msg':'Login verificado!'}), 200
        else:
            return jsonify({'msg':'Informações incorretas'}), 401
    except Exception as e:
         return jsonify({'msg':'Informe cnpj e senha do cliente.', 'error': str(e)}), 401

@app.route('/api/send-xml', methods=['POST'])
def sendXml():
    try:
        type= request.json['type']
        cnpj = request.json['cnpj']
        password = request.json['password']
        customer = customerCtr.login(cnpj, password)
        if(customer):
            xml = xmlCtr.add(request.json, customer)
            if xml:
                return jsonify({'msg':'XML adicionado com sucesso!'}), 200
            else:
                return jsonify({'msg':f'Ocorreu uma falha ao adicionar o Xml. {xmlCtr.error}'})
                
        else:
            return jsonify({'msg':'CNPJ ou senha incorretos'}), 401
    except Exception as e:
         return jsonify({'msg':'Informe CNPJ e senha do cliente.', 'error': str(e)}), 401
    

@app.route('/')
@login_required
def home():
    if isAdmin():
        return redirect('/accountants')
    
    return redirect('/customers')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404