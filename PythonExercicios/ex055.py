# Leia 6 pesos e mostre do menor para o maior

'''
import random
lista = []
for i in range(0, 6):
   peso = random.uniform(80, 100)
   lista.append(peso)

lista.sort(reverse=False)
print(lista)
ultimodalista = int(len(lista))
for i in range(0, len(lista)):
  print('Segue Peso: {:.2f}'.format(lista[i]))
print('O menos e mais pesado estão com {:.2f} e {:.2f}, respectivamente.'.format(lista[0], lista[len(lista)-1]))
'''

# Resolucao do Professor
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
