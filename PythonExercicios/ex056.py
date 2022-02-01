'''
from faker import Faker
from datetime import datetime
import pandas as pd

faker = Faker()

# Gerar dados com Faker
lista = []
for i in range(0, 5):
    # faker.simple_profile()
    # print(f'Age: {faker.simple_profile()}')
    lista.append(faker.simple_profile())

# Transformar lista em DataFrame
df = pd.DataFrame(lista, columns=['name', 'birthdate', 'sex'])
# print(type(df))

# Pega o ano atual
currentYear = datetime.now().year
# print(currentYear)

import time
# teste = (df['birthdate'][0].year)

# Criar coluna no DataFrame de Year com os dados de birthdate
df['age'] = ''
for i in range(len(df)):
    # print(df['birthdate'][i].year)
    df['age'][i] = currentYear - df['birthdate'][i].year

# print(df)

# Descobrir a media de idade
print('A média de idade é: {:.0f}'.format(df['age'].mean()))
print('='*50)
#
# Qual o nome do homem mais velho
df1 = df.sort_values('age', inplace=False)
# print(df.loc[df['sex'] == 'M'].sort_values('age', ascending=True).head(1))
print('O homem mais velho é: {}'.format(df1['name'].loc[df['sex'] == 'M'].head(1)))
print('='*50)
#
# Quantas mulheres tem menos de 20 anos
# print(df.loc[(df['age'] < 20) & (df['sex'] == 'F')].shape[0])
print('Quantidade de Mulheres com menos de 20 anos: \n{} mulher(es).'.format(df.loc[(df['age'] < 20) & (df['sex'] == 'F')].shape[0]))








# lista.sort(reverse=False)
# printing the list using loop
# for i in range(len(lista)):
#     print(lista[i])

# print((lista).sort(key=birthdate, reverse=False))

# print(lista[1]['name'], lista[1]['sex'], lista[1]['birthdate'])
# if lista[0]['sex'] == 'F':
#     print(lista[0])
#
# # limpar lista usando pop()
# for i in range(len(lista)):
#     lista[i].pop('username', None)
#     lista[i].pop('address', None)
#     lista[i].pop('mail', None)
#     # print(lista[i])
#
# # Adicionar idade na lista
# age = []
# currentyear = [2021]
# print(lista[0]['birthdate'])
#     x = datetime.now() - (lista[0]['birthdate'])
#
# print(datetime.datetime.now()) -
#
# # mostrar média do grupo

'''

#Resolucao do Professor

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for i in range(1,5):
    print('------- {} PESSOA --------'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm': # Se digitar M maiusculo ou minusculo vai aceitar
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
