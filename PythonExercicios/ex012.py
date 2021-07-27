preco = float(input('Qual o preco do produto? R$ '))
novo = preco - (preco * 5 / 100)      # Forma de ler: cinco por cento de ... é:
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))