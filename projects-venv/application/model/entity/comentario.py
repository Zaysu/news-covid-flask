class Comentario:
    
    def __init__(self, nome, email, comentario):
        self.nome = nome
        self.email = email
        self.comentario = comentario
    
    def getNomeC(self):
        return self.nome
    
    def getEmail(self):
        return self.email
    
    def getComentario(self):
        return self.comentario