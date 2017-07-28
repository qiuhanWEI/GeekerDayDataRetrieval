from flask import Flask
from flask import request
from flask import jsonify
import sys, os
sys.path.append(os.path.dirname(__file__)+'/database/')
print (sys.path)
from database_operation import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return app.send_static_file('test.html')

# from route.operation import operation
# app.register_blueprint(operation, url_prefix='/operation')

@app.route('/select', methods=['POST'])
def select():
    form = request.form
    name = ''
    phone = ''
    email = ''
    if 'name' in form:
        name = request.form['name']
    if 'phone' in form:
        phone = request.form['phone']
    if 'email' in form:
        email = request.form['email']
    print (name, phone, email)

    # hello()
    result = selectInDB({'name': name.encode('utf-8'), 'phone': phone.encode('utf-8'), 'email': email.encode('utf-8')})
    print result
    # result = [1, 3]
    return jsonify(result)

@app.route('/insert', methods=['POST'])
def insert():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    company = request.form['company']
    department = request.form['department']
    position = request.form['position']

    # print (name, phone, email, company, department, position)
    result = insertInDB({'name': name.encode('utf-8'), 'phone': phone.encode('utf-8'), 'email': email.encode('utf-8'), 'company': company.encode('utf-8'), 'department': department.encode('utf-8'), 'position': position.encode('utf-8')})
    if result == 'success':
        result = 1
    else:
        result = 0

    return jsonify({status: result})

@app.route('/delete', methods=['POST'])
def delete():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    company = request.form['company']
    department = request.form['department']
    position = request.form['position']

    print (name, phone, email, company, department, position)

    result = deleteInDB({'name': name.encode('utf-8'), 'phone': phone.encode('utf-8'), 'email': email.encode('utf-8')})
    if result == 'success':
        result = 1
    else:
        result = 0

    return jsonify({status: result})

@app.route('/update', methods=['POST'])
def update():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    company = request.form['company']
    department = request.form['department']
    position = request.form['position']
    print (name, phone, email, company, department, position)

    result = updateInDB({'name': name.encode('utf-8'), 'phone': phone.encode('utf-8'), 'email': email.encode('utf-8'), 'company': company.encode('utf-8'), 'department': department.encode('utf-8'), 'position': position.encode('utf-8')})

    if result == 'success':
        result = 1
    else:
        result = 0

    return jsonify({status: result})


# @app.route('', methods=['POST'])
# def ():
#
#     return jsonify()
#
# @app.route('', methods=['POST'])
# def ():
#
#     return jsonify()

if __name__ == '__main__':
    app.run()
