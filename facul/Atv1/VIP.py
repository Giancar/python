from Ingresso import Ingresso

class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor + (valor * 0.1))
    