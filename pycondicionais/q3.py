#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
#e lhe contraram para desenvolver o programa que calculará os reajustes.
#a. Faça um programa que recebe o salário de um colaborador e o reajuste
#segundo o seguinte critério, baseado no salário atual:

#b. salários até R$ 280,00 (incluindo) : aumento de 20%
#c. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#d. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#e. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser
#realizado, informe na tela:
#f. o salário antes do reajuste;
#g. o percentual de aumento aplicado;
#h. o valor do aumento;
#i. o novo salário, após o aumento.

salario = float(input('informe seu salário atual: '))
percentual = 0
aumento = 0.0
novoSalario = 0.0

def calculadora (salario):
    if (salario<=280):
        percentual = 20
        aumento = round(salario*0.2, 2)
        novoSalario = round(salario+aumento, 2)
    if (salario>280 and salario<700):
        percentual = 15
        aumento = round(salario*0.15)
        novoSalario = round(salario+aumento, 2)
    if (salario>=700 and salario<1500):
        percentual = 10
        aumento = round(salario*0.1, 2)
        novoSalario = round(salario+aumento, 2)
    if (salario>=1500):
        percentual = 5
        aumento = round(salario*0.05)
        novoSalario = round(salario+aumento, 2)
    return percentual, aumento, novoSalario

percentual, aumento, novoSalario = calculadora(salario)

print('1. salario anterior ao ajuste: {}\n2. percentual de aumento aplicado: {}\n3. valor de aumento: {}\n4. novo salário: {}'.format(salario, percentual, aumento, novoSalario))

