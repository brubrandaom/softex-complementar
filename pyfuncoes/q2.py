#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

num = int(input('digite um número: '))
digitos = 0
def dig (num, digitos):
    while (num>=1):
        num/=10
        digitos+=1
    return digitos
print(f'{num} possui {dig(num, digitos)} dígitos')
