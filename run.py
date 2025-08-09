# Impotação das classes orientadas à objetos
from model import Livro
from model import Revista

# Pergunta para o usuário o que ele quer cadastrar
print('Opções:')
print('1 - Cadastrar Livro')
print('2- Cadastrar Revista')
pergunta = input('O que deseja cadastrar (1 ou 2)?')

# Define qual item do acervo será cadastrado.
if pergunta == '1':

    # Solicita as informações do usuario

    titulo = input('Digite o título do livro: ')
    genero = input('Digite o gênero do livro:')
    editora = input('Digite a editora do livro:')
    ano_publicacao = int(input('Digite o ano de publicação do livro:'))
    autor = input('Digite o(a) autor(a) do livro:')
    isbn = input('Digite o ISBN do livro:')
    numero_paginas  = int(input('Digite o número de páginas do livro:'))
    edicao = input('Digite a edição do livro:')
    volume = input('Digite o volume do livro:')

    # Cadastra Livro

    meu_livro = Livro(titulo, genero, editora, ano_publicacao, autor, isbn, numero_paginas, edicao, volume)
    

if pergunta == 2:

    # Solicita as informações do usuario
    titulo = input('Digite o título da revista: ')
    genero = input('Digite o gênero da revista:')
    editora = input('Digite a editora da revista:')
    ano_publicacao = int(input('Digite o ano de publicação da revista:'))
    issn = input('Digite o ISSN da revista:')
    mes_publicacao =int(input('Digite o mês de publicação da revista:'))
    edicao = input('Digite a edição da revista:')
    volume = input('Digite o volume da revista:')


    # Cadastra Revista

    minha_revista = Revista(titulo, genero, editora, ano_publicacao, issn, mes_publicacao, edicao, volume) # type: ignore