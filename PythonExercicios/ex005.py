n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor \033[1;31m{}\033[m, seu antecessor é {} e o sucessor é {}'.format(n, a, s))

# Outra forma (serve apenas para printar na tela o valor não é armazenado em variaveis)
print('Analisando o valor \033[1;31m{}\033[m, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))