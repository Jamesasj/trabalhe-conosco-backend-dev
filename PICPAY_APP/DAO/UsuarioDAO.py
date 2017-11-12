from PICPAY_APP.MODELO.UsuarioMO import UsuarioMO
from pymongo import MongoClient

class UsuarioDAO():
    def __init__(self):
        self.con = MongoClient('mongodb://127.0.0.1:27017')
        self.db_picpay = self.con.db_picpay
        self.tabela_usuarios = self.db_picpay.tabela_usuarios
        
    def create(self, usuario):
        self.tabela_usuarios.insert_one(usuario.__dict__)

    def consultar_nome_username(self, tx_nome_username):
        print(tx_nome_username)
        lista_usuarios_cursor = self.tabela_usuarios.find(
            {'$or':[
                {'nome': {"$regex": u"{}".format(tx_nome_username)}},
                {'username': {"$regex": u"{}".format(tx_nome_username.lower())}}
                ]}
            )
        lista_usuarios = list()
        for elemento in lista_usuarios_cursor:
            usuario = UsuarioMO(elemento['id'], elemento['nome'],elemento['username'])
            lista_usuarios.append(usuario)
        return lista_usuarios        
        