# Escreva um algoritmo que receba 100 números, e conte quantos deles estão no intervalo de 10 a 20 
# e quantos deles estão fora do intervalo, escrevendo estas informações.

counter = 1
num=int
intervalo=int(0)
fora=int(0)

while counter < 101:
	print("escreva o",counter,"º valor.")
	num = input()
	num=int(num)
	if num>=10 and num<=20:
		intervalo += 1
	else:
		fora +=1	
	counter += 1
print("Numeros dentro do intervalo:",intervalo)
print("Numeros fora do intervalo:",fora)
