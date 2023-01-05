# programas desenvolvidos para ler um número real qualquer e exibir na tela somente a parte inteira
import math
num = float(input('Digite um número real qualquer: '))
inteiro = math.trunc(num)
print('A parte inteira do número {} é {}'.format(num, inteiro))


# outro formato, sem importar a biblioteca

#num2 = float(input('Digite um número real qualquer: '))
#print('A parte inteira do número {} é {:.0f}'.format(num2, num2))
