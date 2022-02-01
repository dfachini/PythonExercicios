'''
Primeiro Termo: 2
Razao: 1
2-> 3-> 4-> 5-> 6-> 7-> 8-> 9-> 10-> 11-> ACABOU
'''


'''
i = 0
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
# for i in range(primeiro, decimo + razao, razao):
#     print('{}'.format(i), end='-> ')
# print('ACABOU')
while i < decimo:
    i += razao
    print('{}'.format(i), end='-> ')
print('ACABOU')
# while i in range(primeiro, decimo + razao, razao):
#     print('{}'.format(i), end='-> ')
# print('ACABOU')
'''

# Resolução do Professor
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
