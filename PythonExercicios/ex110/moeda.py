def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco=0, formato=False):
    res = preco/2
    return res if not formato else moeda(res)

def moeda(preco=0, moeda='R$'):                       # moeda nome da função nao tem relação com a moeda de passagem de parametro. 
    return f'{moeda}{preco:>.2f}'.replace('.', ',')  # Se nao informar a moeda o padrão será o real "R$", se não informar o preço                                                       # o padrão será o 0. 
def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-'*30)