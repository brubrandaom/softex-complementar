# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7

h = float(input('sua altura: '))
genero = str(input('seu genero: '))
def pesoIdeal(h, genero):
    if(genero=='m'):
       return round((72.7*h)-58, 2)
    else:
        return round((62.1*h)-44.7, 2)
print('seu peso ideal é: ',pesoIdeal(h, genero))
