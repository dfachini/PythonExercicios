n = int(input('Digite um numero '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('Voce digitou \033[1;31m{}\033[m. O dobro dele é {}, o triplo é {} e a raiz quadrada é {}'.format(n, dobro, triplo, raiz))

#outra forma
print('\nOutra forma:')
print('O dobro de \033[1;31m{}\033[m vale {}.'.format(n, (n*2)))
print('O triplo de \033[1;31m{}\033[m vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))