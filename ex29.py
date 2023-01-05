#Faça um programa modularizado em Python, para resolver um problema usando listas. 

#O programa deve ter as seguintes funções:

#- entrada_carro(): faz a entrada do modelo de 4 carros via teclado (o usuário irá digitar o modelo de 4 carros),

#- entrada_consumo(): faz a entrada de um número inteiro que é o consumo (em litros) de cada modelo de carro por quilometro (o usuário digita o consumo correspondente a cada carro),

#- economico(): retorna o modelo do carro mais econômico. Observe que o modelo do carro e seu consumo estará na mesma posição na lista, porém em vetores diferentes (carro e consumo).

#A entrada de dados deve ser feita da seguinte forma:

#- O usuário irá digitar o modelo de cada um dos 4 carros, linha por linha em seguida

#- O usuário irá digitar o consumo de cada um dos 4 carros, linha por linha.

#O programa irá apresentar na tela o modelo do carro que tiver o menor valor de consumo.


lista_carros= []
lista_consumo = []
def entrada_carro():
    while True:
        carros = str(input())
        lista_carros.append(carros)
        if len(lista_carros) == 4:
            break
        
def entrada_consumo():
    while True:
        consumos = float(input())
        lista_consumo.append(consumos)
        if len(lista_consumo) == 4:
            break
        
def economico():
    menor_consumo = lista_carros[lista_consumo.index(min(lista_consumo))]
    return menor_consumo