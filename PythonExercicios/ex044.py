'''
preconormal = float(input('Digite valor produto R$ '))
print('='*40)
print('Escolha uma das opções de pagamento')
print('='*40)
print('Escolha [1] para pag. À VISTA no dinheiro ou cheque')
print('Escolha [2] para pag. À VISTA no cartão')
print('Escolha [3] para pag. em 2x no cartão')
print('Escolha [4] para pag. em 3x ou mais no cartão')
print('+'*25)
condicaopag = int(input('Digite a melhor opcão: '))
print('+'*25)
if condicaopag == 1:
    print('Você está recebendo 10% de desconto. Valor a pagar será R$ {}'.format(preconormal - (preconormal * 0.1)))
elif condicaopag == 2:
    print('Você está recebendo 5% de desconto. Valor a pagar será R$ {}'.format(preconormal - (preconormal * 0.05)))
elif condicaopag == 3:
    print('Você não terá desconto. Valor a pagar será R$ {}'.format(preconormal))
elif condicaopag == 4:
    print('Você terá que pagar juros. Valor a pagar será R$ {}'.format(preconormal + (preconormal * 0.2)))
else:
    print('Opção inválida tente novamente.')
'''

# Resolucao do professor
print('{:=^40}'.format(' LOJAS ABC '))   # Centralizar em 40 espaços
preco = float(input('Preço das compras R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra parcelada será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(parcela, totparc))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))
