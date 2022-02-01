'''
#
# # Fn = fn-1 + Fn-2, sendo o  primeiro termo F1= 1 e os valores iniciais F1 = 1, F2 =1.
# F1 = 1
# F2 = 1
before = 0
after = 0

while after < 9:
    print(end="->")
    print('{}'.format(after), end="") # mostra 0, mostra 1 , mostra 1, mostra 2, mostra 3, mostra 5
    after = after + before # 0 + 0, 1 + 0=1, 1 + 1=2, 2+1=3, 3+2=5,
    before = after - before # 0 - 0, 1 - 0=1, 2 - 1=1, 3-1=2, 5-2=3,
    if after == 0:  # 0 == 0, 1 == 0
        after += 1 # 0 + 1,
'''

# Resolução do Professor
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')