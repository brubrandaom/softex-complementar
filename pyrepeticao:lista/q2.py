#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = ''
senha = ''
while (nome==senha):
    nome = input('nome: ')
    senha = input('senha: ')
    if (nome != senha):
        break
    else:
        print('ERRO')
