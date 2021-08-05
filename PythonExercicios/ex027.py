'''
nome = 'David Romero dos Santos Fachini'
fatiar = nome.split()
print(fatiar)
print('primeiro = {}'.format(fatiar[0]))
print('último = {}'.format(fatiar[-1]))
'''


# Resolucao do professor
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))