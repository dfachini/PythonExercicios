'''
salario = float(input('Informe o seu salário ? R$ '))

if salario > 1250:
    print('Seu salário foi de R$ {:.2f} para R$ {:.2f}'.format(salario, salario + (salario*0.10)))
else:
    if salario <= 1250:
        print('Seu salário foi de R$ {:.2f} para R$ {:.2f}.'.format(salario, salario + (salario*0.15)))
'''


# Resolucao do professor
salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 /100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, novo))