class Noticia:
    
    def __init__(self, id, titulo, corpo, autor):
        self.__id = id
        self.__titulo = titulo
        self.__corpo = corpo
        self.__autor = autor
        
    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_corpo(self):
        return self.__corpo
    
    def get_autor(self):
        return self.__autor