'''
num = int(input('Digite um numero entre 0 e 9999: '))
if num < 0 or num > 9999:
    print("Invalid Number")
else:
    transf_num = str(num)
    print('Unidade: {:2}'.format(transf_num[3]))
    print('Dezena: {:10}'.format(transf_num[2]))
    print('Centena: {:2}'.format(transf_num[1]))
    print('Milhar: {:2}'.format(transf_num[0]))
'''



# Resolucao do professor
num = int(input('Informe um número: '))
u = num // 1 % 10       # resto da divisão apenas
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))