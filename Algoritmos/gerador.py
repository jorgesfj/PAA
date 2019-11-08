import random
lista = []
while len(lista)<100000:
	a = random.randint(0, 99999999)
	if a not in lista:
		lista.append(a)
print(lista)
print(len(lista))



