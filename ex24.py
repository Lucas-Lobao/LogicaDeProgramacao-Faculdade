#Faça um programa em Python que, dada a idade de um atleta que será digitada pelo usuário, apresente a mensagem da coluna CATEGORIA de acordo com a tabela abaixo, onde a categoria depende da idade de entrada. Lembre-se de exibir a Categoria, exatamente como consta na tabela abaixo.

#CATEGORIA = IDADE


#Menor que 5 = NÃO TEM IDADE PARA SER ATLETA

#INFANTIL A = 5 a 7

#INFANTIL B = 8 a 10

#JUVENIL A = 11 a 13

#JUVENIL B = 14 a 17

#SÊNIOR = Maior ou igual a 18


idade = int(input('Digite a idade do atleta para saber sua categoria: '))

if idade < 5:
    print ("NÃO TEM IDADE PARA SER ATLETA")

elif idade <8:
    print("INFANTIL A")

elif idade <11:
    print("INFANTIL B")

elif idade <14:
    print("JUVENIL A")

elif idade <18:
    print ("JUVENIL B")

elif idade >= 18:
    print ("SÊNIOR")