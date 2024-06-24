from livro import Livro
from db import db
import csv
import pandas as pd

class Biblioteca(Livro):
    def __init__(self, titulo, autor, isbn, genero, disponivel):
        super().__init__(titulo, autor, isbn, genero, disponivel)

    
    
    def adicionar(self, titulo, autor, isbn, genero, disponivel):
        comando = f'INSERT INTO livro (titulo, autor, isbn, genero, disponivel) VALUES ("{titulo}", "{autor}", {isbn}, "{genero}", {disponivel})'
        cursor = db.cursor()
        cursor.execute(comando)
        db.commit()
        cursor.close()
        db.close()
        resultado = cursor.fetchall()
        print(resultado)
    
    def remover(self, titulo):
        columts = ['titulo', 'autor', 'isbn', 'genero', 'disponivel']
        df = pd.read_csv('db.csv',names=columts)
        df = df.drop(df[df.titulo == titulo].index)
        df.to_csv('db.csv',header=None ,index=False)
        print('Livro Removido')

    def pesquisarTodos(self):
        columts = ['titulo', 'autor', 'isbn', 'genero', 'disponivel']
        df = pd.read_csv('db.csv', header=None, names=columts, index_col=False)
        print(df.to_string())
    
    def editarLivro(self, titulo ,novoTitulo):
        columts = ['titulo', 'autor', 'isbn', 'genero', 'disponivel']
        df = pd.read_csv("db.csv", header=None, names=columts, index_col=False)
        df['titulo'] = df['titulo'].replace({titulo: novoTitulo})
        df.to_csv("db.csv", index=False, header=None )
        print('Livro Editado')
    
    def pesquisar(self,tipo ,variavel):
        columts = ['titulo', 'autor', 'isbn', 'genero', 'disponivel']
        df = pd.read_csv("db.csv", header=None, names=columts, index_col=tipo)
        print(df.loc[variavel])