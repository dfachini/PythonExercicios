'''
i = 0
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
# qtdetermos = 1
while i < decimo:
    i += razao
    print('{}'.format(i), end='-> ')

print('\n')
qtdetermos = int(input('Você quer mostrar mais quantos termos? '))
# qtdetermos1 = primeiro + (qtdetermos - 1) * razao
# maximo = decimo + qtdetermos
while qtdetermos != 0:
    maximo = decimo + qtdetermos
    # qtdetermos = int(input('Você quer mostrar mais quantos termos (dentro)? '))
    while decimo < maximo:
            decimo += razao
            print('{}'.format(decimo), end='-> ')
    print('\n')
    qtdetermos = int(input('Você quer mostrar mais quantos termos? '))
print('0 Termos')
'''

# Resolução do Professor

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10   # são os 10 que o programa começa
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
