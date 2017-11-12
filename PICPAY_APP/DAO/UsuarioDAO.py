from MODELO.UsuarioMO import UsuarioMO
from pymongo import MongoClient

db = connection.test_database
db = connection['forum-database']
forum = {"author": "Thiago Avelino","text": "Python e MongoDB","tags": ["mongodb", "python", "pymongo"]}
imaster = db.imaster
imaster.insert(forum)

class UsuarioDAO():
    def __init__(self):
        self.con = MongoClient()
        self.con = MongoClient('localhost', 27017)
        self.tabela_usuarios = self.con.tabela_usuarios
        
    def create(self,usuario):
        self.tabela_usuarios.insert_one(usuario.__dict__)

    def consultar_nome_username(tx_nome_username):
        lista_usuarios = self.tabela_usuarios.find(
            {'nome': '/.*{}.*/'.format(tx_nome_username),
            'username' : '/.*{}.*/'.format(tx_nome_username)}
            )
        return lista_usuarios        
        