#son unas estructuras de datos parecida a las listas y tuplas
#en ellos se pueden almacenar diferentes tipos de datos incluso listas u otros diccionarios
#los datos se almacenan asociados a una clase de tal forma que se crea una asociacion de
#tipo clave:valor para cada elemento almacenado
#esa clave puede ser un texto un numero una tupla
#los elementos almacenados no estan ordenados, el orden es indiferente a la hora de almacenar
#informacion eun un diccionario
#sintaxis
#paises y capitales
miDiccionario = {"Alemania":"Berlín","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
#Acceder a un elemento, se accede por la clave
print(miDiccionario["Francia"])

#imprimir todo el diccionario
print(miDiccionario)

#como agregar mas elementos
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

#modificar un valor de una clave
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#si ponemos varios valores a una clave, los valores se van sobreescribiendo
#nunca va haber dos claves iguales


#eliminar elementos
del miDiccionario["Reino Unido"]
print(miDiccionario)

#diccionario con mezcla de tipos
diccionarioMezcla={"Alemania":"Berlin", 23:"Jordan","Mosqueteros":3}
print(diccionarioMezcla)

#utilizar una tubla para asignar claves a cada uno de los valores
tupla=["España","Francia","Reino Unido","Alemania"]
diccionario3={tupla[0]:"Madrid",tupla[1]:"Paris",tupla[2]:"Londres",tupla[3]:"Berlin"}
print(diccionario3["Francia"])
print(diccionario3[tupla[1]])

#almacene una tupla como valor de una clave

diccionarioTupla={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":[1991,1992,1996,1997,1998]}
print(diccionarioTupla)
print(diccionarioTupla["Equipo"])
print(diccionarioTupla["Anillos"])

#diccionario con diccionario dentro. Temporadas un subdiccionario y los años es una tupla
diccionarioDiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"temporadas":[1991,1992,1996,1997,1998]}}
print(diccionarioDiccionario)
print(diccionarioDiccionario["Anillos"])

#Metodos importantes en los diccionarios
#metodo KEY que nos devuelve las clase
#metodo VALUES que devuelve los valores
#metodo LEN que devuelve la longitud
print(diccionarioDiccionario.keys())
print(diccionarioDiccionario.values())
print(len(diccionarioDiccionario))



