nome = input('Qual o seu nome? ')
# print('Olá ' + nome +' ! Prazer em te conhecer!')
print('Olá \033[4;33m{}\033[m!. Prazer te conhecer.'.format(nome))