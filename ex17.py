# programa criado para ler o cateto oposto e o cateto adjacente de um triângulo retângulo e calcular o comprimento de sua hipotenusa.
from math import sqrt
catadj = int(input('Digite o comprimento do cateto adjacente: '))
catop = int(input('Digite o comprimento do cateto oposto: '))
hipotenusa = sqrt(catadj**2+catop**2)
print(
    'A hipotenusa do triângulo tem o comprimento de {:.0f}'.format(hipotenusa))
