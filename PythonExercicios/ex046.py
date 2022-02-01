# Contagem Regressiva Fogos artificio
'''
import time

n = 10
print ('A Contagem vai começar: ')
for contador in range(0, 11):
    resultado = n - contador
    print(resultado)
    time.sleep(1)
'''
# Resolucao do professor
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('ACABOU!')
