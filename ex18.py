# programa para ler o seno, cosseno e tangente de um ângulo qualquer
import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O seno do ângulo que você digitou é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}.'.format(
    seno, cos, tan))
