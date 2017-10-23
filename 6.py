# Construa um algoritmo que leia cento e cinquenta números e mostre qual o maior e o menor número lido.

counter = 2
menor=int
maior=int(0)
num=int

print("escreva o 1º valor.")
menor = input()
menor=int(menor)

while counter < 151:
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