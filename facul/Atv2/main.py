from ImovelNovo import ImovelNovo
from ImovelVelho import ImovelVelho

valor = 60
adicional = valor * 0.2
desconto = valor * 0.1
endereco_a = 'rua 1500'
endereco_b = 'rua 3122'
imovel_novo = ImovelNovo(valor, endereco_a, adicional)
imovel_velho = ImovelVelho(valor, endereco_b, desconto)

imovel_novo.imprimeValor()
imovel_novo.imprimirAdicional(adicional)

imovel_velho.imprimeValor()
imovel_velho.imprimirDesconto(desconto)
