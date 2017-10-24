# Faça um algoritmo que receba o salário-base dos 1.200 funcionários de uma fábrica e calcule os
# descontos com vale transporte (vt) em 2% e vale refeição (vr) em 3%. Mostrar o total dos descontos
# efetuados separadamente.

salbase = int
saltotal = int
vt = int
vr = int
pvt = int(2)
pvr = int(3)
nome = str
counter = 1

while counter < 1201:
	print("Dados do",counter,"º Funcionário")
	
	nome = input("Nome do funcionário:")
	salbase = input("Salário Base do Funcionario:")
	salbase = int(salbase)

	vt = (salbase/100)*pvt
	vr = (salbase/100)*pvr

	saltotal = saltotal - vt - vr

	print("Funcionário:",nome)
	print("Descontos de Vale-Transporte:",vt)
	print("Descontos de Vale-Refeição:",vr)
	print("Salário Liquido:",saltotal)

	counter +=1

print("Todos os funcionários ja foram calculádos")	



