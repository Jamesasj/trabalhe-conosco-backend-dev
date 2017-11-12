from flask import Flask, jsonify
from CONTROLE.UsuarioCO import UsuarioCO

class UsuarioAPI():
    @app.route('/usuarios/<srt:tx_usuario_username>',methods=['GET'])
    def pesquisar_usuario(tx_usuario_username):
        lista_usuarios = self.usuarioCO.pesquisar_usuario(tx_usuario_username)
        return jsonify(lista_usuarios)