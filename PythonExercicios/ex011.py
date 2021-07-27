largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua area é de {}mts quadrados'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))