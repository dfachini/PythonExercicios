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
    