from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
from dotenv import dotenv_values
import sqlite3

def criarTable():
    banco  = sqlite3.connect('ControleDeRotasSeven.bd')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE carros (FUNCIONARIO text,CARRO text, DATAHORA datetime , SAIDACHEGADA text, ROTA text, KM text, LOCALIZACAO text)')
    banco.commit()
    cursor.close()

def Inserir(content):
    banco  = sqlite3.connect('ControleDeRotasSeven.bd')
    cursor = banco.cursor()
    lista = [
        content['motorista'],content['carro'],content['dataHora'],content['chegadaSaida'],content['rota'],content['km'],content['loc']
    ]
    cursor.execute('INSERT INTO carros VALUES(?,?,?,?,?,?,?)',lista)
    banco.commit()
    cursor.close()


def getTable():
    lista = []
    try:
        connection = sqlite3.connect('ControleDeRotasSeven.bd')
        cursor = connection.cursor()
        sqlite_select_query = """SELECT * FROM carros"""
        print(sqlite_select_query)
        cursor.execute(sqlite_select_query)
        obj = cursor.fetchall()
        for i in obj:
            lista.append({'FUNCIONARIO':i[0], "CARRO": i[1],"DATAHORA":i[3], "SAIDACHEGADA":i[2],"ROTA":i[4],"KM":i[5],"LOCALIZACAO":i[6]})
        cursor.close()
        return lista
    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if connection:
            connection.close()
            print("The Sqlite connection is closed")


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

#       Adiciona item na tabela
@app.route("/",methods = ['POST'])
def responder():
    content = request.json
    Inserir(content)
    print(content)
    return '200'

#       Criar Tabela
@app.route("/criar",methods = ['GET'])
def criar():
    criarTable()
    return '200'

#       Retorno a tabela
@app.route("/buscar",methods = ['GET'])
def buscar():
    lista = getTable()
    return jsonify(lista)

 
config = dotenv_values(".env" )
print(config['PORT'])

if __name__ == '__main__':
    app.run(port=config['PORT'])
