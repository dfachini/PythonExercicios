'''

laco = 1
total = mais = qtemenos = menor = maior = 0
menorproduto = ''
while laco != 0:
    nome = str(input('Nome produto: ')) # Ovo, Maizena
    preco = float(input('Preço: '))  # 3, 2
    total += preco # 3, 5
    pergunta = str(input('Voce quer continuar ? [S/N]: ')).strip().upper() # S, S
    if pergunta == 'S':
        if preco < 1000: # 2 < 1000?, 3 < 1000?, 1 < 1000?
            qtemenos += 1 # 0 = 1, 1 = 1 + 1, 2 = 2 + 1, 3 = 3 + 1
            if qtemenos == 1: # 1 == 1, 2 ==1?,
                maiorpreco = menorpreco = preco # 1 = 1 = 2,
            else:
                if preco > maiorpreco: # 2 > 1, 3 > 2, 1 > 3,
                    maiorpreco = preco # 1 = 2, 2 = 3
                if preco < maiorpreco: # 1 < 3,
                    menorpreco = preco # 0 = 1,
                    menorproduto = nome # vazio = Manga
        if preco > 1000:
            mais += 1
    else:
        break
print(f'Tchau!, Total R$ {total}, {mais} produtos custam mais de MIL. O menor produtor é o {menorproduto} seu preço é R$ {menorpreco}')
'''

# Resolução do Professor

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:   # Outra forma usando OR para reduzir o código diminuindo um if
        menor = preco
        barato = produto
    # if cont == 1:
    #     menor = preco
    #     barato = produto
    # else:
    #     if preco < menor:
    #         menor = preco
    #         barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')