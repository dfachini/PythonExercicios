# Frase é palindromo ou nao ?

frase = 'O    AME o poema'

frase_modificada = frase.replace(' ', '').lower()

# qtde_caract = int(len(frase_modificada))

# for i in range(0, qtde_caract):
#     print(frase_modificada[i])
# #     print(frase_modificada[::-i])

# qtde_reversa = qtde_caract
# for i in range(0, qtde_reversa):
#     print(frase_modificada[:-i])
# # print((frase_modificada[:-3]))

# for i in reversed(frase_modificada):
#     # print(i, end = "")


# frase_invertida = ""
# for i in frase_modificada:
#     frase_invertida = i + frase_invertida
# # print(frase_invertida)
#
# if frase_modificada == frase_invertida:
#     print('É palindromo')
# else:
#     print('\"{}\" não é um palindromo'.format(frase_modificada))


'''
frase_invertida = ""
for i in range(len(frase_modificada), 0, -1):
    frase_invertida.append(frase_modificada[i])
print(frase_invertida)
'''

# Resolucao do Professor
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()    # Fatiar a frase
# print(palavras)
junto = ''.join(palavras)
# inverso = ''
# for letra in range(len(junto) -1, -1, -1):
# inverso += junto[letra]
inverso = junto[::-1]           # Outra forma de ler de traz pra frente utilizando o fatiamento
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')