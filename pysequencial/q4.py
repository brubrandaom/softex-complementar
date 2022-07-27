#Faça um Programa que peça a temperatura em graus Fahrenheit,
#transforme e mostre a temperatura em graus Celsius.
#a. C=5*((F-32)/9).

tempF = float(input('temperatura em fahrenheit: '))
def conversao(tempF):
    return round(5*((tempF-32)/9), 2)
print('temperatura em celsius: ', conversao(tempF))
