# algoritmo para calcular o aumento de 15% de um funcionário com base em seu salário.
print('-'*30)
salario = int(input('Qual o salário atual do funcionário? R$'))
aumento = salario*15/100
print('O salário desse funcionário com aumento de 15% será de {}R$.'.format(
    salario+aumento))
print('-'*30)
