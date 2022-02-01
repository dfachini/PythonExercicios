'''
from random import randint
from time import sleep


contador = vitorias = comparador = jogador = pc = 0
jogo = True
while jogo == True:
    opcao = str(input('Escolha par ou impar: ')).strip().upper()
    jogador = int(input('Valor: '))
    pc = randint(0, 999999999999)
    # print('PAR...')
    # sleep(1)
    # print('OU...')
    # sleep(1)
    # print('IMPAR!')

    if opcao == 'PAR':
        comparador = (jogador + pc) % 2
        if comparador == 0:
            print(f'Jogador Venceu escolhendo {opcao}')
            vitorias += 1
        else:
            print('Jogador PERDEU!')
            break
    if opcao == 'IMPAR':
        comparador = (jogador + pc) % 2
        if comparador == 1:
            print(f'Jogador Venceu escolhendo {opcao}')
            vitorias += 1
        else:
            print('Jogador PERDEU!')
            break

print(f' jogador: {jogador} , computador: {pc}, vitorias consecutivas do jogador: {vitorias}')
'''


# Resolução do Professor
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')


