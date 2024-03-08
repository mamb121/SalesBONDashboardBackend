from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Welcome</h1>'

@app.route('/hello')
def hello():
    return render_template('test.html',mohammed='ahmed')

@app.get('/salesdata')
def salesdata():
    salestotals =[200000.0,201000.0,102333.0]
    respons ={ 'sales1':
              {
              'id':1,
              'name':'AlTahlia Branch',
              'total':200000.0
              },
              'sales2':
              {
              'id':2,
              'name':'AlMohammadia Branch',
              'total':201000.0
              },
              'sales3':
              {
              'id':3,
              'name':'Safa Branch',
              'total':102333.0
              }
              }
    # return respons
    return jsonify(salestotals)