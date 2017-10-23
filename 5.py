# Construa um algoritmo que leia cinquenta números e mostre qual o menor número lido.

counter = 2
menor=int
num1=int

print("escreva o 1º valor.")
menor = input()
menor=int(menor)

while counter < 51:
	print("escreva o",counter,"º valor.")
	num1 = input()
	num1=int(num1)
	if num1<menor:
		menor = num1
	counter += 1

print("O menor numero é:",menor)	