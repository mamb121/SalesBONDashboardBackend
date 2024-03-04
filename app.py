from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Welcome</h1>'

@app.route('/hello')
def hello():
    return render_template('test.html',mohammed='ahmed')

@app.get('/salesdata')
def salesdata():
    respons ={ 
              {
              'id':1,
              'name':'AlTahlia Branch',
              'total':200000.0
              },
              {
              'id':2,
              'name':'AlMohammadia Branch',
              'total':201000.0
              },
              {
              'id':3,
              'name':'Safa Branch',
              'total':102333.0
              }
              }
    return json.dump(respons)