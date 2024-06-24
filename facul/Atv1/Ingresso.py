class Ingresso: 
    def __init__(self, valor):
        self.valor = valor
        
    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor
    
    def imprimeValor(self):
        print(self.valor)