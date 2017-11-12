class UsuarioMO(object):
    
    def __init__(self, id, nome, username):
        self.id = id
        self.nome = nome
        self.username = username


    def serialize(self):
        return {
            'id':self.id,
            'nome':self.nome,
            'username':self.username
            }