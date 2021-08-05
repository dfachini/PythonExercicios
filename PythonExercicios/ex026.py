'''
frase = 'Arara da Amazonia Azul'
transfomar = frase.lower()
print(transfomar.count('a'))    # Quantas vezes aparece 'a'
print(transfomar.find('a'))     # Em que posicao 'a' aparece a primeira vez
print(transfomar.rfind('a'))    # Em que posicao 'a' aparece a ultima vez
'''

# Resolucao do professor
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
