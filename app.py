#!flask/bin/python
from flask import Flask, jsonify
import json


rep = [
    {'prenom' : 'Antoine',
    'nom' : 'Bour',
    'tel' : '0633741375'},
    {'prenom' : 'Antoine2',
    'nom' : 'Bour2',
    'tel' : '0633741375'}
]


app = Flask(__name__)




@app.route('/')
def index():
    return "Hello, World!"

@app.route('/repertoire')
def repertoire():
    rep_json = json.dumps(rep)
    return(rep_json)

@app.route('/hello')
def hello():
  return 'Hello, greetings from different endpoint'

#adding variables
@app.route('/repertoire/<nom>')
def show_user(nom):
    repert = json.loads(repertoire())
    L = []
    for item in repert:
        if item["nom"] == nom:
            L.append(item)
    return(json.dumps(L))

@app.route('/repertoire/<fullinfo>', methods=['GET','POST'])
def add_user(fullinfo):

    prenom,nom,tel = fullinfo.split("_")
    rep.append(
        {'prenom': prenom,
         'nom': nom,
         'tel': tel}
    )
    rep_json = json.dumps(rep)
    return(json.dumps(rep))

if __name__ == '__main__':
    app.run(debug=True)


#test pour une mise à jour de git