
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero < 0 or numero > 20:
        numero = int(input('Digite um numero entre 0 e 20: '))
    else:
        numPorExtensos = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
        print(f'Voce digitou {numPorExtensos[numero]}')