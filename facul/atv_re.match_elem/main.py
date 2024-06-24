import math
import re

class EquacaoErro(Exception):
    def _init_(self, message):
        super()._init_(message)

def calcular():
    while True:
        try:
            equacao_input = input('Digite a equação : ')
            
            elem = re.match(r'\d+|[+/*-]', equacao_input)
            
            if elem: 
                print('resultado : ', eval(equacao_input))
            else:
                print(f'Equação Inválida')
        except ValueError:
            print('Vc não digitou valor valido')
        except EquacaoErro as ine:
            print(f'Erro: {ine}')
        finally:
            print('-------------------------------------')
            
calcular()