# Importação da superclasse
from .item_acervo import ItemAcervo

# Classe que representa os livros da biblioteca
class Livro (ItemAcervo):

    # Método de construção de objetos.
    def __init__(self, titulo: str, genero: str,  # type: ignore
                    editora: str, ano_publicacao: int, autor: str, 
                    isbn: str, numero_paginas: int = 0,
                    edicao: str = '', # type: ignore
                    volume: str = ''): # type: ignore
        
        # Define a herança de atributos da superclasse.
        super().__init__(titulo, genero, editora,  # type: ignore
                        ano_publicacao, edicao, volume) # type: ignore
        
        # Atributos próprios
        self.autor = autor
        self.isbn = isbn
        self.numero_paginas = numero_paginas # type: ignore

    # Métodos de acesso (GET) aos atributos
    @property
    def autor (self) -> str:
        return self._autor
    
    @property
    def isbn (self) -> str:
        return self._isbn
    
    @property
    def numero_paginas (self) -> int:
        return self.numero_paginas
    
    # Métodos de modificação (SET) dos atributos
    @autor.setter
    def autor (self, valor: str):

        # Verifica se o valor não é vazio
        if valor != '':
            self._autor = valor
        else:
            self._autor = 'Indefinido'

    @isbn.setter
    def isbn (self, valor: str):

        # Verifica se o valor não é vazio
        if valor != '':
            self._isbn = valor
        else:
            self._isbn = 'Indefinido'

    @numero_paginas.setter
    def numero_paginas (self, valor: int):
        if valor > 0:
            self._numero_paginas = valor
        else:
            self._numero_paginas = 0 # ou None