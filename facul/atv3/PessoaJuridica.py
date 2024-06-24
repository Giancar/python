from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self,nome, endereco, valor, cnpj, nomeFantasia, imposto, desconto):
        super().__init__(nome, valor, endereco)

    def calcularPagamento(self, cnpj, nomeFantasia, imposto, desconto):
        print(self.nome)
        print(cnpj)
        print(nomeFantasia)
        print(self.endereco)
        print(self.valor + imposto - desconto)
    