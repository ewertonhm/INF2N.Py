# Construa um algoritmo que leia cem números e mostre qual o maior número que foi lido.

counter = 1
maior=int(0)
num1=int


while counter < 101:
	print("escreva a",counter,"º valor.")
	num1 = input()
	num1=int(num1)
	if num1>maior:
		maior = num1
	counter += 1

print("O maior numero é:",maior)	