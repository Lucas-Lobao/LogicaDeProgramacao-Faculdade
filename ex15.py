# Programa: aluguel de carro
km = float(input('Quantos quilômetros você percorreu com o carro? '))
dias = int(input('Quantos dias você ficou com o carro? '))
valor = float((dias*60)+(km*0.15))
print('o valor a ser pago pelo aluguel do veículo é de R${}'.format(valor))
