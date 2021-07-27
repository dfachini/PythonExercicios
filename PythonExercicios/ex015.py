# diaria = 60.00
# km = 0.15
#
# distancia = float(input('Informe a kilometragem percorrida: '))
# diarias = float(input('Informe a quantidade de diarias: '))
# print('O total a pagar será R${:.2f}'.format((distancia * 0.15) + (diarias * 60)))

dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
