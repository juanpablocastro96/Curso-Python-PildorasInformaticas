#estructuras que extraen valores de uuna funcion y almacenen en objetos iterabes
#estos valores se almacenan de uno en uno
#suspension de estado de un nuevo valor almacenado hasya que se solicita el siguiente

#son mas eficientes que las funciones tradicionales
#muy utiles con listas de valores infinitos


def generadorPares(limite):
	num=1
	
	while num<limite:
		yield num*2
		num=num+1
	
	

#guardo el objeto iterable que creo arriba con el generador
devuelvePares=generadorPares(10)
#for i in devuelvePares:
#	print(i)



#slo los 3 primeros objetos

print(next(devuelvePares))
print("Mas codigo")
print(next(devuelvePares))
print("Mas codigo")
print(next(devuelvePares))