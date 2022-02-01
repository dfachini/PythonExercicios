'''
num_inicial_a1 = int(input('Insira inicial: '))
num_razao_r = int(input('insira razao: '))
qtde_termos = 10

# ultimo = primeiro + (n-1)*r

ultimo = num_inicial_a1 + (10-1)*num_razao_r
ultimo = ultimo + 1

for i in range(num_inicial_a1, ultimo, num_razao_r):
    print(i)
'''


# Resolução do Professor
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{}'.format(i), end='-> ')
print('ACABOU')
