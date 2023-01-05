# Programa em Python que recebe o custo (valor em reais) de um espetáculo teatral e o preço do convite (valor em reais) desse espetáculo. Esse programa calcula e mostra:


# a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.

# b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.


# As quantidades calculadas devem ser um número inteiro, portanto, o resultado da quantidade de convites é arredondado para cima, usando a função matemática apropriada em Python.

import math
custo = float(input('Qual será o custo do evento? '))
precoingresso = float(input('Qual será o preço do ingresso? '))
beneicio = math.ceil(custo/precoingresso)
lucro = math.ceil((custo*1.23)/precoingresso)
print('Para alcançar o valor do custo do evento, precisa vender ',
      (beneicio), ' convites.')
print('Para obter lucro, precisa vender ', (lucro), ' convites.')
