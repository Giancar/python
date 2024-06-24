from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self,nome, endereco, valor, cpf, imposto):
        super().__init__(nome, valor, endereco)

    def calcularPagamento(self, cpf, imposto):
        print(self.nome)
        print(cpf)
        print(self.endereco)
        print(self.valor + imposto)
    