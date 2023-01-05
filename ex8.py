# programa criado para converter medidas de metros para centímetros e milímetros, respectivamente.
n = int(input('Digite um valor em metros: '))
cm = int(n*100)
mili = int(n*1000)
print('O valor convertido em centímetros é igual a {}cm;\nO valor convertido em milímetros é igual a {}mm.'.format(cm, mili))
