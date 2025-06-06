class Postagem:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
        self.comentarios = []

    def lista_comentarios(self, comentario):
        self.comentarios.append(comentario)

class Comentario:
    def __init__(self, conteudo, autor):
        self.conteudo = conteudo
        self.autor = autor