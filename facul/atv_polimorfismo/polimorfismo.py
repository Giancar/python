from typing import Generic, TypeVar, List

T = TypeVar('T')

class Armazem(Generic[T]):
    def __init__(self):
        self.itens: List[T] = []
    
    def adicionar(self, item: T):
        self.itens.append(item)
    
    def tirar(self) -> T:
        if self.itens:
            return self.itens.pop()
        else:
            print('Armazem já vazio')

    def listar(self):
        for i in self.itens:
            print(i, end = '')

itens_str = Armazem[str]()
itens_str.adicionar('gian')
itens_str.adicionar('berna')
itens_str.adicionar('gustavo')
itens_str.listar()
print('\n\n',itens_str.tirar(),'\n')
itens_str.listar()
itens_str.tirar()
itens_str.tirar()
print('\n\n')
itens_str.tirar()