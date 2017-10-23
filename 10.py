# Faça um algoritmo que receba o peso, a idade e a altura de cem pessoas, calcule e informe os
# valores de: maior peso, menor peso, maior altura, menor altura, maior idade e menor idade deste grupo.

counter = 2

peso=int
menorpeso=int
maiorpeso=int(0)

idade=int
menoridade=int
maioridade=int(0)

altura=int
menoraltura=int
maioraltura=int(0)

print("Escreva os dados do 1º participante:")
menorpeso=input("Peso:")
menorpeso=int(menorpeso)

menoridade=input("Idade:")
menoridade=int(menoridade)

menoraltura=input("Altura:")
menoraltura=int(menoraltura)

while counter < 101:
	print("Escreva os dados do",counter,"º participante:")
	peso=input("Peso:")
	peso=int(peso)

	if peso<menorpeso:
		menorpeso = peso
	if peso>maiorpeso:
		maiorpeso = peso

	idade=input("Idade:")
	idade=int(idade)

	if idade<menoridade:
		menoridade = idade
	if idade>maioridade:
		maioridade = idade

	altura=input("Altura:")
	altura=int(altura)

	if altura<menoraltura:
		menoraltura = altura
	if altura>maioraltura:
		maioraltura = altura

	counter += 1

print("O menor peso é:",menorpeso)	
print("O maior peso é:",maiorpeso)
print("A menor altura é:",menoraltura)	
print("A maior altura é:",maioraltura)
print("A menor idade é:",menoridade)	
print("A maior idade é:",maioridade)

