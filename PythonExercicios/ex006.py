n = int(input('Digite um numero '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('Voce digitou {}. O dobro dele é {}, o triplo é {} e a raiz quadrada é {}'.format(n, dobro, triplo, raiz))

#outra forma
print('\nOutra forma:')
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))