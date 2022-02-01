'''
n = i = s = 0
while n >= 0:
    n = int(input('Digite numero: '))
    if n == 999:
        break
    i += 1
    s += n
print(f'{s} soma e {i} qtde')
'''

#Resolucao do Professor
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')