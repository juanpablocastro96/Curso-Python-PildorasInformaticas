#listas no modificables despues de su creacion
#no se permiten busquedas
#si comprobar si hay un elemento
#mas rapidas masnoes espacios
#usar solo para ver su contenido y recorrerlas
#formatear strings y como clave en un diccionario de python
#sintaxis: van entre parantesis opcionales
#cuAndo imprimo una tupla esta sale en parentesis pero en corchetes salen las listas
#las TUPLAS PERMITEN BUSQUEDAS
#usar el metdo index()
nombreTupla = ("Juan", 13, 1, 1996)
#acceder a un elemento en concreto(hay que saber el indice)
print(nombreTupla[2])

#dos metodos para convertir tupla en lista

#convertir una tupla en una lista
milista=list(nombreTupla)

#convertr una lista en una tupla
lista = ["Juan", 13, 1, 1996]
tupla = tuple(lista)

#comprobar si hay elementos en una tupla
print("Juan" in tupla)

#metodo que permite averiguar cuantos elementos que nosotros le digamos aparecen
#cuantas veces aparece el elemento 13
print(tupla.count(13))


#para bucles para averiguar el largo no el indice
print(len(tupla))

#crear tuplas unitarias(un elemento)
unitariaTupla = ("Juan",)
print(len(unitariaTupla))

#otra forma de crear tupla, a veces se confunde por funciones con parametros
#enpaquetado de tupla
tupla2 = "Juan",13,1,1996

#desempaquetado de tupla: asignar todos los valores una tupla a diferentes variables

desTupla=("Juan",13,1,1996)
nombre, dia, mes, anio=desTupla
print(nombre)
print(dia)
print(mes)
print(anio)

#nada de usar nada de modificacion como en las listas






