#Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('em que turno você estuda? \n(digite M caso maturino, V caso vespertivo, N caso noturno): ')
def mensagem (turno):
    match turno:
        case 'M':
            return ('bom dia!')
        case 'V':
            return ('boa tarde!')
        case 'N':
            return ('boa noite!')
        case _:
            return ('valor inválido!')
print(mensagem(turno))
