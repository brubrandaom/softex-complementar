#Faça uma função que peça ao usuário um numero inteiro e escreva uma função para saber se ele é PAR ou IMPAR.

num = int(input('digite um número inteiro: '))
def imparPar(num):
    if (num%2==0):
        return ('PAR!')
    else:
        return ('ÍMPAR!')
print(imparPar(num))
