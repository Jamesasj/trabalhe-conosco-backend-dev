from USUARIOSE.UsuarioMO import UsuarioMO
from USUARIOSE.UsuarioDAO import UsuarioDAO

class UsuarioCO():
    def __init__(self):
        self.dao = UsuarioDAO()

    def pesquisarUsuario(self, tx_nome_username): 
        self.dao = UsuarioDAO()   
        lista_usuarios = self.dao.consultar_nome_username(tx_nome_username)
        return lista_usuarios

    def incluir_usuario(self, usuario):
        self.dao.create(usuario)


    
        