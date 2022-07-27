#Crie uma lista com os seguintes números: [6.0, 8.5, 9.0, 4.2] e crie uma variável com o seguinte nome ValorProcurado = 8.5,
#percorra a lista e mostre em quando índice o valor procurado se encontra.

lista = [6.0, 8.5, 9.0, 4.2]
valorProcurado = 8.5
for i in range (4):
    if (lista[i]==valorProcurado):
        print('o valor procurado se encontra no índice ', i, '!')
