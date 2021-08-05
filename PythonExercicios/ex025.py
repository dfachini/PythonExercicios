'''
nome = 'David Romero dos Santos Fachini'
print('Silva' in nome)
print(nome.find('Silva'))
'''


# Resolucao do professor
nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))