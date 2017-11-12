from MODELO.UsuarioMO import UsuarioMO
from .DAO.UsuarioDAO import UsuarioDAO
class UsuarioCO():
    def __init__(self):
        self.dao = UsuarioDAO()

    def pesquisarUsuario(tx_nome_username):    
        lista_usuarios = self.dao.consultar_nome_username(tx_nome_username)
        return lista_usuarios

    def incluir_usuario(usuario):
        self.dao.create(usuario)
        
        