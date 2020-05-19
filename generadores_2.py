#nueva instruccion yeild from
#simplificar el codigo del generador en caso de utilizar bucles anidados
#podria tener un ejemplo matrices
#una serie de ciuddes
#el asteristo antes de un argumento, que va recibir un numero indterminado de elementos y lo recibira en forma de tubla

#def devuelve_ciudades(*ciudades):
#	for elemento in ciudades:
#		for subElemento in elemento:
#			yield subElemento 
	



def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		#for subElemento in elemento:
			yield from elemento 
ciudades_devueltas= devuelve_ciudades("Madrid","Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))