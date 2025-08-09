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

        # Métodos de acesso aos atributos
        @property
        def titulo (self) -> str:
            return self._titulo
        
        @property
        def genero (self) -> str:
            return self._genero
        
        @property
        def editora (self) -> str:
            return self._editora
        
        @property
        def ano_publicacao (self) -> int:
            return self._ano_publicacao
        
        @property
        def edicao (self) -> int:
            return self._edicao
        
        @property
        def volume (self) -> str:
            return self._volume
        
        @property
        def disponivel (self) -> bool:
            return self._disponivel


