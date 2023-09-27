from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
import sqlite3

def criarTable():
    banco  = sqlite3.connect('ControleDeRotasSeven.bd')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE FIORINO (ID INTEGER, FUNCIONARIO text, DATAHORA datetime , SAIDACHEGADA text, ROTA text, KM text, OBS text)')
    #cursor.execute('INSERT INTO FIORINO VALUES ('+GOOGLE+')')
    banco.commit()
    cursor.close()

def teste():
    GOOGLE = 'NERI'
    banco  = sqlite3.connect('ControleDeRotasSeven.bd')
    cursor = banco.cursor()
    cursor.execute('INSERT INTO FIORINO VALUES ()')
    banco.commit()
    cursor.close()


def DropTable(tabela,limparlista):
    try:
        banco  = sqlite3.connect('bdPainel.bd')
        cursor = banco.cursor()
        cursor.execute('DROP TABLE '+str(tabela)+'')
        banco.commit()
        cursor.close()
        limparlista.clear()
        print('tabela deletada')
    except: print('Nao tem tabela')


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/",methods = ['POST', 'GET'])
def responder():
    content = request.json
    print(content)
    return '200'



if __name__ == '__main__':
    app.run()