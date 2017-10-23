# Uma loja tem 150 clientes cadastrados e deseja mandar uma correspondência a cada um deles anunciando um bônus especial. Escreva um
# algoritmo que leia o nome, o endereço do cliente e o valor de suas compras e calcule um bônus de 10% se o valor das compras for menor ou 
# igual a R$500.000,00 e de 15 %, se superior a este valor.

counter = 1
nome=str
endereco=str
compras=int
bonus1=int(10)
bonus2=int(15)
valorbonus=int

while counter < 151:
	print("Dados do",counter,"º cliente.")
	nome=input("Nome do cliente:")
	endereco=input("Endereço do cliente:")
	compras = input("Valor total das compras:")
	compras=int(compras)

	if compras<=500000:
		valorbonus=(compras/100)*bonus1
	else:
		valorbonus=(compras/100)*bonus2

	print("Cliente:",nome)
	print("Endereço:",endereco)
	print("Total de compras:",compras)
	print("Valor do Bonus:",valorbonus)		

	counter += 1

print("Todos os bonus dos clientes ja foram calculados")	