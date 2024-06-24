from Imovel import Imovel

class ImovelNovo(Imovel):
    def __init__(self, valor, endereco, adicional):
        super().__init__(valor, endereco)

    def imprimirAdicional(self, adicional):
        print('Adicional : ',adicional)
    