from random import randint

tuplaCincoAleatorio = (randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99))
tuplaSort = sorted(tuplaCincoAleatorio)
print(tuplaCincoAleatorio)
print(tuplaSort)
print(f"O maior valor é: {tuplaSort[4]}")
print(f"O menor valor é: {tuplaSort[0]}")

