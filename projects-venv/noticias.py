class Noticia:
    
    def __init__(self, id, titulo, corpo, autor, corpo_corpo, id_estado):
        self.__id = id
        self.__titulo = titulo
        self.__corpo = corpo
        self.__autor = autor
        self.__news_corpo = corpo_corpo
        self.__id_estado = id_estado
        
    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_corpo(self):
        return self.__corpo
    
    def get_autor(self):
        return self.__autor
    
    def get_corpo2(self):
        return self.__news_corpo    
    def get_estado(self):
        if self.__id_estado == 1:
            self.__id_estado = "Acre"
        if self.__id_estado == 2:
            self.__id_estado = "Alagoas"
        if self.__id_estado == 3:
            self.__id_estado = "Amapá"
        if self.__id_estado == 4:
            self.__id_estado = "Bahia"
        if self.__id_estado == 5:
            self.__id_estado = "Ceará"
        if self.__id_estado == 6:
            self.__id_estado = "Distrito Federal"
        if self.__id_estado == 7:
            self.__id_estado = "Espírito Santo"
        if self.__id_estado == 8:
            self.__id_estado = "Goiás"
        if self.__id_estado == 9:
            self.__id_estado = "Maranhão"
        if self.__id_estado == 10:
            self.__id_estado = "Mato Grosso"
        if self.__id_estado == 11:
            self.__id_estado = "Mato Grosso do Sul"
        if self.__id_estado == 12:
            self.__id_estado = "Minas Gerais "
        if self.__id_estado == 13:
            self.__id_estado = "Pará"
        if self.__id_estado == 14:
            self.__id_estado = "Paraná"
        if self.__id_estado == 15:
            self.__id_estado = "Pernambuco"
        if self.__id_estado == 16:
            self.__id_estado = "Rio de Janeiro"
        if self.__id_estado == 17:
            self.__id_estado = "Rio Grande do Norte"
        if self.__id_estado == 18:
            self.__id_estado = "Rio Grande do Sul"
        if self.__id_estado == 19:
            self.__id_estado = "Rondônia"
        if self.__id_estado == 20:
            self.__id_estado = "Roraima"
        if self.__id_estado == 21:
            self.__id_estado = "Santa Catarina"
        if self.__id_estado == 22:
            self.__id_estado = "São Paulo"
        if self.__id_estado == 23:
            self.__id_estado = "Sergipe"
        if self.__id_estado == 24:
            self.__id_estado = "Tocantins"
        return self.__id_estado