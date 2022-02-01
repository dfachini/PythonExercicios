'''
sexo = str(input('Digite o sexo [M/F]: ')).upper()
# while (sexo != 'M') & (sexo != 'F'):
while sexo != 'M' and 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
print('Obrigado!')
'''


#Resolucao do Professor
sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por Favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
