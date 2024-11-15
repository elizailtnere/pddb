import sqlite3
from flask import Flask, render_template, request
import dati 


app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def index():
    return render_template('index.html')

@app.route('/registret', methods=['GET', 'POST'])
def registreties():
    if request.method == 'POST':
        vards = request.form['vards'].capitalize()
        uzvards = request.form['uzvards'].capitalize()
        lietotajvards = request.form['lietotajvards'].capitalize()
        dati.pievienot_lietotaju(vards, uzvards, lietotajvards)
    return render_template('registret.html')

@app.route('/zina', methods=["POST","GET"])
def zina():
    lietotaji = dati.iegut_lietotajus()
    if request.method == 'POST':
        lietotajs_id = request.form['lietotajs_id']
        zina = request.form['zina']
        dati.pievienot_zinojumu(lietotajs_id, zina)
    
    zinas = dati.iegut_zinas()
    return render_template('zinas.html', lietotaji=lietotaji, zinas=zinas)

@app.route('/statistika')
def statistika():
    statistika = dati.iegut_statistiku()
    return render_template('statistika.html', statitika=statistika)

if __name__ == '__main__': 
    app.run(port = 5000)
