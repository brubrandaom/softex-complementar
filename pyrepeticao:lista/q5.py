#Faça uma lista com o nome notas, peça as notas ao usuário e só sair quando ele pressionar o -1, depois disso mostre na tela as notas que ele informou. (USAR O WHILE).

nota = 0
notas = []
i = 0
print('para encerrar digite "-1".')
while (nota != -1):
    nota = float(input('{}ª nota: '.format(i+1)))
    notas.append(nota)
    if (nota == -1):
        break
    i+=1
print(*notas, sep = ', ')
