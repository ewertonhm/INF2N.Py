# Construa um algoritmo que receba a idade de cem pessoas e mostre a média das idades destas pessoas.

counter = 1
numtotal=int(0)
num1=int
nummedia=int

while counter < 101:
	print("escreva a",counter,"ª idade.")
	num1 = input()
	num1=int(num1)
	numtotal = num1 + numtotal
	counter += 1
nummedia = numtotal/(counter-1)
print("A média é:",nummedia)	