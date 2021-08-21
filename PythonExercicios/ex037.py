''' valor em binario, octal e hexadecimal '''
'''
num = int(45)

binario = num % 2
octal = num % 8
hexadecimal = num % 16

usuario = int(input('Digite 1 para Binario, 2 para Octal e 3 para Hexadecimal: '))
if usuario == 1:
    print('O valor binario de {} é: {}'.format(num, binario))
elif usuario == 2:
    print('O valor octal de {} é: {}'.format(num, octal))
elif usuario == 3:
    print('O valor hexadecimal de {} é: {}'.format(num, hexadecimal))
'''

# Resolucao do professor
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')