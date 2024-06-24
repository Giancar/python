class Imovel: 
    def __init__(self, valor, endereco):
        self.valor = valor
        self.endereco = endereco
        
    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor
    
    def getEndereco(self):
        return self.endereco
    
    def setEndereco(self, endereco):
        self.endereco = endereco
    
    def imprimeValor(self):
        print(self.valor)
        print(self.endereco)