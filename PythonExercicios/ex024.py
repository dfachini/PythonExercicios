'''
cidade = 'Vera Cruz'

fatiar = cidade.split()
print(fatiar)
comeco = fatiar[0]
# print(comeco.find('Santo'))
print('Santo' in comeco)
'''

# Resolucao do professor
cidade = str(input('Em que cidade você nasceu?\n')).strip()     # Para eliminar os espaços antes e depois
print(cidade[:5].upper() == 'SANTO')