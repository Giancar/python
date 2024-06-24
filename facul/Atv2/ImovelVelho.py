from Imovel import Imovel

class ImovelVelho(Imovel):
    def __init__(self, valor, endereco, desconto):
        super().__init__(valor, endereco)

    def imprimirDesconto(self, desconto):
        print('Desconto : ',desconto)
    