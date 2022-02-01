#Multiplos de 3 de 1 a 500
# contador = 1
# acumulado = 0
# for contador in range(1, 500):
#     tabuada3 = (contador * 3)
#     if (tabuada3 % 2) == 1:
#         print(tabuada3)
#         acumulado = acumulado + tabuada3
# print('Total: {}'.format(acumulado))
#

'''
sum = 0
for i in range(3, 500, 3):
    if i % 2 == 1:
        sum = sum + i
print('Total: {}'.format(sum))
'''

# Resolucao do professor
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
