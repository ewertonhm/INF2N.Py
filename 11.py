# Escrever um algoritmo que leia 50 números e informe quantos destes valores são negativos.

counter = 1
numtotal=int(0)
num1=int


while counter < 51:
	print("escreva o",counter,"º valor.")
	num1 = input()
	num1=int(num1)
	if num1<0:
		numtotal = num1 + numtotal
	counter += 1

print("A quantidade de numeros negativos é:",numtotal)	