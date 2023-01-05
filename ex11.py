# programa que calcula a área de uma parede e calcula quantos litros de tinta precisaremos para pintá-la
print('-'*50)
larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = float(larg*alt)
TintaNecessaria = area/3
print('A sua parede tem as dimensões de {}x{} e uma área de {}m2 \nPortanto, você precisará de {} litro(s) de tinta'.format(
    larg, alt, area, TintaNecessaria))
print('-'*50)
