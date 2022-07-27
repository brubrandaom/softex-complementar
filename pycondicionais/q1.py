#Faça um Programa que peça dois números e imprima o maior deles

num1 = int(input('primeiro número: '))
num2 = int(input('segundo número: '))
def maiorNum(num1, num2):
    if (num1>num2):
        return ('{} é maior!'.format(num1))
    if (num2>num1):
        return ('{} é maior!'.format(num2))
    else:
        return ('são iguais!')
print(maiorNum(num1, num2))
