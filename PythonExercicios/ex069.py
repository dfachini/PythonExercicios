'''
#
# idade = 0
# sexo = "NA"
# pergunta = "NA"
# print('='*30)
# print('     CADASTRE UMA PESSOA')
# print('='*30)
#
# idade = int(input('Idade: '))
# # sexo = str(input('Sexo: [M/F]: ')).upper()[0]
# while sexo not in 'MmFf':
#     sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
#     while pergunta not in 'SsNn':
#         pergunta = str(input('Quer continuar? [S/N] 1 : ')).strip().upper()[0]
#         while pergunta in 'Ss':
#             print('=' * 30)
#             print('     CADASTRE UMA PESSOA')
#             print('=' * 30)
#             idade = int(input('Idade: '))
#             sexo = str(input('Sexo: [M/F]: ')).upper()[0]
#             pergunta = str(input('Quer continuar? [S/N] 2 : ')).strip().upper()[0]
#         if pergunta == 'N':
#             break
#
# print('Obrigado!')




print('=' * 30)
print('     CADASTRE UMA PESSOA')
print('=' * 30)
idade = int(input('Idade: '))
while idade < 0:
    idade = int(input('Idade: '))
sexo = str(input('Sexo: [M/F]: ')).upper()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo: [M/F]: ')).upper()[0]
pergunta = str(input('Quer continuar? [S/N] 1 : ')).strip().upper()[0]
while pergunta not in 'SN':
    pergunta = str(input('Quer continuar? [S/N] 1 : ')).strip().upper()[0]
    if pergunta == 'S':
        idade = -1
        while idade < 0:
            idade = int(input('Idade: '))
        sexo = str(input('Sexo: [M/F]: ')).upper()[0]
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F]: ')).upper()[0]
        pergunta = str(input('Quer continuar? [S/N] 2 : ')).strip().upper()[0]
    else:
        break

print('Voce digitou N na pergunta')
'''

# Resolução do Professor
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')