from USUARIOSE import app
from USUARIOSE.UsuarioCO import UsuarioCO
from USUARIOSE.UsuarioMO import UsuarioMO

from flask import request, jsonify
 
@app.route('/usuario/<string:tx_nome_username>',methods=['GET'])
def pesquisar_usuario(tx_nome_username):
    controle = UsuarioCO()
    lista_usuarios = controle.pesquisarUsuario(tx_nome_username)
    return jsonify(lUsuario=[elem.serialize() for elem in lista_usuarios])

@app.route('/', methods=['GET'])
def acessar_index():
    return 'sistema rodando'
 
