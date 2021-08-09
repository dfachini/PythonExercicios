num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
soma = num1 + num2
#print('A soma dos 2 numeros é :', soma)
# print('A soma dos 2 numeros é {} '.format(soma))
print('A soma de \033[1;31m{}\033[m + \033[1;32m{}\033[m é: \033[1;33m{}\033[m '.format(num1, num2, soma))
