'''
nome = 'David Romero dos Santos Fachini'
print(nome.upper())                 # Todas maiusculas
print(nome.lower())                 # Todas minusculas
print(len(''.join(nome.split())))   #Tamanho sem espaços
fatiar = nome.split()
contar = len(fatiar[0])
print(contar)
'''

# Resolucao do professor
nome = str(input('Digite seu nome completo: ')).strip()         # strip para remover espaços antes e depois de uma cadeia de caracteres
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))           # Primeira forma de contar
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
