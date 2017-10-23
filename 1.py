# Construa um algoritmo que receba trinta números e mostre a soma total dos números recebidos.

counter = 1
numtotal=int(0)
num1=int

while counter < 31:
	print("escreva o",counter,"º valor.")
	num1 = input()
	num1=int(num1)
	numtotal = num1 + numtotal
	counter += 1

print("A soma total é:",numtotal)	