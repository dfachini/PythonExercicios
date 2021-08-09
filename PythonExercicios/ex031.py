'''
dist = float(input('Qual a distância da viagem? '))
if dist <= 200:
    valor = dist * 0.50
    print('O valor da passagem será R$ {:.2f}'.format(valor))
else:
    valor = dist * 0.45
    print('O valor da passagem será R$ {:.2f}'.format(valor))
'''

# Resolucao do professor
# distancia = float(input('Qual é a distância da sua viagem? '))
# print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45
# print('E o preço da sua passagem será de R${:.2f}'.format(preco))

# Outra forma do professor usando operador ternario (if simplificado)
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))

