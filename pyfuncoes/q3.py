#Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.

conta = float(input('valor da conta: '))
def gorjeta (conta):
    return conta*0.1
print(f'gorjeta do garson: {gorjeta(conta)}')
