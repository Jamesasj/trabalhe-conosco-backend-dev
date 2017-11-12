from PICPAY_APP import app
from PICPAY_APP.CONTROLE.UsuarioCO import UsuarioCO
from PICPAY_APP.MODELO.UsuarioMO import UsuarioMO
from flask import render_template, request, jsonify

@app.route('/')
def acessar_index():
    return render_template('index.html')  

@app.route('/usuario/<string:tx_nome_username>',methods=['GET'])
def pesquisar_usuario(tx_nome_username):
    controle = UsuarioCO()
    lista_usuarios = controle.pesquisarUsuario(tx_nome_username)
    return jsonify(lista_usuarios)