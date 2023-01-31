# def aumentar(n, tax):
#     return n + (n * tax/100)

# def diminuir(n, tax):
#     return n - (n * tax/100) 

# def dobro(num):
#     return num*2

# def metade(n):
#     return n/2




# Resolução do Professor

def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res

def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res

def dobro(preco):
    res = preco * 2
    return res

def metade(preco):
    res = preco/2
    return res
