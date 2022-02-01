'''
soma = 0
n = 0
cont = 0
while n != 999:
    n = int(input('Digite n: '))
    if n != 999:
        cont += 1
        soma += n
print('cont: {} e soma: {}'.format(cont, soma))
'''

# Resolução do Professor
num = cont = soma = 0  # atribui 0 para as 3 variaveis
num = int(input('Digite um número [999 para parar]: ')) # Flag do lado de fora
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))   # Flag do lado de dentro como última linha
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))