''' credito bancario para comprar de uma casa '''
'''
casavalor = float(120000)
salariobase = float(3000)
quitacao = int(10)
parcela = salariobase * 0.3
# if parcela * quitacao == casavalor or parcela * quitacao > casavalor:   # Errei o calculo de saldo devedor anual
if (parcela * 12) * quitacao == casavalor or (parcela * 12) * quitacao > casavalor:
    print('Credito Aprovado!')
else:
    print('Credito não Aprovado')
print('Valor Imovel: R${:.2f} \nSalario Base: R${:.2f} \n Valor parcela: R${:.2f}'.format(casavalor, salariobase, parcela))
'''

# Resolucao do professor
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('minimo R${:.2f}'.format(minimo))
print('Para pagar uma casa de {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')