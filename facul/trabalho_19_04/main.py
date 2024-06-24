# Aluno : Giancarlo Tessarollo
# OBS : eu uso o main.py pra testar, eu ou testando função por função 
#       só descomenta as funçoes pra ir testando, usei o pandas pra mexer com csv.

from livro import Livro
from biblioteca import Biblioteca


titulo = 'tarzan'
autor = 'eu'
isbn = 333333
genero = 'selva'
disponivel = 1

novoTitulo = 'tarzan 2'
biblioteca = Biblioteca(titulo, autor, isbn, genero, disponivel)



biblioteca.adicionar(titulo, autor, isbn, genero, disponivel)
#biblioteca.remover(titulo)
#biblioteca.editarLivro(titulo, novoTitulo)
#biblioteca.pesquisar("autor",autor)
#biblioteca.pesquisarTodos()