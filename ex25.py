#Faça um programa em Python que solicite a quantidade de alunos de uma turma. 

#Após esta informação, o usuário deve digitar a média de cada aluno da turma, e o programa apresentará a mensagem PARABÉNS VOCÊ ESTÁ APROVADO aos alunos com média maior ou igual a 6.0. 

#O programa deve calcular e mostrar, no final da entrada de dados, a média geral da turma.

#Obs.: Caso a quantidade informada de alunos da turma for igual a zero, o programa deve emitir a seguinte mensagem: NÃO HOUVE PROCESSAMENTO


def media_alunos(n):
    if n == 0:
        return 'NÃO HOUVE PROCESSAMENTO'

    soma_notas = 0

    for i in range(n):

        nota = float(input(''))

        if nota >= 6:
            print('PARABÉNS VOCÊ ESTÁ APROVADO')

        soma_notas += nota

    media_notas = soma_notas / n

    return media_notas


print(media_alunos(int(input(''))))