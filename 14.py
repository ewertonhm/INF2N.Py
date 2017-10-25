# Faça um algoritmo que receba o número do apartamento e o consumo em kw/h dos setenta e dois apartamentos de um edifício. Informe os 
# apartamentos com o consumo inferior ou igual a 100 kw/h (inclusive) e os que ultrapassaram este consumo.

leitura = int
counter = int(1)
inferior = []
ultrapassaram = []

while counter < 10:
	print("Consumo do",counter,"º aparatamento")
	leitura = input()
	leitura = int(leitura)

	if leitura <= 100:
		inferior.append(counter)
	else:
		ultrapassaram.append(counter)
	counter += 1

print("Apartamentos com o consumo inferior a 100kw/h:",inferior)
print("Apartamentos com o consumo superior a 100kw/h",ultrapassaram)



