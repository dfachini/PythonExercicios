
'''
a = int(input('Digite primeiro valor: '))
b = int(input('Digite segundo valor: '))

print(30*'=')
print("Menu:\n"
      "[1] - Somar \n"
      "[2] - Multiplicar \n"
      "[3] - Maior \n"
      "[4] - Novos Numeros \n"
      "[5] - Sair")
print(30*'=')
menu = int(input('Escolha uma opção do MENU: '))

while menu == 4:
       a = int(input('Digite primeiro valor: '))
       b = int(input('Digite segundo valor: '))
       print(30 * '=')
       print("Menu:\n"
             "[1] - Somar \n"
             "[2] - Multiplicar \n"
             "[3] - Maior \n"
             "[4] - Novos Numeros \n"
             "[5] - Sair")
       print(30 * '=')
       menu = int(input('Escolha uma opção do MENU: '))

# while menu != 5:
if menu == 1:
       resultado = a + b
       print('A soma de {} e {} é: {}'.format(a, b, resultado))
if menu == 2:
       resultado = a * b
       print('A multiplicação de {} e {} resultou em: {}'.format(a, b, resultado))
if menu == 3:
       resultado = a
       if resultado > b:
              resultado = resultado
       else:
              resultado = b
       print('Entre {} e {}, {} é maior.'.format(a, b, resultado))
if menu == 5:
       print('Digitou SAIR! Tchau!')
'''

#Resolução do Professor
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
         print('''         [1] somar
         [2] multiplicar
         [3] maior
         [4] novos números
         [5] sair do programa''')
         opcao = int(input('Qual é a sua opção? '))
         if opcao == 1:
             soma = n1 + n2
             print('A soma entre {} + {} é {}'.format(n1, n2, soma))
         elif opcao == 2:
             produto = n1 * n2
             print('O resultado de {} * {} é {}'.format(n1, n2, produto))
         elif opcao == 3:
             if n1 > n2:
                 maior = n1
             else:
                 maior = n2
             print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
         elif opcao == 4:
             print('Informe os números novamente:')
             n1 = int(input('Primeiro Valor: '))
             n2 = int(input('Segundo Valor: '))
         elif opcao == 5:
             print('Finalizando...')
         else:
             print('Opção inválida. Tente novamente.')
         print('===' * 10)
print('Fim do programa! Volte Sempre!')