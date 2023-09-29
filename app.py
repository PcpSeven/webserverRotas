from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
from dotenv import dotenv_values
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


config = dotenv_values(".env")

uri = config['URI']
client = MongoClient(uri, server_api=ServerApi('1'))
db_connection = client['controlerotas']
colecao = db_connection.get_collection('carros')

#colecao.insert_one({'carro':'FIORINO'})
#colecao.insert_one({'carro':'PALIO'})
#resultado = colecao.find({'carro':'PALIO'})


def buscarColecao():
    resultadoFInal = []
    resultado = colecao.find()
    for i in resultado:
        resultadoFInal.append({
            "carro":i['carro'],
            'motorista':i['motorista'],
            "chegadaSaida":i['chegadaSaida'],
            "dataHora":i['dataHora'],
            "rota":i['rota'],
            "km":i['km'],
            "loc":i['loc'],
            "obs":i["obs"],
        })
    return resultadoFInal
        

def Inserir(content):
    print(content)
    colecao.insert_one(content)


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#       Adiciona item na tabela
@app.route("/", methods = ['POST'])
def receber():
    content = request.json
    Inserir(content)
    data = {'message': 'SUCCESS'}
    return (jsonify(data), 201)


#       Retorno a tabela
@app.route("/",methods = ['GET'])
def buscar():
    result = buscarColecao()
    return (jsonify(result),200)

# ativar api
@app.route("/ativar",methods = ['GET'])
def ativar():
    data = {'message': 'SUCCESS'}
    return (jsonify(data), 201)



if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', '10000')
    app.run(host=host, port=int(port))
