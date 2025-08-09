# Classe que representa os livros da biblioteca
class Livro:

    # Método de construção de objetos.
    def __init__(self, titulo: str, genero: str,  # type: ignore
                    editora: str, ano_publicacao: int, autor: str, 
                    isbn: str, numero_paginas: int = 0,
                    edicao: str = '', # type: ignore
                    volume: str = ''): # type: ignore
        
        # Define a herança de atributos da superclasse.
        super().__init__(titulo, genero, editora,  # type: ignore
                        ano_publicacao, edicao, volume) # type: ignore