from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

valor = 60
imposto = valor * 0.2
desconto = valor * 0.1
endereco = 'rua 1500'
cpf = 666666666
cnpj = 99999
nome = 'berna'
nomeFantasia = 'rei delas'
pessoafisica = PessoaFisica(nome, valor, endereco, cpf, imposto)
pessoajuridica = PessoaJuridica(nome, valor, endereco, cnpj, nomeFantasia, imposto, desconto)

pessoafisica.calcularPagamento(cpf, imposto)
pessoajuridica.calcularPagamento(cnpj, nomeFantasia, imposto, desconto)

