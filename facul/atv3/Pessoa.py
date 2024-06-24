class Pessoa: 
    def __init__(self, nome, endereco, valor):
        self.nome = nome
        self.valor = valor
        self.endereco = endereco
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
        
    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor
    
    def getEndereco(self):
        return self.endereco
    
    def setEndereco(self, endereco):
        self.endereco = endereco
    
    def calcularPagamento(self):
        print(self.nome)
        print(self.endereco)
        print(self.valor)