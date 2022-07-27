#Considere para os itens abaixo como entrada uma lista de valores reais contendo notas de 0.0 a 10.0. Faça uma função que:
#• Devolve a média.
#• Devolve a quantidade de notas abaixo de 6.0.
#• Devolve a quantidade de notas acima e igual a 6.0.
#• Devolve a quantidade de notas acima e igual a média.
#• Devolve a maior nota.
#• Devolve a menor nota.

notas = []
nota = 0
i = 0
media = 0
abaixo6 = 0
acima6 = 0
acimaMedia = 0
maiorNota = 0
menorNota = 11
print('digite "-1" para encerrar o cadastro de notas.')
while (nota!=-1):
    nota = float(input('{}ª nota: '.format(i+1)))
    notas.append(nota)
    if (nota==-1):
        notas.pop(-1)
        break
    i+=1
def fmedia (notas):
    media = round(sum(notas)/len(notas), 2)
    return media

def fabaixo6 (notas, abaixo6):
    for i in range (len(notas)):
        if (notas[i]<6):
            abaixo6+=1
    return abaixo6
    
def facima6 (notas, acima6):
    for i in range (len(notas)):
        if (notas[i]>=6):
            acima6+=1
    return acima6
    
def facima(notas, acimaMedia):
    for i in range (len(notas)):
        if (notas[i]>=fmedia(notas)):
            acimaMedia+=1
    return acimaMedia
    
def fmaior (notas, maiorNota):
    for i in range (len(notas)):
        if (notas[i]>maiorNota):
            maiorNota=notas[i]
    return maiorNota
    
def fmenor (notas, menorNota):
    for i in range (len(notas)):
        if (notas[i]<menorNota):
            menorNota=notas[i]
    return menorNota

print(f'média: {fmedia(notas)}')
print(f'quantidade de notas abaixo de 6: {fabaixo6(notas, abaixo6)}')
print(f'quantidade de notas acima e igual a 6: {facima6(notas, acima6)}')
print(f'quantidade de notas acima e igual a média: {facima(notas, acimaMedia)}')
print(f'maior nota: {fmaior(notas, maiorNota)}')
print(f'menor nota: {fmenor(notas, menorNota)}')
