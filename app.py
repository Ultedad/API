from flask import Flask, jsonify, request

app = Flask(__name__)
usuarios = [ 
    {
        'cpf':1,
        'nome': 'Jose',
        'DataNasc': '09-05-2002'
    },
]

#[GET] Função para obter os usuarios inseridos
@app.route('/usuarios/obter', methods=['GET'])
def obter_Usuario():
    return jsonify(usuarios)

#[POST] Função para inserir um novo usuario
@app.route('/usuarios/inserir', methods=['POST'])
def inserir_Usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    return jsonify(usuarios)


#
app.run(port=5000,host='localhost',debug=True)