#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int (input('digite um número: '))
def sinal (num):
    if (num<0):
        return ('é negativo!')
    if (num>0):
        return ('é positivo!')
    else:
        return ('é 0!')
print(sinal(num))
