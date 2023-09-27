# Crie uma classe chamada Livro com atributos como título, autor e ano de publicação. Implemente um método que exiba
# todas as informações do livro.

class Livro:
    def __init__(self, livro_titulo, livro_autor, livro_ano):
        self.titulo = livro_titulo
        self.autor = livro_autor
        self.ano = livro_ano

    def infos(self):
        result = {
            "Título": self.titulo,
            "Autor": self.autor,
            "Ano Publicação": self.ano
        }
        return result