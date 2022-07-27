#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for i in range (1, 6):
    soma += int(input('{}º número: '.format(i)))
media = soma/5
print('soma: {}\nmédia: {}'.format(soma, media))
