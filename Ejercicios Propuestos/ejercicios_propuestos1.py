def DevuelveMax(a,b):
	if(a < b):
		print("El número "+str(b)+" es el mayor")
	elif(a == b):
		print("Los números son iguales")
	else:
		print("El número "+str(a)+" es el mayor")
print("Programa para saber cual es el mayor de dos números")		
n = int(input("Ingrese un número "))
m = int(input("Ingrese otro número "))
DevuelveMax(n,m)


