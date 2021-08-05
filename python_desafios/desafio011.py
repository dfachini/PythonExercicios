# Largura e altura de uma parede em metros
# calcular a area
# qtde de tinta necessaria. (cada 1 lt = area 2 mts quadrados)

largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = largura * altura
tinta = area / 2
print('A área é {} metros quadrados. A qtde de tinta para pintar é {} lts'.format(area, tinta))
# print('Sua parede tem a dimensão de {}x{} e sua area é de {}mts quadrados'.format(largura, altura, area))
# print('Para pintar essa parede, você precisará de ')