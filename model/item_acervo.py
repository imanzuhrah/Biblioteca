# Classe que representa os itens do acervo da biblioteca
class ItemAcervo:

    # Método de construção de objetos.
    def __init__(self, titulo: str, genero: str, 
                    editora: str, ano_publicacao: int, edicao: str = '',
                    volume: str = ''):
        
        # Atributos.

        self._titulo = titulo
        self._genero = genero
        self._editora = editora
        self._ano_publicacao = ano_publicacao
        self._edicao = edicao
        self._volume = volume
        self._disponivel = True


        