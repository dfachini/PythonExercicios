
times = ('Atlético Mineiro',
'Palmeiras',
'Flamengo',
'América Mineiro',
'Corinthians',
'Athletico Paranaense',
'Atlético Goianiense',
'Avaí',
'Botafogo',
'Ceará',
'Coritiba',
'Cuiabá ',
'Fluminense',
'Fortaleza',
'Chapecoense',
'Internacional',
'Juventude',
'Red Bull',
'Santos',
'São Paulo')

# Listar apenas os 5 primeiros colocados 
print(times[0:5])

# Listar os apenas os últimos 4 colocados
print(times[16:20])

# Listar ordem alfabetica 
timeOrdenado = sorted(times)
print(timeOrdenado)

# Qual a posição da Chapecoense?

# while time != "Chapecoense":
#     cont = 0
#     for time in times:
#         if time == 'Chapecoense':
#             cont += 1
#             print("A Chapecoense está na posição: ", {cont})

contador = 0
for time in times:
    contador += 1
    if time == "Chapecoense":
        print(f"A Chapecoense está na posição: {contador}" )