# programa que lê o preço de um produto e aplica um desconto de 5% a ele.
preco = float(input('Qual o preço do produto? '))
desconto = preco*5/100
print('O preço desse produto com desconto de 5% é {}R$'.format(preco-desconto))
