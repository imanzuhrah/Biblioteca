# Classe que representa os itens do acervo da biblioteca
class ItemAcervo:

    # Método de construção de objetos.
    def __init__(self, titulo: str, genero: str,  # type: ignore
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
        

        # Métodos de modificação dos atributos
        @titulo.setter
        def titulo (self, valor: str):

            # Verifica se o valor não é vazio
            if valor != '':
                self._titulo = valor
            else:
                self._titulo = 'Indefinido'

        @genero.setter
        def genero (self, valor: str):

            # Verifica se o valor não é vazio
            if valor != '':
                self._genero = valor
            else:
                self._genero = 'Indefinido'


        @editora.setter
        def editora (self, valor: str):

            # Verifica se o valor não é vazio
            if valor != '':
                self._editora = valor
            else:
                self._editora = 'Indefinido'


        @ano_publicacao.setter
        def ano_publicacao (self, valor: int):
            if valor > 0:
                self._ano_publicacao = valor
            else:
                self._ano_publicacao = 0


        @edicao.setter
        def edicao (self, valor: str):

            # Verifica se o valor não é vazio
            if valor != '':
                self._edicao = valor
            else:
                self._edicao = 'Indefinido'


        @volume.setter
        def volume (self, valor: str):

            # Verifica se o valor não é vazio
            if valor != '':
                self._volume = valor
            else:
                self._volume = 'Indefinido'


        @disponivel.setter
        def disponivel (self, valor: bool):

            if isinstance(valor, bool):
                self._disponivel = valor
            else:
                self._disponivel = True


