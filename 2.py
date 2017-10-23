# Construa um algoritmo que receba cinquenta números e mostre a média dos números que foram digitados.

counter = 1
numtotal=int(0)
num1=int
nummedia=int

while counter < 51:
	print("escreva o",counter,"º valor.")
	num1 = input()
	num1=int(num1)
	numtotal = num1 + numtotal
	counter += 1

print("A soma total é:",numtotal)
nummedia = numtotal/(counter-1)
print("A média é:",nummedia)	