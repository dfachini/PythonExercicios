'''
from random import randint
from time import sleep
contador = 0
computador = randint(0, 10)     # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
# sleep(3)
while jogador != computador:
    contador += 1
    jogador = int(input('Mais uma chance. Em que número pensei? '))
if contador > 3:
    print('Se esforce mais voce precisou de {} para me vencer.'.format(contador))
else:
    print('PARABÉNS! Voce mandou bem! Precisou apenas de {} tentativas para me vencer!'.format(contador))

# else:
#     print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
'''

# Resolucao do Professor
from random import randint
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
