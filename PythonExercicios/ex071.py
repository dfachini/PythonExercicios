'''

# cedulas 50, 20, 10 e 1

# valor = int(input('Que valor você quer sacar? R$ '))

valor = 550
qtde50 = qtde20 = qtde10 = qtde1 = 0
resto50 = resto20 = resto10 = resto1 = 0
# while valor > 50:
while True:
    resultado = valor // 50
    resto50 = valor % 50
    qtde50 = resultado
    if resto50 >= 20:
        qtde20 = resto50 // 20
        resto20 = resto50 % 20
        if resto20 >= 10:
            qtde10 = resto20 // 10
            resto10 = resto20 % 10
            if resto10 < 10:
                qtde1 = resto10 // 1
    break
                    # qtde1 = resultado

print(qtde50, qtde20, qtde10, qtde1)
'''

# Resolução do Professor

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor   # 150
ced = 50
totced = 0
while True:
    if total >= ced:   # 150 >= 50, 100 >= 50,
        total -= ced   # 150 = 150 - 50, 100 = 100 - 50
        totced += 1    # 0 = 0 + 1, 
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
