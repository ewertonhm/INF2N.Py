# Construir um algoritmo que receba cem números e informe a média e a soma entre os números positivos.

counter = 1
numtotal=int(0)
num1=int
nummedia=int

while counter < 101:
	print("escreva o",counter,"º valor.")
	num1 = input()
	num1=int(num1)
	if num1>0:
		numtotal = num1 + numtotal
	counter += 1
nummedia = numtotal/(counter-1)
print("A média é:",nummedia)	