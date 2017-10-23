# Construa um algoritmo que receba quinze números quaisquer e informe qual o maior e o menor entre os números que foram lidos.

counter = 2
menor=int
maior=int(0)
num=int

print("escreva o 1º valor.")
menor = input()
menor=int(menor)

while counter < 16:
	print("escreva o",counter,"º valor.")
	num = input()
	num=int(num)
	if num<menor:
		menor = num
	if num>maior:
		maior = num
	counter += 1

print("O menor numero é:",menor)	
print("O maior numero é:",maior)