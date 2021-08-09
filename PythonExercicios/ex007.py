n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A média entre \033[1;31m{:.1f}\033[m e \033[1;32m{:.1f}\033[m é igual a {:.1f}'.format(n1,n2,m))