# Importação da superclasse
from .item_acervo import ItemAcervo

# Classe que representa as revistas da biblioteca
class Revista (ItemAcervo):


    # Método de construção de objetos.
    def __init__(self, titulo: str, genero: str,  # type: ignore
                    editora: str, ano_publicacao: int,  
                    issn: str, mes_publicacao: str,
                    edicao: str = '', # type: ignore
                    volume: str = ''): # type: ignore
        
        # Define a herança de atributos da superclasse.
        super().__init__(titulo, genero, editora, ano_publicacao, edicao, volume) 

        # Atributos próprios
        self.issn = issn
        self.mes_publicacao = mes_publicacao # type: ignore
    

    # Métodos de acesso (GET) aos atributos
    @property
    def issn (self) -> str:
        return self._issn
    
    @property
    def mes_publicacao (self) -> int:
        return self._mes_publicacao # type: ignore
    


    # Métodos de modificação (SET) dos atributos
    @issn.setter
    def issn (self, valor: str):

        # Verifica se o valor não é vazio
        if valor != '':
            self._issn = valor
        else:
            self._issn = 'Indefinido'

    @mes_publicacao.setter
    def mes_publicacao (self, valor: str):
        # Verifica se o valor não é vazio
        if valor != '':
            self.mes_publicacao = valor
        else:
            self.mes_publicacao = 'Indefinido'
    
    